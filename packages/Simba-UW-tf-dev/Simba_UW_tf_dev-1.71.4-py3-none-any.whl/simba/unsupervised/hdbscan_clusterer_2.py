from simba.read_config_unit_tests import (check_if_filepath_list_is_empty,
                                          check_file_exist_and_readable)
from simba.misc_tools import SimbaTimer
from simba.unsupervised.misc import (check_directory_exists,
                                     check_that_directory_is_empty)
from simba.unsupervised.enums import Clustering, Unsupervised
import itertools
import os, glob
import random
import pandas as pd
from simba.utils.printing import stdout_success
from simba.mixins.unsupervised_mixin import UnsupervisedMixin
from simba.unsupervised.umap_embedder_2 import UmapEmbedder
try:
    from cuml.cluster.hdbscan import HDBSCAN
    from cuml.cluster import hdbscan
    gpu_flag = True
except ModuleNotFoundError:
    from hdbscan import HDBSCAN
    import hdbscan


class HDBSCANClusterer(UnsupervisedMixin):
    def __init__(self,
                 data_path: str,
                 save_dir: str):

        super().__init__()
        self.save_dir, self.data_path = save_dir, data_path
        check_directory_exists(directory=save_dir)
        if os.path.isdir(data_path):
            check_directory_exists(directory=data_path)
            self.data_path = glob.glob(data_path + '/*.pickle')
            check_if_filepath_list_is_empty(filepaths=self.data_path, error_msg=f'SIMBA ERROR: No pickle files in {data_path}')

    def fit(self,
            hyper_parameters: dict):

        check_that_directory_is_empty(directory=self.save_dir)
        self.search_space = list(itertools.product(*[hyper_parameters[Clustering.ALPHA.value],
                                                     hyper_parameters[Clustering.MIN_CLUSTER_SIZE.value],
                                                     hyper_parameters[Clustering.MIN_SAMPLES.value],
                                                     hyper_parameters[Clustering.EPSILON.value]]))
        self.embeddings = self.read_pickle(data_path=self.data_path)
        print(f'Fitting {str(len(self.search_space) * len(self.embeddings.keys()))} HDBSCAN model(s)...')
        self.__fit_hdbscan()
        self.timer.stop_timer()
        stdout_success(msg=f'{str(len(self.search_space) * len(self.embeddings.keys()))} saved in {self.save_dir}', elapsed_time=self.timer.elapsed_time_str)

    def __fit_hdbscan(self):
        for k, v in self.embeddings.items():
            fit_timer = SimbaTimer()
            fit_timer.start_timer()
            embedder = v[Unsupervised.DR_MODEL.value][Unsupervised.MODEL.value]
            for cnt, h in enumerate(self.search_space):
                results, self.model, self.model_count = {}, {}, cnt
                self.model_timer = SimbaTimer()
                self.model_timer.start_timer()
                self.model[Unsupervised.HASHED_NAME.value] = random.sample(self.model_names, 1)[0]
                self.model[Unsupervised.PARAMETERS.value] = {Clustering.ALPHA.value: h[0],
                                                             Clustering.MIN_CLUSTER_SIZE.value: h[1],
                                                             Clustering.MIN_SAMPLES.value: h[2],
                                                             Clustering.EPSILON.value: h[3]}
                self.model[Unsupervised.MODEL.value] = HDBSCAN(algorithm="best",
                                                          alpha=self.model[Unsupervised.PARAMETERS.value][Clustering.ALPHA.value],
                                                          approx_min_span_tree=True,
                                                          gen_min_span_tree=True,
                                                          min_cluster_size=self.model[Unsupervised.PARAMETERS.value][Clustering.MIN_CLUSTER_SIZE.value],
                                                          min_samples=self.model[Unsupervised.PARAMETERS.value][Clustering.MIN_SAMPLES.value],
                                                          cluster_selection_epsilon=self.model[Unsupervised.PARAMETERS.value][Clustering.EPSILON.value],
                                                          p=None,
                                                          prediction_data=True)

                self.model[Unsupervised.MODEL.value].fit(embedder.embedding_)
                results[Unsupervised.DATA.value] = v[Unsupervised.DATA.value]
                results[Unsupervised.METHODS.value] = v[Unsupervised.METHODS.value]
                results[Unsupervised.DR_MODEL.value] = v[Unsupervised.DR_MODEL.value]
                results[Clustering.CLUSTER_MODEL.value] = self.model
                self.__save(data=results)

    def __save(self, data: dict) -> None:
        self.write_pickle(data=data, save_path=os.path.join(self.save_dir, f'{self.model[Unsupervised.HASHED_NAME.value]}.pickle'))
        self.model_timer.stop_timer()
        stdout_success(msg=f'Model {self.model_count + 1}/{len(self.search_space)} ({self.model[Unsupervised.HASHED_NAME.value]}) saved...', elapsed_time=self.model_timer.elapsed_time)


    def transform(self,
                  data_path: str,
                  model: str or dict,
                  save_dir: str or None=None,
                  settings: dict or None=None):

        timer = SimbaTimer()
        timer.start_timer()
        if isinstance(model, str):
            check_file_exist_and_readable(file_path=model)
            model = self.read_pickle(data_path=model)

        check_file_exist_and_readable(file_path=data_path)
        umap_embedder = UmapEmbedder()
        umap_embedder.transform(model=model, data_path=data_path, settings={'DATA': None, 'format': None})
        self.label, self.strength = hdbscan.approximate_predict(model[Clustering.CLUSTER_MODEL.value][Unsupervised.MODEL.value], umap_embedder.results[['X', 'Y']].values)
        self.results = pd.DataFrame({'HDBSCAN_LABEL': self.label, 'HDBSCAN_STRENGTH': self.strength}, columns=['HDBSCAN_LABEL', 'HDBSCAN_STRENGTH'], index=umap_embedder.umap_df.index)
        self.results = pd.concat([umap_embedder.results[['X', 'Y']], self.results], axis=1)
        if settings[Unsupervised.DATA.value] == Unsupervised.SCALED.value:
            self.results = pd.concat([umap_embedder.scaled_umap_data, self.results], axis=1)
        elif settings[Unsupervised.DATA.value] == Unsupervised.RAW.value:
            self.results = pd.concat([umap_embedder.umap_df, self.results], axis=1)
        if save_dir:
            save_path = os.path.join(save_dir, f'Transformed_{model[Unsupervised.DR_MODEL.value][Unsupervised.HASHED_NAME.value]}.csv')
            if settings[Unsupervised.FORMAT.value] is Unsupervised.CSV.value:
                self.results.to_csv(save_path)
            timer.stop_timer()
            print(f'Transformed data saved at {save_dir} (elapsed time: {timer.elapsed_time_str}s)')

# hyper_parameters = {'alpha': [1.0], 'min_cluster_size': [10], 'min_samples': [1], 'cluster_selection_epsilon': [20]}
# embedding_dir = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/dr_models'
# save_dir = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/cluster_models'
# config_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/project_folder/project_config.ini'
# clusterer = HDBSCANClusterer(data_path=embedding_dir, save_dir=save_dir)
# clusterer.fit(hyper_parameters=hyper_parameters)


data_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/project_folder/logs/unsupervised_data_20230416145821.pickle'
save_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/dr_models'
clusterer = HDBSCANClusterer(data_path=data_path, save_dir=save_path)
clusterer.transform(model='/Users/simon/Desktop/envs/troubleshooting/unsupervised/cluster_models/awesome_curran.pickle', settings={'DATA': None}, data_path=data_path)

#settings = {'feature_values': True, 'scaled_features': True, 'save_format': 'csv'}
# clusterer_model_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/cluster_models/amazing_burnell.pickle'
# data_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/project_folder/logs/unsupervised_data_20230215093552.pickle'
# save_path = '/Users/simon/Desktop/envs/troubleshooting/unsupervised/dr_models'

# _ = HDBSCANTransform(clusterer_model_path=clusterer_model_path,
#                      data_path=data_path,
#                      save_dir=save_path,
#                      settings=settings)





import abc

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from refaclass.core.model import AbstractModel


class AbstractClusteringMethod(abc.ABC):
    @abc.abstractmethod
    def clustering(self, sentences: list) -> list:
        pass


class KMeansClusteringMethod(AbstractClusteringMethod):
    def __init__(self, model: AbstractModel):
        self.model = model

    def estimate_n_clusters(self, sentences: list) -> int:
        """shilouette analysis"""
        silhouette_scores = []

        if len(sentences) < 2:
            return 1

        k_range = range(2, len(sentences))
        vectors = np.array(
            [self.model.get_sentence_vector(sentence) for sentence in sentences]
        )
        for k in k_range:
            labels = self.clustering(sentences=sentences, n_clusters=k)

            # if all labels are the same, silhouette_score returns error, so return 0
            if len(set(labels)) == 1:
                silhouette_scores.append(0)
                continue

            silhouette_avg = silhouette_score(vectors, labels)
            silhouette_scores.append(silhouette_avg)

        if len(silhouette_scores) == 0:
            optimal_clusters = 1
        else:
            optimal_clusters = np.argmax(silhouette_scores) + 2

        return optimal_clusters

    def clustering(self, sentences: list, n_clusters: int = 2) -> list:
        if len(sentences) < n_clusters:
            n_clusters = len(sentences)

        if len(sentences) == 0:
            return []

        vectors = np.array(
            [self.model.get_sentence_vector(sentence) for sentence in sentences]
        )

        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(vectors)

        labels = kmeans.labels_

        return labels

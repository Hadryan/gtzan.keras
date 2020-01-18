import numpy as np

__all__ = ["majority_voting"]


def majority_voting(scores, dict_genres):
    preds = np.argmax(scores, axis = 1)
    values, counts = np.unique(preds, return_counts=True)
    votes = {k:v for k, v in zip(values, counts)}
    votes = {k: v for k, v in sorted(votes.items(), key=lambda item: item[1], reverse=True)}
    votes = list(votes.keys())
    return [get_genres(x, dict_genres) for x in votes]


def get_genres(key, dict_genres):
    # Transforming data to help on transformation
    labels = []
    tmp_genre = {v:k for k,v in dict_genres.items()}

    return tmp_genre[key]
import numpy as np

def calculate_rig(y_true, y_pred):
    """
    Calculate the RIG (Relative Improvement Gain) metric.

    Parameters:
    y_true (array-like): True values.
    y_pred (array-like): Predicted values.

    Returns:
    float: RIG value.
    """
    y_true = np.array(y_true, dtype=np.float64)
    y_pred = np.array(y_pred, dtype=np.float64)

    epsilon = 1e-15

    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    # 3. Calculate Model Log Loss
    # Formula: -1/N * sum(y * log(p) + (1-y) * log(1-p))
    numerator = -np.mean(y_true * np.log(y_pred) + (1-y_true) * np.log((1-y_pred)))

    denominator = -np.mean(y_pred)*np.log(np.mean(y_pred)) + (1-np.mean(y_pred))*np.log(1-np.mean(y_pred))

    rig = numerator / denominator

    return numerator,rig


def calculate_auc_roc(y_true, y_pred):
    rank = np.argsort(y_pred)
    y_true_sorted = y_true[rank]

    ranks = np.where(y_true_sorted == 1)[0] + 1

    n_pos = np.sum(y_true == 1)
    n_neg = np.sum(y_true == 0)

    auc = (np.sum(ranks) - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)

    return auc
        
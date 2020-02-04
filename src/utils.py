import numpy as np


def iqr(data):
    """compute the interquartile range (excluding nan)"""
    return np.nanquantile(data, 0.75) - np.nanquantile(data, 0.25)

def iqr_rule(data, factor=1.5):
    """returns an outlier filter mask using the iqr rule"""
    iqr_ = iqr(data)
    upper_fence = np.nanquantile(data, 0.75) + factor*iqr_
    lower_fence = np.nanquantile(data, 0.25) - factor*iqr_
    return (data <= upper_fence) & (data >= lower_fence)
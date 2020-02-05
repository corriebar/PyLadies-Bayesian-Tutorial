import numpy as np
import matplotlib.pyplot as plt


def iqr(data):
    """compute the interquartile range (excluding nan)"""
    return np.nanquantile(data, 0.75) - np.nanquantile(data, 0.25)

def iqr_rule(data, factor=1.5):
    """returns an outlier filter mask using the iqr rule"""
    iqr_ = iqr(data)
    upper_fence = np.nanquantile(data, 0.75) + factor*iqr_
    lower_fence = np.nanquantile(data, 0.25) - factor*iqr_
    return (data <= upper_fence) & (data >= lower_fence)


def compare_hist(priors, data):
    fig, ax = plt.subplots(figsize=(20,9), nrows=1, ncols=2)
    ax[0].hist(priors["rent"].flatten(), alpha=0.9, ec="darkblue", bins=70)
    ax[0].set_title("Histogram over possible range of rental prices")
    ax[0].set_xlabel("Monthly Rent [€]")
    ax[1].hist(data["totalRent"], alpha=0.9, ec="darkblue", bins=70)
    ax[1].set_title("Histogram over the actual rental prices")
    ax[1].set_xlabel("Monthly Rent [€]")
    return fig, ax


def draw_models(priors, data):
    area_s = np.linspace(start=-1.5, stop=3.5, num=50)
    draws = np.random.choice(len(priors["alpha"]), replace=False, size=50)
    alpha = priors["alpha"][draws]
    beta = priors["beta"][draws]

    mu = alpha + beta * area_s[:, np.newaxis]

    fig, ax = plt.subplots(figsize=(9,9))
    ax.plot(area_s*np.std(data["livingSpace"]) + data["livingSpace"].mean(), mu, c="#737373", alpha=0.5)
    ax.set_xlabel("Living Area [sqm]", fontdict={"fontsize": 22})
    ax.set_ylabel("Price [€]",  fontdict={"fontsize": 22})
    ax.set_title("Linear model according to our prior")

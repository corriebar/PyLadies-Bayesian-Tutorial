import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA = pd.read_csv("../data/immo_data.csv", dtype={"geo_plz": str})

def iqr(data):
    """compute the interquartile range (excluding nan)"""
    return np.nanquantile(data, 0.75) - np.nanquantile(data, 0.25)

def iqr_rule(data, factor=1.5):
    """returns an outlier filter mask using the iqr rule"""
    iqr_ = iqr(data)
    upper_fence = np.nanquantile(data, 0.75) + factor*iqr_
    lower_fence = np.nanquantile(data, 0.25) - factor*iqr_
    return (data <= upper_fence) & (data >= lower_fence)

def preprocess_data(data):
    data["totalRent"] = np.where(data["totalRent"].isnull(), data["baseRent"], data["totalRent"])

    # since log doesn't work with 0, we replace 0 with 0.5
    # seems reasonable tto say hat a rent of 0€ is the same as 50ct
    data["livingSpace_m"] = np.where(data["livingSpace"] <= 0, 0.5, data["livingSpace"])
    data["totalRent_m"] = np.where(data["totalRent"] <= 0, 0.5, data["totalRent"])
    data["logRent"] = np.log(data["totalRent_m"])
    data["logSpace"] = np.log(data["livingSpace_m"])

    not_outlier = iqr_rule(data["logSpace"], factor=1.5) & iqr_rule(data["logRent"], factor=1.5)
    d = data[not_outlier]
    berlin = d[(d.regio1 == "Berlin")].copy()

    berlin["livingSpace_s"] = (berlin["livingSpace"] - berlin["livingSpace"].mean()) / np.std(berlin["livingSpace"])
    berlin["totalRent_s"] = berlin["totalRent"] / 100

    return berlin

BERLIN = preprocess_data(DATA)


def compare_hist(priors, data):
    fig, ax = plt.subplots(figsize=(20,9), nrows=1, ncols=2)
    ax[0].hist(priors["rent"].flatten()*100, alpha=0.9, ec="darkblue", bins=70)
    ax[0].set_title("Histogram over possible range of rental prices")
    ax[0].set_xlabel("Monthly Rent [€]")
    ax[1].hist(data["totalRent_s"]*100, alpha=0.9, ec="darkblue", bins=70)
    ax[1].set_title("Histogram over the actual rental prices")
    ax[1].set_xlabel("Monthly Rent [€]")
    return fig, ax


def draw_models(priors, data):
    area_s = np.linspace(start=-2, stop=3.5, num=50)
    draws = np.random.choice(len(priors["alpha"]), replace=False, size=50)
    alpha = priors["alpha"][draws]
    beta = priors["beta"][draws]

    mu = alpha + beta * area_s[:, None]

    fig, ax = plt.subplots(figsize=(9,9))
    ax.plot(area_s*np.std(data["livingSpace"]) + data["livingSpace"].mean(), mu*100, c="#737373", alpha=0.5)
    ax.set_xlabel("Living Area [sqm]", fontdict={"fontsize": 22})
    ax.set_ylabel("Price [€]",  fontdict={"fontsize": 22})
    ax.set_title("Linear model according to our prior")
    return fig, ax


def standardize_area(x):
    return (x - BERLIN["livingSpace"].mean()) / np.std(BERLIN["livingSpace"])


def destandardize_area(x):
    return (x * np.std(BERLIN["livingSpace"])) + BERLIN["livingSpace"].mean()

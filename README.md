# PyLadies-Bayesian-Tutorial

Repository with notebooks (and solutions) for my Bayesian tutorial at the PyLadies Meetup Feb 11, 2020.

# Setup

## Download the code from Github
The recommended way to download the code is through git:

```
git clone git@github.com:corriebar/PyLadies-Bayesian-Tutorial.git
```
This will download all code and create the folder `PyLadies-Bayesian-Tutorial` in your current folder.

## Install all packages

I'm using [pipenv](http://docs.pipenv.org/en/latest/install/#installing-pipenv) with Python 3.7 (the code might also work with other Python 3 versions but then you'll need to change the version in the Pipfile).

To install pipenv, run
```
pip install pipenv
```
Then install the necessary packages, using
```
cd PyLadies-Bayesian-Tutorial
pipenv install
```
To activate the environment and start the notebooks from it, run
```
pipenv shell
python -m ipykernel install --user --name=$(basename $(pwd))
jupyter lab
# or jupyter notebook
```
Then, inside jupyter, pick the according kernel for the notebooks.



If you encounter any problems using pipenv, you can also install the packages from the `requirements.txt` file using pip:
```
pip install -r requirements.txt
```
## Check that it works and extract the data
Open the notebook `1_Introduction.ipynb` in the folder notebooks and try to run the first cell. If it can load all the packages and runs without problems then you should be good to go for the rest of the tutorial!


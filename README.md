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
### Using Pipenv

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

### Using Conda

To install the packages using conda, use the following command:
```
conda env create -f environment.yml
```
To activate the environment and start the notebook from it, run
```
conda activate PyLadies-Bayesian-Tutorial
ipython kernel install --user --name=$(basename $(pwd))
jupyter lab
# or jupyter notebook
```

### Using Pip

You can also install the packages from the `requirements.txt` file using pip:
```
pip install -r requirements.txt
```

## Check that it works and extract the data
Open the notebook `1_Introduction.ipynb` in the folder notebooks and try to run the first cell. If it can load all the packages and runs without problems then you should be good to go for the rest of the tutorial!


# The tutorial
The tutorial consists of four notebooks:

- [Introduction](notebooks/1_Introduction.ipynb) which contains some installation checks & extracts the data as well as short motivation why we'd want to use Bayesian methods. If you already know why to use Bayesian methods then this can easily be skipped (except for the installation cell).
- In [Starting simple](notebooks/2_Starting_simple.ipynb), we have a short look at our data and the start constructing a linear regression in PyMC3. We then learn how to understand your prior and experiment with different priors.
- In [Dit it converge](notebooks/3_Dit_it_converge.ipynb), we then finally run our first model and check if everything went well. We'll also have a first look at the results.
- To go [beyond linear](notebooks/4_Beyond_linear.ipnyb), we then extend our linear model by adding some hierarchies. 

The notebooks in the notebook folders contain small exercises and some missing code.
If you prefer to just tag along with the tutorial or get lost at some point, the full notebooks can be found in [solutions](solutions).


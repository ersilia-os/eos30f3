FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

# Create Conda environment
RUN conda create -n chemprop python=3.8

# Activate Conda environment
SHELL ["conda", "run", "--no-capture-output", "-n", "chemprop", "/bin/bash", "-c", "source activate chemprop"]

# Install RDKit and other dependencies
#RUN conda install -c conda-forge rdkit

RUN pip install rdkit

WORKDIR /repo
COPY . /repo

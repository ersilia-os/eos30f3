FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install chemprop
RUN pip install rdkit

WORKDIR /repo
COPY . /repo

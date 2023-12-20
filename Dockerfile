FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2023.9.2
RUN pip install git+https://github.com/bp-kelley/descriptastorus
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn==1.3.2
RUN pip install torch==2.1.1
RUN pip install pandas==2.0.3
RUN pip install scipy>=1.4.1
RUN pip install hyperopt==0.2.7
RUN pip install protobuf==3.18.3


WORKDIR /repo
COPY . /repo

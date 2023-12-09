FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install git+https://github.com/bp-kelley/descriptastorus
RUN pip install tqdm>=4.62.2
RUN pip install typed-argument-parser==1.6.1
RUN pip install scikit-learn
RUN pip install torch
RUN pip install pandas
RUN pip install tensorboardX==2.0
RUN pip install scipy>=1.4.1
RUN pip install hyperopt

#RUN pip install --upgrade protobuf==3.20.0
#RUN pip install protoc >= 3.19.0
#RUN pip install --upgrade bentoml
#ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

WORKDIR /repo
COPY . /repo

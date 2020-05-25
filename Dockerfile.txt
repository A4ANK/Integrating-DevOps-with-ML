FROM centos:latest
RUN yum install python36 -y
RUN pip3 install --upgrade pip setuptools
RUN pip3 install numpy matplotlib 
RUN pip3 install tensorflow
RUN pip3 install keras
LABEL "maintainer"="author"
LABEL "version"="1.0"
LABEL "info"="Used for training model on MNIST Handwritten Digit Dataset"
WORKDIR /storage
COPY mnist.npz .
CMD ["python3","training.py"]

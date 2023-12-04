FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y \
    cmake libsm6 libxext6 libxrender-dev protobuf-compiler \
    && rm -r /var/lib/apt/lists/*

RUN useradd -m gmanbus

COPY --chown=gmanbus:gmanbus . /home/gmanbus/app

USER gmanbus

WORKDIR /home/gmanbus/app

RUN pip install --upgrade pip \
    && pip install --default-timeout=100 Flask pandas Keras-Preprocessing scikit-learn

RUN pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
ENV APP_ENVIRONMENT production
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

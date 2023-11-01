FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y \
        cmake libsm6 libxext6 libxrender-dev protobuf-compiler \
    && rm -r /var/lib/apt/lists/*

RUN useradd -m gmanbus

COPY --chown=gmanbus:gmanbus . /home/gmanbus/app

USER gmanbus

WORKDIR /home/gmanbus/app

RUN pip install --upgrade pip \
    && pip install tensorflow Flask scikit-learn pandas Keras-Preprocessing
ENV APP_ENVIRONMENT production
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM mongo:6.0
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=example
ENV MONGO_INITDB_DATABASE=sampledb
COPY --chown=mongodb:mongodb ./Data/new_data.zip /tmp/
COPY --chown=mongodb:mongodb ./scripts/mongo_import.sh /tmp/mongo_import.sh
RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean
RUN apt-get install -y  zip \
    unzip \
    && rm -rf /var/lib/apt/lists/* \ 
    && mkdir /tmp/data \
    && unzip /tmp/new_data.zip -d /tmp/data
USER mongodb
FROM python:3.5
WORKDIR /usr/src/petshop
ENV PYTHONPATH=/usr/src/petshop
ENV APP_VER=1.0
COPY . .
# RUN wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-oss-6.8.0-amd64.deb && \
RUN dpkg -i filebeat-oss-6.8.0-amd64.deb && \
    rm -rf filebeat-oss-6.8.0-amd64.deb
COPY --chown=root:root filebeat.yml /etc/filebeat/filebeat.yml
RUN chmod 644 /etc/filebeat/filebeat.yml
CMD sed -i "s|APP_VER|$APP_VER|" /etc/filebeat/filebeat.yml && service filebeat start && python ./petshop/main.py
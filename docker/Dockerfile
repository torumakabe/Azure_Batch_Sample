FROM ubuntu:14.04

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y python-pip && \
  pip install azure-storage==0.31.0 pytz && \
  rm -rf /var/lib/apt/lists/*

ADD wordcouny.py /root/wordcouny.py

ENV HOME /root

WORKDIR /root

CMD ["bash"]


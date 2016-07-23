FROM ubuntu:14.04.2

MAINTAINER minimum@cepave.com

ARG DOCKERDIR=docker/ubuntu
ARG PACKFILE=falcon-dashboard.tar.gz
ARG CONFIGDIR=/config
ARG CONFIGFILE=config.py

ENV WORKDIR=/home/dashboard

# Install Open-Falcon Dashboard Component
RUN \
  apt-get update && \
  apt-get install -y python-virtualenv python-dev python-mysqldb && \
  mkdir -p $WORKDIR $CONFIGDIR
ADD $DOCKERDIR/$PACKFILE $WORKDIR
COPY src/$CONFIGFILE $CONFIGDIR/
RUN \
  ln -sf $CONFIGDIR/$CONFIGFILE $WORKDIR/rrd/$CONFIGFILE && \
  virtualenv $WORKDIR/env && \
  pip install -r $WORKDIR/pip_requirements.txt

WORKDIR $WORKDIR
COPY $DOCKERDIR/run.sh $WORKDIR/

# Port
EXPOSE 8081

# Start
ENTRYPOINT ["/bin/bash"]
CMD ["run.sh"]

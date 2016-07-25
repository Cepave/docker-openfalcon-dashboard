FROM ubuntu:14.04.2

MAINTAINER minimum@cepave.com

ARG DOCKERDIR=docker/ubuntu
ARG PACKFILE=falcon-dashboard.tar.gz
ARG CONFIGDIR=/config
ENV WORKDIR=/home/dashboard TZ=Asia/Taipei

# Install Open-Falcon Dashboard Component
RUN \
  apt-get update && \
  apt-get install -y python-virtualenv python-dev python-mysqldb && \
  mkdir -p $WORKDIR $CONFIGDIR
ADD $DOCKERDIR/$PACKFILE $WORKDIR
ARG CONFIGFILE=config.py
COPY src/config.py $CONFIGDIR/$CONFIGFILE
RUN \
  ln -sf $CONFIGDIR/$CONFIGFILE $WORKDIR/rrd/config.py && \
  virtualenv $WORKDIR/env && \
  pip install -r $WORKDIR/pip_requirements.txt

WORKDIR $WORKDIR
COPY $DOCKERDIR/run.sh $WORKDIR/

# Port
EXPOSE 8081

# Start
ENTRYPOINT ["/bin/bash"]
CMD ["run.sh"]

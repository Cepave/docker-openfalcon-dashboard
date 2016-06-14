FROM alpine:3.4

MAINTAINER minimum@cepave.com

ENV WORKDIR=/home/dashboard PACKFILE=falcon-dashboard.tar.gz CONFIGDIR=/config CONFIGFILE=config.py

# Set timezone, bash, config dir
# Set alias in the case of user want to execute control in their terminal
RUN \
  apk add --no-cache tzdata bash \
  && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
  && echo "Asia/Taipei" > /etc/timezone \
  && apk del tzdata \
  && echo "alias ps='pstree'" > ~/.bashrc \
  && mkdir -p $CONFIGDIR

# Install Open-Falcon Dashboard Component
RUN apk add --no-cache python-dev py-virtualenv py-mysqldb
COPY $CONFIGFILE $CONFIGDIR
ADD $PACKFILE $WORKDIR
RUN \
  ln -snf $CONFIGDIR/$CONFIGFILE $WORKDIR/rrd/$CONFIGFILE \
  && virtualenv $WORKDIR/env \
  && pip install -r $WORKDIR/pip_requirements.txt

WORKDIR $WORKDIR
COPY run.sh $WORKDIR

# Port
EXPOSE 8081

# Start
CMD ["bash", "run.sh"]

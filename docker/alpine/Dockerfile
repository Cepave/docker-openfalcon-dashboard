FROM alpine:3.4

MAINTAINER cheminlin@cepave.com

ARG DOCKERDIR=docker/alpine
ARG PACKFILE=falcon-dashboard.tar.gz
ARG CONFIGDIR=/config
ENV WORKDIR=/home/dashboard

# Set timezone, bash, config dir
# Set alias in the case of user want to execute control in their terminal
RUN \
  apk add --no-cache tzdata bash curl \
  && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
  && echo "Asia/Taipei" > /etc/timezone \
  && echo "alias ps='pstree'" > ~/.bashrc \
  && mkdir -p $CONFIGDIR

# Install Open-Falcon Dashboard Component
WORKDIR $WORKDIR
RUN apk add --no-cache py-pip python-dev py-mysqldb
ADD $DOCKERDIR/$PACKFILE $WORKDIR
ARG CONFIGFILE=config.py
ARG GUNICORN_CONFIGFILE=gunicorn.conf
COPY src/config.py $CONFIGDIR/$CONFIGFILE
COPY src/gunicorn.conf $CONFIGDIR/$GUNICORN_CONFIGFILE
COPY $DOCKERDIR/run.sh $WORKDIR/
RUN \
  ln -sf $CONFIGDIR/$CONFIGFILE $WORKDIR/rrd/config.py \
  && ln -sf $CONFIGDIR/$GUNICORN_CONFIGFILE $WORKDIR/gunicorn.conf \
  && pip install -r $WORKDIR/pip_requirements.txt

# Port
EXPOSE 8081

# Start
ENTRYPOINT ["gunicorn"]
CMD ["-c", "gunicorn.conf", "wsgi:app"]
HEALTHCHECK --interval=60s --timeout=2s \
  CMD curl -sSf http://localhost:8081/api/health || exit 1

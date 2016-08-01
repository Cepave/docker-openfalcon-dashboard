# docker-openfalcon-dashboard

## Build

Enter the following command in the repo directory.

```
$ docker build -t openfalcon-dashboard -f docker/ubuntu/Dockerfile .
```

## Run

### Basic Run

Use default configuration, and falcon-dashboard package.

```
$ docker run -d --name dashboard -p 8081:8081 openfalcon-dashboard
```

### Advanced Run

+ Self-defined configuration

    Replace file **config.py** and **gunicorn.conf** in the volume */config*.  
    For more details about **config.py** and **gunicorn.conf**, see [Dashboard](http://book.open-falcon.com/zh/install/dashboard.html).

For example, **config.py** and **gunicorn.conf** in /tmp/config,

```
$ docker run -d --name dashboard -v /tmp/config/config.py:/config/config.py -v /tmp/config/gunicorn.conf:/config/gunicorn.conf -p 8081:8081 openfalcon-dashboard
```

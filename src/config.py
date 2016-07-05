#-*-coding:utf8-*-
import os

#-- dashboard db config --
DASHBOARD_DB_HOST = "127.0.0.1"
DASHBOARD_DB_PORT = 3306
DASHBOARD_DB_USER = "root"
DASHBOARD_DB_PASSWD = ""
DASHBOARD_DB_NAME = "dashboard"

#-- graph db config --
GRAPH_DB_HOST = "127.0.0.1"
GRAPH_DB_PORT = 3306
GRAPH_DB_USER = "root"
GRAPH_DB_PASSWD = ""
GRAPH_DB_NAME = "graph"

#-- app config --
DEBUG = False
SECRET_KEY = "secret-key"
SESSION_COOKIE_NAME = "open-falcon"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
SITE_COOKIE = "open-falcon-ck"

#-- query config --
QUERY_ADDR = "http://127.0.0.1:9966"

BASE_DIR = "/home/dashboard/"
LOG_PATH = os.path.join(BASE_DIR,"log/")

JSONCFG = {}
JSONCFG['database'] = {}
JSONCFG['database']['host']     = '127.0.0.1'
JSONCFG['database']['port']     = '3306'
JSONCFG['database']['account']  = 'root'
JSONCFG['database']['password'] = ''
JSONCFG['database']['db']       = 'uic'
JSONCFG['database']['table']    = 'session'

JSONCFG['shortcut'] = {}
JSONCFG['shortcut']['falconPortal']     = "http://127.0.0.1:5050"
JSONCFG['shortcut']['falconDashboard']  = "http://127.0.0.1:8081"
JSONCFG['shortcut']['grafanaDashboard'] = "http://127.0.0.1:3000"
JSONCFG['shortcut']['falconAlarm']      = "http://127.0.0.1:9912"
JSONCFG['shortcut']['falconUIC']        = "http://127.0.0.1:1234"

JSONCFG['redirectUrl'] = 'http://127.0.0.1:1234/auth/login?callback=http%3A//127.0.0.1:9912/'

try:
    from rrd.local_config import *
except:
    pass


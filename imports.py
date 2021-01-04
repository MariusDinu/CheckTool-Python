from ftplib import FTP
import sys
from elasticsearch import Elasticsearch
import requests as requests
import time
from msvcrt import getch
import msvcrt
import pymongo
import psycopg2
from urllib.parse import urlparse


class DateConn:
    def __init__(self, uri):
        result = urlparse(uri)
        self.username = result.netloc.split(":")[0]
        self.password = result.netloc.split(":")[1]
        print(self.password)
        self.host = result.netloc.split(":")[1].split("@")[1]


class DateFtp:
    def __init__(self, uri):
        result = urlparse(uri)
        self.username = result.netloc.split(":")[0]
        self.port = result.netloc.split(":")[1]
        self.password = result.netloc.split(":")[1].split("@")[0]
        self.host = result.netloc.split(":")[1].split("@")[1]

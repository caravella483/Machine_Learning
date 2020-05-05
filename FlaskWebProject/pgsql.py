import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
from FlaskWebProject import app
import os


DATABASE_URL = os.environ.get('DATABASE_URL', '') or "postgres://yaqfsxtfrvpnqw:0d59a3e541dd796adf2ef1fbf31c2c0d84c46c59d966db0990cd026ca01894d6@ec2-184-72-235-80.compute-1.amazonaws.com:5432/dbftqqmnch7b9g"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)


def getApiInfo():
    print("entering getapiinfo")
    engine = db.engine
    conn = engine.connect()
    data = pd.read_sql("SELECT * FROM apikey where id=1", conn)
    print(data)
    key= data['api_key'][0]
    baseurl = data['base_url'][0]
    print(key)
    return key , baseurl

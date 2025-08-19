import configparser
import os
import pandas as pd

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../configs/config.ini"))

data_dir = config["paths"]["data_dir"]

dropbox = dict(config["dropbox"])

def read_data(filename, from_web=False):
    if from_web:
        return pd.read_csv(dropbox[filename])
    else:
        return pd.read_csv(os.path.join(data_dir, filename))
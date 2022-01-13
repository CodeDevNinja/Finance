import yaml
import os

def get_stocks():
    with open(os.getcwd()+"/config/stock.yaml", "r", encoding="utf8") as f:
        context = yaml.load(f, Loader=yaml.FullLoader)
    return context

def get_email():
    with open(os.getcwd()+"/config/config.yaml", "r", encoding="utf8") as f:
        context = yaml.load(f, Loader=yaml.FullLoader)
    return context
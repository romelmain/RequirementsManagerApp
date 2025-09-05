import yaml
import json
import os


def read_config():
    """Read config file"""
    dic = ""
    with open("config.yaml", "r") as stream:
        try:
            dic = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return dic


def validate_path(company_path):
    """Validate Path"""
    response = False
    if os.path.exists(company_path):
        response = True
    else:
        response = False
    return response

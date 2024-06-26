import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULE_PATH = BASE_DIR + '/config/rule.json'
RFC_DIR = BASE_DIR + "/abnf/rfc/"

with open(RULE_PATH, 'r') as f:
    CONFIG_RULES = json.load(f)
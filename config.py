import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RULE_PATH = BASE_DIR + '/rule.json'

with open(RULE_PATH, 'r') as f:
    CONFIG_RULES = json.load(f)
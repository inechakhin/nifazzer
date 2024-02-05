import random
import os
import numpy as np
import json
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        return json.JSONEncoder.default(self, obj)


def generate_random_url():
    res = []
    for i in range(10000):
        http = "http://"
        count = random.randint(1, 30)
        for j in range(count):
            new_chr = chr(random.randrange(32, 127))
            if chr != " ":
                http += new_chr
        res.append([http])
    with open("fuzz/random.json", "w") as f:
        json.dump(res, f, cls=MyEncoder, ensure_ascii=False, indent=4)


def main():
    generate_random_url()
    name_prog = BASE_DIR + "/url_validation_test.py"
    subprocess.run([sys.executable, name_prog, "random"])


if __name__ == "__main__":
    main()

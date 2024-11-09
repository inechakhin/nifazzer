import json
import sys

from urllib.parse import urlparse

import validators

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import re


def url_validator1(url):
    return validators.url(url)


def url_validator2(url):
    val = URLValidator()
    try:
        val(url)
        return True
    except ValidationError:
        return False
        # traceback.print_exc()


def url_validator3(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def url_validator4(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None


def main():
    name = "fuzz"
    if (len(sys.argv) == 2):
        name = sys.argv[1]
    with open("../fuzz/" + name + ".json", "r") as json_file:
        list_url = json.load(json_file)
        count_full = 0
        count_true1 = 0
        count_true2 = 0
        count_true3 = 0         
        count_true4 = 0
        res_dict = {}
        for t_url in list_url:
            url = t_url[0]
            count_full += 1
            if url_validator1(url) == True:
                count_true1 += 1
            if url_validator2(url) == True:
                count_true2 += 1
            if url_validator3(url) == True:
                count_true3 += 1
            if url_validator4(url) == True:
                count_true4 += 1
        res_dict["Validators"] = str((count_true1 / count_full) * 100) + "%"
        res_dict["Djando validators"] = str((count_true2 / count_full) * 100) + "%"
        res_dict["UrlParse"] = str((count_true3 / count_full) * 100) + "%"
        res_dict["Regex"] = str((count_true4 / count_full) * 100) + "%"
        print(res_dict)


if __name__ == "__main__":
    main()

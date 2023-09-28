import os
import re
import requests
from config import BASE_DIR
from abnf.util import find_index_of_char


class Abnf_Parser:
    def __init__(self) -> None:
        self.rule_list = {}

    def get_rule_list(self) -> dict:
        return self.rule_list

    # download and save the abnf list from a given rfc-link
    def __download_rfc(self, rfc_number: str) -> None:
        html_content = requests.get(
            "https://www.rfc-editor.org/rfc/rfc" + rfc_number
        ).content
        real_html = html_content.decode("utf8")

        regex_start_abnf = re.compile("[ ]*[a-zA-Z0-9-]*[ ]* = .*")
        regex_end_abnf = re.compile("")

        content_list = real_html.split("\n")
        len_content_list = len(content_list)
        abnf_list = []
        i = 0
        while i < len_content_list:
            if regex_start_abnf.match(content_list[i]) != None:
                abnf_list.append(content_list[i])
                if i < len_content_list:
                    while regex_end_abnf.fullmatch(content_list[i + 1]) == None:
                        abnf_list.append(content_list[i + 1])
                        i += 1
            i += 1
        abnf = "\n".join(abnf_list)
        file_path = BASE_DIR + "/abnf/rfc/rfc" + rfc_number + ".txt"
        with open(file_path, "w") as f:
            f.write(abnf)
        return

    # read the abnf list from a given file
    def parse_rule_list(self, rfc_number: str) -> None:
        file_path = BASE_DIR + "/abnf/rfc/rfc" + rfc_number + ".txt"
        if not os.path.exists(file_path):
            self.__download_rfc(rfc_number)

        self.rule_list[rfc_number] = {}
        key = ""
        f = open(file_path, "r")
        for line in f:
            line = line.strip()

            i = find_index_of_char(line, ";")
            line = line[:i]
            if len(line) == 0:
                continue

            i = find_index_of_char(line, "=")
            if i < len(line):
                if len(line[i + 1 :].strip()) <= 1:
                    continue
                key = line[:i].strip()
                self.rule_list[rfc_number][key] = line[i + 1 :]
            else:
                self.rule_list[rfc_number][key] = (
                    self.rule_list[rfc_number][key] + " " + line
                )
        f.close()

        self.__expand_rule_list(rfc_number)

    # expand the abnf list when it comes to another rfc
    def __expand_rule_list(self, rfc_number: str) -> None:
        rfc_list = []
        for key in self.rule_list[rfc_number]:
            rule = self.rule_list[rfc_number][key]
            if "see [RFC" not in rule:
                continue
            reg = re.compile(".*<(?P<name>[^,]*), .*RFC(?P<rfc_num>[0-9]*).*")
            res = reg.match(rule).groupdict()
            if res["rfc_num"] not in rfc_list:
                rfc_list.append(res["rfc_num"])
        for rfc_number in rfc_list:
            self.parse_rule_list(self, rfc_number)
        return

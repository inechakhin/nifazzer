import json

from url_validation_test import url_validator1, url_validator2, url_validator4
from url_parser_correct_rfc_test import test_urllib_urlparse, test_urllib3_parse_url


def main():
    validator_num = int(input("From validator enter number:\n0 - Use validators lib\n1 - Use django lib\n2 - Use regex\n"))
    parser_num = int(input("From parser enter number:\n0 - Use urllib urlparse()\n1 - Use urllib3 parse_url()\n"))
    with open("../fuzz/fuzz.json", "r") as json_file:
        list_url = json.load(json_file)
        for t_url in list_url:
            url_string = t_url[0]
            part_url = t_url[1]
            if validator_num == 0:
                if url_validator1(url_string) == False:
                    continue
            elif validator_num == 1:
                if url_validator2(url_string) == False:
                    continue
            else:
                if url_validator4(url_string) == False:
                    continue
            if parser_num == 0:
                test_urllib_urlparse(url_string, part_url)
            else:
                test_urllib3_parse_url(url_string, part_url)
                


if __name__ == "__main__":
    main()
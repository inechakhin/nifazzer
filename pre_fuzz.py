import json
import numpy as np
import traceback
import sys
from optparse import Values, OptionParser
from abnf.parser import Abnf_Parser
from abnf.generate import Abnf_Generate
from config import BASE_DIR
from mutation import mutation
from util import banner, loading

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        return json.JSONEncoder.default(self, obj)


def generate_all(rfc_number: str, rule_name: str, count: str, parts: str, def_val: str, output: str) -> list:
    list_part = parts.split(",")
    my_abnf_parser = Abnf_Parser()
    my_abnf_parser.parse_rule_list(rfc_number)
    my_abnf_generate = Abnf_Generate(my_abnf_parser.get_rule_list(), list_part, def_val)
    count = int(count)
    res = []
    for i in range(0, count):
        generate_res, part_rule = my_abnf_generate.generate(rule_name, rfc_number)
        if part_rule == {}:
            res.append(generate_res)
        else:
            res.append([generate_res, part_rule])
        print("Generating " + loading(i, count), end='\r')
    save_data(res, output)
    return res


def save_data(data: object, output: str) -> None:
    FUZZ_PATH = BASE_DIR + "/" + output + ".json"
    with open(FUZZ_PATH, "w") as f:
        json.dump(data, f, cls=MyEncoder, ensure_ascii=False, indent=4)


def parse_options() -> Values:
    parser = OptionParser()
    parser.add_option(
        "-r",
        "--rfc",
        dest="rfc",
        default="1738",
        help="the RFC number of the ABNF rule to be extracted",
    )
    parser.add_option(
        "-f",
        "--field",
        dest="field",
        default="url",
        help="the field to be fuzzed in ABNF rules",
    )
    parser.add_option(
        "-c",
        "--count",
        dest="count",
        default="255",
        help="the amount of ambiguity data that needs to be generated according to ABNF rules",
    )
    parser.add_option(
        "-p",
        "--parts",
        dest="parts",
        default="",
        help="the parts of field that needs tracking during generated according to ABNF rules",
    )
    parser.add_option(
        "-d",
        "--default-value",
        dest="def_val",
        default="None",
        help="default value for the tracked part (by standard this is None(Null))"
    )
    parser.add_option(
        "-o",
        "--output",
        dest="output",
        default="fuzz",
        help="name of the json file in which the generation result will be saved"
    )
    (options, args) = parser.parse_args()
    return options


def main():
    try:
        print(banner())
        options = parse_options()
        generate_all(options.rfc, options.field, options.count, options.parts, options.def_val, options.output)
    except Exception as e:
        traceback.print_exc()
        print(("Usage: python " + sys.argv[0] + " [Options] use -h for help"))
        print(("Error: " + str(e)))
        sys.exit()


if __name__ == "__main__":
    main()

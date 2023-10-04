import json
import numpy as np
import traceback
import sys
from optparse import OptionParser
from abnf.abnf_parser import Abnf_Parser
from abnf.abnf_generate import Abnf_Generate
from config import FUZZ_PATH
from mutation import mutation


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        return json.JSONEncoder.default(self, obj)


def generate_all(rfc_number: str, rule_name: str, count: str):
    my_abnf_parser = Abnf_Parser()
    my_abnf_parser.parse_rule_list(rfc_number)
    my_abnf_generate = Abnf_Generate(my_abnf_parser.get_rule_list())
    count = int(count)
    res = []
    for i in range(0, count):
        res.append(my_abnf_generate.generate(rule_name, rfc_number))
    # res = mutation(res)
    data = {}
    data[rule_name] = res
    save_data(data)

    print(res)

    return res


def save_data(data):
    with open(FUZZ_PATH, "w") as f:
        json.dump(data, f, cls=MyEncoder, ensure_ascii=False, indent=4)
    return


def parse_options():
    parser = OptionParser()
    parser.add_option(
        "-r",
        "--rfc",
        dest="rfc",
        default="1738",
        help="The RFC number of the ABNF rule to be extracted.",
    )
    parser.add_option(
        "-f",
        "--field",
        dest="field",
        default="url",
        help="The field to be fuzzed in ABNF rules.",
    )
    parser.add_option(
        "-c",
        "--count",
        dest="count",
        default="255",
        help="The amount of ambiguity data that needs to be generated according to ABNF rules.",
    )
    (options, args) = parser.parse_args()
    return options


def main():
    try:
        # banner?
        options = parse_options()
        generate_all(options.rfc, options.field, options.count)
    except Exception as e:
        traceback.print_exc()
        # print(("Usage: python " + sys.argv[0] + " [Options] use -h for help"))
        # print(("Error: " + str(e)))
        sys.exit()


if __name__ == "__main__":
    main()

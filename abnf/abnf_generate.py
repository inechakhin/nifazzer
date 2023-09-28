from treelib import Tree
import re
from abnf.util import find_pair, get_repeat
from abnf.abnf_basedata import *
from config import CONFIG_RULES

BUILT_IN_RULES = {
    "ALPHA": Alpha(),
    "BIT": Bit(),
    "CHAR": Char(),
    "CR": Cr(),
    "CRLF": Crlf(),
    "CTL": Ctl(),
    "DIGIT": Digit(),
    "DQUOTE": Dquote(),
    "HEXDIG": Hexdig(),
    "HTAB": Htab(),
    "LF": Lf(),
    "SP": Sp(),
    "WSP": Wsp(),
    "LWSP": Lwsp(),
    "OCTET": Octet(),
    "VCHAR": Vchar(),
}


class Abnf_Generate:
    def __init__(self, rule_list: dict) -> None:
        self.rule_list = rule_list

    # make an expression-tree for a given rule
    def __parse_rule(self, rule: str, tree: Tree, curr_nid: int) -> None:
        rule = rule.strip()

        if len(rule) == 0:
            return

        idx = 0
        if rule[0] == "/":
            parent_node = tree.parent(curr_nid)
            if parent_node.tag != "/":
                new_node = tree.create_node(tag="/", parent=parent_node.identifier)
                subtree = tree.remove_subtree(curr_nid)
                tree.paste(new_node.identifier, subtree)

                curr_node = tree.create_node(tag="+", parent=new_node.identifier)
                curr_nid = curr_node.identifier
            else:
                curr_node = tree.create_node(tag="+", parent=parent_node.identifier)
                curr_nid = curr_node.identifier
        elif rule[0] == "[":
            node = tree.create_node(tag="[]", parent=curr_nid)
            node = tree.create_node(tag="+", parent=node.identifier)
            idx = find_pair(rule, "]", 0)
            self.__parse_rule(rule[1:idx], tree, node.identifier)
        elif rule[0] == "<":
            reg = re.compile(".*<(?P<name>[^,]*), .*RFC(?P<rfc_num>[0-9]*).*")
            match = reg.match(rule)
            if match == None:
                node = tree.create_node(tag="<>", parent=curr_nid)
                node = tree.create_node(tag="+", parent=node.identifier)
                idx = find_pair(rule, ">", 0)
                self.__parse_rule(rule[1:idx], tree, node.identifier)
            else:
                res = match.groupdict()
                node = tree.create_node(tag="=>", parent=curr_nid)
                node = tree.create_node(
                    tag=res["name"] + "," + res["rfc_num"], parent=node.identifier
                )
        elif rule[0] == "(":
            node = tree.create_node(tag="()", parent=curr_nid)
            node = tree.create_node(tag="+", parent=node.identifier)
            idx = find_pair(rule, ")", 0)
            self.__parse_rule(rule[1:idx], tree, node.identifier)
        elif rule[0] == '"':
            node = tree.create_node(tag='""', parent=curr_nid)
            idx = find_pair(rule, '"', 0)
            node = tree.create_node(tag=rule[1:idx].encode(), parent=node.identifier)
        elif rule[0] == "%":
            node = tree.create_node(tag="%", parent=curr_nid)
            idx = find_pair(rule, " ", 0)
            node = tree.create_node(tag=rule[1:idx], parent=node.identifier)
        elif rule[0] == "*" or (len(rule) > 1 and rule[1] == "*"):
            reg = re.compile("^(?P<min>[0-9]*)[*](?P<max>[0-9]*)(?P<paren>[(]*)")
            res = reg.match(rule).groupdict()
            node = tree.create_node(
                tag="*" + res["min"] + "," + res["max"], parent=curr_nid
            )
            if res["paren"] != "":
                idx = find_pair(rule, ")", len(res["min"] + "*" + res["max"]))
                self.__parse_rule(
                    rule[len(res["min"] + "*" + res["max"]) : idx + 1],
                    tree,
                    node.identifier,
                )
            else:
                idx = find_pair(rule, " ", len(res["min"] + "*" + res["max"]))
                self.__parse_rule(
                    rule[len(res["min"] + "*" + res["max"]) : idx],
                    tree,
                    node.identifier,
                )
        elif rule[0].isdigit():
            reg = re.compile("^(?P<num>[0-9]*)(?P<paren>[(]*)")
            res = reg.match(rule).groupdict()
            node = tree.create_node(
                tag="*" + res["num"] + "," + res["num"], parent=curr_nid
            )
            if res["paren"] != "":
                idx = find_pair(rule, ")", len(res["num"]))
                self.__parse_rule(
                    rule[len(res["num"]) : idx + 1], tree, node.identifier
                )
            else:
                idx = find_pair(rule, " ", len(res["num"]))
                self.__parse_rule(rule[len(res["num"]) : idx], tree, node.identifier)
        else:
            idx = find_pair(rule, " ", 0)
            node = tree.create_node(tag=rule[:idx], parent=curr_nid)

        self.__parse_rule(rule[idx + 1 :], tree, curr_nid)

    # walk the tree for a random result
    def __parse_tree(self, tree: Tree, nid: int, rfc_number):
        tag = tree.get_node(nid).tag
        children = tree.children(nid)

        res = b""
        if tag == "+":
            for i in range(0, len(children)):
                res += self.__parse_tree(tree, children[i].identifier, rfc_number)
        elif tag == "/":
            idx = random.randint(0, len(children) - 1)
            res += self.__parse_tree(tree, children[idx].identifier, rfc_number)
        elif tag == "()":
            res += self.__parse_tree(tree, children[0].identifier, rfc_number)
        elif tag == "<>":
            res += self.__parse_tree(tree, children[0].identifier, rfc_number)
        elif tag == "[]":
            temp = random.randint(0, 1)
            if temp == 1 and len(children) > 0:
                res += self.__parse_tree(tree, children[0].identifier, rfc_number)
        elif tag[0] == "*":
            atleast, atmost = get_repeat(tag)
            for i in range(0, atleast):
                res += self.__parse_tree(tree, children[0].identifier, rfc_number)
            repeat = atleast
            while repeat < atmost:
                temp = random.randint(0, 1)
                if temp == 1:
                    res += self.__parse_tree(tree, children[0].identifier, rfc_number)
                    repeat = repeat + 1
                else:
                    break
        elif tag == '""':
            if len(children) > 0:
                res = children[0].tag
        elif tag == "%":
            numeric = Numeric(children[0].tag)
            res = numeric.generate()
        elif tag == "=>":
            rule_name, rfc_number = (
                children[0].tag.split(",")[0],
                children[0].tag.split(",")[1],
            )
            res = self.generate(rule_name, rfc_number)
        else:
            rule_name = tag
            res = self.generate(rule_name, rfc_number)
        return res

    # get a random result for a given rule
    def generate(self, rule_name: str, rfc_number: str):
        res = b""
        if rule_name in CONFIG_RULES:
            count = len(CONFIG_RULES[rule_name])
            res = CONFIG_RULES[rule_name][random.randint(0, count - 1)].encode()
        elif rule_name in BUILT_IN_RULES:
            res = BUILT_IN_RULES[rule_name].generate()
        elif rule_name in self.rule_list[rfc_number]:
            rule = self.rule_list[rfc_number][rule_name]
            tree = Tree()
            tree.create_node(tag="+")
            node = tree.create_node(tag="+", parent=tree.root)
            self.__parse_rule(rule, tree, node.identifier)
            res = self.__parse_tree(tree, tree.root, rfc_number)
        else:
            print("Error: unknown rule name <" + rule_name + ">")
        return res

import json
import re

from email.utils import parseaddr

from validate_email import validate_email


def email_validator1(email):
    regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return re.match(regex, email) is not None


def email_validator2(email):
    regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    return re.match(regex, email) is not None


def email_validator3(email):
    regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(regex, email) is not None


def email_validator4(email):
    regex = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    return re.match(regex, email) is not None


def email_validator5(email):
    tuple = parseaddr(email)
    if tuple[1] == "":
        return False
    else:
        return True


def email_validator6(email):
    return validate_email(email)


def main():
    with open("fuzz/email_fuzz.json", "r") as json_file:
        list_email = json.load(json_file)
        count_full = 0
        count_true1 = 0
        count_true2 = 0
        count_true3 = 0
        count_true4 = 0
        count_true5 = 0
        # count_true6 = 0
        res_dict = {}
        for email in list_email:
            count_full += 1
            if email_validator1(email) == True:
                count_true1 += 1
            if email_validator2(email) == True:
                count_true2 += 1
            if email_validator3(email) == True:
                count_true3 += 1
            if email_validator4(email) == True:
                count_true4 += 1
            if email_validator5(email) == True:
                count_true5 += 1
            # long time of calculate
            # if email_validator6(email) == True:
            #   count_true6 += 1
        res_dict["Regex1"] = str((count_true1 / count_full) * 100) + "%"
        res_dict["Regex2"] = str((count_true2 / count_full) * 100) + "%"
        res_dict["Regex3"] = str((count_true3 / count_full) * 100) + "%"
        res_dict["Regex4"] = str((count_true4 / count_full) * 100) + "%"
        res_dict["email.utils"] = str((count_true5 / count_full) * 100) + "%"
        # res_dict["validate_email"] = str((count_true6 / count_full) * 100) + "%"
        print(res_dict)


if __name__ == "__main__":
    main()

import json

from urllib.parse import urlparse

from urllib3.util import parse_url


def test_urllib_urlparse(url, part_url):
    try:
        o = urlparse(url)
        if (part_url["scheme"] != None):
            if (o.scheme != None):
                if (o.scheme != part_url["scheme"]):
                    print("Problem in scheme:\n", url, "\n", part_url["scheme"], "\n", o.scheme)
            else:
                print("Problem in scheme:\n", url, "\n", part_url["scheme"], "\n", "Not parsing")
        if (o.username != None):
            if (o.password != None):
                userinfo = o.username + ":" + o.password
            else:
                userinfo = o.username
        else:
            userinfo = None
        if (part_url["userinfo"] != None and part_url["userinfo"] != ''):
            if (userinfo != None):
                if (userinfo != part_url["userinfo"]):
                    print("Problem in userinfo:", url, "\n", part_url["userinfo"], "\n", userinfo)
            else:
                print("Problem in userinfo:", url, "\n", part_url["userinfo"], "\n", "Not parsing")
        if (part_url["host"] != None and part_url["host"] != ''):
            if (o.hostname != None):
                if (o.hostname != part_url["host"].lower()):
                    print("Problem in host:", url, "\n", part_url["host"], "\n", o.hostname)
            else:
                print("Problem in host:", url, "\n", part_url["host"], "\n", "Not parsing")
        if (part_url["port"] != None and part_url["port"] != ''):
            if (o.port != None):
                if (o.port != int(part_url["port"])):
                    print("Problem in port:", url, "\n", part_url["port"], "\n", o.port)
            else:
                print("Problem in port:", url, "\n", part_url["port"], "\n", "Not parsing")
        if (part_url["path-abempty"] != ''):
            if (o.path != ''):
                if (o.path != part_url["path-abempty"]):
                    print("Problem in path-abempty:", url, "\n", part_url["path-abempty"], "\n", o.path)
            else:
                print("Problem in path-abempty:", url, "\n", part_url["path-abempty"], "\n", "Not parsing")
        if (part_url["query"] != None and part_url["query"] != ''):
            if (o.query != ''):
                if (o.query != part_url["query"]):
                    print("Problem in query:", url, "\n", part_url["query"], "\n", o.query)
            else:
                print("Problem in query:", url, "\n", part_url["query"], "\n", "Not parsing")
        if (part_url["fragment"] != None and part_url["fragment"] != ''):
            if (o.fragment != ''):
                if (o.fragment != part_url["fragment"]):
                    print("Problem in fragment:", url, "\n", part_url["fragment"], "\n", o.fragment)
            else:
                print("Problem in fragment:", url, "\n", part_url["fragment"], "\n", "Not parsing")
    except:
        pass
        

def test_urllib3_parse_url(url, part_url):
    try:
        scheme, auth, host, port, path, query, fragment = parse_url(url)
        if (part_url["scheme"] != None):
            if (scheme != None):
                if (scheme != part_url["scheme"]):
                    print("Problem in scheme:\n", url, "\n", part_url["scheme"], "\n", scheme)
            else:
                print("Problem in scheme:\n", url, "\n", part_url["scheme"], "\n", "Not parsing")
        if (part_url["userinfo"] != None and part_url["userinfo"] != ''):
            if (auth != None):
                if (auth != part_url["userinfo"]):
                    print("Problem in userinfo:", url, "\n", part_url["userinfo"], "\n", auth)
            else:
                print("Problem in userinfo:", url, "\n", part_url["userinfo"], "\n", "Not parsing")
        if (part_url["host"] != None and part_url["host"] != ''):
            if (host != None):
                if (host != part_url["host"].lower()):
                    print("Problem in host:", url, "\n", part_url["host"], "\n", host)
            else:
                print("Problem in host:", url, "\n", part_url["host"], "\n", "Not parsing")
        if (part_url["port"] != None and part_url["port"] != ''):
            if (port != None):
                if (port != int(part_url["port"])):
                    print("Problem in port:", url, "\n", part_url["port"], "\n", port)
            else:
                print("Problem in port:", url, "\n", part_url["port"], "\n", "Not parsing")
        if (part_url["path-abempty"] != None and part_url["path-abempty"] != ''):
            if (path != None):
                if (path != part_url["path-abempty"]):
                    print("Problem in path-abempty:", url, "\n", part_url["path-abempty"], "\n", path)
            else:
                print("Problem in path-abempty:", url, "\n", part_url["path-abempty"], "\n", "Not parsing")
        if (part_url["query"] != None):
            if (query != None):
                if (query != part_url["query"]):
                    print("Problem in query:", url, "\n", part_url["query"], "\n", query)
            else:
                print("Problem in query:", url, "\n", part_url["query"], "\n", "Not parsing")
        if (part_url["fragment"] != None):
            if (fragment != None):
                if (fragment != part_url["fragment"]):
                    print("Problem in fragment:", url, "\n", part_url["fragment"], "\n", fragment)
            else:
                print("Problem in fragment:", url, "\n", part_url["fragment"], "\n", "Not parsing")
    except:
        pass


def main():
    num = int(input("Enter number:\n0 - Use urllib urlparse()\n1 - Use urllib3 parse_url()\n"))
    with open("fuzz/fuzz.json", "r") as json_file:
        list_url = json.load(json_file)
        for t_url in list_url:
            if (num == 0) :
                test_urllib_urlparse(t_url[0], t_url[1])
            else:
                test_urllib3_parse_url(t_url[0], t_url[1])


if __name__ == "__main__":
    main()

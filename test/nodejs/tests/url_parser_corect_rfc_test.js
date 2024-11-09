import url from 'url';
import fs from 'fs';
import whatwg from 'whatwg-url';
import readline from "readline";

function test_url(urlAddress, partUrl) {
    let parseUrl = url.parse(urlAddress, false);
    if (partUrl["scheme"] != null) {
        if (parseUrl["protocol"] != null) {
            if ((partUrl["scheme"] + ':').localeCompare(parseUrl["protocol"]) != 0) {
                console.log("Problem in scheme:\n", urlAddress, "\n", partUrl["scheme"], "\n", parseUrl["protocol"])
            }
        } else {
            console.log("Problem in scheme:\n", urlAddress, "\n", partUrl["scheme"], "\nNot parsing")
        }
    }
    if (partUrl["userinfo"] != null) {
        if (parseUrl["auth"] != null) {
            if (partUrl["userinfo"].localeCompare(parseUrl["auth"]) != 0) {
                console.log("Problem in userinfo:\n", urlAddress, "\n", partUrl["userinfo"], "\n", parseUrl["auth"])
            }
        } else {
            console.log("Problem in userinfo:\n", urlAddress, "\n", partUrl["userinfo"], "\nNot Parsing")
        }
    }
    if (partUrl["host"] != null) {
        if (parseUrl["hostname"] != null) {
            if (partUrl["host"].toLowerCase().localeCompare(parseUrl["hostname"]) != 0) {
                console.log("Problem in host:\n", urlAddress, "\n", partUrl["host"], "\n", parseUrl["hostname"])
            }
        } else {
            console.log("Problem in host:\n", urlAddress, "\n", partUrl["host"], "\nNot parsing")
        }
    }
    if (partUrl["port"] != null && partUrl["port"].localeCompare('') != 0) {
        if (parseUrl["port"] != null) {
            if (partUrl["port"].localeCompare(parseUrl["port"]) != 0) {
                console.log("Problem in port:\n", urlAddress, "\n", partUrl["port"], "\n", parseUrl["port"])
            }
        } else {
            console.log("Problem in port:\n", urlAddress, "\n", partUrl["port"], "\nNot parsing")
        }
    }
    if (partUrl["path-abempty"] != null) {
        if (parseUrl["pathname"] != null) {
            if (partUrl["path-abempty"].localeCompare(parseUrl["pathname"]) != 0) {
                console.log("Problem in path-abempty:\n", urlAddress, "\n", partUrl["path-abempty"], "\n", parseUrl["pathname"])
            }
        } else {
            console.log("Problem in path-abempty:\n", urlAddress, "\n", partUrl["path-abempty"], "\nNot parsing")
        }
    }
    if (partUrl["query"] != null) {
        if (parseUrl["query"] != null) {
            if (partUrl["query"].localeCompare(parseUrl["query"]) != 0) {
                console.log("Problem in query:\n", urlAddress, "\n", partUrl["query"], "\n", parseUrl["query"])
            }
        } else {
            console.log("Problem in query:\n", urlAddress, "\n", partUrl["query"], "\nNot parsing")
        }
    }
    if (partUrl["fragment"] != null) {
        if (parseUrl["hash"] != null) {
            if (('#' + partUrl["fragment"]).localeCompare(parseUrl["hash"]) != 0) {
                console.log("Problem in fragment:\n", urlAddress, "\n", partUrl["fragment"], "\n", parseUrl["hash"])
            }
        } else {
            console.log("Problem in fragment:\n", urlAddress, "\n", partUrl["fragment"], "\nNot parsing")
        }
    }
}


function test_whatwg_url(urlAddress, partUrl) {
    let parseUrl = whatwg.parseURL(urlAddress);
    if (parseUrl == null) {
        return;
    }
    if (partUrl["scheme"] != null) {
        if (parseUrl["scheme"] != null) {
            if ((partUrl["scheme"] + ':').localeCompare(parseUrl["scheme"]) != 0) {
                console.log("Problem in scheme:\n", urlAddress, "\n", partUrl["scheme"], "\n", parseUrl["scheme"])
            }
        } else {
            console.log("Problem in scheme:\n", urlAddress, "\n", partUrl["scheme"], "\nNot parsing")
        }
    }
    let userinfo;
    if (parseUrl["username"] == null && parseUrl["password"] == null) {
        userinfo = null;
    } else if (parseUrl["username"] != null && parseUrl["password"] == null) {
        userinfo = parseUrl["username"];
    } else {
        userinfo = parseUrl["username"] + ":" + parseUrl["password"]
    }
    if (partUrl["userinfo"] != null) {
        if (userinfo != null) {
            if (partUrl["userinfo"].localeCompare(userinfo) != 0) {
                console.log("Problem in userinfo:\n", urlAddress, "\n", partUrl["userinfo"], "\n", userinfo)
            }
        } else {
            console.log("Problem in userinfo:\n", urlAddress, "\n", partUrl["userinfo"], "\nNot Parsing")
        }
    }
    if (partUrl["host"] != null) {
        if (parseUrl["host"] != null) {
            if (partUrl["host"].toLowerCase().localeCompare(parseUrl["host"]) != 0) {
                console.log("Problem in host:\n", urlAddress, "\n", partUrl["host"], "\n", parseUrl["host"])
            }
        } else {
            console.log("Problem in host:\n", urlAddress, "\n", partUrl["host"], "\nNot parsing")
        }
    }
    if (partUrl["port"] != null && partUrl["port"].localeCompare('') != 0) {
        if (parseUrl["port"] != null) {
            if (partUrl["port"].localeCompare(parseUrl["port"]) != 0) {
                console.log("Problem in port:\n", urlAddress, "\n", partUrl["port"], "\n", parseUrl["port"])
            }
        } else {
            console.log("Problem in port:\n", urlAddress, "\n", partUrl["port"], "\nNot parsing")
        }
    }
    if (partUrl["path-abempty"] != null) {
        if (parseUrl["path"] != null) {
            if (partUrl["path-abempty"].localeCompare(parseUrl["path"]) != 0) {
                console.log("Problem in path-abempty:\n", urlAddress, "\n", partUrl["path-abempty"], "\n", parseUrl["path"])
            }
        } else {
            console.log("Problem in path-abempty:\n", urlAddress, "\n", partUrl["path-abempty"], "\nNot parsing")
        }
    }
    if (partUrl["query"] != null) {
        if (parseUrl["query"] != null) {
            if (partUrl["query"].localeCompare(parseUrl["query"]) != 0) {
                console.log("Problem in query:\n", urlAddress, "\n", partUrl["query"], "\n", parseUrl["query"])
            }
        } else {
            console.log("Problem in query:\n", urlAddress, "\n", partUrl["query"], "\nNot parsing")
        }
    }
    if (partUrl["fragment"] != null) {
        if (parseUrl["fragment"] != null) {
            if (('#' + partUrl["fragment"]).localeCompare(parseUrl["fragment"]) != 0) {
                console.log("Problem in fragment:\n", urlAddress, "\n", partUrl["fragment"], "\n", parseUrl["fragment"])
            }
        } else {
            console.log("Problem in fragment:\n", urlAddress, "\n", partUrl["fragment"], "\nNot parsing")
        }
    }
}

export function runParserTest() {
    fs.readFile('../fuzz/fuzz.json', (err, data) => {
        if (err) {
            console.log("Error reading file from disk: ${err}");
        } else {
            const read = readline.createInterface({
                input: process.stdin,
                output: process.stdout,
            });
            read.question("Choose option:\n0 - Use url lib\n1 - Use whatwg-url lib\n", num => {
                const listUrl = JSON.parse(data)
                listUrl.forEach(tUrl => {
                    let urlAddress = tUrl[0];
                    const partUrl = tUrl[1];
                    try {
                        if (num == 0) {
                            test_url(urlAddress, partUrl);
                        } else {
                            test_whatwg_url(urlAddress, partUrl);
                        }
                    } catch (e) { }
                });
                read.close();
            });
        }
    })
}

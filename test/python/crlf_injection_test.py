import json
import os
import webbrowser

import requests

import urllib3

from urllib.parse import urlparse


# api_url = "https://webhook.site/bd5bf9ae-61a3-4236-847c-852ad98ea695/crlfsuite\r\n%20Set-Cookie:nefcore=crlfsuite;"
# api_url = "https://webhook.site%0d%0aSet-Cookie:nefcore=crlfsuite;/bd5bf9ae-61a3-4236-847c-852ad98ea695/crlfsuite"
# api_url = "https://webhook.site/bd5bf9ae-61a3-4236-847c-852ad98ea695"
api_url = "http://+@google.com#@example.com"

import logging
import http.client as http_client

http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def use_requests(api_url):
    urlparse(api_url)
    requests.get(
        api_url, headers={"Host": "webhook.site\r\nSet-Cookie:nefcore=crlfsuite;"}
    )

    http = urllib3.PoolManager()
    response = http.request("GET", api_url)

    # json_response = json.loads(response.text)
    return


use_requests(api_url)

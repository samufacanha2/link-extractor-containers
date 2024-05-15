import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import ssl
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager


class UnsafeLegacyAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.options |= 0x4  # SSL_OP_LEGACY_SERVER_CONNECT
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        kwargs["ssl_context"] = context
        return super(UnsafeLegacyAdapter, self).init_poolmanager(*args, **kwargs)


def extract_links(url):
    session = requests.Session()
    session.mount("https://", UnsafeLegacyAdapter())
    res = session.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    base = url
    links = []
    for link in soup.find_all("a"):
        links.append(
            {
                "text": " ".join(link.text.split()) or "[IMG]",
                "href": urljoin(base, link.get("href")),
            }
        )
    return links


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(sys.argv[-1]):
        print("[{}]({})".format(link["text"], link["href"]))

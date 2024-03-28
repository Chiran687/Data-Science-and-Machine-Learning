import requests
from Example import timer

url = "https://httpbin.org/uuid"


def fetch(session, url):
    with session.get(url) as respomse:
        print(respomse.json()['uuid'])


@timer(1, 1)
def main():
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, url)

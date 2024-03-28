import requests
from Week_3.Day_4.Example import timer
from concurrent.futures import ProcessPoolExecutor

url = "https://httpbin.org/uuid"


def fetch(session, url):
    with session.get(url) as respomse:
        print(respomse.json()['uuid'])


@timer(1, 5)
def main():
    with ProcessPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 100, [url] * 100)
            executor.shutdown(wait=True)

#!/usr/bin/env python3
import requests
import random
import time
from generators import gen_txid, gen_addr


def post(endpoint, data=None):
    r = requests.post('http://localhost:8080' + endpoint, data=data)
    r.raise_for_status()


def add_edge(from_, to, value):
    post('/add-edge', {
        'from':   from_,
        'to':     to,
        'value':  value,
        'title':  '{value} FTM at {txid}'.format(value=value, txid=gen_txid()),
    })


def main():
    post('/reset')

    N, M = 100, 30

    for _ in range(N):
        post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})

    post('/ready')

    time.sleep(1)

    post('/add-vertex', {'value': '100', 'group': '2', 'title': gen_addr()})
    post('/add-vertex', {'value': '10', 'group': '3', 'title': gen_addr()})
    add_edge(N, N + 1, 2)

    for i in range(M):
        time.sleep(1)
        add_edge(N, i, 1)


if __name__ == '__main__':
    main()

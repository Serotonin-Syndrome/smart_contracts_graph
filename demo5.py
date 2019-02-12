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

    N, NROUNDS = 200, 6

    for _ in range(N):
        post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})

    post('/ready')

    time.sleep(1)

    # creator
    post('/add-vertex', {'value': '10', 'group': '2', 'title': gen_addr()})
    add_edge(N, 0, 0)

    for i in range(1, NROUNDS):
        m = 1 << i
        for j in range(m):
            time.sleep(0.5)
            add_edge(
                (m // 2 + j // 2) - 1,
                (m + j) - 1,
                0)


if __name__ == '__main__':
    main()

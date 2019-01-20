#!/usr/bin/env python3
import requests
import random
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

    for i in range(200):
        group = 1+(i // 10) if i < 30 else 0
        value = 100         if i < 30 else 1
        post('/add-vertex', {'value': str(value), 'group': str(group), 'title': gen_addr()})

    for i in range(3):
        for _ in range(20):
            while True:
                from_ = random.randint(i * 10, (i + 1) * 10 - 1)
                to    = random.randint(i * 10, (i + 1) * 10 - 1)
                if from_ != to:
                    break
            add_edge(str(from_), str(to), '50')

    post('/ready')


if __name__ == '__main__':
    main()

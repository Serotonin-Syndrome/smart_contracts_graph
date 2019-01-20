#!/usr/bin/env python3
import requests
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

    # 0
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 1
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 2
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 3
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 4
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 5
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 6
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 7
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 8
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 9
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 10
    post('/add-vertex', {'value': '10', 'group': '3', 'title': gen_addr()})
    # 11
    post('/add-vertex', {'value': '10', 'group': '3', 'title': gen_addr()})

    add_edge('0', '2', '20')
    add_edge('1', '2', '15')
    add_edge('2', '3', '24')
    add_edge('2', '4', '10')
    add_edge('3', '4', '12')
    add_edge('0', '9', '9')
    add_edge('5', '8', '8')
    add_edge('6', '7', '7')

    post('/ready')


if __name__ == '__main__':
    main()

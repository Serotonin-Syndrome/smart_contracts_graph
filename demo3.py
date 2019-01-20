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
    post('/add-vertex', {'value': '2', 'group': '1', 'title': gen_addr()})
    # 1
    post('/add-vertex', {'value': '2', 'group': '1', 'title': gen_addr()})
    # 2
    post('/add-vertex', {'value': '2', 'group': '1', 'title': gen_addr()})
    # 3
    post('/add-vertex', {'value': '2', 'group': '1', 'title': gen_addr()})

    # 4
    post('/add-vertex', {'value': '15', 'group': '2', 'title': gen_addr()})
    # 5
    post('/add-vertex', {'value': '10',  'group': '3', 'title': gen_addr()})

    # 6
    post('/add-vertex', {'value': '2', 'group': '1', 'title': gen_addr()})

    # 7
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})
    # 8
    post('/add-vertex', {'value': '10', 'group': '1', 'title': gen_addr()})

    # 9
    post('/add-vertex', {'value': '10', 'group': '5', 'title': gen_addr()})
    # 10
    post('/add-vertex', {'value': '9', 'group': '5', 'title': gen_addr()})
    # 11
    post('/add-vertex', {'value': '8', 'group': '5', 'title': gen_addr()})
    # 12
    post('/add-vertex', {'value': '7', 'group': '5', 'title': gen_addr()})
    # 13
    post('/add-vertex', {'value': '6', 'group': '5', 'title': gen_addr()})

    add_edge('0', '1', '1')
    add_edge('0', '2', '1')
    add_edge('0', '3', '1')
    add_edge('0', '4', '5')
    add_edge('0', '5', '0')
    add_edge('4', '6', '2')
    add_edge('4', '5', '10')
    add_edge('7', '5', '3')
    add_edge('4', '8', '1')
    add_edge('4', '8', '1')

    post('/ready')


if __name__ == '__main__':
    main()

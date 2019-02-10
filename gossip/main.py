#!/usr/bin/env python3
import bottle
import os
import json


STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def _json(obj):
    bottle.response.content_type = 'application/json'
    return json.dumps(obj)


@bottle.get('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root=STATIC_ROOT)


@bottle.get('/')
def index():
    return bottle.redirect('/static/index.html')


@bottle.get('/network')
def network():
    NROUNDS = 8

    edges = []
    for i in range(1, NROUNDS):
        m = 1 << i
        for j in range(m):
            edges.append((m // 2 + j // 2, m + j))

    return _json({
        'edges': edges,
        'size': (1 << NROUNDS) - 1,
        'start_from': 1,
    })


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8035)

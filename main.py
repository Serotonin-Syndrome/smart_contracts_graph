#!/usr/bin/env python3
import bottle
import json
from collections import defaultdict
import os


STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def _json(obj):
    bottle.response.content_type = 'application/json'
    return json.dumps(obj)


VERTICES = []
EDGES = []
TITLES_BY_EDGE = defaultdict(list)
READY = False
EPOCH = 0


@bottle.get('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root=STATIC_ROOT)


@bottle.get('/')
def index():
    return bottle.redirect('/static/index.html')


@bottle.get('/get-epoch')
def get_epoch():
    return _json({'epoch': EPOCH})


@bottle.get('/get-graph')
def get_graph():
    epoch = int(bottle.request.query['epoch'])
    since_v = int(bottle.request.query['since_v'])
    since_e = int(bottle.request.query['since_e'])

    if epoch != -1 and epoch != EPOCH:
        return bottle.HTTPError(418)

    if not READY:
        return _json({'vertices': [], 'edges': []})

    return _json({'vertices': VERTICES[since_v:], 'edges': EDGES[since_e:]})


@bottle.get('/get-edge-titles')
def get_edge_titles():
    assert READY

    from_  = int(bottle.request.query['from'])
    to     = int(bottle.request.query['to'])

    return _json(TITLES_BY_EDGE[(from_, to)])


@bottle.post('/add-vertex')
def add_vertex():
    value = float(bottle.request.forms['value'])
    group = int(bottle.request.forms['group'])
    title = bottle.request.forms['title']

    index = len(VERTICES)
    VERTICES.append((value, group, title))

    return _json({'ok': True, 'index': index})


@bottle.post('/add-edge')
def add_edge():
    from_  = int(bottle.request.forms['from'])
    to     = int(bottle.request.forms['to'])
    value  = float(bottle.request.forms['value'])
    title  = bottle.request.forms['title']

    TITLES_BY_EDGE[(from_, to)].append(title)
    EDGES.append((from_, to, value))

    return _json({'ok': True})


@bottle.post('/ready')
def ready():
    global READY
    READY = True

    return _json({'ok': True})


@bottle.post('/reset')
def reset():
    global READY, VERTICES, EDGES, TITLES_BY_EDGE, EPOCH

    READY = False
    VERTICES = []
    EDGES = []
    TITLES_BY_EDGE = defaultdict(list)
    EPOCH += 1

    return _json({'ok': True})


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080)

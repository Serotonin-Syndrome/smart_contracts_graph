#!/usr/bin/env python3
import bottle
import json
from collections import defaultdict


VERTICES = []
EDGES = []
TITLES_BY_EDGE = defaultdict(list)
READY = False
EPOCH = 0


@bottle.get('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static')


@bottle.get('/')
def index():
    return bottle.redirect('/static/index.html')


@bottle.get('/get-epoch')
def get_epoch():
    return json.dumps({'epoch': EPOCH})


@bottle.get('/get-graph')
def get_graph():
    epoch = int(bottle.request.query['epoch'])
    since_v = int(bottle.request.query['since_v'])
    since_e = int(bottle.request.query['since_e'])

    if epoch != -1 and epoch != EPOCH:
        return bottle.HTTPError(418)

    if not READY:
        return json.dumps({'vertices': [], 'edges': []})

    bottle.response.content_type = 'application/json'
    return json.dumps({'vertices': VERTICES[since_v:], 'edges': EDGES[since_e:]})


@bottle.get('/get-edge-titles')
def get_edge_titles():
    assert READY

    from_  = int(bottle.request.query['from'])
    to     = int(bottle.request.query['to'])

    bottle.response.content_type = 'application/json'
    return json.dumps(TITLES_BY_EDGE[(from_, to)])


@bottle.post('/add-vertex', method='post')
def add_vertex():
    value = float(bottle.request.forms['value'])
    group = int(bottle.request.forms['group'])
    title = bottle.request.forms['title']

    VERTICES.append((value, group, title))

    bottle.response.content_type = 'application/json'
    return json.dumps({'ok': True})


@bottle.post('/add-edge', method='post')
def add_edge():
    from_  = int(bottle.request.forms['from'])
    to     = int(bottle.request.forms['to'])
    value  = float(bottle.request.forms['value'])
    title  = bottle.request.forms['title']

    TITLES_BY_EDGE[(from_, to)].append(title)
    EDGES.append((from_, to, value))

    bottle.response.content_type = 'application/json'
    return json.dumps({'ok': True})


@bottle.post('/ready', method='post')
def ready():
    global READY
    READY = True

    bottle.response.content_type = 'application/json'
    return json.dumps({'ok': True})


@bottle.post('/reset', method='post')
def reset():
    global READY, VERTICES, EDGES, TITLES_BY_EDGE, EPOCH

    READY = False
    VERTICES = []
    EDGES = []
    TITLES_BY_EDGE = defaultdict(list)
    EPOCH += 1

    bottle.response.content_type = 'application/json'
    return json.dumps({'ok': True})


if __name__ == '__main__':
    bottle.run(host="0.0.0.0", port=8080)

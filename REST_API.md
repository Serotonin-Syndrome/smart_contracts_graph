The server maintains a directed graph with vertices and edges having numeric
values.

The state may be either locked on unlocked; locked means all the changes being
made are not flushed to the front-end immediately; unlocked means they are.
Initially, the state is locked.

Following is the list of REST API endpoints; use POST method to access all of
these. The base URL is `http://localhost:8080`.

# `/reset`

Resets the state to the initial one; that is, clears the graph and locks the
state.

### Request:

(no fields)

### Response example:

````
{"ok": true}
````

# `/ready`

Unlocks the state and flushes the current state to the front-end.

**You have to call this method in order to have anything shown!**

### Request:

(no fields)

### Response example:

````
{"ok": true}
````

# `/add-vertex`

Add a vertex to the graph.

### Request:

|  Key     | Type   | Explanation                            |
| -------- | ------ | -------------------------------------- |
| `value`  | float  | vertex size relative to other vertices |
| `group`  | int    | vertex group ID (used for coloring)    |
| `title`  | string | information about the vertex           |

### Response example:

````
{"ok": true, "index": 0}
````

# `/add-edge`

### Request:

Add an edge to the graph.

|  Key     | Type   | Explanation                            |
| -------- | ------ | -------------------------------------- |
| `from`   | int    | “from” vertex index                    |
| `to`     | int    | “to” vertex index                      |
| `value`  | float  | edge size relative to other edges      |
| `title`  | string | information about the edge             |

### Response example:

````
{"ok": true}
````

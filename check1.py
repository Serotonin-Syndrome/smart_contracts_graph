#!/usr/bin/env python3
import requests


def assert_eq(endpoint, obj):
    r = requests.get('http://localhost:8080' + endpoint)
    r.raise_for_status()
    found = r.json()
    if found != obj:
        print('=== ERROR ===')
        print('ENDPOINT:', endpoint)
        print('EXPECTED:', obj)
        print('FOUND:', found)
        exit(1)

    print(endpoint, 'OK')


def main():
    assert_eq(
        '/get-graph?epoch=-1&since_v=0&since_e=0',
        {
            "vertices": [
                [2001.0, 1, "00000001"],
                [952.0, 1, "00000003"],
                [952.0, 1, "00000004"],
                [952.0, 1, "00000005"],
                [952.0, 1, "00000006"],
                [952.0, 1, "00000007"],
                [952.0, 1, "00000008"],
                [952.0, 1, "00000009"],
                [0.0, 2, "00000002"],
            ],
            "edges": [
                [0, 8, 10.0],
                [1, 8, 1.0],
                [8, 1, 1.0],
                [1, 8, 2.0],
                [8, 1, 2.0],
                [1, 8, 3.0],
                [8, 1, 3.0],
                [2, 8, 1.0],
                [8, 2, 1.0],
                [2, 8, 2.0],
                [8, 2, 2.0],
                [2, 8, 3.0],
                [8, 2, 3.0],
                [3, 8, 1.0],
                [8, 3, 1.0],
                [3, 8, 2.0],
                [8, 3, 2.0],
                [3, 8, 3.0],
                [8, 3, 3.0],
                [4, 8, 1.0],
                [8, 4, 1.0],
                [4, 8, 2.0],
                [8, 4, 2.0],
                [4, 8, 3.0],
                [8, 4, 3.0],
                [5, 8, 1.0],
                [8, 5, 1.0],
                [5, 8, 2.0],
                [8, 5, 2.0],
                [5, 8, 3.0],
                [8, 5, 3.0],
                [6, 8, 1.0],
                [8, 6, 1.0],
                [6, 8, 2.0],
                [8, 6, 2.0],
                [6, 8, 3.0],
                [8, 6, 3.0],
                [7, 8, 1.0],
                [8, 7, 1.0],
                [7, 8, 2.0],
                [8, 7, 2.0],
                [7, 8, 3.0],
                [8, 7, 3.0],
            ],
        }
    )

    assert_eq('/get-edge-titles?from=0&to=0', [])
    assert_eq('/get-edge-titles?from=0&to=1', [])
    assert_eq('/get-edge-titles?from=0&to=2', [])
    assert_eq('/get-edge-titles?from=0&to=3', [])
    assert_eq('/get-edge-titles?from=0&to=4', [])
    assert_eq('/get-edge-titles?from=0&to=5', [])
    assert_eq('/get-edge-titles?from=0&to=6', [])
    assert_eq('/get-edge-titles?from=0&to=7', [])
    assert_eq('/get-edge-titles?from=0&to=8', ["10 FTM at 000000000a"])
    assert_eq('/get-edge-titles?from=1&to=0', [])
    assert_eq('/get-edge-titles?from=1&to=1', [])
    assert_eq('/get-edge-titles?from=1&to=2', [])
    assert_eq('/get-edge-titles?from=1&to=3', [])
    assert_eq('/get-edge-titles?from=1&to=4', [])
    assert_eq('/get-edge-titles?from=1&to=5', [])
    assert_eq('/get-edge-titles?from=1&to=6', [])
    assert_eq('/get-edge-titles?from=1&to=7', [])
    assert_eq('/get-edge-titles?from=1&to=8', ["1 FTM at 000000000b", "2 FTM at 000000000d", "3 FTM at 000000000f"])
    assert_eq('/get-edge-titles?from=2&to=0', [])
    assert_eq('/get-edge-titles?from=2&to=1', [])
    assert_eq('/get-edge-titles?from=2&to=2', [])
    assert_eq('/get-edge-titles?from=2&to=3', [])
    assert_eq('/get-edge-titles?from=2&to=4', [])
    assert_eq('/get-edge-titles?from=2&to=5', [])
    assert_eq('/get-edge-titles?from=2&to=6', [])
    assert_eq('/get-edge-titles?from=2&to=7', [])
    assert_eq('/get-edge-titles?from=2&to=8', ["1 FTM at 0000000011", "2 FTM at 0000000013", "3 FTM at 0000000015"])
    assert_eq('/get-edge-titles?from=3&to=0', [])
    assert_eq('/get-edge-titles?from=3&to=1', [])
    assert_eq('/get-edge-titles?from=3&to=2', [])
    assert_eq('/get-edge-titles?from=3&to=3', [])
    assert_eq('/get-edge-titles?from=3&to=4', [])
    assert_eq('/get-edge-titles?from=3&to=5', [])
    assert_eq('/get-edge-titles?from=3&to=6', [])
    assert_eq('/get-edge-titles?from=3&to=7', [])
    assert_eq('/get-edge-titles?from=3&to=8', ["1 FTM at 0000000017", "2 FTM at 0000000019", "3 FTM at 000000001b"])
    assert_eq('/get-edge-titles?from=4&to=0', [])
    assert_eq('/get-edge-titles?from=4&to=1', [])
    assert_eq('/get-edge-titles?from=4&to=2', [])
    assert_eq('/get-edge-titles?from=4&to=3', [])
    assert_eq('/get-edge-titles?from=4&to=4', [])
    assert_eq('/get-edge-titles?from=4&to=5', [])
    assert_eq('/get-edge-titles?from=4&to=6', [])
    assert_eq('/get-edge-titles?from=4&to=7', [])
    assert_eq('/get-edge-titles?from=4&to=8', ["1 FTM at 000000001d", "2 FTM at 000000001f", "3 FTM at 0000000021"])
    assert_eq('/get-edge-titles?from=5&to=0', [])
    assert_eq('/get-edge-titles?from=5&to=1', [])
    assert_eq('/get-edge-titles?from=5&to=2', [])
    assert_eq('/get-edge-titles?from=5&to=3', [])
    assert_eq('/get-edge-titles?from=5&to=4', [])
    assert_eq('/get-edge-titles?from=5&to=5', [])
    assert_eq('/get-edge-titles?from=5&to=6', [])
    assert_eq('/get-edge-titles?from=5&to=7', [])
    assert_eq('/get-edge-titles?from=5&to=8', ["1 FTM at 0000000023", "2 FTM at 0000000025", "3 FTM at 0000000027"])
    assert_eq('/get-edge-titles?from=6&to=0', [])
    assert_eq('/get-edge-titles?from=6&to=1', [])
    assert_eq('/get-edge-titles?from=6&to=2', [])
    assert_eq('/get-edge-titles?from=6&to=3', [])
    assert_eq('/get-edge-titles?from=6&to=4', [])
    assert_eq('/get-edge-titles?from=6&to=5', [])
    assert_eq('/get-edge-titles?from=6&to=6', [])
    assert_eq('/get-edge-titles?from=6&to=7', [])
    assert_eq('/get-edge-titles?from=6&to=8', ["1 FTM at 0000000029", "2 FTM at 000000002b", "3 FTM at 000000002d"])
    assert_eq('/get-edge-titles?from=7&to=0', [])
    assert_eq('/get-edge-titles?from=7&to=1', [])
    assert_eq('/get-edge-titles?from=7&to=2', [])
    assert_eq('/get-edge-titles?from=7&to=3', [])
    assert_eq('/get-edge-titles?from=7&to=4', [])
    assert_eq('/get-edge-titles?from=7&to=5', [])
    assert_eq('/get-edge-titles?from=7&to=6', [])
    assert_eq('/get-edge-titles?from=7&to=7', [])
    assert_eq('/get-edge-titles?from=7&to=8', ["1 FTM at 000000002f", "2 FTM at 0000000031", "3 FTM at 0000000033"])
    assert_eq('/get-edge-titles?from=8&to=0', [])
    assert_eq('/get-edge-titles?from=8&to=1', ["1 FTM at 000000000c", "2 FTM at 000000000e", "3 FTM at 0000000010"])
    assert_eq('/get-edge-titles?from=8&to=2', ["1 FTM at 0000000012", "2 FTM at 0000000014", "3 FTM at 0000000016"])
    assert_eq('/get-edge-titles?from=8&to=3', ["1 FTM at 0000000018", "2 FTM at 000000001a", "3 FTM at 000000001c"])
    assert_eq('/get-edge-titles?from=8&to=4', ["1 FTM at 000000001e", "2 FTM at 0000000020", "3 FTM at 0000000022"])
    assert_eq('/get-edge-titles?from=8&to=5', ["1 FTM at 0000000024", "2 FTM at 0000000026", "3 FTM at 0000000028"])
    assert_eq('/get-edge-titles?from=8&to=6', ["1 FTM at 000000002a", "2 FTM at 000000002c", "3 FTM at 000000002e"])
    assert_eq('/get-edge-titles?from=8&to=7', ["1 FTM at 0000000030", "2 FTM at 0000000032", "3 FTM at 0000000034"])
    assert_eq('/get-edge-titles?from=8&to=8', [])


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import json
import sys


NROUNDS = 7


def main():
	edges = []
	for i in range(1, NROUNDS):
		m = 1 << i
		for j in range(m):
			edges.append((m // 2 + j // 2, m + j))

	json.dump(dict(edges=edges,
	               size=(1 << NROUNDS) - 1,
	               start_from=1),
	          sys.stdout)


if __name__ == '__main__':
	main()

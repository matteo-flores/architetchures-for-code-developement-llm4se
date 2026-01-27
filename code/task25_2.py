import math
from typing import List

def range_add_range_sum(n: int, queries: List[tuple]) -> List[int]:
    """Processes range add and range sum queries on an array of size n using a segment tree.

    Args:
        n: The size of the array.
        queries: A list of queries. Each query is a list:
            - [0, s, t, x]: Add x to all elements in the range [s, t].
            - [1, s, t]: Query the sum of elements in the range [s, t].

    Returns:
        A list of results for all range sum queries.
    """
    tree_size = 4 * n
    tree_sum = [0] * tree_size
    lazy = [0] * tree_size

    def push_down(node, start, end):
        if lazy[node] != 0:
            tree_sum[node] += lazy[node] * (end - start + 1)
            if start != end:
                lazy[2 * node] += lazy[node]
                lazy[2 * node + 1] += lazy[node]
            lazy[node] = 0

    def push_up(node, start, end):
        if start != end:
            tree_sum[node] = tree_sum[2 * node] + tree_sum[2 * node + 1]

    def update_range(node, start, end, l, r, val):
        push_down(node, start, end)
        if start > end or start > r or end < l:
            return
        if l <= start and end <= r:
            lazy[node] += val
            push_down(node, start, end)
            return
        mid = (start + end) // 2
        update_range(2 * node, start, mid, l, r, val)
        update_range(2 * node + 1, mid + 1, end, l, r, val)
        push_up(node, start, end)

    def query_sum(node, start, end, l, r):
        if start > end or start > r or end < l:
            return 0
        push_down(node, start, end)
        if l <= start and end <= r:
            return tree_sum[node]
        mid = (start + end) // 2
        p1 = query_sum(2 * node, start, mid, l, r)
        p2 = query_sum(2 * node + 1, mid + 1, end, l, r)
        return p1 + p2

    results = []
    for query in queries:
        if query[0] == 0:
            _, s, t, x = query
            update_range(1, 1, n, s, t, x)
        else:
            _, s, t = query
            results.append(query_sum(1, 1, n, s, t))
    return results
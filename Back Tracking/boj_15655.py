# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15655


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()


def backtracking(sequence, idx):
    if len(sequence) == m:
        print(*sequence)
        return

    for i in range(idx + 1, n):
        sequence.append(num_list[i])
        backtracking(sequence, i)
        sequence.pop()


backtracking([], -1)

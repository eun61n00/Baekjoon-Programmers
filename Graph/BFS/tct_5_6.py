# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다(나동빈, 한빛미디어)
# 5-6 인접 행렬 방식 예제

INF = 999999999

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
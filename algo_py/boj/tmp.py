# Title: 수도쿠
# Link: https://www.acmicpc.net/problem/2580

import sys


sys.setrecursionlimit(10 ** 6)


read_list_str = lambda: list(sys.stdin.readline().strip().split(' '))

def cross(aa: list, bb: list):
    return [a + b for a in aa for b in bb]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
            for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
            for s in squares)


def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all (eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
    
    if len(dplaces) == 0:
        return False
    elif len(dplaces) == 1:
        if not assign(values, dplaces[0], d):
            return False
    return values


def display(values):
    for r in rows:
        row = []
        for c in cols:
            row.append(values['{}{}'.format(r, c)])
        print(' '.join(row))
        



def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values


def grid_values(grid: list):
    ans = ''
    for row in grid:
        ans += ''.join(row)
    
    chars = [c for c in ans if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))


def some(seq):
    for e in seq:
        if e: 
            return e
    return False


def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def solution(problem: list):
    display(search(parse_grid(problem)))


def main():
    problem = []
    for _ in range(9):
        problem.append(read_list_str())
    solution(problem)


if __name__ == '__main__':
    main()
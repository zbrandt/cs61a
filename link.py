class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def tens(s):
    def f(suffix, total):
        if total % 10 == 0:
            print(total)
        if suffix is not Link.empty:
            f(suffix.rest, total + suffix.first)
    f(s.rest, s.first)

def replace(s, t, i, j):
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        replace(s.rest, t, i - 1, j - 1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
        end = t
        while end.rest is not Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest

class State:
    electors = {}
    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors

def print_all(s):
    for x in s:
        print(x)

def wins(states, k):
    if not states and k <= 0:
        yield Link.empty
    if states:
        first = states[0].electors

        for win in wins(states[1:], k - first):
            yield Link(states[0].code, win)
        yield from wins(states[1:], k + first)

def insert(l, value, before):
    if l.rest is Link.empty:
        return Link(value)
    elif l.first == before:
        return Link(value, l)
    else:
        return Link(l.first, insert(l.rest, value, before))

def max_pair_sum(s):
    if s is Link.empty or s.rest is Link.empty:
        return 0
    n = s.first + s.rest.first
    
    if s.rest.rest is Link.empty:
        return n 
    else:
        return max(n + max_pair_sum(s.rest.rest.rest), max_pair_sum(s.rest))

class Chain(Link):
    def add(self, v):
        self.rest = Chain(v, self.rest)
        return self

class Blink:
    def __init__(self, s):
        if s is not Link.empty:
            self.rest = Blink(s.rest)

            self.sublists = self.rest.sublists.copy()
            self.sublists[s.first] = s 
        else:
            self.sublists = {}
        self.link = s

def segment(n, grouped):
    part = Link.empty
    parts = Link.empty

    while n:
        if part is Link.empty or grouped(n % 10, part.first):
            part = Link(n % 10, part)
        else: 
            parts = Link(part, parts)
            part = Link(n % 10)
        n = n // 10
    return Link(part, parts) 

def desert(n):
    return segment(n, lambda a, b: abs(a - b) == 1)

def shake(it):
    if it is not Link.empty and it.rest is not Link.empty:
        if it.first + 1 < it.rest.first:
            it.rest = Link(it.rest.first-1, it.rest)
            shake(it)
        else:
            shake(it.rest)

#it = Link(2, Link(5, Link(7)))
#off = Link(1, it.rest)
#shake(it)

def cruel(summer):
    while summer is not Link.empty:
        yield summer.first
        summer = summer.rest
        if summer is not Link.empty:
            summer = summer.rest 
summer = Link(1, Link(2, Link(3, Link(4))))

def swipe(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

def skip_factorial(n):
    if n - 2 <= 0:
        return n
    else:
        return n * skip_factorial(n - 2)

def hailstone(n):
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
     return 1 + hailstone(n // 2)

def odd(n):
    if n == 1:
        return 1 
    else:
        return 1 + hailstone((3 * n) + 1)

def is_prime(n):
    def factor(i):
        if i == 0:
            return True
        elif n % i == 0 and i != 1:
            return False
        else:
            return factor(i - 1)
    return factor(n - 1)

def sevens(n, k):
    def f(i, who, direction):
        if i == n:
            return who
        elif has_seven(i):
            direction = direction * -1

        who = who + direction

        if (who < 1):
            who = k
        elif (who > k):
            who = 1
        print('Who:', who, 'Number:', i, 'Direction:', direction)
        return f(i + 1, who, direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    elif n % 7 == 0:
        return True
    else:
        return has_seven(n // 10)


def paths(m, n):
    def helper(o, p):
        if o == m and p == n:
            return 1
        elif o > m or p > n:
            return 0
        else:
            return helper(o + 1, p) + helper(o, p + 1)
    return helper(1, 1)

def max_product(s):
    if len(s) == 0:
        return 1
    return max(s[0] * max_product(s[2:]), max_product(s[1:]))


def sums(n, m):
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     
        return [sums_to_zero] 
    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n - k, m) if rest == [] or k != rest[0]]
    return result

def differences(t):
    while True:
        x = next(t)
        y = next(t)
        yield y - x

def differences_two(t):
    first = next(t)
    for _ in t:
        print(_)
        second = next(t)
        yield second - first
        first = second

def partition_gen(n, m):
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        yield str(n - m) + next(partition_gen(n - m, m)) 
    if m > 1:
        yield next(partition_gen(n, m - 1))

class Library:
    def __init__(self, titles):
        self.books = {t: Book(t, self) for t in titles}
        self.out = []

    def checkout(self, title):
        assert title in self.books, title + " isn't in this library's collection"
        book = self.books[title]

        if book not in self.out:
            self.out.append(book)
            return book
        else:
            print(book, ' is checked out')

class Book:
    def __init__(self, title, library):
        self.title = title
        self.library = library

    def bring_back(self):
        self.library.out.remove(self)

    def __str__(self):
        return repr(self.title)


        
def fit(total, n):
    def f(total, n, k):
        if total == n * k * k:
            return True
        elif k * k > total:
            return False
        else:
            return f(total, n, k + 1) or f(total - k**2, n - 1, k)
    return f(total, n, 1)

def count_park(n):
    if n < 0:
        return 0
    if n == 0:
        return 1 
    return 2 * count_park(n - 1) + count_park(n - 2) 

def park(n):
    if n == 0:
        yield ''
    elif n > 0:
        for s in park(n - 1):
            yield '%' + s
            yield '.' + s
        for s in park(n - 2):
            yield '<>' + s

def pack(n):
    def f(n, k):
        if n == 0 and k == 0:
            yield ''
        elif n > 0:
            yield from g(n-1, k-1, '<', '%')
            yield from g(n-1, k, '.', '.')
            yield from g(n-2, k+1, '%', '<>')

    def g(n, k, no, yes):
        yield from (yes + x for x in f(n, k) if len(x) == 0 or x[0] != no)

    yield from f(n, 0)

def a_then_b(a, b):
    yield from (x + 1 for x in a)
    yield from b

class Chungus:
    wholesome = True

    def __init__(self, name):
        self.name = name

    def exude(self):
        print('Ahhhhh')

class Snake:
    legs = 0
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def run(self, s):
        print("Snakes don't run")
        return self.crawl()
    def crawl(self):
        print(f"{self} crawled")
    def eat(self, s):
        self.run(s)
        print("Nom nom")

class Python(Snake):
    def run(self, s):
        print(eval(s))

def roll(outcomes):
    while True:
        for i in outcomes:
            yield i

def roll_dice(num_rolls, dice):
    rolls = [next(dice) for i in range(num_rolls)]
    if 1 in rolls:
        return 1
    return sum(rolls)


def count_subsets(s):
    def helper(sum_so_far, index):
        if index == len(s):
            if sum_so_far == 100:
                return 1
            return 0
        return helper(sum_so_far, index+1) + helper(sum_so_far + s[index], index + 1)
    return helper(0, 0)

def change(n, coins):
    if n == 0:
        return True
    elif len(coins) == 0:
        return False
    coin = coins.pop()
    print(coin)
    return change(n, list(coins)) or change(n - coin, list(coins))

def amounts(coins):
    if not coins:
        return [0]

    coin = coins[0]
    rest = amounts(coins[1:])
    return sorted(rest + [k + coin for k in rest if k + coin not in rest])

class Valet:
    def __init__(self):
        self.tips = 0
        self.garage = None

    def park(self, car):
        self.garage.cars[car] = self

    def wash(self, car, tip):
        self.tips += tip / 2
        self.garage.cars[car].tips += tip / 2

class Garage:
    def __init__(self, valets):
        self.cars = {}
        for valet in valets:
            valet.garage = self

def ring(s):
    while True:
        yield from s

def fork(t):
    s = []
    def copy():
        i = 0
        while True:
            if i == len(s):
                s.append(next(t))
            yield s[i]
            i += 1
    return copy(), copy()

def snap(f, g, s):
    return [(x, y) for x, y in [(x, f(x)) for x in s] if g(y)]

def max_diff(s, f):
    assert s
    v, w = None, None
    for x in s:
        for y in s:
            if v is None or f(x) - f(y) > f(v) - f(w):
                v, w = x, y
    return v, w

def max_diff_fast(s, f):
    return max(s, key=f), min(s, key=f)

def filter_index(f, s):
    def helper(i, s):
        if s is Link.empty:
            return s
        filtered_rest = helper(i + 1, s.rest)
        if f(i):
            return Link(s.first, helper(i + 1, s.rest))
        else:
            return filtered_rest
    return helper(0, s)

class Version:
    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit
    def __str__(self):
        return self.edit.apply(self.previous.__str__())

class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c

class Insert(Edit):
    def apply(self, t):
        return t[:self.i] + self.c + t[self.i:]

class Delete(Edit):
    def apply(self, t):
        return t[:self.i] + t[self.i + self.c:]

class State:
    electors = {}
    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors

def generate_constant(x):
    while True:
        yield x

def black_hole(seq, trap):
    for i in seq:
        if i != trap:
           yield i 
        else:
            yield from generate_constant(trap)

def word_finder(letter_tree, words_list):
    def helper(t, words, word, i):

        if word[i] == t:
            yield check
        for w in words:
            yield from helper(t, words, w, "") 
    yield from [helper(letter_tree, words_list, word, 0) for word in words_list] 

def integers(n):
    while True:
        yield n
        n += 1

def drop(s, n):
    for _ in range(n):
        next(s)
        #print('hello')
    for elem in s:
        yield elem

# def powers_of_two(ints=integers(0)):
#    curr = next(ints)
#    yield 2**curr
#    yield from powers_of_two(ints)

def powers_of_two(ints=integers(1)):
    curr = next(ints)
    yield curr
    yield from powers_of_two(drop(ints, curr-1))

def times(f, x):
    def repeat(z):
        yield f(z)
        yield from repeat(f(z))

    def g(y):
        n = 0
        for w in repeat(x):
            print(w)
            if w == y:
                return n + 1
            n += 1
    return g


def word_rope(s):
    result = []
    word = []
    for x in s:
        if x == ' ':
            result.append(word)
            word += []
            word = word[-1]
        else:
            print(x)
            word = word + [x]
    return result

def chain(g):
    g(True, g)

def add_copy(p, then):
    copy = result
    if p: 
        copy.append(1)
        result.append(list(copy))
        return then(not p, add_copy)
    else:
        copy.append(2)

class Expression:
    def __init__(self, original):
        assert len(original) > 0
        self.dialect = {'yes': 'aye', 'hi': 'ahoy', 'said': 'says', 'are': 'arrrr'}
        previous = None
        for w in original:
            current = Word(w, self, previous)
            previous = current
        self.first = previous 

    def __str__(self):
        return str(self.first)

class Word:
    def __init__(self, w, exp, then):
        self.w = w
        self.exp = exp
        self.then = then

    def say(self):
        return self.exp.dialect.get(self.w, self.w) 
    
    def __str__(self):
        first = self.say()

        if self.then:
            return first + ' ' + str(self.then)
        else:
            return first

def longest_pairing(s):
    assert len(s) > 0 and len(s) % 3 == 2, 's must have length 3*n-1 for a positive integer n'

    result, pair, skip = [], [], False

    for x in s:
        if not skip:
            pair.append(x)
        else:
            skip = False


        if len(pair) == 2:
            result.append(tuple(pair)) # append((pair[0], pair[1]))

            pair, skip = [], True

    return result

def is_pair_sequence(s):
    return all([type(x) == tuple and isinstance(x, tuple) for x in s]) and all(map(lambda x: len(x) == 2, s))

def is_pairing(s, pairs):
    assert is_pair_sequence(pairs)
    print(pairs, s)
    if not pairs:
        return True
    if len(s) < 2:
        return False
    if pairs[0] == tuple(s[:2]):
        return is_pairing(s[3:], pairs[1:])
    return is_pairing(s[1:], pairs)

def unequal_pairs(s):
    if len(s) >= 2:
        yield from unequal_pairs(s[1:])
        if s[0] != s[1]:
            pair = (s[0], s[1])
            yield [pair] 
            for rest in unequal_pairs(s[3:]):
                yield [pair] + rest 

def cars(k, n):
    if k == 0:
        return 1 
    if n < 2:
        return 0
    return cars(k - 1, n - 2) + cars(k, n - 1)

def pair(s):
    assert len(s) % 2 == 0
    return [s[(2 * i):(2 * (1 + i))] for i in range(len(s) // 2)]

def naturals(k):
    yield k 
    yield from naturals(k + 1)

def gen_pairs(t):
    while True:
        yield [next(t), next(t)]

class Log:
    logged = {}
    def __init__(self, f):
        if f not in self.logged:
            self.logged[f] = []
        self.f = f 
        self.args = self.logged[f]

    def call(self, n):
        self.args.append(n)
        return self.f(n)

class Counter:
    def __init__(self):
        self.obs = []
    def observe(self, vs):
        self.obs.append(list(vs))
    def count(self, v):
        return sum([i.count(v) for i in self.obs])
    def forget(self):
        self.obs.pop()

def near(i, j):
    return abs(i - j) == 1

def is_worm(n):
    if n < 10:
        return True
    return near(n % 10, (n // 10) % 10) and is_worm(n // 10)

def sandworm(n):
    if n == 0:
        return 0

    def use_last(n):
        return tooth(n // 10, n % 10)
    
    def tooth(n, d):
        if n == 0:
            return d
        
        skip = tooth(n // 10, d)
        
        if near(n % 10, d):
            return max(skip, 10 * use_last(n) + d)
        else:
            return skip
    return max(sandworm(n // 10), use_last(n))

triple = lambda z: 3 * z
dec = lambda z: z - 1 

def alt(f, g):
    def h(x):
        print(fns[0](fns[1](x)))
        fns[0] = fns[1]
        fns[1] = fns[0]
        return h
    fns = [f, g]
    return h

def find_pair(s):
    for i in s:
        for j in s:
            if i + j == 2020 and i != j:
                return [i, j]
coins = (1, 5, 10, 25, 50)
def count_change_register(amount, k):
    def helper(remaining, coin_index, n):
        if coin_index == len(coins) or remaining < 0 or n > k:
            return 0
        if remaining == 0:
            return 1 
        return (helper(remaining - coins[coin_index], coin_index, n + 1) + helper(remaining, coin_index + 1, n))
    return helper(amount, 0, 0)

triple = lambda z: 3 * z
dec = lambda z: z - 1
def alt(f, g):
    def h(x):
        print(fns[0](fns[1](x)))
        fns[0] = fns[1]
        fns[1] = fns[0]
        return h
    fns = [f, g]
    return h

class Sub:
    fns = [lambda z: str(z) + str(z), lambda z: 2 * z]
    def __init__(self, f, g):
        self.fns = [f, g]
    def h(self, x):
        print(Sub.fns[0](Sub.fns[1](x)))
        Sub.fns = self.fns
        return self

    def __repr__(self):
        return str(self.fns[0]('ha'))

class Pub(Sub):
    fns = [lambda z: [z], lambda z: z]

    def __init__(self, f, g):
        fns = [f, g]

def is_strip(s):
    return len(s) == 0 or s == list(range(s[0], s[0] + len(s)))

def drip(s, t):
    while s and t:
        if s[0] + 1 == t[0]:
            s, t = t, s[1:]
        elif len(s) > 1 and s[0]+1 == s[1]:
            s = s[1:]
        else:
            return False
    return is_strip(s)

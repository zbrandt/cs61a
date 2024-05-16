class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        return f'Tree({self.label}, {[b.__repr__() for b in self.branches]})'

def label(tree):
    return tree.label

def branches(tree):
    return tree.branches

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def exclude(t, x):
    filtered_branches = map(lambda y: exclude(y, x), t.branches)

    bs = []
    for b in filtered_branches:
        if label(b) == x:
            bs.extend(branches(b))
        else:
            bs.append(b)
    return Tree(t.label, bs)

def remove(t, x):
    t.branches = exclude(t, x).branches
    return t

def only_paths(t, n):
    if is_leaf(t) and t.label == n:
        return t
    new_branches = [only_paths(b, n-t.label) for b in t.branches]
    if any(new_branches):
        return Tree(t.label, [b for b in new_branches if b is not None])

only_paths = (lambda f: lambda t, n: f(t, n - 1))(only_paths)
def only_long_paths(t, n):
    return only_paths(t, n)

def is_hydra(t):
    if is_leaf(t):
        return t.label == 1
    if len(t.branches) != 2:
        return False
    return (t.label == sum([b.label for b in t.branches])) and all([is_hydra(b) for b in t.branches])

def chop_head(hydra, n):
    assert is_hydra(hydra)
    assert n > 0 and n <= hydra.label
    if is_leaf(hydra):
        hydra.label = 2
        hydra.branches = [Tree(1), Tree(1)]
        return
    hydra.label += 1
    left, right = hydra.branches
    if n > left.label:
        chop_head(right, n - left.label)
    else:
        chop_head(left, n)

def word_finder(letter_tree, words_list):
    def helper(t, word):
        if word in words_list and is_leaf(t):
            yield word
        for b in t.branches:
            yield from helper(b, word + b.label) 
    yield from helper(letter_tree, letter_tree.label)

def bounds(t, low, high):
    count = 0
    if is_leaf(t) and low <= t.label and t.label <= high:
        count = 1
    return count + sum([bounds(b, low - t.label, high - t.label) for b in t.branches])

def big_paths(t):
    def f(s):
        if t.label > s.label:
            return 0
        elif is_leaf(s):
            return 1
        else:
            return sum([f(b) for b in s.branches])
    return f(t)

def gen(t, n):
    for b in t.branches:
        if t.label + b.label == n:
            yield [t.label, b.label]
        yield from gen(b, n)

def fruited_branch(t):
    return len(t.branches) == 1 and is_leaf(t.branches[0])

def sum_fruit_labels(t):
    if fruited_branch(t):
        return t.branches[0].label
    else:
        return 0 + sum([sum_fruit_labels(b) for b in t.branches])

def pruned(t):
    if fruited_branch(t):
        return t
    cut = [pruned(b) for b in t.branches]
    if any(cut):
        return Tree(t.label, [b for b in cut if b is not None])

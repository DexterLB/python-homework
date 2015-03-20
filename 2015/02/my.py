def extract_type(pairs, filter_type):
    pairs = filter(lambda pair: type(pair[0]) is filter_type, pairs)
    return ''.join([str(value) * count for value, count in pairs])


def reversed_dict(dictionary):
    return {value: key for key, value in dictionary.items()}


def flatten_dict(tree):
    flattened = {}
    for key, value in tree.items():
        if type(value) is dict:
            for internal_key, internal_value in flatten_dict(value).items():
                flattened[key + '.' + internal_key] = internal_value
        else:
            flattened[key] = value
    return flattened

def insert_path(tree, path, value):
    if '.' not in path:
        tree[path] = value
    else:
        key, path = path.split('.', 1)
        if key not in tree:
            tree[key] = {}
        insert_path(tree[key], path, value)

def unflatten_dict(flattened):
    tree = {}
    for key, value in flattened.items():
        insert_path(tree, key, value)
    return tree

def reps(collection):
    repeated = {item for item in collection if collection.count(item) > 1}
    return tuple(item for item in collection if item in repeated)

<<<<<<< HEAD
ALPHABET_CYR = 'явертъуиопасдфгхйклзьцжбнмюч'
ALPHABET_LAT = 'qwertyuiopasdfghjklzxcvbnm'


def is_pangram(sentence):
    return set(ALPHABET_CYR).issubset(set(sentence.lower()))


def char_histogram(text):
    histogram = {}
    for char in text:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1
    return histogram


def sort_by(func, arguments):
    if len(arguments) <= 1:
        return arguments
    pivot = arguments.pop(0)
    left = []
    right = []
    center = [pivot]
    while arguments:
        current_argument = arguments.pop(0)
        coef = func(pivot, current_argument)
        if coef > 0:
            left.append(current_argument)
        elif coef < 0:
            right.append(current_argument)
        else:
            center.append(current_argument)
    return sort_by(func, left) + center + sort_by(func, right)


def group_by_type(dictionary):
    big_dic = {}
    for key, value in dictionary.items():
        if type(key) in big_dic:
            big_dic[type(key)][key] = value
        else:
            big_dic[type(key)] = {key: value}
    return big_dic


def word_letter_set(word):
    return set(word).intersection(set(ALPHABET_CYR).union(set(ALPHABET_LAT)))


def anagrams(words):
    classes = []
    while words:
        base_word = words.pop()
        cur_class = [word for word in words
                     if word_letter_set(word) == word_letter_set(base_word)]
        words = [word for word in words if word not in cur_class]
        cur_class.append(base_word)
        classes.append(cur_class)
    return classes
=======
from collections import Counter, defaultdict
from functools import cmp_to_key
import string

CYRILIC = 'абвгдежзийклмнопрстуфхцчшщъьюя'
LATIN = string.ascii_lowercase
ALPHABETS = CYRILIC + LATIN


def is_pangram(sentence):
    return all(map(lambda letter: letter in sentence.lower(), CYRILIC))


def char_histogram(text):
    return Counter(text)


def sort_by(func, arguments):
    return sorted(arguments, key=cmp_to_key(func))


def group_by_type(dictionary):
    result = defaultdict(dict)
    for key, value in dictionary.items():
        result[type(key)][key] = value
    return result


def anagrams(words):
    result = set()
    for word in words:
        group = {w for w in words if
                 Counter(''.join([c for c in w.lower() if c in ALPHABETS])) ==
                 Counter(''.join([c for c in word.lower() if c in ALPHABETS]))}
        result.add(tuple(group))
    return [list(element) for element in result]
>>>>>>> 27b8bc94a0affac85b2780f057b389ff39faf9ac

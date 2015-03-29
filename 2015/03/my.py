from math import sqrt
from itertools import count


def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    return all(number % divisor for divisor in range(2, int(sqrt(number)) + 2))


def primes():
    return (number for number in count(1) if is_prime(number))


def alphabet(*, code=None, letters=""):
    if not letters:
        if code == 'lat':
            letters = 'abcdefghijklmnopqrstuvwxyz'
        elif code == 'bg':
            letters = 'абвгдежзийклмнопрстуфхцчшщъьюя'
    return (letter for letter in letters)


def intertwined_sequences(sequences, *, generator_definitions={}):
    sequence_functions = {
        'alphabet': alphabet,
        'primes': primes,
        'fibonacci': fibonacci
    }
    sequence_functions.update(generator_definitions)

    sequence_iterators = {}
    for sequence in sequences:
        sequence_arguments = dict(sequence)

        sequence_name = sequence_arguments.pop('sequence')
        length = sequence_arguments.pop('length')

        if sequence_name not in sequence_iterators:
            sequence_iterators[sequence_name] = sequence_functions[
                sequence_name
            ](**sequence_arguments)

        iterator = sequence_iterators[sequence_name]

        for _ in range(length):
            yield next(iterator)

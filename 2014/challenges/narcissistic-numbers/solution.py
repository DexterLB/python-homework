<<<<<<< HEAD

def from_base(digits, base):
    result = 0
    while digits:
        digit = digits.pop(0)
        result += digit * (base ** len(digits))
    return result

def is_narcissistic(number, base=10):
    digits = [int(digit_chr) for digit_chr in number]
    narcissistic_sum = sum([digit ** len(digits) for digit in digits])
    return (narcissistic_sum == from_base(digits, base))

print(is_narcissistic('10'))
print(is_narcissistic('223', 4))
print(is_narcissistic('115132219018763992565095597973971522401'))
=======
def is_narcissistic(number, base=10):
    return (sum([int(digit, base) ** len(number) for digit in number]) ==
            int(number, base))
>>>>>>> 27b8bc94a0affac85b2780f057b389ff39faf9ac

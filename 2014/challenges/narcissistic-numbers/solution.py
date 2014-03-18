
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

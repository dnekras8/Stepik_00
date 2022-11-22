#2022/11/19
def to_dec(string: str):
    if string.isdigit():
        return(int(string))
    elif string in ('ABCDEFG'):
        return 10 + (ord(string)-ord('A'))
    else:
        return None

def to_decimal(string, nfrom):
    return sum(to_dec(string[-1-i]) * (nfrom ** i) for i in range(len(string)))

def from_dec(num: int):
    if num > 9:
        return chr(ord('A')+(num - 10))
    else:
        return str(num)

def from_decimal(num, nfrom):
    text = ''
    while num > 0:
        text = from_dec(num % nfrom) + text
        num //= nfrom
    return text

# print(from_dec(12))
# print(to_decimal('111111', 2))
# print(from_decimal(63, 2))
# print(to_decimal('1AF2', 16))
# print(from_decimal(6898, 16))
#print(from_decimal(513, 2))

print(to_dec('G'))



# for i in range(2, 17):
#     if to_decimal('88', i) == to_decimal('32', i) + to_decimal('22', i) + to_decimal('16', i) + to_decimal('17', i):
#         print(i, to_decimal('88', i))
#         break
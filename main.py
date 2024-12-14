def input_set(prompt):
    return set(map(int, input(prompt).strip('{}').split(',')))

def union(a, b):
    result = a.copy()
    for elem in b:
        if elem not in result:
            result.add(elem)
    return result

def intersection(a, b):
    result = set()
    for elem in a:
        if elem in b:
            result.add(elem)
    return result

def difference(a, b):
    result = set()
    for elem in a:
        if elem not in b:
            result.add(elem)
    return result

def complement(u, a):
    result = set()
    for elem in u:
        if elem not in a:
            result.add(elem)
    return result

def symmetric_difference(a, b):
    return union(difference(a, b), difference(b, a))

def cartesian_product(a, b):
    result = set()
    for elem_a in a:
        for elem_b in b:
            result.add((elem_a, elem_b))
    return result

def is_subset(a, b):
    for elem in a:
        if elem not in b:
            return False
    return True

def are_equal(a, b):
    if len(a) != len(b):
        return False
    for elem in a:
        if elem not in b:
            return False
    return True

def to_bitstring(u, a):
    bitstring = []
    for elem in u:
        if elem in a:
            bitstring.append('1')
        else:
            bitstring.append('0')
    return ''.join(bitstring)

def from_bitstring(u, bitstring):
    result = set()
    for i, bit in enumerate(bitstring):
        if bit == '1':
            result.add(u[i])
    return result

def bitwise_not(bitstring):
    return ''.join('1' if bit == '0' else '0' for bit in bitstring)

def bitwise_or(bitstring1, bitstring2):
    return ''.join('1' if bit1 == '1' or bit2 == '1' else '0' for bit1, bit2 in zip(bitstring1, bitstring2))

def bitwise_and(bitstring1, bitstring2):
    return ''.join('1' if bit1 == '1' and bit2 == '1' else '0' for bit1, bit2 in zip(bitstring1, bitstring2))

def bitwise_xor(bitstring1, bitstring2):
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(bitstring1, bitstring2))

A = input_set("Введіть множину A (елементи через кому, наприклад: 1,2,3): ")
B = input_set("Введіть множину B (елементи через кому, наприклад: 4,5,6): ")
U = input_set("Введіть універсальну множину U (елементи через кому, наприклад: 1,2,3,4,5,6): ")

print("Об'єднання A і B:", union(A, B))
print("Перетин A і B:", intersection(A, B))
print("Різниця A \ B:", difference(A, B))
print("Доповнення A в U:", complement(U, A))
print("Симетрична різниця A і B:", symmetric_difference(A, B))
print("Декартовий добуток A і B:", cartesian_product(A, B))

print("Чи є A підмножиною B:", is_subset(A, B))
print("Чи рівні множини A і B:", are_equal(A, B))

print("Бітовий рядок для множини A:", to_bitstring(U, A))
print("Бітовий рядок для множини B:", to_bitstring(U, B))

bit_A = to_bitstring(U, A)
bit_B = to_bitstring(U, B)

print("Бітовий рядок для множини A:", bit_A)
print("Бітовий рядок для множини B:", bit_B)

not_A = bitwise_not(bit_A)
not_A_set = from_bitstring(list(U), not_A)
print("NOT A:", not_A, "-> Множина:", not_A_set, "-> Збіг з п.1:", are_equal(not_A_set, complement(U, A)))

or_AB = bitwise_or(bit_A, bit_B)
or_AB_set = from_bitstring(list(U), or_AB)
print("A OR B:", or_AB, "-> Множина:", or_AB_set, "-> Збіг з п.1:", are_equal(or_AB_set, union(A, B)))

and_AB = bitwise_and(bit_A, bit_B)
and_AB_set = from_bitstring(list(U), and_AB)
print("A AND B:", and_AB, "-> Множина:", and_AB_set, "-> Збіг з п.1:", are_equal(and_AB_set, intersection(A, B)))

xor_AB = bitwise_xor(bit_A, bit_B)
xor_AB_set = from_bitstring(list(U), xor_AB)
print("A XOR B:", xor_AB, "-> Множина:", xor_AB_set, "-> Збіг з п.1:", are_equal(xor_AB_set, symmetric_difference(A, B)))

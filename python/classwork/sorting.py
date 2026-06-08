
ints = [1]*4 + [2]*4 + [3]*4 + [4]*4
chars = ['a']*4 + ['b']*4 + ['c']*4 + ['d']*4

zipped = list(zip(ints, chars))

print(zipped)
print()

s1 = sorted(zipped, key=lambda x: -x[0])

print(s1)
print()

s2 = sorted(zipped, key=lambda x: x[1])

print(list(s2))
print()




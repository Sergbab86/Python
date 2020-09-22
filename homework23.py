
d = {

  	'apple': ['malum', 'pomum', 'popula'],

  	'fruit': ['baca', 'bacca', 'popum'],

  	'punishment': ['malum', 'multa']

}

a = list(d.keys())
print(a)

b = list(d.values())
print(b)

# c = [(tuple(x), y) for x, y in zip(b, a)]
# print(c)

new_dict = dict([(tuple(x), y) for x, y in zip(list(d.values()), list(d.keys()))])
print(new_dict)

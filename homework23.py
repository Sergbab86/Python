
d = {

  	'apple': ['malum', 'pomum', 'popula'],

  	'fruit': ['baca', 'bacca', 'popum'],

  	'punishment': ['malum', 'multa']

}

a = list(d.keys())
print(a)

b = list(d.values())
print(b)


c = dict.fromkeys(list(d.keys()), (i for i in list(d.values())))
print(c)
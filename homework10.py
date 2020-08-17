
s = 'With the hare and run with the hounds'

h1 = s.find('h')
h2 = s.rfind('h')
s1 = s[h1+1:h2].replace('h', 'H')
print(s1)
print(s[:h1+1] + s1 + s[h2:])

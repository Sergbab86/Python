
lst = [
    [34587, 'LearningPython,MarkLutz', 4, 40.95],
    [98762, 'ProgrammingPython,MarkLutz', 5, 56.80],
    [77226, 'HeadFirstPython,PaulBarry', 3, 32.95],
    [88112, 'EinfuhrunginPython3,BerndKlein', 3, 24.99]
    ]


def up():
    for lst1 in lst:
        if lst1[2] * lst1[3] < 100:
            lst1[3] += 10
        lst1.append(lst1[2] * lst1[3])
        del(lst1[1:4])


up()
res = list(map(tuple, lst))
print(res)

"""How many positive integers are there under 1 million whose digits sum to 19?"""

trials = 1000000
num = 19

onesplace = range(10)
tensplace = range(10)
hundredsplace = range(10)
thousandsplace = range(10)
tensthousandsplace = range(10)
hundredthousandsplace = range(10)
test = []
for i in onesplace:
    for j in tensplace:
        for k in hundredsplace:
            for l in thousandsplace:
                for m in tensthousandsplace:
                    for n in hundredthousandsplace:
                        if i + j + k + l + m + n == num:
                            test.append((i, j, k, l, m, n))
print(len(test))
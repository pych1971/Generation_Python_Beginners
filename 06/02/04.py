city1, city2, city3 = input(), input(), input()
minimum = min(len(city1), len(city2), len(city3))
maximum = max(len(city1), len(city2), len(city3))
if len(city1) == minimum:
    print(city1)
elif len(city2) == minimum:
    print(city2)
else:
    print(city3)
if len(city1) == maximum:
    print(city1)
elif len(city2) == maximum:
    print(city2)
else:
    print(city3)

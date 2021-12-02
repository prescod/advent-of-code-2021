count = 0
_sum = None
last_sum = 99999999999999
last_3 = []
with open("1.txt") as f:
    for line in f:
        last_3.append(int(line))
        if len(last_3) == 4:
            last_3.pop(0)
            _sum = sum(last_3)
            if _sum > last_sum:
                count += 1
            last_sum = _sum
print(count)

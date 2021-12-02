count = 0
last_data = 99999999999999
with open("1.txt") as f:
    for line in f:
        data = int(line)
        if data > last_data:
            count += 1
        last_data = data
print(count)

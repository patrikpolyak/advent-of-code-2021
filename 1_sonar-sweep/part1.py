count_larger = 0
prev = 0

with open('input.txt', 'r') as f:
    for line in f:
        number = int(line.strip('\n'))

        if prev != 0 and number > prev:
            count_larger += 1

        prev = number

print(count_larger)

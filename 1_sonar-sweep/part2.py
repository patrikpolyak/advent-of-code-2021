import copy

count_larger = 0
current = []
prev = []

with open('input.txt', 'r') as f:
    for line in f:
        number = int(line.strip('\n'))

        # Remove oldest entry only we have already 3 measurements
        if len(current) == 3:
            current.pop(0)
        # Add new measurement regardless
        current.append(number)

        # Only compare if we have already 3 previous measurements
        if len(prev) == 3 and sum(current) > sum(prev): 
            count_larger += 1

        # Make sure that we don't get a shallow copy
        prev = copy.deepcopy(current)

print(count_larger)

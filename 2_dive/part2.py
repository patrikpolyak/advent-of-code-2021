horizontal = 0
depth = 0 
aim = 0

with open('input.txt', 'r') as f:
    for line in f:
        (direction, step) = line.strip('\n').split(' ')
        step = int(step)

        match direction:
            case "forward":
                horizontal += step
                depth = depth + aim * step
            case "up":
                aim -= step
            case "down":
                aim += step

print(f"We moved {horizontal} steps forward and changed depth by {depth} steps")

result = horizontal * depth
print(f"Result is: {result}")

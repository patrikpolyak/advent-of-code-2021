# Solve part 1 with copilot

file = 'input.txt'

# read lines from file and calculate the most common value per bit
line_length = 0
with open(file) as f:
    lines = f.readlines()
    line_length = len(lines[0]) - 1
    bits = [0] * line_length
    for line in lines:
        for i in range(line_length):
            bits[i] += line[i] == '1'

# set 1 where more than half of the bits are 1
gamma_rate = ''.join(['1' if bits[i] > len(lines) // 2 else '0' for i in range(line_length)])

# flip bits of gamma_rate and set to epsilon_rate
epsilon_rate = ''.join(['1' if gamma_rate[i] == '0' else '0' for i in range(line_length)])

print(f"Epsilon rate: {epsilon_rate}")
print(f"Gamma rate: {gamma_rate}")

# Convert binary to decimal
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)

print(f"Epsilon rate decimal: {epsilon_rate_decimal}")
print(f"Gamma rate decimal: {gamma_rate_decimal}")

# Multiply epsilon_rate_decimal by gamma_rate_decimal to get the result
result = epsilon_rate_decimal * gamma_rate_decimal

print(f"Result: {result}")
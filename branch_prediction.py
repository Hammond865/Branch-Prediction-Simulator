import sys
def zero_bit_prediction(lines):
    incorrect = 0
    for current in lines:
        # Split line along spaces; address then result
        substrings = current.split()
        # Assume every branch fails
        if int(substrings[1]) == 1:
            incorrect += 1

    return incorrect


def one_bit_prediction(lines, size):
    incorrect = 0
    table = []
    # Default value of zero at each index
    for i in range(0, size):
        table.append(0)

    for current in lines:
        # Split line along spaces; address then result
        substrings = current.split()
        index = int(substrings[0], 16) % size
        actual = int(substrings[1])
        # Check if prediction (value at index) matches result
        if table[index] != actual:
            incorrect += 1
        # Update value at index
        table[index] = actual

    return incorrect


def two_bit_prediction(lines, size):
    incorrect = 0
    table = []
    # Default value of zero at each index
    for i in range(0, size):
        table.append(0)

    for current in lines:
        # Split line along spaces; address then result
        substrings = current.split()
        index = int(substrings[0], 16) % size
        actual = int(substrings[1])
        # Check if prediction matches result, update values as needed
        match table[index]:
            # Predict not taken
            case 0:
                if actual == 1:
                    incorrect += 1
                    table[index] += 1
            case 1:
                if actual == 1:
                    incorrect += 1
                    table[index] += 1
                else:
                    table[index] -= 1
            # Predict taken
            case 2:
                if actual == 1:
                    table[index] += 1
                else:
                    incorrect += 1
                    table[index] -= 1
            case 3:
                if actual == 1:
                    # Do nothing
                    trash = 0
                else:
                    incorrect += 1
                    table[index] -= 1
        
    return incorrect


def three_bit_prediction(lines, size):
    incorrect = 0
    table = []
    # Default value of zero at each index
    for i in range(0, size):
        table.append(0)

    for current in lines:
        # Split line along spaces; address then result
        substrings = current.split()
        index = int(substrings[0], 16) % size
        actual = int(substrings[1])
        # Check if prediction matches result, update values as needed
        match table[index]:
            # Predict not taken
            case 0:
                if actual == 1:
                    incorrect += 1
                    table[index] += 1
            case 1 | 2 | 3:
                if actual == 1:
                    incorrect += 1
                    table[index] += 1
                else:
                    table[index] -= 1
            # Predict taken
            case 4 | 5 | 6:
                if actual == 1:
                    table[index] += 1
                else:
                    incorrect += 1
                    table[index] -= 1
            case 7:
                if actual == 1:
                    # Do nothing, keeping if statement the same for consistency/readability
                    trash = 0
                else:
                    incorrect += 1
                    table[index] -= 1
    return incorrect


filename = sys.argv[1]
num_bits = sys.argv[2]
bht_size = sys.argv[3]
result = -1

lines = []
infile = open(filename, "r")
for line in infile:
    lines.append(line)

if num_bits == 0:
    result = zero_bit_prediction(lines)
elif num_bits == 1:
    result = one_bit_prediction(lines, bht_size)
elif num_bits == 2:
    result = two_bit_prediction(lines, bht_size)
elif num_bits == 3:
    result = three_bit_prediction(lines, bht_size)

# Convert to percentage gotten correct
result = (1-(float(result)/len(lines))) * 100

print("%d branches in %s with %d bits and %d size: %f percent correct" % (len(lines), filename, num_bits, bht_size, result))

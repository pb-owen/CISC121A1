
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    # Check if list is empty
    if len(A) == 0:
        return []

    # Copy list
    rotated = [0] * len(A)

    for index in range(len(A)):

        new_index = (index + K) % len(A)

        rotated[new_index] = A[index]

    return rotated


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    # Find the distance that the frog needs to travel
    distance = Y - X
    # Find the number of jumps
    jumps = distance // D
    # Check if the frog has reached desired distance in # of predetermined jumps, if not go one more
    if distance % D != 0:
        jumps += 1

    return jumps


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    expected_sum = 0

    # Find out the sum of all expected number
    for number in range(1,len(A) + 2):
        expected_sum += number

    actual_sum = 0

    # Find out the actual sum of numbers
    for number in A:
        actual_sum += number

    # Use the difference to find the missing number
    missing = expected_sum - actual_sum

    return missing


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # Make empty dict to count occurances
    counts = {}

    # Count number of times each number appears
    for number in A:

        if number in counts:
            counts[number] +=1

        else:
            counts[number] = 1

    # Find the number that appears an odd number of times (see which is left unpaired)
    for number in counts:
        if counts[number] % 2 == 1:
            return number


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # Check length of list
    n = len(A)

    # List to track the numbers encountered
    seen = [False] * (n + 1)

    # Iterate through to check each number
    for number in A:

        # Checking if number is in valid range
        if number < 1 or number > n:
            return 0

        # Checking if number is a duplicate
        if seen[number]:
            return 0

        # Number has been seen already
        seen[number] = True

    # All required numbers have been seen exactly one time, therefor valid
    return 1

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[1:]

fib_numbers = fibonacci(101)

for idx, num in enumerate(fib_numbers, start=1):
    print(f"{idx}: {num}")

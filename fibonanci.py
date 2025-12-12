import time
import sys

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def measure_time(func, n, trials=3):
    times = []
    for _ in range(trials):
        start = time.perf_counter()
        result = func(n)
        end = time.perf_counter()
        times.append((end - start) * 1000)
    return result, sum(times) / len(times)

# === DEMO: Run for a single n ===
if __name__ == "__main__":
    # You can change this for testing
    n = int(input("Masukan Nilai N: "))

    print(f"Computing Fibonacci({n})...\n")

    # Iterative
    result_it, time_it = measure_time(fib_iterative, n)
    print(f"Iterative: F({n}) = {result_it}")
    print(f"Time: {time_it:.4f} ms\n")

    # Recursive (will be slow for n > 35)
    if n > 35:
        print("⚠️ Warning: Recursive version may take very long for n > 35.")
    try:
        result_rec, time_rec = measure_time(fib_recursive, n)
        print(f"Recursive: F({n}) = {result_rec}")
        print(f"Time: {time_rec:.4f} ms\n")
    except RecursionError:
        print("❌ RecursionError: n too large for recursive version.\n")
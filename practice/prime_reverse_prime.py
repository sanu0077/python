def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

start, end = map(int, input("Enter range (start end): ").split())
emirps = [n for n in range(start, end + 1) if is_prime(n) and is_prime(int(str(n)[::-1]))]

print(f"Emirps: {emirps}\nCount: {len(emirps)}")

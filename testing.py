a = int(input("Enter the first number of the range: "))
b = int(input("Enter the last number in the range: "))

prime_numbers = []

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers within the range from", a, "to", b, "are:", prime_numbers)

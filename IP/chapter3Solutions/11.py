def calculate_simple_interest(principal, rate, time):
    """
    Calculates the simple interest based on the provided principal, interest rate, and time.
    """
    interest = (principal * rate * time) / 100
    return interest


def calculate_compound_interest(principal, rate, time):
    """
    Calculates the compound interest based on the provided principal, interest rate, and time.
    """
    interest = principal * ((1 + rate / 100) ** time - 1)
    return interest


# Get user input
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate and display simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print("Simple Interest:", simple_interest)

# Calculate and display compound interest
compound_interest = calculate_compound_interest(principal, rate, time)
print("Compound Interest:", compound_interest)

import scipy.stats as stats
def normal_distribution():
    # Mean and standard deviation
    mean = float(input("Enter the mean (μ): "))
    std_dev = float(input("Enter the standard deviation (σ): "))
    x = float(input("Enter the value (x): "))

    # Calculate cumulative probability P(X ≤ x)
    prob = stats.norm.cdf(x, mean, std_dev)
    print(f"P(X ≤ {x}) = {prob}")

def binomial_distribution():
    # Number of trials and probability of success
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success (p): "))
    k = int(input("Enter the number of successes (k): "))

    # Calculate the probability of exactly k successes
    prob = stats.binom.pmf(k, n, p)
    print(f"P(X = {k}) = {prob}")

def poisson_distribution():
    # Mean (λ)
    lam = float(input("Enter the mean (λ): "))
    k = int(input("Enter the number of occurrences (k): "))

    # Calculate the probability of exactly k occurrences
    prob = stats.poisson.pmf(k, lam)
    print(f"P(X = {k}) = {prob}")

def exponential_distribution():
    # Rate parameter (λ)
    lam = float(input("Enter the rate (λ): "))
    x = float(input("Enter the value (x): "))

    # Calculate the probability P(X ≤ x)
    prob = stats.expon.cdf(x, scale=1/lam)
    print(f"P(X ≤ {x}) = {prob}")

def uniform_distribution():
    # Lower and upper bounds
    a = float(input("Enter the lower bound (a): "))
    b = float(input("Enter the upper bound (b): "))
    x = float(input("Enter the value (x): "))

    # Calculate cumulative probability P(X ≤ x)
    prob = stats.uniform.cdf(x, a, b-a)
    print(f"P(X ≤ {x}) = {prob}")

def main():
    while True:
        print("\nProbability Calculator")
        print("1. Normal Distribution")
        print("2. Binomial Distribution")
        print("3. Poisson Distribution")
        print("4. Exponential Distribution")
        print("5. Uniform Distribution")
        print("6. Exit")

        choice = int(input("Choose a distribution (1-6): "))

        if choice == 1:
            normal_distribution()
        elif choice == 2:
            binomial_distribution()
        elif choice == 3:
            poisson_distribution()
        elif choice == 4:
            exponential_distribution()
        elif choice == 5:
            uniform_distribution()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
        
if __name__ == "_main_":
    main()

import math

class Calculator:
    """A more complex calculator class with additional mathematical functionality."""

    def __init__(self):
        """Initializes the calculator object."""
        pass

    def add(self, a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtracts the second number from the first number."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides the first number by the second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Calculates the power of a number."""
        return base ** exponent

    def sqrt(self, a: float) -> float:
        """Calculates the square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(a)

    def factorial(self, n: int) -> int:
        """Calculates the factorial of a non-negative integer."""
        if n < 0:
            raise ValueError("Cannot calculate factorial of a negative number.")
        return math.factorial(n)

    def logarithm(self, value: float, base: float = math.e) -> float:
        """Calculates the logarithm of a number with the specified base."""
        if value <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(value, base)

    def gcd(self, a: int, b: int) -> int:
        """Calculates the greatest common divisor (GCD) of two integers."""
        return math.gcd(a, b)

    def sin(self, angle: float) -> float:
        """Calculates the sine of an angle in radians."""
        return math.sin(angle)

    def cos(self, angle: float) -> float:
        """Calculates the cosine of an angle in radians."""
        return math.cos(angle)

    def tan(self, angle: float) -> float:
        """Calculates the tangent of an angle in radians."""
        return math.tan(angle)


if __name__ == "__main__":
    # Example usage
    calc = Calculator()

    # Addition
    print(f"Addition: 3.5 + 2.5 = {calc.add(3.5, 2.5)}")

    # Subtraction
    print(f"Subtraction: 10 - 4.5 = {calc.subtract(10, 4.5)}")

    # Multiplication
    print(f"Multiplication: 3 * 7 = {calc.multiply(3, 7)}")

    # Division
    try:
        print(f"Division: 10 / 2 = {calc.divide(10, 2)}")
    except ValueError as e:
        print(e)

    # Power
    print(f"Power: 2^3 = {calc.power(2, 3)}")

    # Square root
    try:
        print(f"Square Root: √16 = {calc.sqrt(16)}")
    except ValueError as e:
        print(e)

    # Factorial
    try:
        print(f"Factorial: 5! = {calc.factorial(5)}")
    except ValueError as e:
        print(e)

    # Logarithm
    try:
        print(f"Logarithm: log(100) = {calc.logarithm(100, 10)}")
    except ValueError as e:
        print(e)

    # Greatest Common Divisor (GCD)
    print(f"GCD: gcd(48, 18) = {calc.gcd(48, 18)}")

    # Trigonometric functions
    print(f"Sine: sin(π/2) = {calc.sin(math.pi / 2)}")
    print(f"Cosine: cos(π) = {calc.cos(math.pi)}")
    print(f"Tangent: tan(π/4) = {calc.tan(math.pi / 4)}")

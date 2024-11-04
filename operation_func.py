class Calculator:
    """A simple calculator class to demonstrate basic arithmetic functionality."""

    def __init__(self):
        """Initializes the calculator object."""
        pass

    def add(self, a: float, b: float) -> float:
        """Adds two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtracts the second number from the first number.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of a - b.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides the first number by the second number.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of a / b.

        Raises:
            ValueError: If the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Calculates the power of a number.

        Args:
            base (float): The base number.
            exponent (float): The exponent to raise the base to.

        Returns:
            float: The result of base raised to the power of exponent.
        """
        return base ** exponent


if __name__ == "__main__":
    # Example usage
    calc = Calculator()

    # Addition
    result_add = calc.add(3.5, 2.5)
    print(f"Addition: 3.5 + 2.5 = {result_add}")

    # Subtraction
    result_subtract = calc.subtract(10, 4.5)
    print(f"Subtraction: 10 - 4.5 = {result_subtract}")

    # Multiplication
    result_multiply = calc.multiply(3, 7)
    print(f"Multiplication: 3 * 7 = {result_multiply}")

    # Division
    try:
        result_divide = calc.divide(10, 2)
        print(f"Division: 10 / 2 = {result_divide}")
    except ValueError as e:
        print(e)

    # Power
    result_power = calc.power(2, 3)
    print(f"Power: 2^3 = {result_power}")

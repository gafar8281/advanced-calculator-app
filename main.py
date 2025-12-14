class AdvancedCalculator:
    def __init__(self) -> None:
        self.result = 0
        self.TOLERANCE = 0.000001

    def add(self, val1: float, val2: float) -> float:
        return val1 + val2

    def subtract(self, val1: float, val2: float) -> float:
        return val1 - val2

    def multiply(self, val1: float, val2: float) -> float:
        return val1 * val2

    def divide(self, val1: float, val2: float) -> float:
        if val2 == 0:
            raise ZeroDivisionError("Unable to divide by zero")

        return val1 / val2

    # --- Advanced Mathematical Functions (Square root, Factorial, Exponents, nth root, Logarithms, Sine function)

    def square_root(self, val: int) -> float:
        """Implement the Babylonian method."""
        if val < 0:
            raise ValueError("Cannot calculate square root of negative number")
        if val == 0:
            return 0

        guess: float = val / 2
        while True:
            next_guess: float = 0.5 * (guess + val / guess)

            if abs(next_guess - guess) < self.TOLERANCE:
                return next_guess
            guess = next_guess

    def factorial(self, val: int) -> int:
        if val < 0:
            raise ValueError("Cannot find factorial of negative numbers")
        if val == 0 and val == 1:
            return 1

        output = 1
        for i in range(val, 0, -1):
            output *= i

        return output

    def exponents(self, base: int, power: int) -> int:
        return base**power

    def nth_root(self, x: float, n: float) -> float:
        """
        Calculates the n-th root of x (x^(1/n)).

        Args:
            x: The number (base).
            n: The degree of the root (exponent denominator).

        """
        return x ** (1 / n)

    def sine_taylor(self, x: float, terms: int = 5) -> float:
        """Taylor Series Formula for Sine: sin(x)= x - x³/3! + x⁵/5! - x⁷/7! + ..."""
        sin_x = 0
        for n in range(terms):
            sign = (-1) ** n
            sin_x += sign * (x ** (2 * n + 1)) / self.factorial(2 * n + 1)

        return sin_x

    def logarithms(self, a: float, b: float) -> float:
        """Calculates the logarithm, logb(a) = c  <==>  b^c = a."""
        for i in range(500):
            if b**i == a:
                return i

        return None

    # --- Financial Functions (EMI, Percentage)

    def emi_calculator(
        self, loan_amount: int, ann_interest: int, duration_months: int
    ) -> float:
        """
        Calculates the Equated Monthly Installment (EMI) for a loan.

        Args:
            loan_amount (float): The total principal loan amount.
            ann_interest (float): The annual interest rate (e.g., 8.5 for 8.5%).
            duration_months (int): The loan duration in months.

        Returns:
            float: The calculated EMI amount.

        """
        if loan_amount <= 0 or duration_months <= 0 or ann_interest < 0:
            raise ValueError("Values must be grater than zero.")

        # Calculate monthly interest
        r: float = ann_interest / (12 * 100)

        # Apply EMI formula
        a: float = (1 + r) ** duration_months
        n: float = loan_amount * r * a
        emi: float = n / (a - 1)

        return emi

    def percentage_calculator(self, percentage: float, num: float) -> float:
        calculated_percentage: float = (percentage * num) / 100
        return calculated_percentage

    def run(self) -> None:
        calculator_title = "Python Advanced CLI Calculator"
        print(calculator_title)
        print("-" * 40)
        print(
            "We support different types of calculators:\n \
               \na) Basic calculator-> +, -, *, / \
               \nb) Advanced Calculator -> Square root, Factorial, Exponent, nth root, Sine, Logarithm \
               \nc) Financial Calculator -> EMI calculator, Percentage calculator \
               \n \nSo, select your desired calculator"
        )
        print("-" * 40)

        while True:
            calculator_type = input("\nEnter your calculator type : ")

            if calculator_type in ["quit", "exit"]:
                print("Exiting calculator. Goodbye!")
                break

            calculator_map = {"a": "basic", "b": "advanced", "c": "financial"}

            if calculator_type in calculator_map:
                if calculator_map[calculator_type] == "basic":
                    print("\nBasic calculator-> +, -, *, /")

                    num1 = float(input("Enter the num 1: "))
                    operator = input("Enter the operator: ")
                    num2 = float(input("Enter the num 2: "))

                    if operator == "+":
                        self.result: float = self.add(num1, num2)
                    elif operator == "-":
                        self.result: float = self.subtract(num1, num2)
                    elif operator == "*":
                        self.result: float = self.multiply(num1, num2)
                    elif operator == "/":
                        self.result: float = self.divide(num1, num2)

                    print(f"\nResult: {num1} {operator} {num2} = {self.result}\n")

                elif calculator_map[calculator_type] == "advanced":
                    print(
                        "\nAdvanced Calculator -> \n1. Square root \n2. Factorial \n3. Exponent \
                           \n4. nth root \n5. Logarithms \n6. Sine value"
                    )

                    operator = int(input("Enter the operator: "))
                    adv_opertor_map: dict[int, str] = {
                        1: "square root",
                        2: "factorial",
                        3: "exponent",
                        4: "nth root",
                        5: "logarithm",
                        6: "sine",
                    }
                    if operator in {1, 2}:  # square root, factorial
                        val = float(input("Enter the val: "))

                        if operator == 1:
                            self.result = self.square_root(val)
                        else:
                            self.result = self.factorial(val)
                        print(
                            f"\nResult: {adv_opertor_map[operator]}({val}) = {self.result}\n"
                        )

                    elif operator in {4, 5}:  # nth root, logarithm
                        x = int(input("Enter the v1: "))
                        y = int(input("Enter the v2: "))

                        if operator == 4:
                            self.result = self.nth_root(x, y)
                        else:
                            self.result = self.logarithms(x, y)
                        print(
                            f"\nResult: {adv_opertor_map[operator]}({x}, {y}) = {self.result}\n"
                        )

                    elif operator == 3:  # exponent
                        base = int(input("Enter the base: "))
                        power = int(input("Enter the power: "))

                        self.result = self.exponents(base, power)
                        print(
                            f"\nResult: {adv_opertor_map[operator]}({base}, {power}) = {self.result}\n"
                        )

                    elif operator == 6:  # sine
                        x = int(input("Enter the base: "))

                        self.result = self.sine_taylor(x)
                        print(f"Sin({x}) : {self.result}")

                elif calculator_map[calculator_type] == "financial":
                    print(
                        "\nFinancial Calculator -> \n1. EMI calculator \n2. Percentage calculator"
                    )
                    operator = int(input("Enter the operator: "))

                    if operator == 1:  # EMI calculator
                        # loan_amount, ann_interest, duration
                        loan_amount = int(input("Enter the loan amount : ₹"))
                        ann_interest = int(input("Enter the annula interest : "))
                        duration = int(input("Enter the duration : "))

                        self.result = self.emi_calculator(
                            loan_amount, ann_interest, duration
                        )
                        print(f"EMI amount: {self.result}")

                    else:  # percentage calculator
                        percentage = float(input("Enter the percentage : "))
                        number = float(input("Enter the num : "))
                        self.result = self.percentage_calculator(percentage, number)
                        print(f"{percentage}% of {number} is {self.result}")

            else:
                print("Give valid option!!!")


if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.run()

import os


class CalculatorEngine:
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

    def square_root(self, val: int, tolerance: float = 0.000001) -> float:
        """Implement the Babylonian method."""
        if val < 0:
            raise ValueError("Cannot calculate square root of negative number")
        if val == 0:
            return 0

        guess: float = val / 2
        while True:
            next_guess: float = 0.5 * (guess + val / guess)

            if abs(next_guess - guess) < tolerance:
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


class AdvancedCalulator:
    def __init__(self) -> None:
        self.engine = CalculatorEngine()

    def clear_screen(self) -> str:
        cmd = "clear" if os.name == "posix" else "cls"
        os.system(cmd)

    def display_result(self, output_str) -> None:
        print(
            f"{'\033[92m'}{'\033[1m'} {output_str} {'\033[0m'}{'\033[92m'}{'\033[0m'}"
        )
        input("\nPress Enter to continue...")

    def run(self) -> None:
        while True:
            self.clear_screen()
            print(f"╔{'═' * 58}╗")
            print(f"║ Python Advanced CLI Calculator{' ' * 27}║")
            print(f"╚{'═' * 58}╝")
            print(
                "\n[1] Basic calculator-> Add, Subtract, Divide, Multiply \
                \n[2] Advanced Calculator -> Square root, Factorial, Exponent, nth root, Sine, Logarithm \
                \n[3] Financial Calculator -> EMI calculator, Percentage calculator \
                \n[Q] Quit \
                \n "
            )
            print("-" * 40)

            calculator_type = input("\nSelect mode > ")

            if calculator_type.lower() == "q":
                break

            if calculator_type == "1":
                self.basic_operation()

            elif calculator_type == "2":
                self.advanced_operation()

            elif calculator_type == "3":
                self.financial_operation()

            else:
                print("Give valid option!!!")

    def basic_operation(self) -> None:
        print(
            "\nBasic operation => \
                  \n[1] Add \
                  \n[2] Subtract \
                  \n[3] Divide \
                  \n[4] Multiply"
        )

        operator = input("\nEnter the operator: ")

        num1 = float(input("Enter the num 1: "))
        num2 = float(input("Enter the num 2: "))

        result = 0
        opr = ""

        try:
            if operator == "1":
                result, opr = self.engine.add(num1, num2), "+"
            elif operator == "2":
                result, opr = self.engine.subtract(num1, num2), "-"
            elif operator == "3":
                result, opr = self.engine.divide(num1, num2), "/"
            elif operator == "4":
                result, opr = self.engine.multiply(num1, num2), "*"

            output_str = f"\nResult: {num1} {opr} {num2} = {result}\n"
            self.display_result(output_str)

        except Exception as e:
            print(f"error : {e}")

    def advanced_operation(self) -> None:
        print(
            "\nAdvanced Calculator =>  \
                \n[1] Square root  \
                \n[2] Factorial  \
                \n[3] Exponent \
                \n[4] nth root  \
                \n[5] Logarithms \
                \n[6] Sine value"
        )

        operator = input("\nEnter the operator: ")
        result = 0
        opr = ""

        if operator in {"1", "2"}:  # square root, factorial
            val = int(input("Enter the val: "))

            if operator == "1":
                result, opr = self.engine.square_root(val), "sqrt"
            else:
                result, opr = self.engine.factorial(val), "fact"

            output_str = f"\nResult: {opr}({val}) = {result}\n"
            self.display_result(output_str)

        elif operator in {"4", "5"}:  # nth root, logarithm
            x = int(input("Enter the v1: "))
            y = int(input("Enter the v2: "))

            if operator == "4":
                result, opr = self.engine.nth_root(x, y), "nth_root"
            else:
                result, opr = self.engine.logarithms(x, y), "log"

            output_str = f"\nResult: {opr}({x}, {y}) = {result}\n"
            self.display_result(output_str)

        elif operator == "3":  # exponent
            base = int(input("Enter the base: "))
            power = int(input("Enter the power: "))

            result = self.engine.exponents(base, power)
            output_str = f"\nResult: Exponent({base}, {power}) = {result}\n"
            self.display_result(output_str)

        elif operator == "6":  # sine
            x = int(input("Enter the base: "))
            result = self.engine.sine_taylor(x)

            output_str = f"\nResult: Sin({x}) : {result}"
            self.display_result(output_str)

    def financial_operation(self) -> None:
        print(
            "\nFinancial Calculator ->  \
             \n[1] EMI calculator \
             \n[2] Percentage calculator"
        )
        operator = int(input("\nEnter the operator: "))

        if operator == 1:  # EMI calculator
            # loan_amount, ann_interest, duration
            loan_amount = int(input("Enter the loan amount : ₹"))
            ann_interest = int(input("Enter the annula interest : "))
            duration = int(input("Enter the duration : "))

            result = self.engine.emi_calculator(loan_amount, ann_interest, duration)
            output_str = f"\nEMI amount: {result}"
            self.display_result(output_str)

        else:  # percentage calculator
            percentage = float(input("Enter the percentage : "))
            number = float(input("Enter the num : "))
            result = self.engine.percentage_calculator(percentage, number)

            output_str = f"\n{percentage}% of {number} is {result}"
            self.display_result(output_str)


if __name__ == "__main__":
    calculator = AdvancedCalulator()
    calculator.run()
    print("\nGoodbye!!!")

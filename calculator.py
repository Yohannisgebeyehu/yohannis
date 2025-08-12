def calculator():
    print("Standard Calculator")
    try:
        while True:
            operator = input("Enter operator [+,-,/,*,**, or 'exit']: ").strip().lower()
            if operator == "exit":
                print("Exiting the calculator")
                break

            valid_operators = ["+", "-", "*", "/", "**"]
            if operator not in valid_operators:
                print("Please enter a valid operator")
                continue

            numbers = []
            while True:
                number = input("Enter a number (or '=' to calculate): ").strip()
                if number == "=":
                    if len(numbers) < 2:
                        print("Enter at least two numbers before calculating.")
                        continue
                    break
                try:
                    num = float(number)
                    numbers.append(num)
                except ValueError:
                    print("Please enter numbers only.")
                    continue

            result = numbers[0]

            try:
                if operator == "+":
                    for num in numbers[1:]:
                        result += num
                    print(" + ".join(map(str, numbers)) + f" = {result}")

                elif operator == "-":
                    for num in numbers[1:]:
                        result -= num
                    print(" - ".join(map(str, numbers)) + f" = {result}")

                elif operator == "*":
                    for num in numbers[1:]:
                        result *= num
                    print(" * ".join(map(str, numbers)) + f" = {result}")

                elif operator == "/":
                    for num in numbers[1:]:
                        if num == 0:
                            raise ZeroDivisionError()
                        result /= num
                    print(" / ".join(map(str, numbers)) + f" = {result}")

                elif operator == "**":
                    for num in numbers[1:]:
                        result **= num
                    print(" ** ".join(map(str, numbers)) + f" = {result}")

            except ZeroDivisionError:
                print("Error: Division by zero is not allowed:")

    except Exception as e:
        print(f"An error occurred: {e}")

    print("Developed by yohannis")

calculator()



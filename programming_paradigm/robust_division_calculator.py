def safe_divide(numerator, denominator):

    try:

        x = float(numerator)

        y = float(denominator)

        return x / y

    except ZeroDivisionError:

        return "Error: Cannot divide by zero."

    except ValueError:

        return "Error: Please enter numeric values only."



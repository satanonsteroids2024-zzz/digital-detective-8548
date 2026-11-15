"""Number converter for Mission 5.

Asks for a decimal number and shows it in binary and hexadecimal.
Run it with:  python3 number_converter.py
"""


def main():
    text = input("Enter a decimal number: ")

    try:
        number = int(text)          # turns the typed text into a whole number
    except ValueError:
        print("That is not a whole number. Please type digits only, like 25.")
        return

    if number < 0:
        print("Please enter a positive number (or zero).")
        return

    binary = bin(number)            # e.g. 13 -> '0b1101'
    hexadecimal = hex(number)       # e.g. 255 -> '0xff'

    print(f"Decimal:     {number}")
    print(f"Binary:      {binary[2:]}   (Python shows it as {binary})")
    print(f"Hexadecimal: {hexadecimal[2:].upper()}   (Python shows it as {hexadecimal})")


if __name__ == "__main__":
    main()

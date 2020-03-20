def convert_binary_to_decimal(binary_value):
    """Function responsible for converting the informed binary value to
    decimal.

    Parameters
    ----------
    binary_value : str
        Value in binary. It comes as a string because the 'input' function
        returns just that type.

    Returns
    -------
    int
        Value converted from binary to decimal
    """
    return int(int(binary_value, 2))


def bin2dec_system_output(binary_value, decimal_value):
    """Displays conversion values ​​to the user on success. In case of failure,
    it shows the reason why the conversion is not possible.
    
    Parameters
    ----------
    binary_value : str
        Value entered by the user to be converted to decimal.
    decimal_value : int
        Value converted from decimal to binary.
    """
    if decimal_value:
        print(
            f"\nBinary value: {binary_value}"
            f"\nDecimal value: {decimal_value}\n"
        )
    else:
        print(
            f"\nThe value '{binary_value}' is not a binary. Try again.\n"
        )


def user_input():
    """Function to receive the binary value to be converted for the user.
    
    Returns
    -------
    str
        Value entered by the user.
    """
    return input("What value do you want to convert from binary to decimal? ")


def loop():
    """Infinite loop to process conversions until the user gets tired.
    """
    while True:
        informed_binary = user_input()
        try:
            converted_binary_to_decimal_value = convert_binary_to_decimal(
                binary_value=informed_binary
            )
        except ValueError:
            converted_binary_to_decimal_value = None

        bin2dec_system_output(
            binary_value=informed_binary,
            decimal_value=converted_binary_to_decimal_value,
        )


def main():
    """Main function in which the Bin2Dec processing loop is called.
    """
    print("Welcome to Bin2Dec!\nTo exit, press 'CTRL + C'.\n")

    try:
        loop()
    except KeyboardInterrupt:
        print("\n\nBye, bye!!\n")


if __name__ == "__main__":
    main()

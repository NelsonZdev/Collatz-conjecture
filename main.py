def verify_even_and_odd(number):
    return number % 2


def main():
    user_number = int(input('Please inpt one number: '))
    number_buffer = user_number
    result = user_number
    #
    while (result != 1):
        if verify_even_and_odd(number_buffer) == 0:
            result = int(number_buffer / 2)
        else:
            result = (number_buffer * 3) + 1
        print(result)
        number_buffer = result


if __name__ == "__main__":
    main()

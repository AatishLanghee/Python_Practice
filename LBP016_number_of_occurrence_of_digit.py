def number_of_occurrence_of_digit(num_: int, digit_: int) -> None:
    print(f'Given number is: {num_}')
    print(f'Given digit to find occurrence is: {digit_}')
    count: int = 0
    for d in str(num):
        if d == str(digit_):
            count += 1

    print(f'Number of occurrence of the digit {digit_} in {num_} is: {count}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    digit: int = int(input("Enter the digit: "))
    number_of_occurrence_of_digit(num, digit)

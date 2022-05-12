def duck_number(num_: str) -> None:
    print(f'Given number is: {num_}')
    temp_num: int = int(num_)
    if temp_num >= 0:
        if num_[0] == "0":
            print("Not a duck number.")
        else:
            if "0" in str(temp_num):
                print("Duck number.")
            else:
                print("Not a duck number.")


if __name__ == '__main__':
    num: str = input("Enter the number: ")
    duck_number(num)

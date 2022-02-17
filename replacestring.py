def replace_string(user_str, input_str):
    user_str = user_str.replace("<<UserName>>", input_str)
    return user_str


def main():
    input_str = ''
    while len(input_str) < 3:
        input_str = input("Enter your name ")
    output_str = replace_string("Hello <<UserName>>, How are you?", input_str)
    print(output_str)


if __name__ == "__main__":
    main()

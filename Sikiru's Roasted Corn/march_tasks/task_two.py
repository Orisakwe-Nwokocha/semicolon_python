import re


def task_two(user_input: str) -> str:
    letters = re.sub('[^a-zA-Z]', '', user_input)
    digits = re.sub('[^0-9]', '', user_input)

    return f"LETTERS {len(letters)} DIGITS {len(digits)}"


def second_try(user_input: str) -> dict:
    letters = re.sub('[^a-zA-Z]', '', user_input)
    digits = re.sub('[^0-9]', '', user_input)
    dictionary = {"LETTERS": len(letters), "DIGITS": len(digits)}
    return dictionary


if __name__ == '__main__':
    print(task_two('hello world! 123'))
    print(second_try('hello world! 123'))

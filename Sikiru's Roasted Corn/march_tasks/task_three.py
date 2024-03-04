import re


def task_three(user_input: str) -> str:
    upper_case_letters = re.findall('[A-Z]', user_input)
    lower_case_letters = re.findall('[a-z]', user_input)

    return f"UPPER CASE {len(upper_case_letters)} LOWER CASE {len(lower_case_letters)}"


def second_try(user_input: str) -> dict:
    upper_case_letters = re.findall('[A-Z]', user_input)
    lower_case_letters = re.findall('[a-z]', user_input)
    dictionary = {"UPPER CASE": len(upper_case_letters), "LOWER CASE": len(lower_case_letters)}
    return dictionary


if __name__ == "__main__":
    print(task_three("Hello world!"))
    print(second_try("Hello world!"))


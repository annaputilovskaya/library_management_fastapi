def convert_camel_to_snake_case(input_str: str) -> str:
    """
    Преобразует текст, в котором слова начинаются с заглавной буквы и пишутся подряд,
    в текст, где все слова с маленькой буквы через нижнее подчеркивание.
    Аббревиатуры объединяются в одно слово.
    """
    chars = []
    for i, char in enumerate(input_str):
        if i and char.isupper():
            next_i = i + 1
            flag = next_i >= len(input_str) or input_str[next_i].isupper()
            prev_char = input_str[i - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append("_")
        chars.append(char.lower())
    return "".join(chars)

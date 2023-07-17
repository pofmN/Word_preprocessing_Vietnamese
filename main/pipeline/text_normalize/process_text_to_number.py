number_dict = {
    'lẻ': -1,
    'linh': -1,
    'phẩy': -2,
    'phần': -3,
    'không': 0,
    'một': 1,
    'mốt': 1,
    'hai': 2,
    'ba': 3,
    'bốn': 4,
    'tư': 4,
    'năm': 5,
    'lăm': 5,
    'rưỡi': 5,
    'sáu': 6,
    'bảy': 7,
    'tám': 8,
    'chín': 9,
    'mười': 10,
    'mươi': 10,
    'chục': 10,
    'trăm': 100,
    'nghìn': 1000,
    'ngàn': 1000,
    'triệu': 1000000,
    'tỷ': 1000000000
}

def _calculate_number(tupl: tuple()) -> int:
    number_str = _convert_tup_to_str(tupl)
    try:
        return eval(number_str)
    except:
        return None

def _convert_tup_to_str(tupl: tuple()) -> str:
    return "".join([str(value) for value in tupl])

def covert_text_to_number(list_word_number: list) -> int:
    stack_number = tuple()
    num_biggest_10 = 0
    num_bigger_10 = 0
    result_number = ()

    for i, text_number in enumerate(list_word_number):
        number = number_dict[text_number]
        if number == -2 or number == -3:
            if number == -2:
                result_number = (_calculate_number(stack_number), ".")
            if number == -3:
                result_number = (_calculate_number(stack_number), "/")
            stack_number = ()
            num_biggest_10 = 0
            num_bigger_10 = 0
            continue

        if number == -1:
            stack_number = (_calculate_number(stack_number), "+",)

        elif number == -2:
            stack_number += ("+0.",)

        elif number >= 10:
            if number > num_bigger_10:
                if number > num_biggest_10:
                    if stack_number:
                        stack_number = (_calculate_number(stack_number) * number,)
                    else:
                        stack_number = (number,)
                    num_biggest_10 = number
                else:
                    stack_number = (stack_number[0], "+",) + (_calculate_number(stack_number[2:]) * number,)
            else:
                stack_number += ("*", number,)

            num_bigger_10 = number
        else:
            pre_number = int(number_dict[list_word_number[i - 1]])

            if text_number == "mốt" and pre_number >= 10:
                stack_number += ("+", int(pre_number / 10),)
            else:
                if i - 1 >= 0 and pre_number >= 10:
                    stack_number += ("+",)
                    if i == len(list_word_number) - 1 or list_word_number[i + 1] in ["phần", "phẩy"]:
                        stack_number += (int(number * pre_number / 10),)
                    else:
                        stack_number += (number,)
                else:
                    if i == 0 and number == 0:
                        return None
                    stack_number += (number,)
    if result_number:
        result_number += (_calculate_number(stack_number),)
        return _convert_tup_to_str(result_number)
    else:
        return _calculate_number(stack_number)

def special_cases(list_word_number: list):
    if list_word_number[-1] in ["linh", "lẻ", "phẩy", "phầnba"]:
        list_word_number = list_word_number[:-1]
    elif list_word_number[0] in ["linh", "lẻ", "phẩy", "phần"]:
        list_word_number = list_word_number[1:]
    elif len(list_word_number) == 2 and list_word_number[1] == "năm":
        list_word_number = []
    return list_word_number



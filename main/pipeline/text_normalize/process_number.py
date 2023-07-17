import re
from .process_measure import covert_measure,unit_measure
from .process_text_to_number import number_dict,covert_text_to_number,special_cases

_patten_texts = "[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễếệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]"
_patten_split_2_units = r"([\d+.,/]+)?(" + _patten_texts + r"+/" + _patten_texts + r"+)"
_pattens_number_commas = r"^\d+(?:[.,]\d{3})+$"

def _split_2_units(token:str):
    token_split = re.split(_patten_split_2_units, token)
    return list(filter(None, token_split))

def normalize_number(list_words,i):
    token = list_words[i]
    new_i = 0

    list_covert_measure = covert_measure(token)
    list_split_2_units = _split_2_units(token)

    # 300.000 -> 300000
    if re.search(_pattens_number_commas, token):
        list_words[i] = re.sub(r"[.,]", "", token)
    # 2km5 -> 2.5 km
    elif len(list_covert_measure) == 2:
        list_words = list_words[:i] + list_covert_measure + list_words[i + 1:]
    # 2km/h -> 2 km/h
    elif len(list_split_2_units) == 2:
        list_words = list_words[:i] + list_split_2_units + list_words[i + 1:]
    # mười lăm -> 15
    elif token in number_dict.keys():
        k = i
        t = 0
        len_list_words = len(list_words)
        for j in range(i, len_list_words):
            word_next = list_words[j]
            if word_next in number_dict.keys():
                if word_next in ["nghìn","ngàn","triệu","tỷ"]:
                    t += 1
                else:
                    t = 0
                k = j - t if j == len_list_words-1 else j
            else:
                k -= t
                break
        if i < k + 1:
            list_word_number = special_cases(list_words[i:k + 1])
            number_coverted = covert_text_to_number(list_word_number)
            if number_coverted:
                if len(list_word_number) == 0:
                    new_i = 1
                elif len(list_word_number) == 1:
                    if 0 <= number_dict[list_word_number[0]] <= 10 and ((i - 1 >= 0 and list_words[i - 1] in unit_measure) or (
                            i + 1 < len(list_words) and list_words[i + 1] in unit_measure)):
                        list_words = list_words[:i] + [str(number_coverted)] + list_words[k + 1:]
                    else:
                        new_i = 1
                else:
                    list_words = list_words[:i] + [str(number_coverted)] + list_words[k + 1:]
            else: new_i = k+1 - i
        else:
            new_i = 1
    # 1 km 2 -> 1km2
    elif i - 2 >= 0 and list_words[i - 1] in unit_measure and token.isdigit() and list_words[i - 2].isdigit():
        list_words = list_words[:i - 2] + [str(list_words[i - 2] + list_words[i - 1] + token)] + list_words[i + 1:]
        new_i = -2
    else:
        new_i = 1
    return list_words,new_i
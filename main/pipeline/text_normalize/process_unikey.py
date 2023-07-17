import ujson
import re
def __load_file_dict(file="./pipeline/text_normalize/dictionary/dict_fix_unikey.json") -> dict:
    with open(file, encoding="utf8") as f:
        return ujson.load(f)

_dictionary_fix_unikey = __load_file_dict()
_dictionary_err = _dictionary_fix_unikey["errors"]
_dictionary_hat = _dictionary_fix_unikey["error_hat"]

def __switch_to_unikey(token: str,pre_token:str | None=None,after_token:str=None) -> str:
    """
    Hàm sửa ee -> ê, oo -> ô, ow -> ơi, uw -> ư
    :param token: một từ trong câu
    :return: trả về từ đã chuyển đúng dấu
    """
    check_word_vn = is_vn(token, pre_token, after_token)
    if check_word_vn[1]:
        for key, value in _dictionary_hat.items():
            if key in token:
                token = token.replace(key, value)
                break
        for key, value in _dictionary_err.items():
            if key in token:
                token = token.replace(key, value)
                break
        output = token
    else:
        output = check_word_vn[0]
    return output

pattern = r'[íỉĩịìáàảãạăắằặẳẵâấầậẫẩéẻèẽẹêếệểễôốổồộổơờớỡởợưứừửữựýỵỳỷỹỈĨỊÌÁÀẢÃẠĂẮẰẶẲẴÂẤẦẬẪẨÉẺÈẼẸÊẾỆỂỄÔỐỔỒỘỔƠỜỚỠỞỢƯỨỪỬỮỰÝỴỲỶỸĐđ]'
def _contains_vietnamese_chars(text):
    matches = re.findall(pattern, text)
    return len(matches) > 0


mid = ["ai", "ao", "au", "ay", "âu", "ây", "êu", "eo", "ia", "ie", "iê", "yê", "iu", "oa", "oe", "oă", "oa", "oi","oe","ơi", "ua", "uâ", "uă", "uâ", "ue", "ua", "ui", "ưi", "uo", "ươ", "ưu", "uơ", "uy"]
start_one = ["b", "c", "d", "đ", "g", "h", "i", "k", "l", "m", "n", "q", "p", "r", "s", "t", "v", "x"]
start_two = ["tr", "ph", "ng", "gh", "ch", "qu", "gi", "kh", "th", "qu", "ph", "nh"]
end_two = ["ch", "ng", "nh"]
mid_one = ["a", "ă", "â", "e", "ê", "i", "y", "o", "ô", "ơ", "u", "ư"]
end_one = ["c", "t", "p", "m", "n", "y", "i", "e", "a", "o"]
def is_vn(tk, tk_prev=None, tk_next=None):
    token = tk.strip()
    input = token[::-1].replace("f", "", 1).replace("s", "", 1).replace("r", "", 1).replace("x", "", 1).replace("dd","d",1).replace("j", "", 1)[::-1].lower()
    input = input.replace(".", "").replace(",", "").replace("?", "").replace(":", "").replace(";", "").replace("!", "").replace('"', "").replace("'", "")
    flat = False

    # def remo_tone(input):
    #     output = input
    #     if input.endswith("s"):
    #          output = output[::-1].replace("s","",1)[::-1]
    #     if input.endswith("f"):
    #         output = output[::-1].replace("f","",1)[::-1]
    #     if input.endswith("r"):
    #         output = output[::-1].replace("r","",1)[::-1]
    #     if input.endswith("x"):
    #         output = output[::-1].replace("x","",1)[::-1]
    #     if input.endswith("j"):
    #         output = output[::-1].replace("j","",1)[::-1]
    #
    #     return output
    #
    #
    #
    # input = remo_tone(input)

    if tk_prev is not None and tk_next is not None:
        if is_vn(tk_prev)[1] is not True and is_vn(tk_next)[1] is not True:
            flat = False
            return (tk, flat)

    if (input.count('e') >= 2):
        input = input[::-1].replace("e", "", 1)[::-1]
    if (input.count('a') >= 2):
        input = input[::-1].replace("a", "", 1)[::-1]
    if (input.count('w') >= 1):
        input = input[::-1].replace("w", "", 1)[::-1]
    if (input.count('o') >= 2):
        input = input[::-1].replace("o", "", 1)[::-1]

    if len(tk) == 1:
        return (token, flat)

    if len(tk) > 9:
        return (token, flat)

    if (input.count('e') >= 2):
        flat = False
        return (token, flat)

    if (input.count('a') >= 2):
        flat = False
        return (token, flat)

    if (input.count('w') >= 1):
        flat = False
        return (token, flat)

    if (input.count('o') >= 2):
        flat = False
        return (token, flat)

    if 3 <= len(tk) <= 9:
        if (len(input) == 7):
            if input[0:3] == "ngh" and input[3:5] in mid and input[5:7] == "ng":
                flat = True
            else:
                flat = False
        if len(input) == 5:
            if input[0:3] == "ngh" and input[3:5] in mid:
                flat = True
            if input[0:2] in start_two:  # nh a nh
                if input[3:5] in end_two:
                    if input[2] in ["a", "e", "i", "y", "o", "u"]:
                        flat = True
                if input[4] in end_one:
                    if input[2:4] in mid:
                        flat = True
            if input[0] in start_one:
                if input[1:3] in mid:
                    if input[3:5] in end_two:
                        flat = True
        if len(input) == 6:
            if input[0:3] == "ngh" and input[3:5] in mid and input[5] in start_one:
                flat = True
            if input[0:2] in start_two and input[2:4] in mid and input[4:6] in end_two:
                flat = True
            if input[0:2] in start_two and input[2:4] in mid and input[4:6] in ["en"]:
                flat = True
        if len(input) == 4:
            if input[0:3] == "ngh" and input[3] in mid_one:
                flat = True
            if input[0:2] in start_two and input[2] in mid_one and input[3] in end_one:
                flat = True
            if input[0] in start_one and input[1] in mid_one and input[2:4] in end_two:
                flat = True
            if input[0:2] in mid and input[2:4] in end_two:
                flat = True
            if input[0] in start_one and input[1:3] in mid:
                flat = True
        if len(input) == 3:
            if input[0:2] in start_two and input[2] in mid_one:
                flat = True
            if input[0] in start_one and input[1] in mid_one and input[2] in end_one:
                flat = True
            if input[0] in mid_one and input[1:3] in end_two:
                flat = True
            if input[0] in start_one and input[1:3] in mid:
                flat = True
            # flat = False
        if len(input) == 2:
            if input[0] in start_one and input[1] in mid_one:
                flat = True
            if input in mid:
                flat = True
        if len(input) == 1:
            flat = True

    if (_contains_vietnamese_chars(input)):
        flat = True
        return (token, flat)

    return (token, flat)

list_end = ["c", "t", "p", "m", "n", "i", "y", "ch", "ng", "nh"]
list_start = ["b", "c", "d", "đ", "g", "h", "i", "k", "l", "m", "n", "q", "p", "r", "s", "t", "v", "x", "tr", "ph",
              "ng", "gh", "ch", "qu", "gi", "kh", "ngh", "th", "qu", "ph"]
list_tone = ["s", "f", "x", "r", "j"]
def fix_tone(token: str, pre_token:str = "", after_token:str = "") -> str:
    if pre_token is not None and after_token is not None:
        check_is_vn = is_vn(token, pre_token, after_token)
    else:
        check_is_vn = is_vn(token)

    if (check_is_vn[1]):
        if token[-1] in list_tone:
            if len(token) >= 5:  # 3 - 2
                if (token[0:3] == "ngh" and token[-3:-1] in list_end):
                    start = token[0:3]
                    mid = token[3:len(token) - 3] + token[-1]
                    end = token[-3:-1]
                    token = start + mid + end
                    return token

            if len(token) >= 6 and token[0:2] in list_start and token[-3:-1] in list_end:  # 2 - 2
                start = token[0:2]
                mid = token[2:len(token) - 3] + token[-1]
                end = token[-3:-1]
                token = start + mid + end
                return token

            if token[0:2] in list_start and token[-2:-1] in list_end:  # 2 - 1
                start = token[0:2]
                mid = token[2:len(token) - 2] + token[-1]

                end = token[-2:-1]
                token = start + mid + end
                return token

            if token[0:1] not in list_start and token[0:2] not in list_start and token[-2:-1] in list_end:  # 0 - 1
                mid = token[0:len(token) - 2] + token[-1]
                end = token[-2:-1]
                token = mid + end
                return token
            if token[0:1] not in list_start and token[0:2] not in list_start and token[-3:-1] in list_end:  # 0 -2

                mid = token[0:len(token) - 3] + token[-1]
                end = token[-3:-1]
                token = mid + end
                return token

            if token[0:1] in list_start and token[-2:-1] in ["c", "t", "p", "m", "n", "y"]:  # 1 - 1
                start = token[0:1]
                mid = token[1:len(token) - 2] + token[-1]
                end = token[-2:-1]
                token = start + mid + end
                return token

            if token[0:1] in list_start and token[-3:-1] in ["ch", "ng", "nh"]:  # 1 - 2
                start = token[0:1]
                mid = token[1:len(token) - 3] + token[-1]
                end = token[-3:-1]
                token = start + mid + end
                return token

    return token

def process_unikey(token: str,pre_token:str | None= None,after_token: str | None=None) -> str:
    token = __switch_to_unikey(token, pre_token, after_token)
    output = fix_tone(token, pre_token, after_token)
    output = " ".join(output.split())
    return __switch_to_unikey(output, pre_token, after_token)


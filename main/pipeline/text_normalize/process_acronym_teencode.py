import ujson
import re

def _load_file(file=r"./pipeline/text_normalize/dictionary/dict_acronym.json") -> dict:
    with open(file, encoding="utf8") as f:
        return ujson.load(f)

_dict_acronym = _load_file()
_patten_number = "[-+]?(?:\d*\.*\d+)" #word_regex số
list_special_cases = {
        "m": "mét",
        "g": "gam",
        "k": "nghìn",
        "đ": "đồng",
        "tr": "triệu",
        "l": "lít",
        "s": "giây",
        "v": "vôn",
        "j": "jun",
        "ha": "héc-ta",
        "ft": "feet",
        "in": "inch",
    }

def process_acronym(token: str,pre_token:str=""):
    """
    Hàm nhận vào một từ và chuyển từ đó thành từ không viết tắt
    :param token: một từ trong câu
    :return: trả về từ đã chuyển từ viết tắt thành không viết tắt
    """
    word_lower = token.lower()
    if re.search(_patten_number,pre_token) and word_lower in list_special_cases.keys():
        token = list_special_cases[word_lower]
    elif word_lower in _dict_acronym:
        token = _dict_acronym[word_lower]
    return token

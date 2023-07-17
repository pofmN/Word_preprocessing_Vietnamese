import re
import ujson

pattens = "[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễếệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]"

def _load_file(file="./pipeline/text_normalize/dictionary/dict_tone_rules.json") -> dict:
    with open(file, encoding="utf8") as f:
        return ujson.load(f)
_dict_tone_mark = _load_file()

def process_tone_mark(token: str):
    if not re.findall(pattens, token):
        token_copy = token
        token = token.lower()
        for key in _dict_tone_mark.keys():
            if key in token:
                token = token.replace(key, _dict_tone_mark[key])
                break
        if token_copy.istitle():
            token = token.title()
        elif token_copy.isupper():
            token = token.upper()
    return token


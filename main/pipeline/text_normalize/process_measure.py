import re
# from .process_acronym_teencode import list_special_cases

unit_measure = ["mm",
                "cm",
                "dm",
                "m",
                "mg",
                "g",
                "kg",
                "cân",
                "kí",
                "mét",
                "km",
                "tr",
                "nghìn",
                "ngàn",
                "triệu",
                "tỷ",
                "k",
                "ml",
                "l",
                "lít",
                "đ",
                "inch",
                "feet",
                "dặm",
                "chai",
                "xị",
                "lít",
                "củ",
                "tỏi"
                ]
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
_pattens_check = r"(\d+(?:[.,]\d+)?)([^0-9\.]+)(\d*)"

def covert_measure(token : str):
    try :
        token_split = re.split(_pattens_check,token)
        token_split = list(filter(None, token_split))
        if (len(token_split) == 2 or len(token_split) == 3) and token_split[1] in unit_measure:
            if len(token_split) == 3:
                if token_split[0] == "2" and token_split[1] == "k":
                    token_split = [str(eval(token_split[0]+"*1000+"+token_split[2]))]
                else:
                    token_split = [str(eval(token_split[0]+"+0."+token_split[2])), token_split[1]]
            if len(token_split) == 2 and token_split[1] in list_special_cases.keys():
                token_split[1] = list_special_cases[token_split[1]]
        return token_split
    except:
        return []
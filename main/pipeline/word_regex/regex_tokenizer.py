# -*- coding: utf-8 -*-
import re, sys

VIETNAMESE_CHARACTER_UPPER = "[" + "|".join([
    "ABCDEFGHIJKLMNOPQRSTUVXYZ",
    "ÀÁẢÃẠ",
    "ĂẰẮẲẴẶ",
    "ÂẦẤẨẪẬ",
    "Đ",
    "ÈÉẺẼẸ",
    "ÊỀẾỂỄỆ",
    "ÌÍỈĨỊ",
    "ÒÓỎÕỌ",
    "ÔỒỐỔỖỘ",
    "ƠỜỚỞỠỢ",
    "ÙÚỦŨỤ",
    "ƯỪỨỬỮỰ",
    "ỲÝỶỸỴ"
]) + "]"
VIETNAMESE_CHARACTER_LOWER = VIETNAMESE_CHARACTER_UPPER.lower()
CHARAC = "[" + VIETNAMESE_CHARACTER_UPPER[1:-1] + VIETNAMESE_CHARACTER_LOWER[1:-1] + "]"

VIETNAMESE_NUMBER_UPPER = "[" + "|".join([
    "LINH", "Linh",
    "LẺ", "Lẻ",
    "PHẨY", "Phẩy"
    "PHẦN", "Phần"
    "KHÔNG", "Không",
    "MỘT", "Một",
    "MỐT", "Mốt",
    "HAI", "Hai",
    "BA", "Ba",
    "BỐN", "Bốn",
    "TƯ", "Tư",
    "NĂM", "Năm",
    "LĂM", "Lăm",
    "RƯỠI", "Rưỡi",
    "SÁU", "Sáu",
    "BẢY", "Bảy",
    "TÁM", "Tám",
    "CHÍN", "Chín",
    "MƯỜI", "Mười",
    "MƯƠI", "MƯƠI",
    "CHỤC", "Chục",
    "TRĂM", "Trăm",
    "NGHÌN", "Nghìn",
    "NGÀN", "Ngàn",
    "TRIỆU", "Triệu",
    "TỶ", "Tỷ",
    "TỈ", "Tỉ"
]) + "]"
VIETNAMESE_NUMBER_LOWER = VIETNAMESE_NUMBER_UPPER.lower()

NUMBER = "[" + VIETNAMESE_NUMBER_UPPER[1:-1] + VIETNAMESE_NUMBER_LOWER[1:-1] + "]"  # upper and lower
#################################################
# PRIORITY 1                                    #
#################################################
specials = [
    r"\=+\>+",
    r"->",
    r"\.{2,}",
    r"-{2,}",
    r"\>+\>+",
    r"[\d,./]+x+(?:[,./x\d])+", # e.g 3x4x...
    r"v\.v\.\.\.",
    r"v\.v\.",
    r"v\.v",
    r"°[CF]"
]
specials = "(?P<special>(" + "|".join(specials) + "))"

abbreviations = [
    r"[A-ZĐ]+&[A-ZĐ]+",  # e.g. H&M
    r"\d+[A-Za-z]+(\w?)+-\d+.\d+", # e.g. 43H-053.09 | 43H1-053.09
    r"[A-Za-z]+-+[A-Za-z]+([A-Za-z-]+)?", # e.g 1GZ-FE, MC-Asenal-MU
    r"[\d.,]+\%|[\d.,]+\‰|[\d.,]+\‱", #e.g 100% | 100‰ | 100‱
    r"Tp\.",
    r"Mr\.", r"Mrs\.", r"Ms\.",
    r"Dr\.", r"ThS\.", r"Th.S", r"Th.s", r"TS\.", r"Ts\.", r"T.S",
    r"[A-Za-z]+\.+[A-Za-z]+",  # dot at middle of word e.g PGS.TS
    f"{VIETNAMESE_CHARACTER_UPPER}+(?:\.{CHARAC}+)+\.?",
    f"{CHARAC}+['’]{CHARAC}+",  #  e.g. H'Mông, xã N’Thôn Hạ
    r"[A-ZĐ]+\.(.?!;$)"  # dot at the end of word
]
abbreviations = "(?P<abbr>(" + "|".join(abbreviations) + "))"

acronym = [
    f"(?<={NUMBER}\s)({CHARAC}+/+{CHARAC}+)+", # e.g 2 triệu lần/ngày
    f"(?<=[.,\d]\s)({CHARAC}+/+{CHARAC}+)+",  # e.g 2 lần/ngày
    f"[.,\d]+{CHARAC}+/+{CHARAC}+", # e.g 4lần/ngày
    r"([.,\d]?)+[A-Za-z/]+[/\d]+([A-Za-z/]|[/\d]?)+", # e.g A/F/300/200
    r"([.,\d])+[A-Za-z]+([/\d]?)+(\"|\')?" #e.g 1.05Jx19" | 1M5
]
acronym = "(?P<acro>(" + "|".join(acronym) + "))"

#################################################
# PRIORITY 2                                    #
#################################################

# urls pattern from nltk
# https://www.nltk.org/_modules/nltk/tokenize/casual.html
# with Vu Anh's modified to match fpt protocol
url = r"""             # Capture 1: entire matched URL
  (?:
  (ftp|http)s?:               # URL protocol and colon
    (?:
      /{1,3}            # 1-3 slashes
      |                 #   or
      [a-z0-9%]         # Single letter or digit or '%'
                        # (Trying not to match e.g. "URI::Escape")
    )
    |                   #   or
                        # looks like domain name followed by a slash:
    [a-z0-9.\-]+[.]
    (?:[a-z]{2,13})
    /
  )
  (?:                                  # One or more:
    [^\s()<>{}\[\]]+                   # Run of non-space, non-()<>{}[]
    |                                  #   or
    \([^\s()]*?\([^\s()]+\)[^\s()]*?\) # balanced parens, one level deep: (...(...)...)
    |
    \([^\s]+?\)                        # balanced parens, non-recursive: (...)
  )+
  (?:                                  # End with:
    \([^\s()]*?\([^\s()]+\)[^\s()]*?\) # balanced parens, one level deep: (...(...)...)
    |
    \([^\s]+?\)                        # balanced parens, non-recursive: (...)
    |                                  #   or
    [^\s`!()\[\]{};:'".,<>?«»“”‘’]     # not a space or one of these punct chars
  )
  |                        # OR, the following to match naked domains:
  (?:
    (?<!@)                 # not preceded by a @, avoid matching foo@_gmail.com_
    [a-z0-9]+
    (?:[.\-][a-z0-9]+)*
    [.]
    (?:[a-z]{2,13})
    \b
    /?
    (?!@)                  # not succeeded by a @,
                           # avoid matching "foo.na" in "foo.na@example.com"
  )
"""
url = "(?P<url>" + url + ")"

email = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
email = "(?P<email>" + email + ")"

phone = [
    r"\d{2,}-\d{3,}-\d{3,}"  # e.g. 03-5730-2357
    # very careful, it's easy to conflict with datetime
]
phone = "(?P<phone>(" + "|".join(phone) + "))"

datetime = [
    # date
    r"\d{1,2}\/\d{1,2}\/\d+",  # e.g. 02/05/2014
    r"\d{1,2}\/\d{1,4}(/+[A-Za-zĐ]+-+[A-Za-zĐ]+)?",  # e.g. 02/2014
    # [WIP] conflict with number 1/2 (a half)
    r"\d{1,2}-\d{1,2}-\d+",  # e.g. 02-03-2014
    r"\d{1,2}\-\d{1,4}(/+[A-Za-zĐ]+-+[A-Za-zĐ]+)?",  # e.g. 08-2014
    # [WIP] conflict with range 5-10 (from 5 to 10)
    r"\d{1,2}\.\d{1,2}\.\d+",  # e.g. 20.08.2014
    r"\d{4}\/\d{1,2}\/\d{1,2}",  # e.g. 2014/08/20
    r"\d{2}:\d{2}:\d{2}|\d{2}:\d{2}",  # e.g. 10:20:50 | 10:20
    r"\d+[Hh]+\d+[Pp]+\d+[Ss]+|\d+[Hh]+\d+[Pp]+\d+[']+|\d+[Hh]+\d+[Pp]+|\d+[Hh]+\d+"
    # e.g 14h20p30s,14H20P30S | 14h20p, 14H20P | 14h20,14H20
]
datetime = "(?P<datetime>(" + "|".join(datetime) + "))"

number = [
    r"\d+(?:\.\d+)+,\d+",  # e.g. 4.123,2,..
    r"\d+(?:\.\d+)+",  # e.g. 60.542.000,..
    r"\d+(?:,\d+)+",  # e.g. 100,000,000,...
    r"\d+(?:\/\d+)+", # e.g 255/255/3/...
    r"\d+(?:\-\d+)+", # e.g 055-022-0000-...
    r"\d+(?:[\.,_]\d+)?"  # 123
]
number = "(?P<number>(" + "|".join(number) + "))"

emoji = [
    r":+\)+",
    r"=+\)+",
    r"÷+\)+",
    r":D+(?=\s)",
    r":D+(?=$)",
    r"""
    (?:
      [<>]?
      [:;=8]                     # eyes
      [\-o\*\']?                 # optional nose
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      |
      [\)\]\(\[dDpP/\:\}\{@\|\\] # mouth
      [\-o\*\']?                 # optional nose
      [:;=8]                     # eyes
      [<>]?
      |
      </?3                       # heart
    )"""
]
emoji = "(?P<emoji>(" + "|".join(emoji) + "))"

punct = [
    r"\.",
    r"\,",
    r"\(",
    r"\)",
    r"ʺ"
]
punct = "(?P<punct>(" + "|".join(punct) + "))"

#################################################
# PRIORITY 3                                    #
#################################################
word = r"(?P<word>\w+)"

word_hyphen = [
    r"(?<=\b)\w+\-[\w+-]*\w+",  # before word_hyphen must be word boundary
    # case to notice: 1.600m-2.000m
]
word_hyphen = "(?P<word_hyphen>(" + "|".join(word_hyphen) + "))"

symbol = [
    r"\+",
    r"×",
    r"-",
    r"÷",
    r":+",
    r"%",
    r"\$",
    r">=",
    r"<=",
    r"\=+",
    r">",
    r"<",
    r"\^",
    r"_",
    r":+"
]
symbol = "(?P<sym>(" + "|".join(symbol) + "))"

non_word = r"(?P<non_word>[^\w\s])"

# Caution: order is very important for regex
regex_patterns = [
    specials,  # Priority 1
    abbreviations,
    url,  # Priority 2
    email,
    phone,
    datetime,  # datetime must be before
    acronym,
    number,
    emoji,
    punct,
    word_hyphen,  # Priority 3
    word,
    symbol,
    non_word  # non_word must be last
]
recompile_regex_patterns = False
regex_patterns_combine = r"(" + "|".join(regex_patterns) + ")"
if sys.version_info < (3, 0):
    regex_patterns_combine = regex_patterns_combine.decode('utf-8')
patterns = re.compile(regex_patterns_combine, re.VERBOSE | re.UNICODE)

# regex pattern to match extacted word "Viện nghiên cứu" or "chien luoc"
# and not match to other multi tokens word, such as "quoc gia"
pattern = re.compile(r"(\w+)(?:\s+)(\w+)", re.UNICODE)


def extract_match(m):
    for k, v in m.groupdict().items():
        if v is not None:
            return v, k


def tokenize(text, format=None, tag=False, use_character_normalize=True, use_token_normalize=True, fixed_words=[]):
    """
    tokenize text for word segmentation

    Args:
        use_token_normalize: use token normalize or not
        use_character_normalize: use character normalize or not
        tag: return token with tag or not
        format: format of result, default is None
    """
    global recompile_regex_patterns
    global patterns
    if len(fixed_words) > 0:
        compiled_fixed_words = [re.sub(' ', '\ ', fixed_word) for fixed_word in fixed_words]
        fixed_words_pattern = "(?P<fixed_words>" + "|".join(compiled_fixed_words) + ")"
        merged_regex_patterns = [fixed_words_pattern] + regex_patterns
        regex_patterns_combine = r"(" + "|".join(merged_regex_patterns) + ")"
        patterns = re.compile(regex_patterns_combine, re.VERBOSE | re.UNICODE)
        recompile_regex_patterns = True
    matches = [m for m in re.finditer(patterns, text)]
    tokens = [extract_match(m) for m in matches]

    if tag:
        return tokens

    tokens = [token[0] for token in tokens]

    if format == "text":
        return " ".join(tokens)

    return tokens
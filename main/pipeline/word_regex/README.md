# 🪄 Word Regular Expression <img src="https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?fit=476%2C280&ssl=1" width="100" height="45"/>

---
## Khái niệm, mục tiêu
>RegEx - hay còn được biết Regular Expression(Biểu thức chính quy) - là các mẫu(pattern) thay vì các chuỗi cụ thể được sử dụng để tìm/thay thế(Find/Replace).

>Mục tiêu của việc RegEx là tách từng từ theo pattern đã đưa ra. Điều này giúp ta xử lý Tiếng Việt và sử dụng ngôn ngữ này dễ dàng và hiệu quả hơn.

>Tham khảo từ code RegEx của [Under The Sea](https://github.com/undertheseanlp/underthesea/blob/main/underthesea/pipeline/word_tokenize/regex_tokenize.py) khoảng 50 pattern và phát triển thêm khoảng 30 pattern.
---
## Các phần được thêm và chỉnh sửa
Ặcccc

---
##  Mục lục 📑

[1. Liệt kê các ký tự và số](#1-liệt-kê-các-ký-tự-và-số-)

[2. RegEx có mức độ ưu tiên 1](#2-regex-có-mức-độ-ưu-tiên-1%EF%B8%8F⃣)

[3. RegEx có mức độ ưu tiên 2](#3-regex-có-mức-độ-ưu-tiên-2%EF%B8%8F⃣)

-    [a. Pattern về URL](#a-pattern-về-url-)
   
-    [b. Pattern về email](#b-pattern-về-email-%EF%B8%8F)
  
-    [c. Pattern về số điện thoại](#c-pattern-về-số-điện-thoại-%EF%B8%8F)
  
-    [d. Pattern về ngày tháng](#d-pattern-về-ngày-tháng-)
  
-    [e. Pattern về danh từ chỉ đơn vị đi kèm](#e-pattern-về-danh-từ-chỉ-đơn-vị-đi-kèm-)
  
-    [f. Pattern về số](#f-pattern-về-số-)
  
-    [g. Pattern về biểu cảm](#g-pattern-về-biểu-cảm-)
  
-    [h. Pattern về dấu](#h-pattern-về-dấu-)
    
[4. RegEx có mức độ ưu tiên 3](#4-regex-có-mức-độ-ưu-tiên-3%EF%B8%8F⃣)

[5. Thêm pattern](#5-thêm-pattern-)

[6. Trích xuất match](#6-trích-xuất-match-%EF%B8%8F)

[7. Hàm tokenize](#7-hàm-tokenize)

---
## 1. Liệt kê các ký tự và số 🔤🔢
`CHARACTER`: chữ hoa và thường của ký tự có dấu(á, ắ, ấ, ...)
```python
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
```
`NUMBER`: chữ hoa và thường của số ở dạng chữ(một, mốt, hai, ...)
```python
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

NUMBER = "[" + VIETNAMESE_NUMBER_UPPER[1:-1] + VIETNAMESE_NUMBER_LOWER[1:-1] + "]"
```
---
## 2. RegEx có mức độ ưu tiên 1️⃣
### Pattern về dấu và viết tắt 🗒️
`specials`: pattern về trường hợp đặt biệt của dấu (`Ex`: =>, ->, °C, ...)
```python
specials = [
    r"\=+\>+", # e.g ==>>
    r"->", # e.g -->>
    r"\.{2,}", # e.g ...
    r"-{2,}", # e.g ---
    r"\>+\>+", # e.g >>>
    r"[\d,./]+x+(?:[,./x\d])+", # e.g 3x4x...
    r"v\.v\.\.\.", # e.g v.v....
    r"v\.v\.", 
    r"v\.v",
    r"°[CF]" # e.g °C
]
specials = "(?P<special>(" + "|".join(specials) + "))"
```
`abbreviations`: pattern về từ viết tắt(`Ex`: TP.Hồ Chí Minh, PGS.TS, H'Mông, ...)
```python
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
```
---
## 3. RegEx có mức độ ưu tiên 2️⃣
### a. Pattern về URL 🔣
`URL`: pattern về URL(`Ex`: github.com/ketdoannguyen/AI_EmbeddingVietnameseNLP)

>Code có tham khảo từ [NLTK](https://www.nltk.org/_modules/nltk/tokenize/casual.html)

```python
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
```
### b. Pattern về email ✉️
`email`: pattern về email(`Ex`: nhokmant2003@gmail.com)
```python
email = r""" ([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|
            \"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+
            (\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])
        """
email = "(?P<email>" + email + ")"
```
### c. Pattern về số điện thoại ☎️
`phone`: pattern về phone(`Ex`: +84xxxxxxxxx, 0084xxxxxxxxx, 09-xxxx-xxxx, ...)
```python
phone = [
    r"\d{2,}-\d{3,}-\d{3,}",  # e.g. 03-5730-2357
    r"(?:\+84)+(\s?)+[\d-]+", # e.g +84xxx-xxx-xxx
    r"(?:0084)+(\s?)+[\d-]+", # e.g 0084xxx-xxx-xxx
    r"(?:00\s84)+(\s?)+[\d-]+" # e.g 00 84xxx-xxx-xxx
    # very careful, it's easy to conflict with datetime
]
phone = "(?P<phone>(" + "|".join(phone) + "))"
```
### d. Pattern về ngày tháng 📅
`datetime`: pattern về datetime(`Ex`: 11/07/2023, 11:35:10, 11H35P10', ...)
```python
datetime = [
    # date
    r"\d{1,2}\/\d{1,2}\/\d+",  # e.g. 02/05/2014
    r"\d{1,2}\/\d{1,4}",  # e.g. 02/2014
    # [WIP] conflict with number 1/2 (a half)
    r"\d{1,2}-\d{1,2}-\d+",  # e.g. 02-03-2014
    r"\d{1,2}-\d{1,4}",  # e.g. 08-2014
    # [WIP] conflict with range 5-10 (from 5 to 10)
    r"\d{1,2}\.\d{1,2}\.\d+",  # e.g. 20.08.2014
    r"\d{4}\/\d{1,2}\/\d{1,2}",  # e.g. 2014/08/20
    r"\d{2}:\d{2}:\d{2}|\d{2}:\d{2}",  # e.g. 10:20:50 | 10:20
    r"\d+[Hh]+\d+[Pp]+\d+[Ss']+|\d+[Hh]+\d+[Pp]+|\d+[Hh]+\d+"
    # e.g 14h20p30s, 14H20P30S | 14h20p, 14H20P | 14h20,14H20
]
datetime = "(?P<datetime>(" + "|".join(datetime) + "))"
```

### e. Pattern về danh từ chỉ đơn vị đi kèm 💲
`units`: pattern về units(`Ex`: lần/ngày, 1M5, ...)
```python
units = [
    f"(?<={NUMBER}\s)({CHARAC}+/+{CHARAC}+)+",  # e.g 2 triệu lần/ngày
    f"(?<=[.,\d]\s)({CHARAC}+/+{CHARAC}+)+",  # e.g 2 lần/ngày
    f"[.,\d]+{CHARAC}+/+{CHARAC}+",  # e.g 4lần/ngày
    r"([.,\d]?)+[A-Za-z/]+[/\d]+([A-Za-z/]|[/\d]?)+",  # e.g A/F/300/200
    r"([.,\d])+[A-Za-z]+([/\d]?)+(\"|\')?"  # e.g 1.05Jx19" | 1M5
]
units = "(?P<acro>(" + "|".join(units) + "))"
```
### f. Pattern về số 🔢
`number`: pattern về number(`Ex`: 4.123,2 | 60.231.222 | 23,333,122 |...)
```python
number = [
    r"\d+(?:\.\d+)+,\d+",  # e.g. 4.123,2,..
    r"\d+(?:\.\d+)+",  # e.g. 60.542.000,..
    r"\d+(?:,\d+)+",  # e.g. 100,000,000,...
    r"\d+(?:\/\d+)+", # e.g 255/255/3/...
    r"\d+(?:\-\d+)+", # e.g 055-022-0000-...
    r"\d+(?:[\.,_]\d+)?"  # 123
]
number = "(?P<number>(" + "|".join(number) + "))"  
```
### g. Pattern về biểu cảm 🗿
`emoji`: pattern về emoji(`Ex`: :), :P, :D, <3, ...)
>Code có tham khảo từ [NLTK](https://www.nltk.org/_modules/nltk/tokenize/casual.html)
```python
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
      [:;=83v]                     # eyes
      [<>]?
      |
      </?3                       # heart
    )"""
]
```
### h. Pattern về dấu 🔣
`punct`: pattern về punct(`Ex`: . , ( ) )
```python
punct = [
    r"\.",
    r"\,",
    r"\(",
    r"\)",
    r"ʺ"
]
punct = "(?P<punct>(" + "|".join(punct) + "))"
```
---
## 4. RegEx có mức độ ưu tiên 3️⃣
### Pattern về từ, gạch nối từ, dấu trong toán và non-word  🔤➖♾️
`word`: pattern về word(`Ex`: a, b, c, ...)
```python
word = r"(?P<word>\w+)"
```
`word_hyphen`: pattern về word hyphen(`Ex`: Anh-Em, ...)
```python
word_hyphen = [
    r"(?<=\b)\w+\-[\w+-]*\w+",  # before word_hyphen must be word boundary
    # case to notice: 1.600m-2.000m
]
word_hyphen = "(?P<word_hyphen>(" + "|".join(word_hyphen) + "))"
```
`symbol`: pattern về symbol(`Ex`: +, -, x, ÷, ...)
```python
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
```
`non_word`: pattern về non word(`Ex`: { } | ...)
```python
non_word = r"(?P<non_word>[^\w\s])"
```
---
## 5. Thêm pattern ➕
```python
# Caution: order is very important for regex
regex_patterns = [
    specials,  # Priority 1
    abbreviations,
    url,  # Priority 2
    email,
    phone,
    datetime,  # datetime must be before
    units,
    number,
    emoji,
    punct,
    # Priority 3
    word_hyphen,
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
```
- `regex_patterns` đưa patterns đã soạn vào một pattern chung
- `regex_patterns_combine` combine các patterns
- `patterns` compile cac patterns
---
## 6. Trích xuất match ➡️
```python
def extract_match(m):
    for k, v in m.groupdict().items():
        if v is not None:
            return v, k
```
- `extract_match` nhóm các từ đã được RegEx bằng `groupdict`
---
## 7. Hàm tokenize
```python
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
```
- Hàm `tokenize` có đầu vào là một text, `format` là text
- Nếu text có văn bản hàm sẽ tách các từ theo pattern và nhóm lại bằng `extract_match`
---

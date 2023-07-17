from .process_acronym_teencode import process_acronym
from .process_unikey import process_unikey
from .process_tone_marks import process_tone_mark
from .process_number import normalize_number
import unicodedata

def _normalize_each_token(token: str) -> str:
    if not type(token) == str:
        token = token.decode("utf-8")
    token = unicodedata.normalize("NFC", token)
    token = process_tone_mark(token)
    return token

def normalize(list_words):
    i = 0
    while i < len(list_words):
        token = str(list_words[i])
        token = process_unikey(token,list_words[i-1],list_words[i+1]) if i>0 and i<len(list_words)-1 else process_unikey(token)
        token = process_acronym(token,list_words[i-1]) if i>0 else process_acronym(token)
        list_words[i] = _normalize_each_token(token)
        list_words,new_i = normalize_number(list_words,i)
        i += new_i
    return list_words

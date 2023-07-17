with open(r'data/VnVocab.txt', encoding="utf8") as f:
    vn_vocab = f.readlines()
with open(r'data/TuLay.txt', encoding="utf8") as l:
    tulay_vocab = l.readlines()
with open(r'data/TuGhep.txt', encoding="utf8") as g:
    tughep_vocab = g.readlines()

dictionary = vn_vocab[0]
def search_tulay_tughep(token: str):
    dictionary = vn_vocab[0]
    result = []
    dictionary = dictionary.split(", ")

    if token.count(' ')>=1:
        word_value = [token, check_tulay(token)]
        result.append(word_value)
    else:
        for word in dictionary:
            word_split = word.split()
            for character in word_split:
                if token.strip().lower() == character.strip().lower():
                    word_value = [word,check_tulay(word)]
                    result.append(word_value)

    return result


# def search_tulay_tughep(token: str):
#     dictionary = vn_vocab[0]
#     result = []
#     dictionary = dictionary.split(", ")
#
#     for word in dictionary:
#         token=token
#         if token in word:
#             word_value = [word, check_tulay(word)]
#             result.append(word_value)
#
#     return result
def check_tulay(word):
    dictionary_tulay = tulay_vocab[0]
    dictionary_tughep = tughep_vocab[0]
    if word in dictionary_tulay:
        return "Từ Láy"
    elif word in dictionary_tughep:
        return "Từ Ghép"
    else:
        return "Không Xác Định"


# print(check_tulay("y sĩ"))

list = search_tulay_tughep("nhí")
## Nhập 1 từ đơn thì nó sẽ tìm trong Vnvocab các từ nào chứa từ đơn đó rồi segment ra từ láy, từ ghép
print(list)
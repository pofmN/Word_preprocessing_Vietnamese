import json
from tqdm import tqdm

with open('../application/segment_tulay_tughep/data/VnVocab.txt', encoding="utf8") as f:
    vn_vocab = f.read()
list_vocab = vn_vocab.split(", ")
dict_vocab = {}
for vocab in tqdm(list_vocab):
    list_vocab_con = []
    last_word = vocab.split()[-1]
    for vocab_con in list_vocab:
        if last_word == vocab_con.split()[0]:
            list_vocab_con.append(vocab_con)
    if list_vocab_con:
        dict_vocab[vocab] = list_vocab_con

with open('./vocab_connect.txt', 'w', encoding="utf8") as convert_file:
    convert_file.write(json.dumps(dict_vocab, ensure_ascii=False))

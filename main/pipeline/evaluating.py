from word_regex import process_regex
from sentence_segmentation import sentence_segmentation
from text_normalize import normalize
import glob, os
import pathlib

PATH = r"C:\users\ad\Desktop\Linh tinh\data_test\test\neg"
for i, file in enumerate(pathlib.Path(PATH).glob('*.txt')):
    if 1 <= i <= 240:
        with open(file, "r", encoding="utf8") as f:
            sentences = f.read()
            sentences = sentences.replace("_", " ")
            # print(sentences)

            sentences_arr: list = sentence_segmentation(sentences)
            print("\n".join(sentences_arr))
            print()
            for sentence in sentences_arr:
                tokens = process_regex(sentence)
                tokens_copy = tokens
                tokens = normalize(tokens)
                new_sent = ""
                for token_copy, token in zip(tokens_copy, tokens):
                    if token_copy != token:
                        new_sent += " " + token + "$"
                    else:
                        new_sent += " " + token
                print(" ".join(new_sent.split()))
    else:
        continue

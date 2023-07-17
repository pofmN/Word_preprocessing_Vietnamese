import re
import json

def __load_file(file=r"../main/pipeline/text_normalize/dictionary/dict_acronym.json") -> dict:
    f = open(file, encoding="utf8")
    return json.load(f)


def convert_teencode(text):
    vocabulary = __load_file()
    text = text.split("\n")
    for i in range(len(text)):
        words = text[i].split()
        for j in range(len(words)):
            word = words[j].lower()
            if word in vocabulary:
                words[j] = vocabulary[word]
        text[i] = " ".join(words)
    text = "\n".join(text)
    return text
def sent_seg(text):
    sent_reg = r'(?<!\w.\s\w.)(?<![A-Z][a-z]\.)(?<=\n|\.|\?|\!)\s'
    sents = re.split(sent_reg, text)
    return sents

if __name__ == '__main__':
    text ="""
Word2vec là một mô hình đơn giản và nổi tiếng giúp 
tạo ra các biểu diễn embedding của từ trong một không gian có số chiều thấp hơn nhiều lần so với số từ trong từ điển
Ý tưởng của word2vec đã được sử dụng trong nhiều bài toán với dữ liệu khác xa với dữ liệu ngôn ngữ! Trong cuốn sách này, ý tưởng của word2vec sẽ được trình bày và một ví dụ minh họa ứng dụng word2vec để tạo một mô hình product2vec giúp tạo ra các embedding khác nhau cho thực phẩm và đồ gia dụng. Thanh niên hiện nay chiều cao trung bình = 1.75 m. Rất nhiều người đã dùng thuốc tăng chiều cao. PGS. Huỳnh Công Pháp là người lớn nhất. Tôi đang sống tại TPHCM. Tôi biết.
TS. Nguyễn Hữu Nhật Minh sống tại Hòa Vang, Lộc Bổn, T.T.Huế.  TPHCM tôi mượn acc chơi game. uBnD xã lộc bổn nói rằng a iu e. T.P HCM đã nói ko vs tệ nạn xh.  gần nhà tôi gần TPHCM. Tôi hay qua chơi."""

    text = convert_teencode(text)
    sent_seg(text)
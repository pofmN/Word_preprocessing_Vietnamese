# 📦 Phân đoạn câu
> *File này mô tả về kĩ thuật phân đoạn câu trong tiếng Việt.*
* Bạn có thể xem code [tại đây](https://github.com/ketdoannguyen/AI_EmbeddingVietnameseNLP/blob/master/main/pipeline/sentence_segmentation/sent_segment.py) \
 [![Project](https://img.shields.io/badge/Languages-Vietnamese-brightgreen)](https://github.com/ketdoannguyen/AI_EmbeddingVietnameseNLP)

### Tại sao cần phân đoạn câu?
Phân đoạn câu là một trong những phần quan trọng nhất của NLP nói chung và tiếng Việt nói riêng. Trong đó, văn bản được phân tách thành các câu dựa trên các câu. Tiếng Việt sử dụng các dấu câu để phân đoạn các câu (dấu chấm ".", dấu chấm cảm "!", dấu chấm hỏi "?")
cùng với đó là sự phân biệt giữa chữ viết hoa và chữ viết thường cũng góp phần hỗ trợ cho việc phân đoạn câu.
### 💭Thuật toán:
* Để xử lý tác vụ phân đoạn này, chúng tôi xử lý các trường hợp tách câu theo dấu câu đã nói ở trên. Tuy nhiên, trong tiếng Việt có các trường hợp đặc biệt xử dụng dấu chấm "." để phục vụ viết tắt(ví dụ như Tiến sĩ Nguyễn Hữu Nhật Minh thường được viết TS. Nguyễn Hữu Nhật Minh, hoặc Thừa Thiên Huế thường được viết T.T.Huế), chính vì vậy cũng cần phải xử lý những trường hợp này vì chúng gây ảnh hưởng đáng kể đến tác vụ phân đoạn câu.
* Đầu tiên, chúng tôi tôi có từ điển chứa các từ viết tắt và các dạng viết đầy đủ của chúng. Để xử lý các trường hợp viết tắt đó, cần duyệt các từ trong câu văn bản đầu vào để đối chiếu với các từ trong từ điển viết tắt, nếu có trong từ điển, từ viết tắt sẽ được chuyển về dạng đầy đủ của nó.
 ```python
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
   ```
* Tiếp đó, viết biểu thức chính quy xác định các quy tắc kết thúc câu. Thêm vào đó, biểu thức này cũng đảm bảo rằng câu sẽ không bị tách sai bởi dấu chấm của các từ viết tắt(ví dụ : TS. Nguyễn Hữu Nhật Minh sẽ không bị tách ra theo dấu chấm).
```python
def sent_seg(text):


    sent_reg = r'(?<!\w.\s\w.)(?<![A-Z][a-z]\.)(?<=\n|\.|\?|\!)\s'
    sents = re.split(sent_reg, text)
    return sents
   ```
### 🌟Độ chính xác:
Chúng tôi đã thử qua các mô hình xử lý tiếng Việt khác. Hầu hết các mô hình này bỏ qua các trường hợp đặc biệt trong tác vụ phân đoạn câu. Điều này gây ảnh hưởng đến các tác vụ khác của mô hình. Mô hình của chúng tôi không chỉ xử lý được các trường hợp cơ bản mà còn xử lý được các trường hợp đặc biệt mà các mô hình khác không làm được. Chính vì vậy, độ chính xác của mô hình này cũng cao hơn đáng kể so với các mô hình xử lý tiếng Việt hiện có.
### Kết luận:
* Mô hình của chúng tôi đã khắc phục được đáng kể các trường hợp phân đoạn câu bị sai so với các mô hình khác.
* Độ chính xác được cải thiện hơn so với các mô hình đi trước.
### Hướng phát triển:
Chúng tôi sẽ tiếp tục nghiên cứu và phát triển mô hình với mục tiêu nâng cao độ chính xác của tác vụ lên mức cao nhất có thể.
### ✍️ Người soạn : 
#### Rondeptraicute6mui

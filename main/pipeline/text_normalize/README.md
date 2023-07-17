# Module Text Normalize

>Chuẩn hóa từ ngữ là quá trình điều chỉnh, sắp xếp và đồng nhất các từ và cụm từ trong ngôn ngữ để tạo ra một hệ thống chuẩn mực và thông minh. Trong tiếng Việt, việc chuẩn hóa từ ngữ là một hoạt động quan trọng nhằm duy trì sự rõ ràng, đồng nhất và thuận tiện trong xử lý.

>Mục tiêu của chuẩn hóa từ ngữ là tạo ra một tập hợp các quy tắc và tiêu chuẩn cho việc sử dụng từ ngữ. Điều này giúp ta xử lý Tiếng Việt và sử dụng ngôn ngữ này một cách dễ dàng và hiệu quả hơn.

### Mục lục  

[1. Acronym](#1-acronym-)  

[2. Convert text to number](#2-convert-text-to-number)  

[3. Normalize number](#3-normalize-number)  

[4.Normalize unikey](#4-normalize-unikey)  

[5. Tone marks](#5-tone-marks-)  


## 1. Acronym 🌻

Chuẩn hóa các từ viết tắt và teencode thông dụng, `ex: ko -> không`

- Sử dụng bộ [từ điển](https://github.com/ketdoannguyen/AI_EmbeddingVietnameseNLP/blob/master/main/pipeline/text_normalize/dictionary/dict_acronym.json) khoảng 300 từ viết tắt thông dụng
- `list_special_cases` : từ điển danh sách các trường hợp đặc biệt (đơn vị, tiền,….)
    
    ```python
    list_special_cases = {
          "m": "mét",
          "g": "gam",
          "mg": "mi-li-gam",
          "k": "nghìn",
          "đ": "đồng",
          "tr": "triệu",
          "l": "lít",
          "s": "giây",
          "v": "vôn",
          "j": "jun",
          "kg": "ki-lô-gam",
          "ml": "mi-li-lít",
          "ha": "héc-ta",
          "phân": "xăng-ti-mét",
          "cm": "xăng-ti-mét",
          "ft": "feet",
          "in": "inch",
      }
    
    ```
    
- Explain
    
    ```python
    def process_acronym(pre_token:str,token: str):
      """
      Hàm nhận vào một từ và chuyển từ đó thành từ không viết tắt
      :param token: một từ trong câu
      :return: trả về từ đã chuyển từ viết tắt thành không viết tắt
      """
      patten_number = "[-+]?(?:\\d*\\.*\\d+)" #word_regex số
      word_lower = token.lower()
      dict_acronym = _load_file()
      if re.search(patten_number,pre_token) and word_lower in list_special_cases.keys():
          token = list_special_cases[word_lower]
      elif word_lower in dict_acronym:
          token = dict_acronym[word_lower]
      return token
    
    ```
    
    - Hàm `process_acronym` có tham số đầu vào là token hiện tại (`token`) và token trước nó (`pre_token`)
    - Nếu `pre_token` là số và `token` có ở trong `list_special_cases` thì sẽ trả về giá trị trong từ điển trường hợp đặc biệt
    - Sau đó nếu `token` có trong từ điển thì trả về giá trị trong từ điển

## 2. Convert text to number

Chuẩn hóa các từ thành số, `ex: "mười ba" -> 13`

## 3. Normalize number

Chuẩn hóa giá trị trong các đơn vị đo lường, `ex: 1m2 -> 1,2m`

## 4. Normalize unikey

Chuẩn hóa từ bị lỗi unikey `ex: tranhs nhieemj -> tránh nhiệm`

## 5. Tone marks 🤠

Chuẩn hóa vị trí dấu trong tiếng Việt `ex: qúa -> quá`

### Nguyên âm trong tiếng Việt

- Xét về mặt chữ viết thì tiếng Việt có tổng cộng 11 nguyên âm đơn, 32 nguyên âm đôi và 13 nguyên âm ba. Các cụ thể:
    - 12 nguyên âm đơn: a, ă, â, e, ê, i, y, o, ô, ơ, u, ư. Bởi vì chữ i và y có phát âm giống nhau nên sẽ giảm đi 1 nguyên âm so với chữ viết.
    - 33 nguyên âm đôi trong tiếng Việt: ai, ao, au, ay, âu, ây, êu, eo, ia, iê, yê, iu, oa, oe, oă, oa, oi, oe, oo, ôô, ơi, ua, uâ, uă, ue, ua, ui, ưi, uo, ươ, ưu, uơ, uy.
    - 13 nguyên âm ba: oai, oao, uao, oeo, iêu/yêu, uôi, ươu, uyu, uyê, ươi, oay, uây, ươi.

### Dấu thanh trong tiếng Việt

Tiếng Việt có 6 thanh điệu: bằng(-), sắc('), huyền(`), hỏi(?), ngã(~), nặng(.).

### Quy tắc đặt dấu

- Những quy tắc đặt dấu trong tiếng Việt:
    - Quy tắc 1: Với những âm tiết chỉ có một chữ nguyên âm thì dấu thanh được đặc trên chữ nguyên âm đó. Ví dụ: á, à, ạ,..
    - Quy tắc 2: Với những âm tiết mà chỉ cần chứa một nguên âm mang dấu phụ(ê, ư, ơ,..) thì dấu được đặc trên nguyên âm mang dấu phụ đó.
    - Quy tắc 3: Với những âm tiết có hai con chữ nguyên âm và kết thúc bằng một con chữ phụ âm hoặc tổ hợp con chữ phụ âm, thì dấu thanh được đặt trên nguyên âm chót. Ví dụ: choàng, cùng, thoát,..
    - Quy tắc 4: Với những âm tiết kết thúc bằng oa, oe, uy thì dấu được đặt trên nguyên âm chót. Ví dụ hoè, hoạ,..
    - Quy tắc 5: Với những âm tiết kết thúc khác oa, oe, uy thì dấu được đặt trên nguyên âm áp chót. Ví dụ: đào, giúi, bài, bảy,..

### Những trường hợp đặc biệt

Ngoài ra, những trường hợp đặc biệt của cặp nguyên âm ua, ia, để xác định vị trí đặt dấu của cặp nguyên âm đôi này còn phải dựa trên sự xuất hiện của phụ âm q và g. Nếu phía trước của nguyên âm đôi ua có sự xuất hiện của q thì dấu được đặt trên nguyên âm a, tương tự với nguyên âm đôi ia, khi có sự xuất hiện của phụ âm g thì dấu được trên nguyên âm a.

- Ví dụ:
    - "qùa": "quà",
    - "ủôi": "uổi",
    - "uýê": "uyế",
    - "gìa": "già",
    - "kìa": "kìa"
    
    > Code example:
    > 
    
    ```
        text = "Nhìn kià, ông ấy tuy tủôi đã cao những không thấy bất cứ sự gìa đi nào trên cơ thể ông ấy"
        result = process_tone_mark(text)
        print(result)
    
    ```
    
    > Kết quả:
    > 
    
    ```
        "Nhìn kìa, anh ấy tuy tuổi đã cao nhưng không thấy bất cứ sự già đi nào trên cơ thể anh ấy"
    
    ```
    

 Reference from [Under the sea toolkit](https://underthesea.readthedocs.io/en/latest/readme.html)

## 6. Implementation

`Code mẫu bày cách import,chạy,.....`

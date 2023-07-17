from .word_segment import WordSegment
w = WordSegment()
# input = """
# Tờ mờ sáng , nhiều người còn ngủ say thì Trần Nguyễn Văn Thái, một du học sinh tại tỉnh Gyeonggi mới trở về ký túc xá từ chỗ làm thêm .
#
# Cậu nhận "théc-be" ( phân loại , bốc xếp hàng hóa đặt qua mạng ) cho một "đầu nậu" người Hàn Quốc thiếu nhân công chính quy . Thái tranh thủ thời gian hết mức có thể để kiếm chút ít trang trải học phí , sinh hoạt phí ; dư thì gửi về quê trả khoản nợ gia đình đã mượn trước khi cậu sang Hàn Quốc du học .
#
# Du học sinh "al-ba" ( làm bán thời gian ) như Trần Văn Thái ở các tỉnh vùng ven thủ đô Seoul là không ít . Chấp nhận làm "chui" , vượt quá quy định 20 tiếng một tuần đối với du học sinh là để có thể tự lo chuyện học tập và tồn tại được ở Hàn Quốc . Đây cũng là sự biến tướng của loại hình du học dưới dạng vừa học vừa làm . Nhiều trường đại học tại Hàn Quốc cũng " làm lơ " trong việc điểm danh , cho du học sinh được đi làm thêm kiểu này vì nhiều lẽ .
# """
# strs = w.segment_tokenize_string(input, True)
# # strs1 = w.segment_tokenize_string(input, False)
# print(strs)
# # print(strs1)
# output: str = w.word_segment(input, "Trong tiết sinh_học của thầy Tiến")
# print(output)


def word_segmentation(sentences: list) -> str:
    for i,sentence in enumerate(sentences):
        sentences[i] = w.word_segment(sentence)

    return ' '.join(sentences)

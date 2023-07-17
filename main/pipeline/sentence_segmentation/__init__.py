from .sent_segment import sent_seg


def sentence_segmentation(sentences: str = "") -> list:
    return sent_seg(sentences)

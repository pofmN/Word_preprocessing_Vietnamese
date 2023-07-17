from ..sentence_segmentation import sentence_segmentation
from ..word_regex import process_regex
from .process_tone_marks import process_tone_mark

def _sent_segment_and_regex(sentences):
    sentences = sentence_segmentation(sentences)
    sentences = list(dict.fromkeys(sentences))
    sentences = [' '.join(process_regex(sentence)) for sentence in sentences]
    return sentences

def process_tone_mark_api(sentences):
    sentences = [process_tone_mark(token) for token in sentences.split()]
    return " ".join(sentences)
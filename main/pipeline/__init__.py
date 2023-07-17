from .word_regex import process_regex
from .sentence_segmentation import sentence_segmentation
from .text_normalize import normalize
from .word_segmentation import word_segmentation
from tqdm import tqdm

def process(sentences: str):
    sentences = sentence_segmentation(sentences)
    sentences = list(dict.fromkeys(sentences))
    for i, sentence in tqdm(enumerate(sentences)):
        if len(sentence) > 0:
            sentence = process_regex(sentence)
            sentence = normalize(sentence)
            sentences[i] = ' '.join(sentence)
    return word_segmentation(sentences)



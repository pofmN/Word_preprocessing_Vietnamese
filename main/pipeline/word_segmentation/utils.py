from .fwobject import FWObject

class Utils:
    def __init__(self):
        """
        Read file word correction -> Normalizer using change token is not correct to correct
        """
        self._NORMALIZER = {"òa": "oà", "óa": "oá", "ỏa": "oả", "õa": "oã", "ọa": "oạ", "òe": "oè", "óe": "oé",
                            "ỏe": "oẻ", "õe": "oẽ", "ọe": "oẹ", "ùy": "uỳ", "úy": "uý", "ủy": "uỷ", "ũy": "uỹ",
                            "ụy": "uỵ", "Ủy": "Uỷ"}

    def get_condition(self, str_condition: str) -> FWObject:
        """
        Get rule in RDRTree and get condition from rule
        """
        condition = FWObject(False)
        for rule in str_condition.split(" and "):
            rule: str = rule.strip()
            key: str = rule[rule.index(".") + 1: rule.index(" ")]
            value: str = self.get_concrete_value(rule)

            if key == "prevWord2":
                condition.context[4] = value
            elif key == "prevTag2":
                condition.context[5] = value
            elif key == "prevWord1":
                condition.context[2] = value
            elif key == "prevTag1":
                condition.context[3] = value
            elif key == "word":
                condition.context[1] = value
            elif key == "tag":
                condition.context[0] = value
            elif key == "nextWord1":
                condition.context[6] = value
            elif key == "nextTag1":
                condition.context[7] = value
            elif key == "nextWord2":
                condition.context[8] = value
            elif key == "nextTag2":
                condition.context[9] = value

        return condition


    def get_object(self, word_tags: list, size: int, index: int) -> FWObject:
        ob = FWObject(True)
        if index > 1:
            ob.context[4] = word_tags[index - 2].word
            ob.context[5] = word_tags[index - 2].tag

        if index > 0:
            ob.context[2] = word_tags[index - 1].word
            ob.context[3] = word_tags[index - 1].tag

        current_word: str = word_tags[index].word
        current_tag: str = word_tags[index].tag

        ob.context[1] = current_word
        ob.context[0] = current_tag

        if index < size - 1:
            ob.context[6] = word_tags[index + 1].word
            ob.context[7] = word_tags[index + 1].tag

        if index < size - 2:
            ob.context[8] = word_tags[index + 2].word
            ob.context[9] = word_tags[index + 2].tag

        return ob

    def get_concrete_value(self, strs: str) -> str:

        if "\"\"" in strs:
            if "Word" in strs:
                return "<W>"
            else:
                return "<T>"
        conclusion = strs[strs.index("\"") + 1: len(strs) - 1]
        return conclusion

    @property
    def NORMALIZER(self) -> dict:
        return self._NORMALIZER

    @property
    def NORMALIZER_KEYS(self):
        return self._NORMALIZER.keys()

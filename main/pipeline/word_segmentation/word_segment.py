from .vocabulary import Vocabulary
from .word_tag import WordTag


class WordSegment:
    def __init__(self):
        self._vocab = Vocabulary()
        # self.__model_path = model_path
        # self._root: Node = None
        # self.__model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        # try:
        #     if model_path is None:
        #         self.construct_tree_from_rules_file("../main/pipeline/word_segmentation/Model.RDR")
        #     else:
        #         self.construct_tree_from_rules_file(model_path)
        # except Exception as e:
        #     print(f"Message Error: {e}")

    # def construct_tree_from_rules_file(self, rule_file_path: str) -> None:
    #     self._root = Node(FWObject(False), "NN", None, None, None, 0)
    #
    #     current_node: Node = self._root
    #     current_depth: int = 0
    #
    #     with open(rule_file_path, 'r', encoding="utf8") as rule_file:
    #         for index_file_rule, line in enumerate(rule_file):
    #             depth = 0
    #             for i in range(0, 7):
    #                 if line[i] == '\t':
    #                     depth += 1
    #                 else:
    #                     break
    #             if index_file_rule == 0:
    #                 continue
    #
    #             line = line.strip()
    #             if len(line) == 0:
    #                 continue
    #
    #             if "cc:" in line:
    #                 continue
    #             condition: str = utils.get_condition(line.split(" : ")[0].strip())
    #             conclusion: str = utils.get_concrete_value(line.split(" : ")[1].strip())
    #
    #             node: Node = Node(condition, conclusion, None, None, None, depth)
    #
    #             if depth > current_depth:
    #                 current_node.set_except_node(node)
    #             elif depth == current_depth:
    #                 current_node.set_if_not_node(node)
    #             else:
    #                 while current_node.get_depth() != depth:
    #                     current_node = current_node.get_father_node()
    #                 current_node.set_if_not_node(node)
    #             node.set_father_node(current_node)
    #
    #             current_node = node
    #             current_depth = depth
    #
    # def find_fired_node(self, ob: FWObject) -> Node:
    #     current_node: Node = self._root
    #     fired_node: Node = None
    #     while True:
    #         if current_node.satisfy(ob):
    #             fired_node = current_node
    #             if current_node.get_except_node() is None:
    #                 break
    #             else:
    #                 current_node = current_node.get_except_node()
    #         else:
    #             if current_node.get_if_not_node() is None:
    #                 break
    #             else:
    #                 current_node = current_node.get_if_not_node()
    #
    #     return fired_node

    # def all_is_letter(self, strs: str) -> bool:
    #     for char in strs:
    #         if char.isalpha() == False:
    #             return False
    #     return True
    #
    # def all_is_upper(self, strs: str) -> bool:
    #
    #     for char in strs:
    #         if char.isupper() == False:
    #             return False
    #     return True
    def __is_first_upper(self, words: str):
        # Nguyễn Trần Tiến -> True
        words: list = words.strip().split()
        for word in words:
            if not word[0].isupper():
                return False
        return True

    def maximum_matching_left(self, sentence: str) -> list:
        word_tags = []
        conditions = self._vocab.VN_PRONOUNS
        tokens: list = sentence.split()
        lower_tokens: list = sentence.lower().split()
        sen_length = len(tokens)
        i = 0
        while i < sen_length:
            token: str = tokens[i]
            if token.isalpha():
                # ông Nguyễn Văn A => ông = B
                if token[0].islower() and (i + 1) < sen_length and tokens[i + 1][0].isupper():
                    word_tags.append(WordTag(token, "B"))
                    i += 1
                    continue
                is_single_syllable: bool = True
                for j in range(min(i + 4, sen_length), i + 1, -1):
                    word: str = ' '.join(lower_tokens[i:j])
                    if word in self._vocab.VN_DICT \
                            or word in self._vocab.VN_LOCATIONS \
                            or word in self._vocab.COUNTRY_L_NAME \
                            and not self.__is_first_upper(word):

                        if i > 0 and word == ' '.join(lower_tokens[i - 2:j - 2]):
                            for k in range(i, j - 1):
                                word_tags.append(WordTag(tokens[k], "B"))
                            lower_tokens.insert(j - 1, '-')
                            tokens.insert(j - 1, '-')
                            sen_length += 1
                        else:
                            word_tags.append(WordTag(token, "B"))
                            for k in range(i + 1, j):
                                word_tags.append(WordTag(tokens[k], "I"))
                        i = j - 1
                        is_single_syllable = False
                        break
                if is_single_syllable:
                    # if token.lower() in self.__vocab.VN_FIRST_SENT_WORDS:
                    #     word_tags.append(WordTag(token, "B"))
                    #     i += 1
                    #     continue
                    if token[0].isupper() \
                            and len(word_tags) > 0 \
                            and word_tags[len(word_tags) - 1].word.lower() in conditions \
                            and word_tags[len(word_tags) - 1].tag == "B":
                        # if len(word_tags) > 1 \
                        #         and word_tags[len(word_tags) - 2].word.lower() in conditions\
                        #         and word_tags[len(word_tags) - 1].word.lower() in conditions:
                        #     word_tags.append(WordTag(token, "I"))
                        # else:
                        word_tags.append(WordTag(token, "B"))
                        i = i + 1
                        continue
                    if i > 0 \
                            and token[0].isupper() \
                            and tokens[i - 1][0].isupper():
                        word_tags.append(WordTag(token, "I"))
                        i += 1
                        continue
                    word_tags.append(WordTag(token, "B"))
            else:
                word_tags.append(WordTag(token, "B"))
            i += 1
        return word_tags

    def maximum_matching_right(self, sentence: str) -> list:
        conditions = self._vocab.VN_PRONOUNS
        word_tags: list = []
        tokens: list = sentence.split()
        lower_tokens: list = sentence.lower().split()
        length: int = len(lower_tokens)
        while length > 0:
            token: str = tokens[length - 1]
            if token.isalpha():
                # học sinh học rất tốt
                is_single_syllable = True
                j = length
                for i in range(max(length - 4, 0), j - 1):
                    word = ' '.join(lower_tokens[i:j])
                    if word in self._vocab.VN_DICT \
                            or word in self._vocab.VN_LOCATIONS \
                            or word in self._vocab.COUNTRY_L_NAME \
                            and not self.__is_first_upper(word):
                        if j + 2 < len(lower_tokens) \
                                and word == ' '.join(lower_tokens[i + 2:j + 2]):
                            for k in range(i + 1, j):
                                word_tags.append(WordTag(tokens[k], "B"))

                            lower_tokens.insert(j, "-")
                            tokens.insert(j, "-")
                            i += 1
                        else:
                            for k in range(j - 1, i, -1):
                                word_tags.append(WordTag(tokens[k], "I"))
                            word_tags.append(WordTag(tokens[i], "B"))

                        length = i + 1
                        is_single_syllable = False
                        break

                if is_single_syllable:
                    if length - 1 > 0 \
                            and token[0].isupper() \
                            and tokens[length - 2][0].isupper() \
                            and tokens[length - 2].lower() not in conditions \
                            and token.lower() not in conditions:
                        word_tags.append(WordTag(token, "I"))
                        length -= 1
                        continue
                    word_tags.append(WordTag(token, "B"))
            else:
                word_tags.append(WordTag(token, "B"))

            length -= 1

        word_tags = list(reversed(word_tags))
        return word_tags

    # def maximum_matching_right(self, sentence: str) -> list:
    #     if self.__vocab_path is None:
    #         vocab = Vocabulary()
    #     else:
    #         vocab = Vocabulary(self.__vocab_path)
    #
    #     for word_regex in utils.NORMALIZER_KEYS:
    #         if word_regex in sentence:
    #             sentence = sentence.replace(word_regex, utils.NORMALIZER[word_regex])
    #
    #     word_tags: list = []
    #     tokens: list = sentence.split()
    #     lower_tokens: list = sentence.lower().split()
    #     length: int = len(lower_tokens)
    #     while length > 0:
    #         token: str = tokens[length - 1]
    #         if token.isalpha():
    #             is_single_syllabel: bool = True
    #             j: int = length
    #             for i in range(max(length - 4, 0), j):
    #                 word: str = ' '.join(lower_tokens[i:j])
    #                 if word in vocab.VN_DICT \
    #                         or word in vocab.VN_LOCATIONS \
    #                         or word in vocab.COUNTRY_L_NAME:
    #                     if j + 2 <= len(lower_tokens) \
    #                             and word == ' '.join(lower_tokens[i + 2:j + 2]):
    #                         for k in range(i + 1, j):
    #                             word_tags.append(WordTag(tokens[k], "B"))
    #                         lower_tokens.insert(j, "-")
    #                         tokens.insert(j, "-")
    #                         i += 1
    #                     else:
    #                         for k in range(j - 1, i, -1):
    #                             word_tags.append(WordTag(tokens[k], "I"))
    #                         word_tags.append(WordTag(tokens[i], "B"))
    #                     length = i + 1
    #                     is_single_syllabel = False
    #                     break
    #             if is_single_syllabel:
    #                 lower_cased_token: str = lower_tokens[length - 1]
    #                 if lower_cased_token in vocab.VN_FIRST_SENT_WORDS \
    #                         or token[0].islower() \
    #                         or token.isupper() \
    #                         or lower_cased_token in vocab.COUNTRY_S_NAME \
    #                         or lower_cased_token in vocab.WORLD_COMPANY:
    #                     word_tags.append(WordTag(token, "B"))
    #                     length -= 1
    #                     continue
    #
    #             i_lower = length - 1
    #             for i_lower in range(length - 2, max(length - 8, 0), -1):
    #                 n_token: str = tokens[i_lower]
    #                 if n_token[0].islower() \
    #                         or not n_token.isalpha() \
    #                         or n_token == "LBKT" \
    #                         or n_token == "RBKT":
    #                     break
    #             if i_lower < length - 1:
    #                 for k in range(i_lower + 1, length):
    #                     if lower_tokens[k] in vocab.VN_FAMILY_NAMES:
    #                         for q in range(length - 1, k, -1):
    #                             word_tags.append(WordTag(tokens[q], "I"))
    #                         word_tags.append(WordTag(tokens[k], "B"))
    #                         break
    #                     else:
    #                         word_tags.append(WordTag(tokens[k], "B"))
    #                 length = i_lower + 2
    #             else:
    #                 word_tags.append(WordTag(token, "B"))
    #         else:
    #             word_tags.append(WordTag(token, "B"))
    #         length -= 1
    #     return word_tags
    def segment_tokenize_string(self, strs: str, left: bool) -> str:
        """
        Mục tiêu hàm sẽ nhận vào một chuỗi đã được xử lý qua Regex sau đó sẽ tiến hành
        Maximum Matching và đưa vào cây RDR -> Word Segment
        :param strs: Chuỗi cần Word Segment
        :param left: Là chiều duyệt của Maximum Matching
        :return: Chuỗi đã được Word Segment bao gồm đã kiểm tra RDR
        """
        line: str = strs.strip()
        str_token: list = []
        if len(line) == 0:
            return "\n"
        if left:
            word_tags: list = self.maximum_matching_left(line)
        else:
            word_tags: list = self.maximum_matching_right(line)
        for word_tag in word_tags:
            # ob: FWObject = utils.get_object(word_tags=word_tags, size=size, index=i)
            # fired_node: Node = self.find_fired_node(ob)
            #
            # if fired_node.get_depth() > 0:
            #     if fired_node.get_conclusion() == "B":
            #         str_token.append(" " + word_tags[i].form)
            #     else:
            #         str_token.append("_" + word_tags[i].form)
            # else:
            if word_tag.tag == "B":
                str_token.append(" " + word_tag.form)
            else:
                str_token.append("_" + word_tag.form)

        return ''.join(str_token).strip()

    def word_segment(self, strs: str):
        """
        Mục tiêu tìm ra câu tách đúng với ngữ cảnh nhất
        :param strs: là raw string chưa chuẩn hóa
        :param before_strs: là chuỗi trước đó
        :return: trả về word_segment phù hợp với ngữ cảnh trước đó
        """
        # Xíu nữa mình sẽ thêm một string đã qua Regex để so sánh chừ dùng tạm
        maximum_left: str = self.segment_tokenize_string(strs=strs, left=True)
        maximum_right: str = self.segment_tokenize_string(strs=strs, left=False)

        # if before_strs is None:
        #     return maximum_left
        # else:
        if maximum_right == maximum_left:
            return maximum_left
        else:
            list_left = maximum_left.split()
            list_right = maximum_right.split()
            for i in range(len(list_left)):
                if list_left[i] != list_right[i]:
                    maximum_left_new = " ".join(list_left[max(0,i-5):min(i + 6 ,len(list_left)-1)])
                    maximum_right_new = " ".join(list_right[max(0, i - 5):min(i + 6, len(list_right) - 1)])
                    break
            print("L : ", maximum_left_new)
            print("R : ", maximum_right_new)
            f = open("./data/dataset_train_crf.txt", "a", encoding='utf-8')
            try:
                choose = int(input("1-L or 2-R : "))
                if choose == 1:
                    f.write("\n"+maximum_left)
                elif choose == 2:
                    f.write("\n"+maximum_right)
                elif choose == 3:
                    f.write("\n"+maximum_left+"\n"+maximum_right)
                f.close()
            except:
                print("Slow")
            return maximum_left
            # return self.cosine_similarity([before_strs, maximum_left, maximum_right])

    # def cosine_similarity(self, sentences: list) -> str:
    #     """
    #     param: sentences: một mảng gồm câu trước và 2 câu được Maximum Matching 2 chiều
    #     return: Trả về câu có cosine similarity với câu trước đó cao nhất
    #     """
    #     # Tính embedding của từng câu
    #     embeddings = self.__model.encode(sentences)
    #
    #     arr = np.array(embeddings)
    #     emb_a = arr[0]
    #     emb_b1 = arr[1]
    #     emb_b2 = arr[2]
    #
    #     # Tính cosine câu trước đó và câu maximum matching
    #     cos1 = np.dot(emb_a, emb_b1) / (np.linalg.norm(emb_a) * np.linalg.norm(emb_b1))
    #     cos2 = np.dot(emb_a, emb_b2) / (np.linalg.norm(emb_a) * np.linalg.norm(emb_b2))
    #
    #     return sentences[1] if cos1 > cos2 else sentences[2]

class WordTag:
    def __init__(self, iword: str, itag: str):
        self._word = iword.lower()
        self._form = iword
        self._tag = itag

    @property
    def word(self) -> str:
        return self._word

    @property
    def form(self) -> str:
        return self._form

    @property
    def tag(self) -> str:
        return self._tag

    @word.setter
    def word(self, value: str) -> None:
        self._word = value

    @form.setter
    def form(self, value) -> None:
        self._form = value

    @tag.setter
    def tag(self, value) -> None:
        self._tag = value

    @property
    def show_tag(self):
        return f"Word: {self._word}, Tag: {self._tag}, Form: {self._form}"

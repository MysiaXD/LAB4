import re


class Letter:
    def __init__(self, char: str):
        # ініцліт
        self.char = char

    def __str__(self):
        return self.char


class Word:
    def __init__(self, letters: list[Letter]):
        # ініцслов
        self.letters = letters

    def __str__(self):
        return "".join(str(l) for l in self.letters)

    def to_lower_str(self) -> str:
        # нижнрегрядк
        return str(self).lower()


class Punctuation:
    def __init__(self, char: str):
        # ініцроздзнак
        self.char = char

    def __str__(self):
        return self.char


class Sentence:
    def __init__(self, elements: list):
        # ініцреч
        self.elements = elements

    def get_words(self) -> list[Word]:
        # отрвсіслов
        return [el for el in self.elements if isinstance(el, Word)]

    def __str__(self):
        return "".join(str(el) for el in self.elements)


class Text:
    def __init__(self, raw_text: str):
        # зампробтаб
        cleaned = re.sub(r'[\t ]+', ' ', raw_text).strip()

        if not cleaned:
            # помпусттекст
            raise ValueError("текст порожній")

        # ініцспреч
        self.sentences = self._parse(cleaned)

    def _parse(self, raw_text: str) -> list[Sentence]:
        # парсрядктекст
        raw_sentences = re.split(r'(?<=[.!?])\s*', raw_text)
        sentences = []

        for rs in raw_sentences:
            if not rs:
                continue
            elements = []

            # ТУТ ВИПРАВЛЕННЯ: тепер ми не ігноруємо пробіли (\W захоплює все, крім літер/цифр)
            # розбзнаксловпроб
            tokens = re.findall(r'\w+|\W', rs)

            for t in tokens:
                if re.match(r'\w+', t):
                    # додліт
                    letters = [Letter(c) for c in t]
                    elements.append(Word(letters))
                else:
                    # ствроздпроб
                    elements.append(Punctuation(t))

            sentences.append(Sentence(elements))
        return sentences

    def find_unique_word(self) -> str | None:
        # пошукунікслов
        if len(self.sentences) < 2:
            # поммалреч
            raise ValueError("треба >1 реч")

        first_sentence_words = self.sentences[0].get_words()
        other_words_str = set()

        for s in self.sentences[1:]:
            for w in s.get_words():
                # додслмнж
                other_words_str.add(w.to_lower_str())

        for w in first_sentence_words:
            if w.to_lower_str() not in other_words_str:
                # знайдунік
                return str(w)

        return None


if __name__ == "__main__":
    # вхтекстпроб
    input_text = "Якесь\tперше  речення з  унікальним словом! А це вже друге речення. І третє речення тут."

    try:
        # ствобтекст
        text_obj = Text(input_text)

        # викпош
        result = text_obj.find_unique_word()

        if result:
            # друкрез
            print(f"знайдене слово: {result}")
        else:
            # друквідс
            print("такого слова немає")

    except ValueError as e:
        # обрпом
        print(f"помилка даних: {e}")
    except Exception as e:
        # обрневідпом
        print(f"непередбачувана помилка: {e}")
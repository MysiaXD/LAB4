from unittest import TestCase
from main import Text, Sentence, Word, Letter, Punctuation


class TestTextArchitecture(TestCase):

    def test_parsing_logic(self):
        # ініцтекст
        t = Text("Привіт! Як справи?")

        # перкількреч
        self.assertEqual(len(t.sentences), 2)

        # первідтвтекст
        self.assertEqual(str(t.sentences[0]), "Привіт!")
        self.assertEqual(str(t.sentences[1]), "Як справи?")

    def test_find_unique_word_success(self):
        # текстнормдан
        text = "Якесь унікальне слово. А тут немає. І тут немає."

        # ініцкл
        t = Text(text)

        # перрез
        self.assertEqual(t.find_unique_word(), "Якесь")

    def test_no_unique_word(self):
        # текстбезунік
        text = "Слово один. Слово два. Один два."

        # ініцкл
        t = Text(text)

        # первідсрез
        self.assertIsNone(t.find_unique_word())

    def test_empty_text_error(self):
        # порожтекст
        text = "   \t  "

        # первикпом
        with self.assertRaises(ValueError):
            Text(text)

    def test_one_sentence_error(self):
        # однереч
        text = "Тільки одне речення."

        # ініцкл
        t = Text(text)

        # первикпом
        with self.assertRaises(ValueError):
            t.find_unique_word()

    def test_word_to_lower(self):
        # ствслов
        w = Word([Letter('Т'), Letter('Е'), Letter('С'), Letter('Т')])

        # пернижрег
        self.assertEqual(w.to_lower_str(), "тест")
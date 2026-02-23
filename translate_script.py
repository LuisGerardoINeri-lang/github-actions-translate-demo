from translate import Translator

translator = Translator(to_lang="hi")

with open("file1.txt", "r") as file:
    english_text = file.read()

hindi_text = translator.translate(english_text)

with open("file2.txt", "w", encoding="utf-8") as file:
    file.write(hindi_text)

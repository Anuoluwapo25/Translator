from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']

input_text = input("Enter the text to translate: ")
source_language = "en"  # English

target_language_igbo = "ig"
translated_text_igbo = translate_text(input_text, target_language_igbo)
print("Igbo translation:", translated_text_igbo)

# Translate to Hausa
target_language_hausa = "ha"
translated_text_hausa = translate_text(input_text, target_language_hausa)
print("Hausa translation:", translated_text_hausa)

#text_to_translate = "today is good."
target_language = "yo"  # Yoruba
translated_text_yoruba = translate_text(input_text, target_language)
print("Yoruba translation:", translated_text_yoruba)

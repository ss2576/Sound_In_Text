""" Модуль для преобразования голоса в текст. Используется PyAudio==0.2.11, SpeechRecognition==3.8.1
    1. В SpeechRecognition используется класс Microphone для прослушивания речи с микрофона и распознования его в
       текст через метод recognize_google и запись результата в текстовый файл.
    2. В SpeechRecognition используется класс AudioFile для подхвата аудиофайла формата WAV и отправки его через
       метод recognize_google и запись результата в текстовый файл."""


import speech_recognition as sr


# путь к файлу в который записывается текст.
TEXT_FILE = 'text.txt'
# путь к файлу с голосом.
VOICE_FILE = 'voice2.wav'
# кодировка для отправки в Гугл.
VOICE_LANGUAGE = 'ru-RU'
# кодировка для записи в текстовый файл.
CODE = 'utf-8'
# первые 50 секунд ,которые нужно распознать из файла.
TIME_RECORD = 50


class SoundInText:
    def __init__(self):
        self.text_file = TEXT_FILE
        self.voice_file = VOICE_FILE
        self.voice_language = VOICE_LANGUAGE
        self.code = CODE
        self.time_record = TIME_RECORD
    
    @property
    def voice_to_text(self):
        """отправка голоса через микрофон в Гугл и получение текста"""
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print('Слушаю...')
            audio = r.listen(source)
        query = r.recognize_google(audio, language=self.voice_language)
        self.text_to_file(query)
    
    @property
    def record_to_text(self):
        """отправка звукового файла в Гугл и получение текста"""
        sample_audio = sr.AudioFile(self.voice_file)
        r = sr.Recognizer()
        with sample_audio as audio_file:
            audio = r.record(audio_file, duration=self.time_record)
        query = r.recognize_google(audio, language=self.voice_language)
        self.text_to_file(query)
    
    def text_to_file(self, query):
        """запись полученного текста из Гугл в текстовый файл"""
        with open(self.text_file, 'w', encoding=self.code) as file:
            file.write(query)
            print(query)


def main():
    try:
        record = SoundInText()
        # record.voice_to_text  # для обработки голоса через микрофон
        record.record_to_text  # для обработки звукового файла
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()
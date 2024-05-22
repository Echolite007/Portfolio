def loud(text):
    return text.upper()

def whisper(text):
    return text.lower()

def hello(func):
    print(text := func("Hello"))

hello(loud)
hello(whisper)
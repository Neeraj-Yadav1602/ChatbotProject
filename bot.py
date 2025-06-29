import time

#QUESTION:answer
now = time.ctime()
qna = {
    "hi": "hey",
    "how are you": "I am fine",
    "what is your name": "My name is Jarvis",
    "how old are you": "I am 20 years old",
    "what is the time now": now
}

while True:
    qs = input()
    if (qs == "quit"):
        break
    else:
        if qs in qna:
            print(qna[qs])
        else:
            print("I don't understand that question.")
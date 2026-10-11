# building an app that gives user a sentence to tpe and measures their speed and accuracy...

import random
import time
import pyttsx3
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[92].id)
letters = "abcdefghijklmnopqrust"
sentence = []
num_of_words = random.randint(1, 11)
for i in range(1, num_of_words):
    random_words = random.randint(2, 5)
    sentence.append(random_words)


final_sentence = []
for numbers in sentence:
    adding_words = ''.join(random.choices(letters, k = numbers))
    final_sentence.append(adding_words)

last_final_sentence = ' '.join(final_sentence)    
print(last_final_sentence)

engine.setProperty('rate', 120)
def daemon_ex():
    for final_senn in final_sentence:
         engine.say(final_senn)
         engine.runAndWait()

thread = threading.Thread(target=daemon_ex, daemon=True)
input()

thread.start()
start_time = time.time()
say = input("Start writing here: ")
end_time = time.time()
time_taken = end_time - start_time


for final_sen, your_written in zip(last_final_sentence, say):
    if your_written != final_sen:
        print(f"You wrote these wrong: {your_written} instead of {final_sen}")
    elif your_written == "":
        print('Bro, write something...')

print(f"You took:  {round(time_taken, 2)} seconds to write.")

 
'''жена попросила написать викторину для школы. дети рады. какая то Маруся из компьютера задаёт вопросы.
если не хочешь после каждого ответа нажимать enter "сделал специально, что бы Маруся лошадей не гнала",
 то закоментируй 92 - 94 и раскоментируй 78 - 80. что бы в любой момент можно было выйти из викторины
голосовой командой "хватит"'''


import os
from gtts import gTTS
import random
import playsound
import speech_recognition as sr
import winsound
import time


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("слушаю тебя:")
        delay_pause(r, source)
        audio = r.listen(source)
        print('услышала: ')

    try:
        our_speech = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: " + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        print(e)
    except TimeoutError:
        return 'ошибка'  

def delay_pause(r, source):
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source, duration=1)


def do_tris_command(message):
    message = message.lower()
   
    
    ls = [
        ("Средство передвижения, имеющее два колеса, но без мотора и без педалей, варианты ответов: велосипед, самокат, лыжи", "Самокат"),
        ("Колючий садовый ягодный кустарник, варианты ответов: кактус, крапива, крыжовник", "Крыжовник"),
        ("сколько будет 2 + 2 и умножить  на 2, варианты, 8, 6, 4", "6"),
        ("Небесное тело, расположенное ближе всего к Земле, варианты ответов: луна, солнце, меркурий", "Луна"),
        ("Спектакль, в котором действующие лица не разговаривают, а только поют, варианты ответов: пьесса, опера, самодеятельность", "Опера"),
        ("Круглая цирковая площадка для выступлений, варианты ответов: загон, арена, амфитеатр", "Арена"),
        ("Человек, стоящий спиной к зрителям, а лицом к музыкантам, варианты ответов: режисёр, дирижёр, дрессировщик ", "Дирижёр"),
        ("Самый маленький из существующих на Земле материков, варианты ответов: австралия, антарктида, африка", "Австралия"),
        ("Музыкальный ансамбль, состоящий из трёх исполнителей, варианты ответов: квартет, трио, дуэт", "Трио"),
        ("Автор сказок о Незнайке и его друзьях, варианты ответов: андерсен, пушкин, носов", "Носов"),
        ("назови столицу нашей страны, варианты ответов: санкт-петербург, москва, новгород", "москва"),
        ("Самый большой на Земном Шаре океан, варианты ответов: атлантический, индийский, тихий", "Тихий"),
        ("От какого дикого зверя берут происхождение собаки?, варианты ответов: медведь, волк, крокодил ", "волк"),
        ("Профессия человека, создающего новые машины и самолеты?, варианты ответов: конструктор, инструктор, плотник", "Конструктор"),
        ("Что делает человек всю жизнь, не останавливаясь?, варианты ответов: бегает, прыгает, дышит", "Дышит"),
        ("Древесина, какого дерева больше всего подходит для производства спичек?, варианты ответов: дуб, осина, баобаб", "Осина"),
        ("Без этого предмета не сыграешь на скрипке, варианты ответов: без шапки, без смычка, без нот", "Без смычка"),
        ("Из нежной сердцевины этого травянистого растения Древние египтяне делали свитки, а потом на них писали, варианты ответов: бамбук, хлопок, папирус", "папирус"),
        ("где родина страуса? варианты, австрия, австралия, аргентина", "австралия"),
        ("Летучая мышь – это кто?, варианты ответов: птица, млекопитающие, тиктокер", "Млекопитающие")
        ]
    
    answers_counter = [0,0] 
    answers_counter[0] += 1 
    
    for q, a in ls:
        # say_message('тишина в классе')
        say_message("\nвопрос № : {} ".format(answers_counter[0]))
        say_message(q)
        time.sleep(3)
        winsound.Beep(1000,1000)
        answer = listen_command()

        # if answer == 'хватит':
        #     say_message('как хочешь')
        #     exit()

        if answer == a.lower():    
            say_message("это правильный ответ")
            answers_counter[0] += 1 
            answers_counter[1] += 1 

        else:
            say_message("это неправильный ответ, правильный ответ " + a)
            answers_counter[0] += 1 
        # say_message('нажми enter для продолжения, z для выхода')
        
        w = input()
        if w == 'z':
            exit()

    answers_counter[0] -= 1
    if answers_counter[0] == answers_counter[1]:
        say_message('поздравляю, ты на все вопросы ответил верно')

    if answers_counter[0] != answers_counter[1]:
        say_message('не на все вопросы ответил верно, в следующий раз всё получится')
    say_message("\nвсего задано вопросов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))
    exit()  

def say_message(message):

    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(random.randint(0, 100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Маруся: "+message)


if __name__ == '__main__':

    say_message('привет я маруся.  я для вас приготовила викторину, ну что потягаемся в знаниях. на раздумье 3 секунды, отвечай после звукового сигнала и сидите тихо, чтобы я правильно оценила ответы, после каждого ответа нажми enter для продолжения, z для выхода, если готов - скажи начнём') 


    while True:
               
            command = listen_command()  # слушает команду
            do_tris_command(command)  # обрабатывает команду
            

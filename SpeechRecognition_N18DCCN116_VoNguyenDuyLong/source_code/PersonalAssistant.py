# thư viện giao diện
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PersonalAssistantUI import Ui_MainWindow

# thư viện nhận dạng giọng nói
import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import wikipedia
# ----------------------------------------------------------------------------------------------------

# tạo khung cho trợ lý ảo gồm ba bộ phận miệng, tai và não
# mô phỏng ba hoạt động: tai-nghe => não-suy nghĩ => miệng-trả lời

#-----------------------------------------------1.Miệng-----------------------------------------------
friday_mouth=pyttsx3.init() # khởi tạo bộ phận
friday_mouth.setProperty('rate', 160) # tốc độ đọc
voices = friday_mouth.getProperty('voices')
friday_mouth.setProperty('voice', voices[0].id) # cài giới tính voices[0].id -> giọng nam , voices[1].id -> giọng nữ

def speak(audio):
    friday_mouth.say(audio) # nói
    friday_mouth.runAndWait()

#-----------------------------------------------2.Tai------------------------------------------------  
def command():
    friday_ear=sr.Recognizer() # khởi tạo bộ phận
    with sr.Microphone() as source: # lấy mic
        friday_ear.pause_threshold=2
        friday_ear.adjust_for_ambient_noise(source, duration = 0.5)
        audio = friday_ear.listen(source) # nghe
    try:
        query = friday_ear.recognize_google(audio,language='en-US') # nhận dạng và đặt ngôn ngữ nhận dạng là tiếng Anh
        print("You: " + query) # in ra màn hình những gì trợ lý đã nghe
    except sr.UnknownValueError: # nếu không nhận dạng được bằng giọng nói thì nhận dạng lại
        speak('Sorry Boss! I didn\'t get that!! Try saying again')
        query = command()
    return query

#-----------------------------------------------3.Não------------------------------------------------
#---------------------Tính giờ-----------------------
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is " + Time)

#---------------------Tính ngày----------------------
def day():
    Day = datetime.datetime.now().strftime("%B %d, %Y") 
    speak("Today is " + Day)

#---------------------Chào hỏi-----------------------
def welcome():
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12: # sáng 
            speak("Good morning Boss! I'm Friday. Your personal assistant")
        elif hour>=12 and hour<18: # trưa
            speak("Good afternoon Boss! I'm Friday. Your personal assistant")
        elif hour>=18 and hour<24: # chiều
            speak("Good evening Boss! I'm Friday. Your personal assistant")
        speak("How can I help you?") 

# -------------------------------------------------------Form--------------------------------------------------------
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.btnStart.clicked.connect(lambda: self.start())

    def show(self):       
        self.main_win.show()

    def formWelcome(self):
        hour=datetime.datetime.now().hour
        self.uic.plainTextEdit.insertPlainText("-------------------------------------------------------------")
        if hour >= 6 and hour<12: # sáng 
            self.formPrint("FRIDAY: Good morning Boss! I'm Friday. Your personal assistant")
        elif hour>=12 and hour<18: # trưa
            self.formPrint("FRIDAY: Good afternoon Boss! I'm Friday. Your personal assistant")
        elif hour>=18 and hour<24: # tối
            self.formPrint("FRIDAY: Good evening Boss! I'm Friday. Your personal assistant")
        self.formPrint("FRIDAY: How can I help you?")
        welcome()

    def listen(self):   
        query = command().lower()
        self.formPrint("You: " + query)
        query = query.lower()
        return query

    def start(self):
        self.formWelcome()
        while True:
            query = self.listen()
            if "google" in query: # Khi người dùng yêu cầu mở và tra Google...
                self.formPrint("FRIDAY: Opening Google!!!")
                speak("Opening Google!!!")
                self.formPrint("FRIDAY: What should I search on Google Boss?")
                speak("What should I search on Google Boss?")
                search = self.listen()
                url = f"https://google.com/search?q={search}"
                wb.get().open(url)
                self.formPrint("FRIDAY: Here it is Boss!!!")
                speak(f'Here it is Boss')
        
            elif "youtube" in query: # Khi người dùng yêu cầu mở và tra Youtube...
                self.formPrint("FRIDAY: Opening Youtube!!!")
                speak("Opening Youtube!!!")              
                self.formPrint("FRIDAY: What should I search on Youtube Boss?")
                speak("What should I search on Youtube Boss?")
                search=self.listen()
                url = f"https://youtube.com/search?q={search}"
                wb.get().open(url)
                self.formPrint("FRIDAY: Here it is Boss!!!")
                speak(f'Here it is Boss')

            elif "facebook" in query: # Khi người dùng yêu cầu mở và tra Facebook...
                self.formPrint("FRIDAY: Opening Facebook!!!")
                speak("Opening Facebook!!!")
                url = f"https://facebook.com"
                wb.get().open(url)
                self.formPrint("FRIDAY: Here it is Boss!!!")
                speak(f'Here it is Boss')


            elif "time" in query: # Khi người dùng hỏi về giờ...
                self.formPrint("FRIDAY: It's " + datetime.datetime.now().strftime("%I:%M:%p"))
                time()

            elif "day" in query: # Khi người dùng hỏi về ngày...  
                self.formPrint("FRIDAY: It's " + datetime.datetime.now().strftime("%B %d, %Y"))
                day()

            elif "who are you" in query: # Khi người dùng muốn biết về trợ lý...
                self.formPrint("FRIDAY: I'm FIRDAY. Your personal assistant")
                speak("I'm FIRDAY. Your personal assistant")

            elif "wiki" in query or "wikipedia" in query or "define" in query or "search" in query: # Khi người dùng muốn tra từ điển Wiki...
                self.formPrint("FRIDAY: What do you want to know?")
                speak("What do you want to know? ")
                result = self.listen()
                self.formPrint("FRIDAY: " + wikipedia.summary(result, sentences = 2))
                speak(wikipedia.summary(result, sentences = 2))

            elif "quit" in query or "close" in query or "exit" in query: # Thoát
                self.formPrint("FRIDAY: Friday is off. Goodbye Boss!")
                speak("Friday is off. Goodbye Boss!")
                quit()

            self.formPrint("FRIDAY: What's next Boss?")
            speak("What's next Boss?")

    def formPrint(self, text):
        self.uic.plainTextEdit.insertPlainText("\n" + text)
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


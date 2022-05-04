import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import wikipedia

# tạo khung cho trợ lý ảo gồm ba bộ phận miệng, tai và não
# mô phỏng ba hoạt động: tai-nghe => não-suy nghĩ => miệng-trả lời

#-----------------------------------------------1.Miệng-----------------------------------------------
friday_mouth=pyttsx3.init() # khởi tạo bộ phận
friday_mouth.setProperty('rate', 150) # tốc độ đọc
voices = friday_mouth.getProperty('voices')
friday_mouth.setProperty('voice', voices[0].id) # cài giới tính voices[0].id -> giọng nam , voices[1].id -> giọng nữ

def speak(audio):
    print('F.R.I.D.A.Y: ' + audio)
    friday_mouth.say(audio) # nói
    friday_mouth.runAndWait()

#-----------------------------------------------2.Tai------------------------------------------------  
def command():
    c=sr.Recognizer() # khởi tạo bộ phận
    with sr.Microphone() as source: # lấy mic
        c.pause_threshold=2
        audio = c.listen(source) # nghe
    try:
        query = c.recognize_google(audio,language='en-US') # nhận dạng và đặt ngôn ngữ nhận dạng là tiếng Anh
        print("You: " + query) # in ra màn hình những gì trợ lý đã nghe
    except sr.UnknownValueError: # nếu không nhận dạng được bằng giọng nói thì nhận dạng bằng cách nhập vào
        speak('Sorry Boss! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
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

#---------------------Xử lý-----------------------
if __name__  =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query: # Khi người dùng yêu cầu mở và tra Google...
            speak("Opening Google!!!")
            speak("What should I search on Google Boss?")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here it is Boss')
        
        elif "youtube" in query: # Khi người dùng yêu cầu mở và tra Youtube...
            speak("Opening Youtube!!!")
            speak("What should I search on Youtube Boss?")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here it is Boss')

        elif "facebook" in query: # Khi người dùng yêu cầu mở và tra Facebook...
            speak("Opening Facebook!!!")
            url = f"https://facebook.com"
            wb.get().open(url)

        elif "time" in query: # Khi người dùng hỏi về giờ...
            time()

        elif "day" in query: # Khi người dùng hỏi về ngày...  
            day()

        elif "who are you" in query: # Khi người dùng muốn biết về trợ lý...
            speak("I'm FIRDAY. Your personal assistant")

        elif "what can you do" in query or "help" in query: # Khi người dùng muốn biết về các chức năng...
            speak("Here are something that I can do: opening application like google, youtube, facebook; telling you date/time; wikipedia everything")
            speak("What do you want me to do?")

        elif "wiki" in query or "wikipedia" in query or "define" in query or "search" in query: # Khi người dùng muốn tra từ điển Wiki...
            speak("What do you want to know? ")
            result = command().lower()
            speak(wikipedia.summary(result, sentences = 2))

        elif "quit" in query or "close" in query or "exit" in query: # Thoát
            speak("Friday is off. Goodbye Boss!")
            quit()

        speak("What's next Boss?")
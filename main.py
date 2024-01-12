import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes  
import webbrowser
import requests
import json 



listner =sr.Recognizer()
eng =pyttsx3.init()
voices=eng.getProperty("voices")
eng.setProperty('voice', voices[1].id)


def talk(text):
     eng.say(text)
     eng.runAndWait()

def greet():
    print("I am emmily")
    talk("Hello I am emmily ")
    print("I am here to assist you !")
    talk("I am here to assist you !")
    print("How can I help you?")
    talk("How can I help you?")
    





def get_weather_report(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    if data["cod"] != "404":
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        report = f"Weather in {city}: {main_weather} ({description})\n"
        report += f"Temperature: {temperature}K\n"
        report += f"Humidity: {humidity}%"

        return report
    else:
        return "City not found"
    
api_key = '6da841da66dcdf3a41606cd57e6936d3'
city = 'Chennai'
weather_report = get_weather_report(city, api_key)
print(weather_report)







def take_command():
     try:
        with sr.Microphone() as source:
                  print("Listening.....")
                  voice =listner.listen(source)
                  command =listner.recognize_google(voice)
                  command =command.lower()
                  if 'hello' in command :
                      command=command.replace('google','')
                      print(command)

     except:
           pass
     return  command







def run_emmily():
    command =take_command()
    print(command)
    if  'play' in command :
        song= command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time =datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who' in command:
        person = command.replace('who','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'are you single ' in command :
        print("I am in relationship with wifi")
        talk("I am in relationship with wifi ")
    
    elif 'owner' in command:
        talk("My owner's name is R Manoj Hariharan ")
        print(talk)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'what' in command :
        person1=command.replace('what','')
        inf=wikipedia.summary(person1,1)
        print(inf)
        talk(inf)

    

    elif 'hello' in command or 'emmily' in command or 'hi' in command:
        greet()
        
    elif 'how are you' in command:
        talk("I am fine , Thank you")
        talk("How are you, ")
    elif "good morning" in command or "good afternoon" in command or "good evening" in command:
        talk("A very" + command)
        talk("Thank you for wishing me! Hope you are doing well!")

    elif 'browser' in command:
        talk("Opening browser\n")
        webbrowser.open_new_tab("google.com")

    elif 'youtube' in command:
        talk('opening YouTube')

        webbrowser.open_new_tab("www.youtube.com")

    

    elif "amazon" in command:
            talk("Opening amazon")
            webbrowser.open_new_tab("www.amazon.in")
    elif "news" in command :
         talk("Here are some latest updates ")
         speak=webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines") 
            

   
   
    elif "mail" in command:
         talk("Opening Gmail")
         webbrowser.open_new_tab("gmail.com")

    elif "weather" in command:
          talk("Showing weather reports")
          print("Showing weather reports")
          get_weather_report(city, api_key)
           

    else:
        print("I could'nt get you\n"
              "Please try again!!")
        talk("I could'nt get you ")
        talk("Please try again!!")




run_emmily()


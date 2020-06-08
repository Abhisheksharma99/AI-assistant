import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechrecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import psutil # pip install psutil
import pyjokes # pip install pyjokes
engine = pyttsx3.init()
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def time():
	Time = datetime.datetime.now().strftime("%I:%M")
	speak('The current time is ')
	speak(Time)
def date():
	Year = str(datetime.datetime.now().year)
	month = str(datetime.datetime.now().month)
	Date = str(datetime.datetime.now().day)
	speak('The current date is ')
	speak(Date)
	speak(month)
	speak(Year)
def greet():
	speak('WELCOME SIR I AM YOUR AI ASSISTANT ')
	time()
	date()
	speak('SIR! , PLEASE LET ME KNOW IF I CAN DO ANY THING FOR YOU?')
def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening.....')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source) 
		r.energy_threshhold = 50
		audio = r.listen(source)
	try :
		print('Recognizing.....')
		query = r.recognize_google(audio, language='en-in')
		print(query)
	except Exception as e:
		print(e)
		speak('SORRY I DID NOT UNDERSTAND THAT , PLEASE SAY THAT AGAIN')
		return "None"
	return query
'''
def hear():
	r=r.recognizer()
	with sr.Microphone as source:
		print ('hearing.....')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		r.energy_threshold = 50
		audio = r.listen(source)
	try :
		print ('OKAY! , processing command')
		query = r.recognize_google(audio , language = 'en-in')
		print (query)
	except Exception as e:
		print(e)
		speak('SORRY! , AN ERROR OCCURED! , TRY AGAIN!')
	return query
'''
def sendmail(to , body):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.login(input('ENTER THE EMAIL: ') , input ('ENTER THE PASSWORD:'))
	server.sendmail(input("RECIEVER'S EMAIL:"), to , body)
	server.close()
def cpu_use():
	usage = str(psutil.cpu_percent())
	speak(' THE CPU USAGE IS' +usage)
def battery_percent():
	battery = psutil.sensors_battery()
	speak('THE BATTERY PERCENTAGE IS')
	speak(battery.percent)
def jokes():
	speak(pyjokes.get_joke())
if __name__ == '__main__':
	greet()
	while True:
		query = takecommand().lower()
		
		if 'time' in query:
			time()
		elif 'date' in query:
			date()
		elif 'what is your name' in query :
			speak ('HELLO SIR! , MY NAME IS INTRUDER')
		elif 'email' in query:
			try:
				speak('TELL ME WHAT SHOULD I SEND IN YOUR EMAIL')
				body = takecommand().lower()
				speak('THE CONTENT OF THE EMAIL IS '+body)
				speak ('PLEASE ENTER THE EMAIL MANUALLY')
				to = input("ENTER THE RECIEVER'S EMAIL:")
				sendmail(to , body)
				speak ('EMAIL HAS BEEN SENT SUCCESFULLY!')
			except Exception as e:
				print (e)
				speak('UNABLE TO SEND EMAIL')
		elif 'wikipedia' in query:
			speak('searching for results')
			query = query.replace('wikipedia','')
			result = wikipedia.summary(query, sentences=2)
			print(result)
			speak(result)
		elif 'firefox' in query:
			speak ('WHAT SHOULD I SEARCH?')
			browser_dir = '/usr/lib/firefox-esr/firefox-esr %s'
			search = takecommand().lower()
			wb.get(browser_dir).open_new_tab(search)
		elif 'shutdown' in query:
			os.system('shutdown -h now')
		elif 'reboot' in query :
			os.system('reboot')
		elif 'logout' in query:
			os.system('logout')
		elif 'play songs' in query:
			songs_dir = ''
			songs = os.listdir(songs_dir)
			os.startfile(os,path.join(songs_dir, songs[0]))
		elif 'remember' in query:
			speak('WHAT SHOULD I REMEMBER?')
			save = takecommand()
			speak (' OKAY SIR! , NOW I WILL REMEMBER THIS' +save)
			remember = open ('data.txt' , 'w')
			remember.write(save)
			remember.close()
		elif 'remind me' in query:
			remember = open ( 'data.txt', 'r')
			print ('YOU SAID ME TO REMEMBER THAT' +remember.read())
			speak ('YOU SAID ME TO REMEMBER THAT' +remember.read())
		elif 'cpu' in query:
			cpu_use()
		elif 'battery' in query:
			battery_percent()
		elif 'joke' in query:
			jokes()		
		elif 'offline'  in query:
			speak('OKAY SIR! , HAVE A GOOD DAY!')
			quit()





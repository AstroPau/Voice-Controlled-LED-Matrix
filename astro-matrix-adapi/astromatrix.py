import speech_recognition as sr
import time
import os, random


parameters = '-C --led-rows=16 --led-cols=32 --led-chain=1 --led-gpio-mapping=adafruit-hat' #My LED Matrix needed parameters
cube_parameters = 'sudo ./demo -D0 --led-rows=16 --led-cols=32 --led-chain=1 --led-slowdown-gpio=2 --led-pwm-bits=11 --led-rgb-sequence=RBG --led-gpio-mapping=adafruit-hat' #Parameters commnand that I've used for the cube and the subscribe image
subscribe_parameters = 'sudo ./demo -D1 AstroSubs.ppm --led-rows=16 --led-cols=32 --led-chain=1 --led-slowdown-gpio=2 --led-pwm-bits=11 --led-rgb-sequence=RBG --led-gpio-mapping=adafruit-hat'


r = sr.Recognizer() #Voice recognizer initialization

boolean = True

while True:
	try:
		with sr.Microphone() as source:
			audio = r.listen(source) #Uses the microphone as audio input
			time.sleep(0.01)
			try:
				recognised_text = r.recognize_google(audio) #Speech to text conversion
				print(recognised_text)
				if "car" in recognised_text:
					img_file = random.choice(os.listdir("/home/pi/astro-matrix-adapi/IMAGES/car")) #Car images folder
					variable = "/home/pi/astro-matrix-adapi/IMAGES/car" + "/" + img_file #Car images folder + image file name
					command = 'sudo ./led-image-viewer' + " " + variable + ' ' + parameters #Command used for displaying the image
					wh_is = 'cd /home/pi/rpi-rgb-led-matrix/utils' #LED Matrix utils folder
					print(img_file)
				elif "plane" in recognised_text:
					img_file = random.choice(os.listdir("/home/pi/astro-matrix-adapi/IMAGES/plane")) #Plane images folder
					variable = "/home/pi/astro-matrix-adapi/IMAGES/plane" + "/" + img_file #Plane images folder + image file name
					command = 'sudo ./led-image-viewer' + " " + variable + ' ' + parameters #Command used for displaying the image
					wh_is = 'cd /home/pi/rpi-rgb-led-matrix/utils' #LED Matrix utils folder
					print(img_file)
				elif "memes" in recognised_text:
					img_file = random.choice(os.listdir("/home/pi/astro-matrix-adapi/IMAGES/gifs")) #Memes images folder
					variable = "/home/pi/astro-matrix-adapi/IMAGES/gifs" + "/" + img_file #Memes images folder + image file name
					command = 'sudo ./led-image-viewer' + " " + variable + ' ' + parameters #Command used for displaying the image
					wh_is = 'cd /home/pi/rpi-rgb-led-matrix/utils' #LED Matrix utils folder
					print(img_file)
				elif "Cube" in recognised_text:
					command = cube_parameters #Command used for displaying the image (Only for cube and subscribe image)
					wh_is = 'cd /home/pi/rpi-rgb-led-matrix/examples-api-use' #LED Matrix examples folder (I used this folder for the cube because it's a drawing and it's an example from the matrix folder)
					print("")
				elif "subscribe" in recognised_text:
					command = subscribe_parameters #Command used for displaying the image (Only for cube and subscribe image)
					wh_is = 'cd /home/pi/rpi-rgb-led-matrix/examples-api-use' #LED Matrix examples folder (For making a moving text I used one example file from the matrix folder and I replaced the .ppm example image to one that I've made in photoshop and converted online)
				else:
					print("I didn't undestand you")
				
				os.system(wh_is + '&&' + command) #Compounded command for the command line
			except sr.UnknownValueError:
				print("")
			except sr.RequestError as e:
				print("")
	except boolean != True:
				print("error")

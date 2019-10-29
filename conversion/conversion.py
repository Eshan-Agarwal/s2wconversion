
import speech_recognition as sr

repeat_keywords = {'Once':1,'Double':2, 'Triple':3,
					'once':1,'double':2, 'triple':3}

def repeater(s):

	"""
	
	prints english words like "Triple A" to AAA or "Doble A" to AA or "Once A" to A 

	Args : 
			s (str) : string tokens

	return : 
			converted string

	"""
	repeats = 0
	s = [ss.strip() for ss in s.split()][::-1]

	for i in range(len(s) - 1):
		if s[i - repeats + 1] in repeat_keywords:
			s[i - repeats] *= repeat_keywords[s[i - repeats + 1]]

			del s[i - repeats + 1]
			repeats += 1

	return ' '.join(s[::-1])


def conversion():

		"""
		converts a spoken English paragraph to written English as per above rule

		Args : 
				Spoken English input

		Return : Written English

		"""
	
		#obtain audio from the microphone
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say something!")
			audio = r.listen(source)

		try:
			# for testing purposes, we're just using the default API key
			# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			# instead of `r.recognize_google(audio)`
			print("Input from user after transcript audio by Google Speech Recognition is :" ,r.recognize_google(audio))
			print("Abbreviations spoken :",repeater(str(r.recognize_google(audio))))
			abb = repeater(str(r.recognize_google(audio)))
			return abb

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

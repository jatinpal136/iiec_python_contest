import pyttsx3
import os
pyttsx3.speak("Hii I am cerena")


while True:
	print("How can I Help you: "  , end='')
	p = input()

	if (("run" in p) or ("execute") or ("open" in p))  and (("chrome" in p) or ("internet" in p)):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) ):
	  os.system("notepad")

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("File Explorer" in p) or ("Files" in p) ):
	  os.system("File Explorer") 

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("paint" in p) or ("drawing" in p) ):
	  os.system("paint") 

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("jupitor notebook" in p) or ("python IDE" in p) ):
	  os.system("jupiter notebook") 

	elif (("run" in p) or  ("execute" in p ) or ("open" in p)) and  (("gallery" in p) or ("photos" in p) ):
	  os.system("photos") 

	elif (("play" in p) or ("open" in p))  and ( ("song" in p) and ("media" in p) ):
	  os.system("wmplayer")

	elif  ( ("exit" in p)  or ("quit" in p) or ("stop" in p) ):
	  break

	else:
	  print("dont support")



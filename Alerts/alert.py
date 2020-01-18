from win10toast import ToastNotifier
import pyttsx3

toaster = ToastNotifier()
txt = "INTRUDER ALERT \n"
txt *= 3
toaster.show_toast("ALERT ALERT", txt)

engine = pyttsx3.init()
engine.say("Intruder alert, intruder alert, intruder alert")
engine.runAndWait()
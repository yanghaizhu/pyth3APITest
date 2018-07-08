import win32com.client
import winsound

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works!")

text="I love you baby 爱你"
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(text)


speak = win32com.client.Dispatch('SAPI.SPVOICE')


speak.Speak("不可能个毛")

winsound.Beep(1000, 1000)


import speech_recognition as sr
import pyautogui

def main():

    r = sr.Recognizer()

    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)  

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")


        # recognize speech using google

        try:
            website = r.recognize_google(audio)
            print("You have said: " + website)
            print("Audio Recorded Successfully \n ")

            # open the website in the default browser
            pyautogui.press("win")
            pyautogui.write("chrome")
            pyautogui.press("enter")
            pyautogui.write("https://www." + website )
            pyautogui.press("enter")

        except Exception as e:
            print("Error :  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":
    main()
# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import Functions as F
import os
import Listen as l
import sys as s


# Initialize the recognizer
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
open_file = ""

# Function to convert text to
# speech

#def SpeakText(command):
#   Initialize the engine
#   engine = pyttsx3.init()
#   engine.say(command)
#   engine.runAndWait()


# Loop infinitely for user to
# speak

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if(MyText == "print"):
                print("Going in to print")
                #need some way to print things in a string or variables
                F.print_in_file()
                continue



            #user must call a this first pretty much always
            if(MyText == "open file"):
                open_file = F.openFile()
                print("")
                continue


            #user can only call runfile after file has opened and run too
            if (MyText == "run file"):
                print("Running file....")
                #runs the file the user has chosen
                if(len(open_file) != 0):

                    os.system(open_file)
                else:
                    print("You cannot run a file prior to creating one, call open file and write some code in it first.")

            #Voice command to stop running.
            if(MyText == "end speech to code" or MyText ==  "and speech to code"):
                print("Exiting speech2code...")
                break

            #gonna need to do some string parsing here
            #variable appleseed equals (or equal) 6

            if (MyText == 'variable'):
                print("Entering variable assignment...")
                varString = F.variableDeclaration()
                print("Output : ", varString)
                continue

            #would like to be able to make variables camelcase
            capital = 'capital'
            if capital in MyText:
                someText = MyText.split(" ")
                print(someText)
                capIndex = someText.index(capital)
                print(capIndex)
                capString = someText[capIndex+1].capitalize()
                someText[capIndex+1] = capString
                someText.remove("capital")
                print("after upper: ")
                #someText.remove("")
                print(someText)
                MyText =  "".join(someText)
                print(MyText)

            print("Audio heard: " + MyText)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
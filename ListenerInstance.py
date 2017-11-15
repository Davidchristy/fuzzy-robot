import time, threading

import speech_recognition as sr
# https://pypi.python.org/pypi/SpeechRecognition/

class ListenerThread(threading.Thread):

    def __init__(self,parent):
        threading.Thread.__init__(self)
        self.parent = parent
        return

    def run(self):
        # recognize speech using Sphinx
        r = sr.Recognizer()
        # for index, name in enumerate(sr.Microphone.list_microphone_names()):
        #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

        # return
        while True:
            with sr.Microphone() as source:
                print("Say something!")
                r.adjust_for_ambient_noise(source)
                print("energy_threshold: {}".format(r.energy_threshold))
                audio = r.listen(source)
            try:
                print("We heard something!")
                print("Sphinx thinks you said: \"{}\"".format(r.recognize_sphinx(audio)))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

            WIT_AI_KEY = self.parent.config["API Keys"]["WIT_AI_KEY"]
            try:
                print("Wit.ai thinks you said: \"{}\"".format(r.recognize_wit(audio, key=)))
            except sr.UnknownValueError:
                print("Wit.ai could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Wit.ai service; {0}".format(e))



            # print("I'm listening, why aren't you talking?")
            time.sleep(1)



class ListenerInstance:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ListenerInstance.__instance == None:
            ListenerInstance()
        return ListenerInstance.__instance

    def __init__(self,config):
        if ListenerInstance.__instance != None:
            raise Exception("This class is a singleton!")
        print("Making ListenerInstance")
        self.config = config
        self.listenerThread = ListenerThread(self)
        self.listenerThread.daemon = True
        self.listenerThread.start()

        ListenerInstance.__instance = self

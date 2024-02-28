from bitcoin_value import currency 
from threading import Thread 
from time import sleep 
from tkinter import messagebox 
import pyttsx3 
from itertools import count 
from pygame import mixer 


class CryptoAlarm:
    def __init__(self, low_thresh,high_thresh,threshold):
        self.low_thresh = low_thresh 
        self.high_thresh = high_thresh 
        self.threshold = threshold 
        self.price = None
        mixer.init() 
        self.price_t = Thread(target=self.get_price)
        self.price_t.start()


    def get_price(self):
        self.price = currency('USD')
        self.check_t = Thread(target=self.check_price)
        self.check_t.start()

        while True:
            try:
                self.price = currency('USD')
            except:
                pass
                print(self.price)
            sleep(3)
        
    def check_price(self):
        for i in count(1):
            if self.price > self.high_thresh:
                mixer.music.load('up.mp3')
                mixer.music.play()
                self.high_thresh += self.threshold 
                self.low_thresh += self.threshold 
            elif self.price < self.low_thresh:
                mixer.music.load('down.mp3')
                mixer.music.play()
                self.high_thresh -= self.threshold 
                self.low_thresh -= self.threshold 

                if i %60 == 0:
                    pass 
                print(f"{self.low_thresh} < {self.price} < {self.high_thresh}")
                sleep(1)
    def say(self,text):
         self.engine.say(text)
         self.engine.runAndWait()


if __name__ == "__main__" :
    CryptoAlarm(59900,60000,100)
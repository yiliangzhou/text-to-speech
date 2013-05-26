#!/usr/local/bin/python

import urllib2   # urllib2.Request urllib2.urlopen
import urllib    # urllib.urlencode
import sys       
from optparse import OptionParser
import pygame

service = 'http://translate.google.com/translate_tts?'

def speak(text, language):
    para_encode = {'ie' : 'utf-8'}
    para_language = {'tl' : language} 
    para_query = {'q' : text}
    
    url = service + urllib.urlencode(para_encode) + '&'  + \
                    urllib.urlencode(para_language) + '&' + \
                    urllib.urlencode(para_query)
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    google_speech = urllib2.urlopen(req).read()
    f = open('.tmp.mp3', 'w')
    f.write(google_speech)
    f.close() 
    pygame.init()
    pygame.mixer.music.load(".tmp.mp3")
    pygame.mixer.music.play() 


def main():
    # read in parameter
    parser = OptionParser()
    parser.add_option("-l", "--language", dest="language",
                      help="to speak the text in which language, to speak\
                      in Chinese, give zh_CN as input for this option",
                      default='en')
    (options, args) = parser.parse_args()
    pre_str = "To speak: "
    while True:
        text = raw_input(pre_str)
        if len(text) == 0:
            break
        speak(text, options.language)
    return

if __name__ == "__main__":
    main()

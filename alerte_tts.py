#!/usr/bin/env python
import sys
import json
from urllib2 import Request, urlopen
import subprocess
import os, glob
import hashlib
import shutil
import time
from pydub import AudioSegment
from flask import Flask
talkie = Flask(__name__)

@talkie.route("/")
def index():
    return "Talkie Web Link !!"

@talkie.route("/hello")
def hello():
    return "Hello World!!"

@talkie.route('/post/phrase=<phrase>&jingle=<jingle>')
def talkjingle(phrase,jingle=None):
    phrase=phrase.encode('utf-8')
    cachepath=os.path.dirname(os.path.dirname(__file__))
    jinglepath=os.path.abspath(os.path.join(os.path.dirname(__file__), 'jingle'))
    file = 'tts'
    filename=os.path.join(cachepath,file+'.wav')
    filenamemp3=os.path.join(cachepath,file+'.mp3')
    os.system('pico2wave -l fr-FR -w '+filename+ ' "' +phrase+ '"')
    song = AudioSegment.from_wav(filename)
    if not jingle:
        songmodified=song
    else:
        jinglename=os.path.join(jinglepath,jingle+'.mp3')
        try:
            os.stat(jinglename)
        except:
            return 'Erreur le jingle %s n\'existe pas' % jinglename
        jinglename=os.path.join(jinglepath,jingle+'.mp3')
        jingle= AudioSegment.from_mp3(jinglename)
        songmodified = jingle+song
    songmodified.export(filenamemp3, format="mp3", bitrate="128k", tags={'albumartist': 'Talkie', 'title': 'TTS', 'artist':'Talkie'}, parameters=["-ar", "44100","-vol", "200"])
    song = AudioSegment.from_mp3(filenamemp3)
    cmd = ['mplayer']
    cmd.append(filenamemp3)
    with open(os.devnull, 'wb') as nul:
		subprocess.call(cmd, stdin=nul)
    return 'Post %s' % phrase

@talkie.route('/post/phrase=<phrase>')
def talk(phrase):
    phrase=phrase.encode('utf-8')
    cachepath=os.path.dirname(os.path.dirname(__file__))
    file = 'tts'
    filename=os.path.join(cachepath,file+'.wav')
    filenamemp3=os.path.join(cachepath,file+'.mp3')
    os.system('pico2wave -l fr-FR -w '+filename+ ' "' +phrase+ '"')
    song = AudioSegment.from_wav(filename)
    songmodified=song
    songmodified.export(filenamemp3, format="mp3", bitrate="128k", tags={'albumartist': 'Talkie', 'title': 'TTS', 'artist':'Talkie'}, parameters=["-ar", "44100","-vol", "200"])
    song = AudioSegment.from_mp3(filenamemp3)
    cmd = ['mplayer']
    cmd.append(filenamemp3)
    with open(os.devnull, 'wb') as nul:
		subprocess.call(cmd, stdin=nul)
    return 'Post %s' % phrase

if __name__ == "__main__":
    talkie.run(host='0.0.0.0')
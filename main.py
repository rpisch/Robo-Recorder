"""from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

led_pinout = [11,13,15,16,18,22,31,36]

GPIO.setmode(GPIO.BOARD)
for led in led_pinout:
    GPIO.setup(led, GPIO.OUT)

for led_off in led_pinout:
    GPIO.output(led_off, GPIO.LOW)


@app.route('/<int:note>')
def notes(note):
    timer = 0
    note = 10

    while True:
        if timer == 50000:
            note -= 1
            timer = 0
            if note == 0:
                note = 10
        else:
            timer = timer + 1
        if note == 1:
            GPIO.output(led_pinout[0], GPIO.LOW)
            GPIO.output(led_pinout[1], GPIO.LOW)
            GPIO.output(led_pinout[2], GPIO.LOW)
            GPIO.output(led_pinout[3], GPIO.LOW)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
            elif (note == 1):
                GPIO.output(led_pinout[0], GPIO.HIGH)
                GPIO.output(led_pinout[1], GPIO.HIGH)
                GPIO.output(led_pinout[2], GPIO.HIGH)
                GPIO.output(led_pinout[3], GPIO.HIGH)
                GPIO.output(led_pinout[4], GPIO.HIGH)
                GPIO.output(led_pinout[5], GPIO.HIGH)
                GPIO.output(led_pinout[6], GPIO.HIGH)
        elif (note == 2):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.HIGH)
            GPIO.output(led_pinout[3], GPIO.HIGH)
            GPIO.output(led_pinout[4], GPIO.HIGH)
            GPIO.output(led_pinout[5], GPIO.HIGH)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 3):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.HIGH)
            GPIO.output(led_pinout[3], GPIO.HIGH)
            GPIO.output(led_pinout[4], GPIO.HIGH)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 4):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.HIGH)
            GPIO.output(led_pinout[3], GPIO.HIGH)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.HIGH)
            GPIO.output(led_pinout[6], GPIO.HIGH)
        elif (note == 5):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.HIGH)
            GPIO.output(led_pinout[3], GPIO.LOW)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 6):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.LOW)
            GPIO.output(led_pinout[3], GPIO.LOW)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 7):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.LOW)
            GPIO.output(led_pinout[2], GPIO.HIGH)
            GPIO.output(led_pinout[3], GPIO.HIGH)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 8):
            GPIO.output(led_pinout[0], GPIO.HIGH)
            GPIO.output(led_pinout[1], GPIO.LOW)
            GPIO.output(led_pinout[2], GPIO.LOW)
            GPIO.output(led_pinout[3], GPIO.LOW)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
        elif (note == 9):
            GPIO.output(led_pinout[0], GPIO.LOW)
            GPIO.output(led_pinout[1], GPIO.HIGH)
            GPIO.output(led_pinout[2], GPIO.LOW)
            GPIO.output(led_pinout[3], GPIO.LOW)
            GPIO.output(led_pinout[4], GPIO.LOW)
            GPIO.output(led_pinout[5], GPIO.LOW)
            GPIO.output(led_pinout[6], GPIO.LOW)
    return (str(note))

app.run(host='127.0.0.1', port=5000, debug=True)
"""

#########################################################
###################### GPIO SETUP #######################
#########################################################

import RPi.GPIO as GPIO

# set mode to use the physical board pin numbers
GPIO.setmode(GPIO.BOARD)

# regular GPIO ports for solenoids
solenoid_pins = [11, 13, 15, 16, 18, 22, 31, 36]

for i in solenoid_pins:
  GPIO.setup(i, GPIO.OUT)

for j in solenoid_pins:
  GPIO.output(j, GPIO.LOW)

#GPIO.output(solenoid_pins[7], GPIO.LOW)

#########################################################
################## NOTES TO SOLENOIDS ###################
#########################################################


def mute():
  GPIO.output(solenoid_pins[7], GPIO.HIGH)

def on_low_C():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.HIGH)
  GPIO.output(solenoid_pins[4], GPIO.HIGH)
  GPIO.output(solenoid_pins[5], GPIO.HIGH)
  GPIO.output(solenoid_pins[6], GPIO.HIGH)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_D():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.HIGH)
  GPIO.output(solenoid_pins[4], GPIO.HIGH) 
  GPIO.output(solenoid_pins[5], GPIO.HIGH)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_E():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.HIGH)
  GPIO.output(solenoid_pins[4], GPIO.HIGH)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_F():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.HIGH)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.HIGH)
  GPIO.output(solenoid_pins[6], GPIO.HIGH)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_G():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.LOW)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_A():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.LOW)
  GPIO.output(solenoid_pins[3], GPIO.LOW)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_Bb():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.LOW)
  GPIO.output(solenoid_pins[2], GPIO.HIGH)
  GPIO.output(solenoid_pins[3], GPIO.HIGH)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_B():
  GPIO.output(solenoid_pins[0], GPIO.HIGH)
  GPIO.output(solenoid_pins[1], GPIO.LOW)
  GPIO.output(solenoid_pins[2], GPIO.LOW)
  GPIO.output(solenoid_pins[3], GPIO.LOW)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)


def on_high_C():
  GPIO.output(solenoid_pins[0], GPIO.LOW)
  GPIO.output(solenoid_pins[1], GPIO.HIGH)
  GPIO.output(solenoid_pins[2], GPIO.LOW)
  GPIO.output(solenoid_pins[3], GPIO.LOW)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)

####### END NOTE TO SOLENOIDS ######

##################################################
############### JACOB's MIDO CODE ################
##################################################

import mido  #Importing libraries
import numpy as np

###############################################





def begin(notes, times):
  for index, note in enumerate(notes):
    if note == 0:
      mute()
    elif note == 60:
      on_low_C()
    elif note == 62:
      on_D()
    elif note == 64:
      on_E()
    elif note == 65:
      on_F()
    elif note == 67:
      on_G()
    elif note == 69:
      on_A()
    elif note == 70:
      on_Bb()
    elif note == 71:
      on_B()
    elif note == 72:
      on_high_C()
    time.sleep(times[index] / 1000)
  GPIO.output(solenoid_pins[0], GPIO.LOW)
  GPIO.output(solenoid_pins[1], GPIO.LOW)
  GPIO.output(solenoid_pins[2], GPIO.LOW)
  GPIO.output(solenoid_pins[3], GPIO.LOW)
  GPIO.output(solenoid_pins[4], GPIO.LOW)
  GPIO.output(solenoid_pins[5], GPIO.LOW)
  GPIO.output(solenoid_pins[6], GPIO.LOW)
  GPIO.output(solenoid_pins[7], GPIO.LOW)
  

# called when user clicks "Play Song"
# takes song and bpm choice
def parseSong(song, bpm):
  songs = {
    "1": "static/files/Hot Cross Buns.mid",
    "2": "static/files/Gentley Sleep.mid",
    "3": "static/files/Merrily We Roll Along.mid",
    "4": "static/files/It's Raining.mid",
    "5": "static/files/Old MacDonald Had A Farm.mid",
    "6": "static/files/When The Saints Go Marching In.mid",
    "7": "static/files/Twinkle Twinkle Little Star.mid",
    "8": "static/files/Ode To Joy.mid",
    "9": "static/files/Through_the_Fire_and_Flames.mid",
    "10": "static/files/French Tune.mid",
    "11": "static/files/Air Test.mid",
    "12": "static/files/For Finger Control.mid",
    "13": "static/files/Jingle Bells.mid",
    "14": "static/files/My Heart Will Go On.mid",
    "15": "static/files/D and F#.mid",
    "16": "static/files/G and F#.mid",
    "17": "static/files/Long Tones.mid",
    "18": "static/files/Jolly Old St. Nick.mid",
    "19": "static/files/The Saints.mid",
    "20": "static/files/Good King Wenceslas.mid",
    "21": "static/files/Fingering Chart.mid"
  }
  mid = mido.MidiFile(songs[song], clip=True)
  temp = parsing(mid, bpm)
  notes = temp[0]
  times = temp[1]
  begin(notes, times)


def C4(length):  #Write each note for length of note in array
  i = 0
  a = 60
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def D4(length):
  i = 0
  a = 62
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def E4(length):
  i = 0
  a = 64
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def F4(length):
  i = 0
  a = 65
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def G4(length):
  i = 0
  a = 67
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def A4(length):
  i = 0
  a = 69
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def Bb4(length):
  i = 0
  a = 70
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def B4(length):
  i = 0
  a = 71
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def C5(length):
  i = 0
  a = 72
  new_midi_part = []
  for i in range(length):
    new_midi_part.append(a)
  return new_midi_part


def EmptyNote(length):  #Used for spaces between notes or rests
  i = 0
  new_midi_part = []  #MIDI files are backwards such that the time value
  for i in range(length -
                 1):  #on each line shows the time until it is executed.
    new_midi_part.append(
      new_midi_part[-1])  #Due to this we apply the previous value to the
  new_midi_part.append(
    np.nan)  #time given to the current blank value until its last
  return new_midi_part  #iteration in which we append a 0


def parsing(mid, bpm):
  num_lines = len(mid.tracks[0])  #Calculate length of song
  notes = []
  times = []

  for i in range(num_lines):  #For each line of the MIDI, iterate
    midi_str = str(mid.tracks[0][i])
    if ('note_on' in midi_str):

      if ('velocity=0' in midi_str):

        #If no sound, apply empty note function

        if ('time=113' in midi_str):  #Sixteenth note
          times.append(113 * 120 / bpm)
        elif ('time=227' in midi_str):  #Eighth note
          times.append(227 * 120 / bpm)
        elif ('time=341' in midi_str):  #Dotted Eighth note
          times.append(341 * 120 / bpm)
        elif ('time=455' in midi_str):  #Quarter note
          times.append(455 * 120 / bpm)
        elif ('time=683' in midi_str):  #Dotted Quarter note
          times.append(683 * 120 / bpm)
        elif ('time=911' in midi_str):  #Half note
          times.append(911 * 120 / bpm)
        elif ('time=1367' in midi_str):  #Dotted half note
          times.append(1367 * 120 / bpm)
        elif ('time=1823' in midi_str):  #Whole note
          times.append(1823 * 120 / bpm)

        #Slurs
        elif ('time=119' in midi_str):  #Sixteenth note
          times.append(119 * 120 / bpm)
        elif ('time=239' in midi_str):  #Eighth note
          times.append(239 * 120 / bpm)
        elif ('time=359' in midi_str):  #Dotted Eighth note
          times.append(359 * 120 / bpm)
        elif ('time=479' in midi_str):  #Quarter note
          times.append(479 * 120 / bpm)
        elif ('time=719' in midi_str):  #Dotted Quarter note
          times.append(719 * 120 / bpm)
        elif ('time=959' in midi_str):  #Half note
          times.append(959 * 120 / bpm)
        elif ('time=1439' in midi_str):  #Dotted half note
          times.append(1439 * 120 / bpm)
        elif ('time=1919' in midi_str):  #Whole note
          times.append(1919 * 120 / bpm)

        if ('note=60' in midi_str):  #If sound, apply function of note value
          notes.append(60)

        elif ('note=61' in midi_str):
          notes.append(61)

        elif ('note=62' in midi_str):
          notes.append(62)

        elif ('note=63' in midi_str):
          notes.append(63)

        elif ('note=64' in midi_str):
          notes.append(64)

        elif ('note=65' in midi_str):
          notes.append(65)

        elif ('note=66' in midi_str):
          notes.append(66)

        elif ('note=67' in midi_str):
          notes.append(67)

        elif ('note=68' in midi_str):
          notes.append(68)

        elif ('note=69' in midi_str):
          notes.append(69)

        elif ('note=70' in midi_str):
          notes.append(70)

        elif ('note=71' in midi_str):
          notes.append(71)

        elif ('note=72' in midi_str):
          notes.append(72)

      elif ('note_on' in midi_str):  #Counts the time in between notes

        if ('time=73' in midi_str):  #Dotted half note break
          times.append(73)
          notes.append(0)

        elif ('time=13' in midi_str):  #Eighth note break
          times.append(13)
          notes.append(0)

        elif ('time=19' in midi_str):  #Dotted eighth break
          times.append(19)
          notes.append(0)

        elif ('time=25' in midi_str):  #Quarter break
          times.append(25)
          notes.append(0)

        elif ('time=37' in midi_str):  #Dotted quarter break
          times.append(37)
          notes.append(0)

        elif ('time=49' in midi_str):  #Half break
          times.append(49)
          notes.append(0)

        elif ('time=7' in midi_str):  #Sixteenth half break
          times.append(7)
          notes.append(0)

        elif ('time=97' in midi_str):  #Whole note break
          times.append(97)
          notes.append(0)

  return notes, times




######## FLASK STUFF #########

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from wtforms import FileField, SubmitField
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
  file = FileField("File", validators=[InputRequired()])
  submit = SubmitField("Upload File")


# index page sends user to home
@app.route('/')
def index():
  return render_template('home.html')


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
  #if len(os.listdir("/static/files")) == 0:
  #return "Upload Files First."
  # replace string with whole file path
  form = UploadFileForm()
  if form.validate_on_submit():
    file = form.file.data
    file.save(
      os.path.join(os.path.abspath(os.path.dirname(__file__)),
                   app.config['UPLOAD_FOLDER'],
                   secure_filename(file.filename)))
  return render_template('edit.html', form=form)


@app.route('/play', methods=["GET", "POST"])
def play():
  """if request.method == "GET":
    song_name = request.form.get("song")
    bpm = request.form.get("bpm")
    #print(song_name)
    print("bpm:", bpm)
    if song_name in songs:
      #print("working")
      parseSong(song_name, bpm)"""
  return render_template('play.html')


@app.route('/playing_song')
def playing_song():
  songs = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
    "16", "17", "18", "19", "20", "21"
  ]
  song_name = request.args.get("song")
  bpm = int(request.args.get("bpm"))
  if song_name in songs:
      #print("working")
      parseSong(song_name, bpm)
  return render_template('playing_song.html')


app.run(host='127.0.0.1', port=5000, debug=True)

"""


#print(mid.tracks[0])
#print(new_midi)

"""

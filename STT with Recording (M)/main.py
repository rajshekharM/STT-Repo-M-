from builtins import LookupError

from flask import Flask, render_template, make_response, Response, send_from_directory, request, redirect
import os
import speech_recognition as sr
app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "images"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico.jpg', mimetype='image/vnd.microsof.icon')

@app.route("/upload",methods=['GET','POST'])
def upload():
    result = ""
    if request.method == "POST":

        if request.files:
            file = request.files["file"]
            print("File Name: ")
            print(file)
            strSplit = file.filename
            print(strSplit)
            strSplit = strSplit.split(".")
            if(True):
                print("okay")

                file.save(os.path.join(app.config["IMAGE_UPLOADS"], file.filename))
                r = sr.Recognizer()
                with sr.AudioFile("images/"+file.filename) as source:  # use the default microphone as the audio source
                    #r.adjust_for_ambient_noise(source)
                    print("Converting Audio to Text")
                    audio = r.record(source)  # listen for the first phrase and extract it into audio data

                try:

                    result = r.recognize_google(audio)
                    print("You said " + result)  # recognize speech using Google Speech Recognition
                except LookupError:  # speech is unintelligible
                    result = "Could not understand audio"
                    print("Could not understand audio")
            else:
                result = "File must be .wav"

            #return redirect(request.url)
    return Response(render_template('result.html' , data=result))

@app.route("/uploadN",methods=['GET','POST'])
def uploadN():
    result = ""
    if request.method == "POST":

        if request.files:
            file = request.files["file"]
            print("File Name: ")
            print(file)
            strSplit = file.filename+".wav"
            print(strSplit)
            strSplit = strSplit.split(".")
            if(True):
                print("okay")

                file.save(os.path.join(app.config["IMAGE_UPLOADS"], file.filename+".wav"))
                r = sr.Recognizer()
                with sr.AudioFile("images/"+file.filename+".wav") as source:  # use the default microphone as the audio source
                    #r.adjust_for_ambient_noise(source)
                    print("Converting Audio to Text")
                    audio = r.record(source)  # listen for the first phrase and extract it into audio data

                try:

                    result = r.recognize_google(audio)
                    print("You said " + result)  # recognize speech using Google Speech Recognition
                except LookupError:  # speech is unintelligible
                    result = "Could not understand audio"
                    print("Could not understand audio")
            else:
                result = "File must be .wav"

            #return redirect(request.url)
    return result

@app.route("/", methods=['GET', 'POST'])
def home():
    Response.charset = 'utf-8'

    return Response(render_template("index.html"))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, threaded=True)
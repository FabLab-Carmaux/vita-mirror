# vita

#gestion des evenements programmés par un cron ?


#install dep
apt-get update
apt-get upgrade -y

#to allow vita to speak
sudo apt-get install libttspico-utils

#speech recognition library (>=3.5
pip install SpeechRecognition

#to use microphone
apt-get install python-all-dev
apt-get install portaudio19-dev
pip install PyAudio

#a tester pour la partie graphique
pip install ipython

#launch vita
python vita.py

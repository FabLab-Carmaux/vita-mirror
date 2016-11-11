# vita

#gestion des evenements programmés par un cron ?


#install dep
apt-get update
apt-get upgrade -y
#to allow vita to speak
sudo apt-get install libttspico-utils
#speech recognition library (>3.4.6 github version for now)
git clone https://github.com/Uberi/speech_recognition.git
python setup.py install
#to use microphone
pip install PyAudio

#a tester pour la partie graphique
pip install ipython

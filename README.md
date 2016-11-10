# vita

#gestion des evenements programmés par un cron ?


#install dep
apt-get update
apt-get upgrade -y
#to allow vita to speak
sudo apt-get install libttspico-utils
#speech recognition library (>3.4.6 github version for now)
pip install SpeechRecognition
#to use miscrophone
pip install PyAudio
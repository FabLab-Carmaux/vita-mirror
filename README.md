# mopa


#install dep
apt-get update
apt-get upgrade -y
sudo apt-get install libttspico-utils sudo apt-get install libttspico-utils


#sphinxbase install

cd /tmp
wget -q -O sphinxbase-5prealpha.tar.gz https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download
tar -xzf sphinxbase-5prealpha.tar.gz
cd sphinxbase-5prealpha
./configure --enable-fixed
make 
sudo make install


#pocketsphinx install

cd /tmp
wget -q -O pocketsphinx-5prealpha.tar.gz wget https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download
tar -xzf pocketsphinx-5prealpha.tar.gz
cd pocketsphinx-5prealpha
./configure
make 
sudo make install

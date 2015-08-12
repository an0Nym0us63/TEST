sudo pip install flask
sudo pip install RPi.GPIO
sudo apt-get install mplayer
sudo apt-get install libav-tools
sudo dpkg -i pico_build/libttspico-data_1.0+git20110131-2_all.deb
sudo dpkg -i pico_build/libttspico0_1.0+git20110131-2_armhf.deb
sudo dpkg -i pico_build/libttspico-utils_1.0+git20110131-2_armhf.deb
sudo amixer set Master 85%
sudo amixer set Headphone 85%
sudo amixer set PCM 85%
chmod +x run_server.sh

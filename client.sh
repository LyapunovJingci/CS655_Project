#!/usr/bin/env bash
sudo apt-get update
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3-pip
sudo python3.7 -m pip install pip
sudo python3.7 -m pip install scikit-image
sudo python3.7 -m pip uninstall scipy
sudo python3.7 -m pip install scipy==1.2.2
sudo python3.7 -m pip install --upgrade pip
sudo python3.7 -m pip install opencv-python==4.4.0.46
sudo python3.7 -m pip install numpy==1.19.4
sudo python3.7 -m pip install flask
sudo apt-get install apache2
cd /var/www/html
sudo wget https://github.com/LyapunovJingci/CS655_Project/blob/main/index.html
sudo mkdir cgi-enabled
sudo chmod 777 cgi-enabled
cd cgi-enabled
sudo wget https://github.com/LyapunovJingci/CS655_Project/blob/main/CGI_Client.py
sudo chmod 777 CGI_Client.py
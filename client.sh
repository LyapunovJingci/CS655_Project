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
sudo mkdir -p /users/geni
cd /users/geni
sudo git clone https://github.com/LyapunovJingci/CS655_Project.git
cd CS655_Project
python3.7 client.py
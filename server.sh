#!/usr/bin/env bash
sudo apt-get update
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3-pip
sudo python3.7 -m pip install --upgrade --force pip
sudo python3.7 -m pip install setuptools==33.1.1
sudo python3.7 -m pip install pip
sudo python3.7 -m pip install numpy==1.19.4
sudo python3.7 -m pip install cmake
sudo python3.7 -m pip install boost
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
sudo python3.7 -m pip install dlib -vvv
sudo python3.7 -m pip install face_recognition
sudo mkdir -p /users/geni
cd /users/geni
sudo git clone https://github.com/LyapunovJingci/CS655_Project.git
cd CS655_Project
python3.7 server.py

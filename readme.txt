psql -U postgres -hlocalhost -c "CREATE DATABASE wialon_message_bot"

#pip3
apt-get install python3-pip

#install python3.6
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

#pip3 install virtualenv

#create venv
virtualenv --python=/usr/bin/python venv
virtualenv venv
source venv/bin/activate
deactivate

#save packages in requirements.txt
pip3 freeze > requirements.txt

#install packages from requirements.txt
pip3 install -r requirements.txt

supervisorctl update

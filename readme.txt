psql -U postgres -hlocalhost -c "CREATE DATABASE wialon_message_bot"


#create venv
virtualenv --python=/usr/bin/python
virtualenv venv
source venv/bin/activate
deactivate

#save packages in requirements.txt
pip3 freeze > requirements.txt

#install packages from requirements.txt
pip3 install -r requirements.txt

supervisorctl update

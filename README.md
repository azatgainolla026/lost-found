clone repository
git clone https://github.com/azatgainolla026/lost-found.git

cd lostandfound

python -m venv venv #to create venv

source venv/bin/activate  # Для macOS/Linux

venv\Scripts\activate  # Для Windows

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

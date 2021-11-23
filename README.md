This is a Dynamic Web Application build using Django and Travello theme.

python -m venv test
test\Scripts\activate.bat
pip install -r requirements.txt
PostgreSQL DB:- travello | postgres | postgres
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
login into localhost:8000/admin
Create 3 destinations
localhost:8000

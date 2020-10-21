pip3 install mysqlclient

python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser --email admin@example.com --username admin
Password: jiffy@123



================================
API
================================
1. list of all author
   ------------------
   http://localhost:8000/authorsapi/
    or
   http://localhost:8000/bookapi/authors/


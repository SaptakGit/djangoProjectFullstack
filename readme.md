https://docs.chaicode.com/getting-started-with-django/

python -m venv .venv
UV extremely fast package manager
process1:  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" --working
process2:  pip install uv --not working
uv venv
.venv\Scripts\activate
deactivate
up pip install Django
django-admin startproject chaiaurDjango
cd chaiaurDjango
python manage.py runserver
python manage.py startapp
uv pip install django-tailwind/  pip install django-tailwind
uv pip install 'django-tailwind[reload]'/ pip install 'django-tailwind[reload]'

python  -m pip install --upgrade / python  -m ensurepip --upgrade

python manage.py tailwind init
python manage.py tailwind install

new terminal for tailwind:
python manage.py tailwind start

python manage.py migrate

python manage.py createsuperuser
python manage.py changepassword <user name>

python -m pip install Pillow

python manage.py makemigrations chai 
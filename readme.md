## run application

~/projects/python$ source djvenv/bin/activate
cd samapi/

python3 manage.py runserver 8080

## Migration script

python3 manage.py makemigrations

## in production

python3 manage.py migrate

## in production for swagger

python3 manage.py collectstatic

## to install the requirements

pip install -r requirements.txt

## Batch Command to update in github

git add .
git commit -m "structure updated"
git push origin main

## Batch Command to pull in server

git stash
git pull origin main
sudo systemctl restart eqapi

git stash
git pull origin main
python3 manage.py migrate
sudo systemctl restart eqapi
sudo rm logs/\*

## Command to pull to production from github

git pull origin main

sudo systemctl restart nginx
sudo supervisorctl restart all

os user pass: qazwsx!@#

## view the Swagger or ReDoc documentation

http://127.0.0.1:8000/swagger/ or
http://127.0.0.1:8000/redoc/

## re-publish to production

qazwsx!@#

sudo -u postgres psql

\c examquestdb;

DROP DATABASE examquestdb;
CREATE DATABASE examquestdb;

git stash
git pull origin main

python3 manage.py migrate

sudo rm -r staticfiles/
python3 manage.py collectstatic

sudo systemctl restart eqapi

# restore database from backup

sudo -u postgres pg_restore -d examquestdb -Fc --verbose /home/ubuntu/examquestapi/backups/examquestdb.dump

# create user and grant permission

CREATE USER examquestdbuser WITH PASSWORD 'examquest12345';
ALTER DATABASE examquestdb OWNER TO examquestdbuser;

GRANT ALL PRIVILEGES ON DATABASE examquestdb TO examquestdbuser;

GRANT CREATE ON SCHEMA public TO examquestdbuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO examquestdbuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO examquestdbuser;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT ALL ON TABLES TO examquestdbuser;

## to drop a table manually

psql -U examquestdbuser -d examquestdb

\c examquestdb;

DROP TABLE app_auditlog CASCADE;

DROP TABLE app_usersev;

update app_software set publisher=null;

# truncate log and view log

truncate -s 0 logs/error.log
truncate -s 0 logs/info.log

cat logs/error.log
cat logs/info.log

# for windows

psql -U postgres
password: postgres_1234%

## oAuth 2.0

super user: admin
password: admin_1234%
Client ID: SFXWoZ8MQnmkb38bOP63n0TQKZ0zj4RusTMIwanb
Client Secret: pbkdf2_sha256$870000$PaP62lI624M5X4nfnTWHqm$nfUYLU+De0FbsviDkMEsIB5HMPI4V+/q5f68800dcY8=

python manage.py createsuperuser
python3 manage.py shell

---

from oauth2_provider.models import Application
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(email="admin@autonoming.com")

app = Application.objects.create(
name="ProcureLogic", # The name of your app
client_type=Application.CLIENT_CONFIDENTIAL, # Confidential application (use CLIENT_PUBLIC for public apps)
authorization_grant_type=Application.GRANT_PASSWORD, # Password grant type for OAuth2
user=user # Assign the superuser or another user
)

print(f"Client ID: {app.client_id}")
print(f"Client Secret: {app.client_secret}")

> > > print(f"Client ID: {app.client_id}")
> > > Client ID: sKP68z6NM4oxzJjBzYvN6DMahkZuVq1drs2LzMZ1
> > > print(f"Client Secret: {app.client_secret}")
> > > Client Secret: pbkdf2_sha256$870000$KFd8w4MB0fY1a9x1xNU5Lo$YHTsHNxCXc6IbLqk38u5QHCt8g9AFvFAgEUwtn4L7T0=

## run application

~/projects/python$ source djvenv/bin/activate
cd exam_quest_api/

python3 manage.py runserver 8080

## Migration script

python3 manage.py makemigrations

## in production

python3 manage.py migrate

## in production for swagger

python3 manage.py collectstatic

## Batch Command to update in github

git add .
git commit -m "structure update, db changed"
git push origin main

## Command to pull to production from github

git pull origin main

sudo systemctl restart nginx
sudo supervisorctl restart all

erpnext user pass: qazwsx!@#

echo "###################Gunicorn Process Start #####################"
echo $PWD
echo "Requeriments Install By Pip Start"
pip install -r app/requirements.txt
echo "Requeriments Install By Pip Success"
echo "Pip Complete"
python3 app/manage.py makemigrations
python3 app/manage.py migrate
python3 app/manage.py collectstatic --no-input
sudo cp -rf gunicorn.socket /etc/systemd/system/
sudo cp -rf gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
# source env/bin/activate
echo "############### Gunicorn Setup Done ############"
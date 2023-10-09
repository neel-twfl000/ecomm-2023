echo "###################Gunicorn Process Start #####################"
# echo $PWD
# echo "Requeriments Install By Pip Start"
pip install -r app/requirements.txt
# python3 app/manage.py makemigrations
# python3 app/manage.py migrate
# python3 app/seed.py
python3 app/manage.py collectstatic --no-input
# sudo cp -rf jenkins/gunicorn/ecom.socket /etc/systemd/system/
# sudo cp -rf jenkins/gunicorn/ecom.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ecom
sudo systemctl start ecom
sudo systemctl status ecom
# source env/bin/activate
echo "############### Gunicorn Setup Done ############"
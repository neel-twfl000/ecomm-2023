sudo nginx -t
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl status nginx
echo "############################# SETUP COMPLETE #############################################"
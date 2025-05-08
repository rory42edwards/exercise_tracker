#!/bin/bash
set -e

echo "Installing systemd units..."

echo "Changing gunicorn_config daemon mode to False..."
sed -i 's/True/False/' gunicorn_config.py

sudo cp systemd/*.service /etc/systemd/system/
sudo cp systemd/*.target /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable repdojo.target

echo "Done. Use 'systemctl start repdojo.target' to start all services."

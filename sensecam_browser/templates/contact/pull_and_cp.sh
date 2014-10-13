#!/bin/bash
while true
do
	git pull
	cp -r ./* /var/www/sensecam_browser/sensecam_browser/templates/contact/
	sudo cp -r /var/www/sensecam_browser/sensecam_browser/templates/contact /home/git/www/sensecam_browser/sensecam_browser/templates/
    sleep 1 
done


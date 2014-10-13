#!/bin/bash
while true
do
	git add main_content.html 
	git commit -m "Bechy Change Main Content"
	git push -u origin master
	sleep 1 
done

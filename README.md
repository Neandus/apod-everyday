# apod-everyday

Brief:
Download a new photo from Astronomy Picture of the Day every day, store it in the database and set it as wallpaper. Finally, automate everything with Apache Airflow. 

Detailed: (action plan)

* Download the relevant picture from Astronomy Picture of the Day every day, store all pictures in the database.
* Sync with all previous photos.
* If the APoD content of that day (or sometime in history) is a movie, skip it and randomly select today's wallpaper.
* If the new photo has not arrived yet, but 24 hours have passed, shorten the time to the next sync.
* If there is more than one photo available on a given day, select one with a higher resolution.
* If the image resolution is low (unacceptable), skip this day.
* Find a way to mark a missed day to sync ... maybe fill the image data with a random image from another day?
* Automate work as a DAG in Apache Airflow. 

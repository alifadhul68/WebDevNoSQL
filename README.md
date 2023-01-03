# Hotel's Hub
Welcome to Hotel's Hub, the premier online destination for hotel reviews!

With Hotel's Hub, you can read reviews from real travelers about hotels all over the world, and write your own reviews to help others plan their travels. Our website is easy to use and constantly updated with the latest reviews, so you can find the best hotel for your next trip.
The website is built using:
- Django / Python
- HTML
- Bootstrap
- CSS
- Javascript
- MongoDB


## Dependencies
- Python 3.11.1 [Download](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)
- MongoDB Server 6.0.3 [Download](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.3-signed.msi)



## Installing venv
Run the following command in cmd:
```
python -m pip install virtualenv
```

## Preparing the virtual environment and installing the requirements
Download this project and extract it. Then enter these commands:
```
cd /path/to/extracted/folder
python -m venv myenv
myenv\Scripts\activate.bat
python -m pip install -r requirements.txt
```
After running all of these commands the virtual environment is now ready to run the django server.

## Running the server
Before running the server it is mandatory need to migrate the models into the MongoDB server by changing the directory to the extracted path then running these commands:
```
cd hotel_hub
python manage.py makemigrations
python manage.py migrate
```
After migrating the changes to the database. Run the server by using the following command:
```
python manage.py runserver
```
Now the server should be up and running. It can be accessed by entering the localhost link:
```
http://127.0.0.1:8000/
```

## Creating the superuser
In order to access the admin site. A superuser must be created first. The superuser is created by using this command:
```
python manage.py createsuperuser
```
This will prompt you to enter username, email and password for the superuser. After creating the superuser. The admin site can be accessed by entering this link:
```
http://127.0.0.1:8000/admin
```

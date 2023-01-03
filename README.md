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
- MongoDB Server 6.0.3 [Download](https://repo.mongodb.org/yum/amazon/2/mongodb-org/6.0/x86_64/RPMS/mongodb-org-server-6.0.3-1.amzn2.x86_64.rpm)



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

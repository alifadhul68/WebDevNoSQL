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

## Populating the database with sample data
In order to properly test the website functionalities you can populate the database with sample data. First run the django project shell by using this command:
```
python manage.py shell
```
After running the shell. Paste the following script:
```
from hotels.models import Hotel
from reviews.models import Review
import random
import datetime
import lorem

# Create the hotels and save them to the database
hotels = [    Hotel(title='The Ritz', city='London', description='Luxury hotel in the heart of London'),    Hotel(title='The Grand Hotel', city='Paris', description='Luxury hotel in the heart of Paris'),    Hotel(title='The Plaza', city='New York', description='Luxury hotel in the heart of New York City'),    Hotel(title='The Grand Hyatt', city='Tokyo', description='Luxury hotel in the heart of Tokyo'),    Hotel(title='The Mandarin Oriental', city='Bangkok', description='Luxury hotel in the heart of Bangkok'),    Hotel(title='The Four Seasons', city='Sydney', description='Luxury hotel in the heart of Sydney'),    Hotel(title='The Ritz-Carlton', city='Dubai', description='Luxury hotel in the heart of Dubai'),    Hotel(title='The Fairmont', city='San Francisco', description='Luxury hotel in the heart of San Francisco'),    Hotel(title='The InterContinental', city='Hong Kong', description='Luxury hotel in the heart of Hong Kong'),]
Hotel.objects.bulk_create(hotels)
hotel_titles = [    'The Ritz', 'The Grand Hotel', 'The Plaza', 'The Grand Hyatt',    'The Mandarin Oriental', 'The Four Seasons', 'The Ritz-Carlton',    'The Fairmont', 'The InterContinental']
# Create the reviews
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Gary', 'Hannah']

for title in hotel_titles:
    hotel = Hotel.objects.get(title=title)
    for i in range(5):
        user = random.choice(names)
        comment = lorem.paragraph()
        rating = random.randint(1, 5)
        days_offset = random.randint(0, 7)
        publish_date = datetime.datetime.now() - datetime.timedelta(days=days_offset)
        review = Review(hotel=hotel, user=user, comment=comment, rating=rating, publish_date=publish_date)
        review.save()
```
Now you can exit the shell and run the server to see the changes.

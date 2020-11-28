# Raahi - A Hotel Booking e-Travel Web Platform

Project towards the fulfillment of credits for Advanced Programming [CS-1202] | Monsoon 2020 | Ashoka University

***

**Branch** `main` **is the latest version**

**IMPORTANT**

This project was made with **Python 3.8.4**. While it might run on other versions of python, we can not guarantee it. While testing, we ran into issues with Python 3.9 when installing dependencies for the project, and there is no guarantee it will work in versions older than 3.8.4 either. To avoid running into any errors, we strongly recommend that you **completely uninstall your current version of Python and install v. 3.8.4. (13 July 2020 release)**

If you are on Windows, download Python 3.8.4 64-bit from this link. (https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe) 
While installing, make sure to install it for all users, install all components, and select the **add to PATH** option. 

***

**Steps to run:**

1. Clone/pull/download this repository
2. Install the virtualenv package with `pip install virtualenv`
3. Navigate to the root directory of this repository in terminal or command prompt and create a virtualenv with `virtualenv env` 
4. Activate the virtualenv with `env\scripts\activate` on Windows OR `source env/bin/activate` on Mac/Linux 
5. Install dependencies with `pip install -r requirements.txt`
6. Run server with `python manage.py runserver`

***

**Features:**
- Authentication - Signup, Login, Logout
- View and edit User Profile
- Change Password
- View all available hotels on the **Browse Hotels** page
- Search for a hotel by its name, or by city
- Filter Hotels by Price floor and ceiling
- View additional details for the hotel
- See ratings and reviews by other users for the hotel
- Leave a rating and a review for a hotel
- Book hotel with Check In and Check Out Date, number of people and number of rooms (Price = Rooms x Cost per room)
- View all reservations made in the User Profile page
- Cancel Reservations made in the User Profile page

***

**Known bugs:**

- Bug 1
- Bug 2

***


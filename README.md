# Awwwards
This is an application where users can showcase their projects.

## Author
Stephen Remmi


## Description
This is an application that allows users to showcase their projects. Other users can view all the projects posted, vote on them based on the design, usability and the content. Users are also able to view each others profile details and even search for specific projects.

## User Story
User can sign in to the application to start using.
Users can view all projects posted.
User can upload pictures to the application as profile image and also project landing page image.
User can view each others profile details.
User can leave a comment after reviewing a project.

# Display of working demo
https://user-images.githubusercontent.com/61972580/87776806-07eac300-c831-11ea-8aa1-4d11244600b3.png

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: rs are also able to view each others profile details and even search for specific projects.
    * **`pip install django`**
* This project requires you to have a secret key from Uploadcare to facilitate cloud storage of uploaded images.
    * The secret key can be gotten by creating a free uploadcare account, starting a new project and navigating to the dashboard
    * The key should be stored as an enviremnetal variable in an .env file as hown below
        * **`SECRET=<your secret key here>`**
    * More info onhow to use the Django pyuploadcare library can be found [here](https://uploadcare.com/docs/guides/django/)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Stephenremmi/awwwards-clone.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.


# Known Bugs
* Search functionality is buggy, fix coming soon

# Versioning
* Version 2 is set to include a vote and like functionality for rating the projects

## Technologies Used
* Python 3.6.9
* Bootstrap3
* Heroku
* HTML5
* CSS3
* Django3.8
* Font awesome
* Google Fonts

## Support and contact details
For more information, questions, or help using the program, get in touch with me via email @stephenremmi@gmail.com

## [License](https://github.com/Stephenremmi/awwwards-clone/blob/master/LICENSE)
MIT Copyright (c) 2020 Stephen Remmi

<!-- ABOUT THE PROJECT -->
##  About The Project
AASHA: A hope to Find your Loved one (Django-based Missing Persons Identification Project)
===================================================

![Screenshot](Screenshot (162).png)

This project is a web-based application for identifying missing persons using state-of-the-art deep learning models like SFace, ArcFace etc. trained on [MLFW: A Database for Face Recognition on Masked Faces](https://paperswithcode.com/paper/mlfw-a-database-for-face-recognition-on) . It also used latest loss function like Quality Adaptive Margin. It allows users to upload images of missing persons, which are then compared to a database of images using advanced facial recognition technology to help identify them.




###  Built With
To achieve the goal of finding missing people, I made use of the following tools and languages,
<p align="left">
<a  href="https://getbootstrap.com"  target="_blank"><img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg"  alt="bootstrap"  width="40"  height="40"/> </a>
<a  href="https://www.w3schools.com/css/"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"  alt="css3"  width="40"  height="40"/> </a>
<a  href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"  alt="javascript"  width="40"  height="40"/> </a>
<a  href="https://www.w3.org/html/"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"  alt="html5"  width="40"  height="40"/> </a>
<a  href="https://www.python.org/"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg"  alt="express"  width="40"  height="40"/> </a>
<a  href="https://www.djangoproject.com/"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg"  alt="express"  width="40"  height="40"/> </a>
<a  href="https://docs.microsoft.com/en-us/azure/cognitive-services/face/"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg"  alt="express"  width="40"  height="40"/> </a>
<a  href="https://www.sqlite.org/index.html"  target="_blank"> <img  src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg"  alt="express"  width="40"  height="40"/> </a>
<a  href="https://git-scm.com/"  target="_blank"> <img  src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg"  alt="git"  width="40"  height="40"/> </a>
<a  href="https://heroku.com"  target="_blank"> <img  src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg"  alt="heroku"  width="40"  height="40"/> </a>
<p align="right">(<a  href="#top">back to top</a>)</p>


![Demo](adaface_demo5.gif)
The demo shows a comparison between AdaFace and ArcFace on a live video.
<!-- GETTING STARTED -->


Table of Contents
-----------------

-   [Installation](#installation)
-   [Usage](#usage)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Contributing](#contributing)
-   [License](#license)

Installation
------------

To use this project, you need to have Python and Django installed on your machine.

1.  Clone this repository onto your machine: `git clone https://github.com/SameetSaurav/AASHA-website/tree/master.git`.
2.  Navigate to the project directory: `cd AASHA-website`.
3.  Install the dependencies: `pip install -r requirements.txt`.

Usage
-----

To start the Django server, run the following command in your terminal:

Copy code

`python manage.py runserver`

You can then navigate to the URL provided in the terminal to use the application.

Features
--------

-   User authentication: The application requires users to create an account and log in before they can upload images or view the database of missing persons.
-   Image uploading: Users can upload images of missing persons, which are then added to the database and compared to existing images using deep learning algorithms.
-   Facial recognition: The application uses state-of-the-art deep learning algorithms to compare uploaded images to a database of images to help identify missing persons using SOTA DeepLearning Models.
-   Database management: The application includes a database management system that allows administrators to add, edit, and delete images and information about missing persons.
-   Centralized Governance

Technologies Used
-----------------

-   Python
-   Django
-   TensorFlow
-   OpenCV
-   SQLite
-   HTML/CSS
-   JavaScript

Contributing
------------

If you would like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch: `git checkout -b your-branch-name`.
3.  Make your changes and commit them: `git commit -m 'Your commit message'`.
4.  Push to the branch: `git push origin your-branch-name`.
5.  Submit a pull request.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for details.

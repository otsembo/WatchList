# WatchList Movie Web Application

The project is a simple web application built with the flask micro-framework. The application consumes TheMovieDB api, it lists movie details and allows for one to make movie reviews.

The web application is deployed on Heroku. Find the application on the following link: https://otsembo-watchlist-flask.herokuapp.com/

Requirements
------------

- This application requires python3.6 to run.

Installation
------------

To install the project, you need to clone the application to your local machine.

- On your git cli run the following command:

    git clone https://github.com/otsembo/WatchList.git

After cloning the project, you need to set it up:

- Set up virtual environment in your project directory

    $python -m venv virtual

- Activate the environment

    $source virtual/bin/activate

- Once activated you need to reinstall the project dependencies

    $pip install - requirements.txt

- Next you need to locate your api key from <a href="https://www.themoviedb.org/documentation/api">The Movie DB</a>

- Finally, open instance/config.py and add your api key.

Screenshots
-----------

Your app will look something like this:

![alt text](https://github.com/otsembo/WatchList/blob/master/image.jpg?raw=true)
# SMART CNAM


This web application is built using the **[Python Flask Framework](https://palletsprojects.com/p/flask/)** and **[SB Admin 2 Theme (Free version)](https://startbootstrap.com/themes/sb-admin-2/)**
Welcome to Smart CNAM , an old data science project developed for my final year study project 2021. This project aims to predict the number of sick people with chronic diseases in Tunisia. 

## Features

- MongoDB database
- Session-Based authentication (Login and Register)
- SMTP Integration
- Gunicorn Deployment script
- **MIT License**
- SB Admin 2 Dashboard Theme
- Illustration from [Undraw.co](https://undraw.co/)
- Support

### Prerequisites

- Python >= 3.5
- Pip, Virtualenv
- MongoDb Database
- SMTP Relay (Gmail, Sendgrid)

### Installing

Follow the steps below to install the application

```bash
$ git clone 
$ cd flask-admin-boilerplate
$
$ virtualenv env
$ source env/bin/activate
$ 
$ # Install requirements
$ pip install -r requirements.txt

```

### Make sure you configure the SMTP and Mongodb Database before running the application
Navigate to __init__.py under the configurations folder to configure your database and SMTP

### Running the application

After installing all the requirements and ensuring that the configurations are done correctly, run the app.

```bash
$ # Run the application
$ python app.py
```

## Deployment

This web application has the basic configuration for deployment with Gunicorn. Makes it easy for the application to be deployed on Heroku.


## License

This project is licensed under the MIT License


## Acknowledgement

* [Python Flask Framework](https://palletsprojects.com/p/flask/) - The web framework used
* [SB Admin 2 Theme (Free version)](https://startbootstrap.com/themes/sb-admin-2/) - The UI theme used

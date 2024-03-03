from app import app
import urllib
import os

# secret key for user session
app.secret_key = "x19OKtsyXj"

#setting up mail
app.config['MAIL_SERVER']='smtp.gmail.com' #mail server
app.config['MAIL_PORT'] = 465 #mail port
app.config['MAIL_USERNAME'] = 'smart.cnam@gmail.com' #email
app.config['MAIL_PASSWORD'] = 'acerm6612'
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = True #security type

#database connection parameters
connection_params = {
    'user': 'Sadmin',
    'password': 'pass123456',
    'host': '127.0.0.1',
    'port': '27017',
    'namespace': '',
}

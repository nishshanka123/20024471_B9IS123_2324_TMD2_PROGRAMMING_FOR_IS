###############################################################################
# __init__.py is the entry point of the flask application, it is the application 
# factory, also this initilizes the package if it is in the package folder (flaskr)
# __init__: A special method used for initializing objects (e.g., __init__() in classes)
###############################################################################

# import the necessory packages
import os
from flask import Flask

# Create and configure the app
# instance_relative_config is a configuraton option available in Flask, if this is True
# Flask will load the configuration from the instance folder availble in the relative path

def createApp(test_config=None):
  application = Flask(__name__, instance_relative_config=True)
  application.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.join(application.instance_path, 'flaskr.sqlite'),
  )

  if test_config is None:
    # load the test config from instance if it is exists when not testing
    application.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if it is passed in
    application.config.from_mapping(test_config)
  
  #ensure the existance of instance folder
  try:
    os.makedirs(application.instance_path)
  except OSError as ex:
    pass

  # page to deploy
  @application.route('/welcome')
  def welcome():
    data = "<h1>Welcome to the jungle....!</h1><br>"
    data += "<p> application name : " + __name__ + "<br>"
    data += "Directory name : </p>"
    return data
  
  from . import db
  db.init_app(application)
  
  return application


app = createApp()

if __name__ == "__main__":
 app.run(host='127.0.0.1', port='8080')



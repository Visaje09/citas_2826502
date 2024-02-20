from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from .config import Config

app = Flask(__name__)

##configurar objeto flask 
app.config.from_object(Config) 

##objeto SQLAlchemy 
db = SQLAlchemy(app)

##objeto para hacer migraciones 
migrate = Migrate(app , db)

##importar los modelos
from .models import Medico  

if __name__ == '__main__':
    app.run()
    
    
    
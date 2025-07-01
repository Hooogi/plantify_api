import os
from flask import Flask
from routes.views import views_blueprint

app = Flask(__name__)

# Datenbank-Konfiguration zentral definieren
app.config['DB_CONFIG'] = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_API_READER"),
    "password": os.getenv("DB_API_READER_PW"),
    "database": os.getenv("DB_NAME")
}

# Blueprint für View-Routen registrieren
app.register_blueprint(views_blueprint)

if __name__ == "__main__":
    #später host auf 0.0.0.0 abändern
    app.run(debug=True, host="192.168.56.102", port=5001)
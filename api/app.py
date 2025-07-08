import os
from flask import Flask
from routes.endpoints import endpoints_blueprint
from routes.plots import plots_blueprint

app = Flask(__name__)

# Datenbank-Konfiguration zentral definieren
app.config['DB_CONFIG'] = {
    "host": "192.168.56.102",
    "user": "admin",
    "password": "thws2025",
    "database": "smartplantpot",
}

# Blueprint für View-Routen registrieren
app.register_blueprint(endpoints_blueprint)
app.register_blueprint(plots_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
from flask import Blueprint, jsonify, current_app, request
import mariadb

def get_db_cursor():
    connection = mariadb.connect(**current_app.config['DB_CONFIG'])
    cursor = connection.cursor(dictionary=True)
    return connection, cursor

def fetch_query_results(query, pot_id, fetchone=False):
    connection, cursor = get_db_cursor()
    cursor.execute(query, (pot_id,))
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route("/ping")
def ping():
    return jsonify({"message": "API läuft"})

@views_blueprint.route("/all-today", methods=["GET"])
def get_all_today():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = "SELECT * FROM viw_AllValues_Today WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route("/sunlight-30days", methods=["GET"])
def get_sunlight_30days():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = "SELECT * FROM viw_SunlightPerDay_last30Days WHERE pot_id = %s"
    return fetch_query_results(query, pot_id)

@views_blueprint.route('/latest-value', methods=['GET'])
def get_latest_value():
    pot_id = request.args.get('pot_id', default=1, type=int)
    query = '''
        SELECT created, temperature, air_humidity, soil_moisture
        FROM viw_LatestValuePerPot
        WHERE pot_id = %s
    '''
    return fetch_query_results(query, pot_id, fetchone=True)

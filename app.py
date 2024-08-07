from flask import Flask
from flask_cors import CORS

from db_manager import fetch_data

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/activites/api/v1.0/all')
def get_all_activites():
    garmin_activites_db_path = './db/garmin_activities.db'
    query_all_activites = "SELECT * FROM activities"
    all_activites_data = fetch_data(garmin_activites_db_path, query_all_activites)
    return all_activites_data

@app.route('/hr/api/v1.0/all')
def get_all_hr():
    garmin_monitoring_db_path = './db/garmin_monitoring.db'
    query_all_hr = "SELECT * FROM monitoring_hr"
    all_hr_data = fetch_data(garmin_monitoring_db_path, query_all_hr)
    return all_hr_data

@app.route('/weight/api/v1.0/all')
def get_all_weight():
    garmin_db_path = './db/garmin.db'
    query_all_weight = 'SELECT * FROM weight'
    all_weight_data = fetch_data(garmin_db_path, query_all_weight)
    return all_weight_data

@app.route('/steps/api/v1.0/all')
def get_all_steps():
    summary_db_path = './db/summary.db'
    query_all_steps = 'SELECT * FROM days_summary'
    all_steps_data = fetch_data(summary_db_path, query_all_steps)
    return all_steps_data

if __name__ == '__main__':
    app.run(debug=True)
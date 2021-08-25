import os
import json
import datetime
from flask import Flask, request, jsonify, Response
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin

from api.models import *

app = Flask(__name__)
cors = CORS(app)

app.config['MONGODB_DB'] = os.environ['MONGODB_DATABASE']
app.config['MONGODB_HOST'] = os.environ['MONGODB_HOST_IP']
app.config['MONGODB_PORT'] = 27017

db.init_app(app)

@app.route('/calibSeries', methods=['POST'])
def get_calib_series():
    record = request.get_json()

    sqtp = record['seq_calib_touch_probe']
    sck = record['seq_calib_kinemat']
    calib_series =  CalibSeries(
                        created_at = datetime.datetime.now,
                        calib_date = convert_to_iso_date(record['calib_date']),
                        mc_name = record['mc_name'],
                        mc_serial = record['mc_serial'],
                        mc_cycle_no = record['mc_cycle_no'],
                        tech_set = record['tech_set'],
                        sphere_dia = record['sphere_dia'],
                        only_check = record['only_check'],
                        cycle_end_status = record['cycle_end_status'],
                        cycle_process_time = record['cycle_process_time'],
                        seq_calib_touch_probe = dict(
                            tol_status = sqtp['tol_status'],
                            meas_val_old_length = sqtp['meas_val_old_length'],
                            meas_val_new_length = sqtp['meas_val_new_length'],
                            meas_val_dev_length = sqtp['meas_val_dev_length'],
                            meas_val_old_radius = sqtp['meas_val_old_radius'],
                            meas_val_new_radius = sqtp['meas_val_new_radius'],
                            meas_val_dev_radius = sqtp['meas_val_dev_radius'],
                        ),
                        seq_calib_kinemat = dict(
                            tol_status = sck['tol_status'],
                            kinemat_calc_mode = sck['kinemat_calc_mode'],
                            kinemat_lin_name_1 = sck['kinemat_lin_name_1'],
                            kinemat_lin_name_2 = sck['kinemat_lin_name_2'],
                            kinemat_lin_name_3 = sck['kinemat_lin_name_3'],
                            kinemat_lin_name_4 = sck['kinemat_lin_name_4'],
                            kinemat_rot_name_1 = sck['kinemat_rot_name_1'],
                            kinemat_rot_name_2 = sck['kinemat_rot_name_2'],
                            kinemat_rot_name_3 = sck['kinemat_rot_name_3'],
                            kinemat_rot_name_4 = sck['kinemat_rot_name_4'],
                            meas_val_old_lin_1 = sck['meas_val_old_lin_1'],
                            meas_val_new_lin_1 = sck['meas_val_new_lin_1'],
                            meas_val_dev_lin_1 = sck['meas_val_dev_lin_1'],
                            meas_val_old_lin_2 = sck['meas_val_old_lin_2'],
                            meas_val_new_lin_2 = sck['meas_val_new_lin_2'],
                            meas_val_dev_lin_2 = sck['meas_val_dev_lin_2'],
                            meas_val_old_lin_3 = sck['meas_val_old_lin_3'],
                            meas_val_new_lin_3 = sck['meas_val_new_lin_3'],
                            meas_val_dev_lin_3 = sck['meas_val_dev_lin_3'],
                            meas_val_old_lin_4 = sck['meas_val_old_lin_4'],
                            meas_val_new_lin_4 = sck['meas_val_new_lin_4'],
                            meas_val_dev_lin_4 = sck['meas_val_dev_lin_4'],
                            meas_val_old_rot_1 = sck['meas_val_old_rot_1'],
                            meas_val_new_rot_1 = sck['meas_val_new_rot_1'],
                            meas_val_dev_rot_1 = sck['meas_val_dev_rot_1'],
                            meas_val_old_rot_2 = sck['meas_val_old_rot_2'],
                            meas_val_new_rot_2 = sck['meas_val_new_rot_2'],
                            meas_val_dev_rot_2 = sck['meas_val_dev_rot_2'],
                            meas_val_old_rot_3 = sck['meas_val_old_rot_3'],
                            meas_val_new_rot_3 = sck['meas_val_new_rot_3'],
                            meas_val_dev_rot_3 = sck['meas_val_dev_rot_3'],
                            meas_val_old_rot_4 = sck['meas_val_old_rot_4'],
                            meas_val_new_rot_4 = sck['meas_val_new_rot_4'],
                            meas_val_dev_rot_4 = sck['meas_val_dev_rot_4'],
                        )
                    )

    calib_series.save()
    return jsonify(calib_series.to_json())


@app.route('/allCalibSeries', methods=['GET'])
@cross_origin()
def query_calib_series():
    generic = request.args.get('generic', default=False, type=bool)
    number_of_items = request.args.get('items', default=None, type=int)

    calib_series = CalibSeries.objects().order_by('calib_date')
    if number_of_items == None:
        calib_series_partion = calib_series
    else:
        calib_series_partion = calib_series[:number_of_items]

    all_data = []
    for cs in calib_series_partion:
        all_data.append((cs.to_json(generic)))

    return jsonify(all_data)


@app.route('/allMachines', methods=['GET'])
@cross_origin()
def query_all_machines():
    calib_series = CalibSeries.objects().order_by('calib_date')

    mc_serials = []
    mc_names = []
    for cs in calib_series:
        if cs.mc_serial not in mc_serials:
            mc_serials.append(cs.mc_serial)
            mc_names.append(cs.mc_name)

    all_data = []
    for i in range(len(mc_serials)):
        d = {'mc_serial': mc_serials[i], 'mc_name': mc_names[i]}
        all_data.append(d)

    return jsonify(all_data)


@app.route('/calibSeries/<date>', methods=['GET'])
@cross_origin()
def query_calib_series_generic_by_calib_date(date=None):
    generic = request.args.get('generic', default=False, type=bool)
    date_db = date.replace('T', ' ').replace('.000Z', '')
    calib_data = CalibSeries.objects(calib_date=date_db).first()

    if not calib_data:
        return jsonify({'error': 'data not found'}), 400
    else:
        return jsonify(calib_data.to_json(generic))



@app.route('/hello', methods=['GET'])
@cross_origin()
def query_hello_from_rest():
    return {'answer': 'hello from rest'}


if __name__ == "__main__":
    app.run(debug=True)
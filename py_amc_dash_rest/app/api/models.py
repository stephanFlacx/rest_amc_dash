from flask_mongoengine import MongoEngine
import datetime

db = MongoEngine()


class CalibTouchProbeSequence(db.EmbeddedDocument):
    tol_status = db.StringField()
    meas_val_old_length = db.FloatField()
    meas_val_new_length = db.FloatField()
    meas_val_dev_length = db.FloatField()
    meas_val_old_radius = db.FloatField()
    meas_val_new_radius = db.FloatField()
    meas_val_dev_radius = db.FloatField()


    def to_json(self):
        return { 
                'tol_status': self.tol_status, 
                'meas_val_old_length': self.meas_val_old_length,
                'meas_val_new_length': self.meas_val_new_length,
                'meas_val_dev_length': self.meas_val_dev_length,
                'meas_val_old_radius': self.meas_val_old_radius,
                'meas_val_new_radius': self.meas_val_new_radius,
                'meas_val_dev_radius': self.meas_val_dev_radius,
                }


    def to_json_generic(self):
        return { 
                'meas_val_old_1': self.meas_val_old_length,
                'meas_val_new_1': self.meas_val_new_length,
                'meas_val_dev_1': self.meas_val_dev_length,
                'meas_val_old_2': self.meas_val_old_radius,
                'meas_val_new_2': self.meas_val_new_radius,
                'meas_val_dev_2': self.meas_val_dev_radius,
                }


class CalibKinematSequence(db.EmbeddedDocument):
    tol_status = db.StringField()
    kinemat_calc_mode = db.StringField()
    kinemat_lin_name_1 = db.StringField()
    kinemat_lin_name_2 = db.StringField()
    kinemat_lin_name_3 = db.StringField()
    kinemat_lin_name_4 = db.StringField()
    kinemat_rot_name_1 = db.StringField()
    kinemat_rot_name_2 = db.StringField()
    kinemat_rot_name_3 = db.StringField()
    kinemat_rot_name_4 = db.StringField()
    meas_val_old_lin_1 = db.FloatField()
    meas_val_new_lin_1 = db.FloatField()
    meas_val_dev_lin_1 = db.FloatField()
    meas_val_old_lin_2 = db.FloatField()
    meas_val_new_lin_2 = db.FloatField()
    meas_val_dev_lin_2 = db.FloatField()
    meas_val_old_lin_3 = db.FloatField()
    meas_val_new_lin_3 = db.FloatField()
    meas_val_dev_lin_3 = db.FloatField()
    meas_val_old_lin_4 = db.FloatField()
    meas_val_new_lin_4 = db.FloatField()
    meas_val_dev_lin_4 = db.FloatField()
    meas_val_old_rot_1 = db.FloatField()
    meas_val_new_rot_1 = db.FloatField()
    meas_val_dev_rot_1 = db.FloatField()
    meas_val_old_rot_2 = db.FloatField()
    meas_val_new_rot_2 = db.FloatField()
    meas_val_dev_rot_2 = db.FloatField()
    meas_val_old_rot_3 = db.FloatField()
    meas_val_new_rot_3 = db.FloatField()
    meas_val_dev_rot_3 = db.FloatField()
    meas_val_old_rot_4 = db.FloatField()
    meas_val_new_rot_4 = db.FloatField()
    meas_val_dev_rot_4 = db.FloatField()

    def to_json(self):
        return { 
                'tol_status': self.tol_status, 
                'kinemat_lin_name_1': self.kinemat_lin_name_1,
                'kinemat_lin_name_2': self.kinemat_lin_name_2,
                'kinemat_lin_name_3': self.kinemat_lin_name_3,
                'kinemat_lin_name_4': self.kinemat_lin_name_4,
                'kinemat_rot_name_1': self.kinemat_rot_name_1,
                'kinemat_rot_name_2': self.kinemat_rot_name_2,
                'kinemat_rot_name_3': self.kinemat_rot_name_3,
                'kinemat_rot_name_4': self.kinemat_rot_name_4,
                'kinemat_calc_mode': self.kinemat_calc_mode, 
                'meas_val_old_lin_1': self.meas_val_old_lin_1,
                'meas_val_new_lin_1': self.meas_val_new_lin_1,
                'meas_val_dev_lin_1': self.meas_val_dev_lin_1,
                'meas_val_old_lin_2': self.meas_val_old_lin_2,
                'meas_val_new_lin_2': self.meas_val_new_lin_2,
                'meas_val_dev_lin_2': self.meas_val_dev_lin_2,
                'meas_val_old_lin_3': self.meas_val_old_lin_3,
                'meas_val_new_lin_3': self.meas_val_new_lin_3,
                'meas_val_dev_lin_3': self.meas_val_dev_lin_3,
                'meas_val_old_lin_4': self.meas_val_old_lin_4,
                'meas_val_new_lin_4': self.meas_val_new_lin_4,
                'meas_val_dev_lin_4': self.meas_val_dev_lin_4,
                'meas_val_old_rot_1': self.meas_val_old_rot_1,
                'meas_val_new_rot_1': self.meas_val_new_rot_1,
                'meas_val_dev_rot_1': self.meas_val_dev_rot_1,
                'meas_val_old_rot_2': self.meas_val_old_rot_2,
                'meas_val_new_rot_2': self.meas_val_new_rot_2,
                'meas_val_dev_rot_2': self.meas_val_dev_rot_2,
                'meas_val_old_rot_3': self.meas_val_old_rot_3,
                'meas_val_new_rot_3': self.meas_val_new_rot_3,
                'meas_val_dev_rot_3': self.meas_val_dev_rot_3,
                'meas_val_old_rot_4': self.meas_val_old_rot_4,
                'meas_val_new_rot_4': self.meas_val_new_rot_4,
                'meas_val_dev_rot_4': self.meas_val_dev_rot_4,
                }

    def to_json_generic(self):
        return {
                'meas_val_old_1': self.meas_val_old_lin_1,
                'meas_val_new_1': self.meas_val_new_lin_1,
                'meas_val_dev_1': self.meas_val_dev_lin_1,
                'meas_val_old_2': self.meas_val_old_lin_2,
                'meas_val_new_2': self.meas_val_new_lin_2,
                'meas_val_dev_2': self.meas_val_dev_lin_2,
                'meas_val_old_3': self.meas_val_old_lin_3,
                'meas_val_new_3': self.meas_val_new_lin_3,
                'meas_val_dev_3': self.meas_val_dev_lin_3,
                'meas_val_old_4': self.meas_val_old_lin_4,
                'meas_val_new_4': self.meas_val_new_lin_4,
                'meas_val_dev_4': self.meas_val_dev_lin_4,
                'meas_val_old_5': self.meas_val_old_rot_1,
                'meas_val_new_5': self.meas_val_new_rot_1,
                'meas_val_dev_5': self.meas_val_dev_rot_1,
                'meas_val_old_6': self.meas_val_old_rot_2,
                'meas_val_new_6': self.meas_val_new_rot_2,
                'meas_val_dev_6': self.meas_val_dev_rot_2,
                'meas_val_old_7': self.meas_val_old_rot_3,
                'meas_val_new_7': self.meas_val_new_rot_3,
                'meas_val_dev_7': self.meas_val_dev_rot_3,
                'meas_val_old_8': self.meas_val_old_rot_4,
                'meas_val_new_8': self.meas_val_new_rot_4,
                'meas_val_dev_8': self.meas_val_dev_rot_4,
                }


class CalibSeries(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now)
    calib_date = db.DateTimeField()
    mc_name = db.StringField()
    mc_serial = db.StringField()
    mc_cycle_no = db.StringField()
    tech_set = db.IntField()
    sphere_dia = db.FloatField()
    only_check = db.BooleanField()
    cycle_end_status = db.StringField()
    cycle_process_time = db.IntField()
    seq_calib_touch_probe = db.EmbeddedDocumentField(CalibTouchProbeSequence)
    seq_calib_kinemat = db.EmbeddedDocumentField(CalibKinematSequence)

    def to_json(self, generic=False):
        if generic:
            return { 
                    'calib_date': convert_date_to_string(self.calib_date),
                    'mc_name': self.mc_name,
                    'mc_serial': self.mc_serial,
                    'mc_cycle_no': self.mc_cycle_no,
                    'tech_set': self.tech_set,
                    'sphere_dia': self.sphere_dia,
                    'only_check': self.only_check,
                    'cycle_end_status': self.cycle_end_status,
                    'cycle_process_time': self.cycle_process_time,
                    'seq_calib_touch_probe': self.seq_calib_touch_probe.to_json_generic(),
                    'seq_calib_kinemat': self.seq_calib_kinemat.to_json_generic(),
                    }

        else:
            return { 
                    'calib_date': convert_date_to_string(self.calib_date),
                    'mc_name': self.mc_name,
                    'mc_serial': self.mc_serial,
                    'mc_cycle_no': self.mc_cycle_no,
                    'tech_set': self.tech_set,
                    'sphere_dia': self.sphere_dia,
                    'only_check': self.only_check,
                    'cycle_end_status': self.cycle_end_status,
                    'cycle_process_time': self.cycle_process_time,
                    'seq_calib_touch_probe': self.seq_calib_touch_probe.to_json(),
                    'seq_calib_kinemat': self.seq_calib_kinemat.to_json(),
                    }


def convert_mc_serial(mc_serial_url):
    mc_serial = mc_serial_url.replace('_', '.')
    return mc_serial


def convert_date_to_string(timestamp):
    date = timestamp.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    return date


def convert_to_iso_date(string_date):
    ls = string_date.split('_')
    date = ls[0]
    time = ls[1]

    ls_date = date.split('-')
    ls_time = time.split('-')

    year = int(ls_date[0])
    month = int(ls_date[1])
    day = int(ls_date[2])

    hour = int(ls_time[0])
    minute = int(ls_time[1])
    second = int(ls_time[2])

    iso_date = datetime.datetime(   year=year, 
                                    month=month, 
                                    day=day, 
                                    hour=hour, 
                                    minute=minute, 
                                    second=second)
    return iso_date


def map_generic_result_table(calib_data):
    new_objects = {}
    for key in calib_data:
        seq_name = 'seq_calib_kinemat'
        if key == seq_name:
            # print(key['meas_val_old_lin_1'])
            new_objects[seq_name] = \
                map_generic_result_table_kinemat(calib_data[key])

    for key in new_objects:
        if key in calib_data:
            calib_data[key] = new_objects[key]
    # print(calib_data)


def map_generic_result_table_kinemat(item):
    return dict(
            meas_val_old_1 = item['meas_val_old_lin_1'],
            meas_val_new_1 = item['meas_val_new_lin_1'],
            meas_val_dev_1 = item['meas_val_dev_lin_1'],
            meas_val_old_2 = item['meas_val_old_lin_2'],
            meas_val_new_2 = item['meas_val_new_lin_2'],
            meas_val_dev_2 = item['meas_val_dev_lin_2'],
            meas_val_old_3 = item['meas_val_old_lin_3'],
            meas_val_new_3 = item['meas_val_new_lin_3'],
            meas_val_dev_3 = item['meas_val_dev_lin_3'],
            meas_val_old_4 = item['meas_val_old_lin_4'],
            meas_val_new_4 = item['meas_val_new_lin_4'],
            meas_val_dev_4 = item['meas_val_dev_lin_4'],
            meas_val_old_5 = item['meas_val_old_rot_1'],
            meas_val_new_5 = item['meas_val_new_rot_1'],
            meas_val_dev_5 = item['meas_val_dev_rot_1'],
            meas_val_old_6 = item['meas_val_old_rot_2'],
            meas_val_new_6 = item['meas_val_new_rot_2'],
            meas_val_dev_6 = item['meas_val_dev_rot_2'],
            meas_val_old_7 = item['meas_val_old_rot_3'],
            meas_val_new_7 = item['meas_val_new_rot_3'],
            meas_val_dev_7 = item['meas_val_dev_rot_3'],
            meas_val_old_8 = item['meas_val_old_rot_4'],
            meas_val_new_8 = item['meas_val_new_rot_4'],
            meas_val_dev_8 = item['meas_val_dev_rot_4'],
            )
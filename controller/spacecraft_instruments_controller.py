from flask import Blueprint, request, jsonify

from service.apollo_service import apollo_service

spacecraft_instruments_controller = Blueprint('spacecraft_instruments_controller', __name__)


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/location',
                                         methods=['GET', 'POST'])
def location_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_location_reading_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                    request.args['location'],
                                                                    request.args['location_unit'],
                                                                    request.args['reading_time'])
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_location_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                             request.args['pageSize'],
                                                                             request.args['pageState'])

        return jsonify(pageSize=request.args['pageSize'], pageState=result.paging_state, data=result.current_rows), 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/pressure',
                                         methods=['GET', 'POST'])
def pressure_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_pressure_reading_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                    request.args['pressure'],
                                                                    request.args['pressure_unit'],
                                                                    request.args['reading_time'])
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_pressure_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                             request.args['pageSize'],
                                                                             request.args['pageState'])

        return jsonify(pageSize=request.args['pageSize'], pageState=result.paging_state, data=result.current_rows), 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/speed',
                                         methods=['GET', 'POST'])
def speed_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_speed_reading_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                 request.args['speed'],
                                                                 request.args['speed_unit'],
                                                                 request.args['reading_time'])
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_speed_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                          request.args['pageSize'],
                                                                          request.args.get('pageState', None))

        return jsonify(pageSize=request.args['pageSize'], pageState=result.paging_state, data=result.current_rows), 200


@spacecraft_instruments_controller.route('/api/spacecraft/<spacecraft_name>/<journey_id>/instruments/temperature',
                                         methods=['GET', 'POST'])
def temperature_reading_for_spacecraft_journey(spacecraft_name, journey_id):
    if request.method == 'POST':
        apollo_service.save_temperature_reading_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                       request.args['temperature'],
                                                                       request.args['temperature_unit'],
                                                                       request.args['reading_time'])
        return {'success': True}, 200

    if request.method == 'GET':
        result = apollo_service.get_temperature_readings_for_spacecraft_journey(spacecraft_name, journey_id,
                                                                                request.args['pageSize'],
                                                                                request.args['pageState'])

        return jsonify(pageSize=request.args['pageSize'], pageState=result.paging_state, data=result.current_rows), 200




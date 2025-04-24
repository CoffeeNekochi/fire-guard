from flask import Blueprint, jsonify, render_template
import requests

# 主頁面 Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('home.html')

@main_bp.route('/components')
def components():
    return render_template('components.html')

# API Blueprint
api_bp = Blueprint('api', __name__)

@api_bp.route('/devices')
def get_devices():
    try:
        response = requests.get('http://140.134.37.19:5000/api/devices')
        response.raise_for_status()  # 檢查 HTTP 錯誤
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/devices/<device_id>')
def get_device_details(device_id):
    try:
        response = requests.get(f'http://140.134.37.19:5000/api/devices/{device_id}')
        response.raise_for_status()  # 檢查 HTTP 錯誤
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500 
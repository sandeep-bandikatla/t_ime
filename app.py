from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from datetime import datetime
import pytz

class TimeResource(Resource):
    def get(self):
        kolkata_tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(kolkata_tz)
        current_time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        return jsonify({
            'server_time': current_time_str,
            'timezone': 'Asia/Kolkata'
        })

class MyFlask(Flask):
    def add_api(self):
        self.api = Api(self)
        self.api.add_resource(TimeResource, "/codegnana/time")

app = MyFlask(__name__)
app.add_api()

# Proper CORS setup with support_credentials=True
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run()

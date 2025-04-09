from flask import Flask, jsonify
from flask_restful import Api, Resource
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
        from flask_restful import Api
        self.api = Api(self)
        self.api.add_resource(TimeResource, "/api/v1/time")

app = MyFlask(__name__)
app.add_api()

if __name__ == '__main__':
    app.run()

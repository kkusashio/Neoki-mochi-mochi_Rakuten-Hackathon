from urllib import response
import requests
import json
import os
import datetime

class Zoom:
    zoom_key = os.environ.get("ZOOM_API_KEY")
    zoom_url = "https://api.zoom.us/v2/"

    TIME_ZONE ="Asia/Tokyo"

    headers = {
        "authorization": "Bearer " + str(zoom_key),
        "content-type": "application/json",
    }

    def create_room(self,date):
        if type(date) is datetime.datetime:
            date = str(date.isoformat)
        data = {
            "topic": "MochiMochi",
            "type": 2,
            "start_time":date,
            "timezone": self.TIME_ZONE,
            "settings": {
                "join_before_host": True,
                "jbh_time": 5
            }
        }
        request = requests.post(self.zoom_url + "users/me/meetings", headers=self.headers, data=json.dumps(data))
        response = request.json()
        return response

if __name__ == "__main__":
    date = datetime.datetime.now()
    zoom = Zoom()
    print(zoom.create_room(date))
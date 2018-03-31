""" Copyright Brett Bushnell 2018 """
from flask import request
from flask_restful import Resource
from ..models.DoorState import DoorState

class Status(Resource):
    """ Class for handeling /status endpoint """

    def post(self):
        """ Post method for /status
            
            Example Request:
            {
                "timestamp": TimeStamp
                "door_state": "open" --or-- "close"
            }

            Example Response:
            {
                "open_garage": bool
            }
        """
        req_json = request.get_json()
        print(req_json)
        # This is where we check db or some queue if there
        # is any requests to open the garage
        # ALso add status to DB
        doorState = DoorState(
                        timestamp=str(req_json.get('timestamp')),
                        door_open=req_json.get('door_state')
                    )
        doorState.add()

        # TODO: Add DB call or queue call to get open status
        open_garage = True

        return {'open_garage': open_garage}

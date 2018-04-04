""" Copyright Brett Bushnell 2018 """
from flask import request, send_file
from flask_restful import Resource
from ..models.DoorState import DoorState

import os, sys, io
import urllib, binascii
from PIL import Image

class ViewGarage(Resource):
    """ Class for handeling /ViewGarage endpoint """

    def get(self):
        """ GET method for /view_garage
        """
        garage_doors = DoorState.query.all()
        photo_data = garage_doors[0].door_open

        self.create_jpg(photo_data)
        # TODO: Add DB call or queue call to get open status
        return send_file('tmp.jpg')

    def create_jpg(self, data):
        """ Function creates a jpg photo from given hexadecimal """
        b_data = binascii.unhexlify(data)
        stream = io.BytesIO(b_data)
        img = Image.open(stream)
        img.size
        outfile = "gos/tmp.jpg"
        img.save(outfile)

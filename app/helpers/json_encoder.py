from datetime import datetime
from json import JSONEncoder
from bson import ObjectId

from app.services.date_service import DateService, DateTypes


class JsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return DateService.datetime_to_string(o, DateTypes.GMT_DATE)
        return JSONEncoder.default(self, o)

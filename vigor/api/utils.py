import datetime
import decimal

try:
    import json
except ImportError:
    import simplejson as json


class ExtraJsonEncoder(json.JSONEncoder):

    def default(self, data):
        if isinstance(data, (datetime.datetime, datetime.date, datetime.time)):
            return data.isoformat()
        elif isinstance(data, decimal.Decimal):
            return str(data)
        else:
            return super(ExtraJsonEncoder, self).default(data)

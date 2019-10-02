# -*- coding: utf-8 -*-

from boto3.dynamodb.types import TypeDeserializer


class DeRecord:
    """
    Deserialized record.
    """

    def __init__(self, rec):
        self.event_name = rec['eventName']
        self.region = rec['awsRegion']
        self.source_table = rec['eventSourceARN'].split('/')[1]
        self.old = self._desi(rec['dynamodb'].get('OldImage'))
        self.new = self._desi(rec['dynamodb'].get('NewImage'))
        self.raw = rec

    def _desi(self, image):
        d = {}
        if image:
            for key in image:
                try:
                    d[key] = TypeDeserializer().deserialize(image[key])
                except TypeError:
                    if image[key].get('B'):
                        d[key] = image[key]['B'].encode()
                    elif image[key].get('BS'):
                        d[key] = [x.encode() for x in image[key]['BS']]
                    else:
                        d[key] = image[key]
                    continue
        return d

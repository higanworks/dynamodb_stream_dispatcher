# -*- coding: utf-8 -*-

from boto3.dynamodb.types import TypeDeserializer


class DeRecord:
    """
    Deserialized record.
    """

    def __init__(self, rec):
        self.event_name = rec['eventName']
        self.old = self._desi(rec['dynamodb'].get('OldImage'))
        self.new = self._desi(rec['dynamodb'].get('NewImage'))

    def _desi(self, image):
        d = {}
        if image:
            for key in image:
                d[key] = TypeDeserializer().deserialize(image[key])
        return d

# -*- coding: utf-8 -*-

from .derecord import DeRecord


class DynamoStreamDispatcher:
    def __init__(self, event):
        self.on_insert = []
        self.on_remove = []
        self.on_modify = []
        self.records = []

        for r in event['Records']:
            self.records.append(DeRecord(r))

        self.raw = event

    def dispatch(self):
        """
        synced dispatcher
        """
        results = []
        for r in self.records:
            try:
                for runner in getattr(self, 'on_' + r.event_name.lower()):
                    results.append(runner(r))
            except AttributeError:
                print("Unknown event " + r.event_name)
                continue

        return results

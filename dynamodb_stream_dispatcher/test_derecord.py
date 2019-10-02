# -*- coding: utf-8 -*-
from .derecord import DeRecord
import decimal

base_obj = {}
base_obj['eventName'] = 'testevent'
base_obj['awsRegion'] = 'us-east-1'
base_obj['eventSourceARN'] = 'arn:foo/bar'
base_obj['dynamodb'] = {}


def test_base():
    assert DeRecord(base_obj)


def test_includes_str():
    test_obj = base_obj
    test_obj['dynamodb']['OldImage'] = {
        "ID": {
            "S": "xxxxxxx-xxxxxxx"
        }
    }
    assert DeRecord(test_obj)


def test_includes_num():
    test_obj = base_obj
    test_obj['dynamodb']['OldImage'] = {
        "ID": {
            "S": "xxxxxxx-xxxxxxx"
        },
        "NUM": {
            "N": 300
        },
    }
    der = DeRecord(test_obj)
    assert der.old.get('ID')
    assert isinstance(der.old['NUM'], decimal.Decimal)


def test_includes_b():
    test_obj = base_obj
    test_obj['dynamodb']['OldImage'] = {
        "ID": {
            "S": "xxxxxxx-xxxxxxx"
        },
        "BIN": {
            "B": "Zm9vYmFy"
        },
    }
    der = DeRecord(test_obj)
    assert der.old.get('ID')
    assert isinstance(der.old['BIN'], bytes)


def test_includes_bs():
    test_obj = base_obj
    test_obj['dynamodb']['OldImage'] = {
        "ID": {
            "S": "xxxxxxx-xxxxxxx"
        },
        "BINS": {
            "BS": [
                "Zm9vYmFy",
                "Zm9vYmFyYmFy"
            ]
        },
    }
    der = DeRecord(test_obj)
    assert der.old.get('ID')
    for x in der.old['BINS']:
        assert isinstance(x, bytes)

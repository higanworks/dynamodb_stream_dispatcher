from __future__ import print_function
from dynamodb_stream_dispatcher import DynamoStreamDispatcher


def after_remove1(rec):
    print("deleted")
    return None


def after_remove2(rec):
    print(rec.old)
    return None


def after_modify(rec):
    print("key updated...")
    print(rec.old)
    print(rec.new)
    return None


def lambda_handler(event, context):
    ds = DynamoStreamDispatcher(event)
    ds.on_insert.append(lambda rec: print(rec.event_name))
    ds.on_insert.append(lambda rec: print(rec.new))
    ds.on_remove.append(after_remove1)
    ds.on_remove.append(after_remove2)
    ds.on_modify.append(after_modify)
    ds.dispatch()
    return True
dynamodb_stream_dispatcher
--------------------------

This library registers and executes a function corresponding to the event of DynamoDB Stream.
This can be used with AWS lambda.


## install

```
cd your/lambda_function/dir
pip install dynamodb-stream-dispatcher -t ./
```

## Usage

1. create function
2. append function to an instance of `DynamoStreamDispatcher`.
3. call `DynamoStreamDispatcher.dispatch` to execute functions by event.

[please show example](./example/lambda_function/).


### creating function

DynamoStreamDispatcher passes deserialized record(DeRecord) to your functions.


`DeRecord` has few variables.

|variable|type|description|example|
|----|----|----|----|
|event_name|string |action of updates |`INSERT` / `MODIFY` / `REMOVE` |
|region|string |AWS Region of Table |`us-west-2` |
|source_table|string| name of Table|`ExampleTableWithStream` |
|old|dict |deserialized NewImage |`{u'Message': u'This item has changed', u'Id': Decimal('101')}` |
|new|dict |deserialized OldImage |`{u'Message': u'This item has changed', u'Id': Decimal('101')}` |
|raw|dict |raw source of record | - |

```
def yourfunc(rec):
   ## code to handle event
```

## Test

```
$ pytest -p no:warnings -v dynamodb_stream_dispatcher
```

## Contributing

1. Fork it ( https://github.com/higanworks/dynamodb_stream_dispatcher/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

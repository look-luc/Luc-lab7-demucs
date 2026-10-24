# Short-sample-requests.py
```python
Separate data/data/short-hop.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
/Users/lucdenardi/Desktop/code_lang/datacenter/Luc-lab7-demucs/short-sample-request.py:24: DeprecationWarning: keys will default to True in jsonpickle 5.0.0
  jsonData = jsonpickle.encode(data)
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 347248
Handling connection for 5001
response code is 500, raw response is {
  "error": "MinIO storage failed: S3 operation failed; code: NoSuchBucket, message: The specified bucket does not exist, resource: None, request_id: None, host_id: None"
}

Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": []
}
Separate data/data/short-dreams.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 210212
Handling connection for 5001
response code is 500, raw response is {
  "error": "MinIO storage failed: S3 operation failed; code: NoSuchBucket, message: The specified bucket does not exist, resource: None, request_id: None, host_id: None"
}

Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": []
}
```

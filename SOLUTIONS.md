# Deploy-local-dev.sh

## Short-sample-requests.py
```bash
uv run short-sample-request.py
Separate data/data/short-hop.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
/Users/lucdenardi/Desktop/code_lang/datacenter/Luc-lab7-demucs/short-sample-request.py:24: DeprecationWarning: keys will default to True in jsonpickle 5.0.0
  jsonData = jsonpickle.encode(data)
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 347248
Handling connection for 5001
{
    "hash": "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-dreams.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 210212
Handling connection for 5001
{
    "hash": "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
```
## Sample-requests.py
```bash
uv run sample-requests.py
Separate data/data/Dreamers Of The Ghetto - Heavy Love.stem.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
/Users/lucdenardi/Desktop/code_lang/datacenter/Luc-lab7-demucs/sample-requests.py:24: DeprecationWarning: keys will default to True in jsonpickle 5.0.0
  jsonData = jsonpickle.encode(data)
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 9018848
Handling connection for 5001
{
    "hash": "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-hop.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 347248
Handling connection for 5001
{
    "hash": "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/Hop Along - Sister Cities.stem.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 8820724
Handling connection for 5001
{
    "hash": "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-dreams.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 210212
Handling connection for 5001
{
    "hash": "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
```

# Deploy-all.sh
## Short-sample-request
```bash
uv run short-sample-request.py
Separate data/data/short-hop.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
/Users/lucdenardi/Desktop/code_lang/datacenter/Luc-lab7-demucs/short-sample-request.py:24: DeprecationWarning: keys will default to True in jsonpickle 5.0.0
  jsonData = jsonpickle.encode(data)
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 347248
Handling connection for 5001
{
    "hash": "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-dreams.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 210212
Handling connection for 5001
{
    "hash": "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
```

## Sample-requests
```bash
uv run sample-requests.py
Separate data/data/Dreamers Of The Ghetto - Heavy Love.stem.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
/Users/lucdenardi/Desktop/code_lang/datacenter/Luc-lab7-demucs/sample-requests.py:24: DeprecationWarning: keys will default to True in jsonpickle 5.0.0
  jsonData = jsonpickle.encode(data)
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 9018848
Handling connection for 5001
{
    "hash": "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-hop.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 347248
Handling connection for 5001
{
    "hash": "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/Hop Along - Sister Cities.stem.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 8820724
Handling connection for 5001
{
    "hash": "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
Separate data/data/short-dreams.mp3
Response to http://localhost:5001/apiv1/separate request is <class 'dict'>
Make request http://localhost:5001/apiv1/separate with json dict_keys(['mp3', 'callback'])
mp3 is of type <class 'str'> and length 210212
Handling connection for 5001
{
    "hash": "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
    "reason": "Song enqueued for separation"
}
Cache from server is
Response to http://localhost:5001/apiv1/queue request is <class 'NoneType'>
Handling connection for 5001
{
    "queue": [
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "c07e8857ca13c0fffbc7ff49f5b57c53c05a2a670186c87546823afc01314630",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28",
        "60439509403778741cae53669a06fc98a33f335cf3e9a34815cf9b89fb326290",
        "83abdba474adf043c6879343f3561e36d5d9b37d3dba90603b33affa2dc2a666",
        "9627ed8f6b9ddd5b86fa495161a6de2ab371e2ed8e052d659a88c51272b4fc28"
    ]
}
```

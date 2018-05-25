import Requests

postdata="{\"jsonrpc\": \"2.0\", \"method\": \"getTag\", \"params\": {\"tagname\": DBL0, \"tagtype\": Double}, \"id\": 1}"
r=requests.post('http://127.0.0.1:8001/DCAF_JSON_RPC/request', postdata)
print(r.text)


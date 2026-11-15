#!/usr/bin/env python3
"""Real stateless analyze->anonymize API workflow, repeated after upgrade/redeploy."""
import base64, json, os, urllib.error, urllib.request
b=os.environ['BASE_URL'].rstrip('/');phase=os.environ['SMOKE_PHASE']
assert phase in ('boot','upgrade','redeploy')
user=os.environ['BASIC_AUTH_USER'];password=os.environ['BASIC_AUTH_PASSWORD']
def request(method,path,payload=None,status=200,auth='valid'):
 headers={'Content-Type':'application/json'}
 if auth!='none':
  pw=password if auth=='valid' else 'incorrect-'+password
  headers['Authorization']='Basic '+base64.b64encode((user+':'+pw).encode()).decode()
 req=urllib.request.Request(b+path,method=method,headers=headers,data=None if payload is None else json.dumps(payload).encode())
 try:r=urllib.request.urlopen(req,timeout=90)
 except urllib.error.HTTPError as e:r=e
 with r:raw=r.read();code=r.code
 assert code==status,f'{method} {path} unexpected status {code}'
 return raw
request('GET','/healthz')
text='Contact validation@example.com or call 212-555-5555';body={'text':text,'language':'en'}
request('POST','/analyze',body,status=401,auth='none')
request('POST','/analyze',body,status=401,auth='invalid')
analysis=json.loads(request('POST','/analyze',body))
assert any(x['entity_type']=='EMAIL_ADDRESS' for x in analysis)
assert any(x['entity_type']=='PHONE_NUMBER' for x in analysis)
result=json.loads(request('POST','/anonymize',{'text':text,'analyzer_results':analysis,'anonymizers':{'DEFAULT':{'type':'replace','new_value':'<REDACTED>'}}}))
assert 'validation@example.com' not in result['text'] and '212-555-5555' not in result['text'] and '<REDACTED>' in result['text']
print(json.dumps({'phase':phase,'ok':True,'scope':'stateless PII detection and actual redaction; positive and negative authentication'}))

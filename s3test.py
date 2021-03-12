import datetime
import hashlib
import base64
import hmac
import requests
import logging
import os
import time
import re
#s3 userguid 991page
#BTKZY9YC08AKLAWGN6RY
#47pxhXLNNqWjDb2GfOCbg3BEPxLHHlwQkmEJnOAj
ACCESS_KEY = 'BTKZY9YC08AKLAWGN6RY'.encode("UTF-8")
SECRET_KEY = '47pxhXLNNqWjDb2GfOCbg3BEPxLHHlwQkmEJnOAj'.encode("UTF-8")
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
host = '10.67.67.238'
port = 80


def generate_auth_string(httpmethod, signurl, my_date, contenttype=''):
    string_to_sign = (httpmethod.strip() + '\n\n'+ contenttype.strip() +'\n' + my_date + '\n' + signurl).encode("UTF-8")
    my_hmac = hmac.new(SECRET_KEY,string_to_sign,hashlib.sha1).digest()
    signature = base64.encodestring(my_hmac).strip()
    req_hash_sig = 'AWS %s:%s' %(ACCESS_KEY,signature)
    print(req_hash_sig)
    return req_hash_sig.strip()

if __name__ == "__main__":
    print('list bucket....f')
    my_date = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    baseurl = 'http://' + host + ':'+str(port) + '/'
    headers = {'Date':my_date,'Authorization':generate_auth_string("GET",'/', my_date)}
    res = requests.get(baseurl,params={},headers=headers)
    print (res.headers, "\n", res.text)
    bucketname = "mytestbucket"

    if True:
        print("\n\ncreate bucket test....")
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname
        headers = {'Date':my_date, 'x-amz-acl':'private ', 'Authorization':generate_auth_string("PUT", 'x-amz-acl:private\n'+'/'+bucketname,my_date)}
        res = requests.put(baseurl,params={},headers=headers)
        print (res.status_code, "\n", res.headers, "\n", res.text)

        mytestdata = 'mytestdata'
        print "\n\n Head bucket...."
        headers = {'Date':my_date,'Authorization':generate_auth_string("HEAD", '/'+bucketname, my_date)}
        res = requests.head(baseurl,params={},headers=headers)
        print (res.headers, "\n", res.text)

        #
        print("\n\n put object to bucket....")
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata
        headers = {'Date':my_date, 'Content-Type': 'application/octet-stream',\
            'x-amz-meta-author1234':'hhhh', \
            'Authorization':generate_auth_string("PUT", 'x-amz-meta-author1234:hhhh' + '\n'+'/'+bucketname+'/'+ mytestdata,my_date, 'application/octet-stream')}
        res = requests.put(baseurl,params={},headers=headers, data="this is my test data")
        print (res.status_code, "\n", res.headers, "\n", res.text)

        print "\n\n get object from bucket...."
        headers = {'Date':my_date,'Authorization':generate_auth_string("GET", '/'+bucketname+'/'+ mytestdata, my_date)}
        res = requests.get(baseurl,params={},headers=headers)
        print (res.headers, "\n", res.text)


        mytestdata = 'myappendobject'
        print "\n\n append object to bucket...."
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata + '?append&position=0'
        headers = {'Date':my_date, \
            'Content-Type': 'application/octet-stream',\
            'x-amz-meta-author1234':'hhhh', \
            'Authorization':generate_auth_string("PUT", 'x-amz-meta-author1234:hhhh' + '\n'+'/'+bucketname+'/'+ mytestdata,my_date, 'application/octet-stream')}
        res = requests.put(baseurl,params={},headers=headers, data="this is my test append data")
        print (res.status_code, "\n", res.headers, "\n", res.text)
        #POST /test-c-sdk-1615290559413-object-bucket/oss_test_append_object?append&position=0 HTTP/1.1

        print "\n\n Head object from bucket...."
        headers = {'Date':my_date,'Authorization':generate_auth_string("HEAD", '/'+bucketname+'/'+ mytestdata, my_date)}
        res = requests.head(baseurl,params={},headers=headers)
        print (res.headers, "\n", res.text)        

    if False:
        
        print """ The subresources that must be included when constructing the CanonicalizedResource Element are acl, lifecycle, location, logging, notification, partNumber, policy, requestPayment, torrent, uploadId, uploads, versionId, versioning, versions, and website.

        Note that in case of multiple subresources, subresources must be lexicographically sorted by subresource name and separated by '&', e.g., ?acl&versionId=value."""
        print "\n\n\n multipart upload test......"

        datamatrix = ""
        item = "1"*1024
        datamatrix = item*1024*6
      

        mytestdata = 'mymultipartupload'
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploads"
        headers = {'Date':my_date, 'Content-Type': 'application/octet-stream',\
            'Authorization':generate_auth_string("POST", '/'+bucketname+'/'+ mytestdata+"?uploads", my_date, 'application/octet-stream')}
        res = requests.post(baseurl,params={},headers=headers)
        print (res.status_code, "\n", res.headers, "\n", res.text)
        uploadid = re.findall("<UploadId>(.*?)</UploadId>", res.text)[0]
        print("\n\nuploadidis", uploadid)

        if False:
            print("\n\n abort...........", uploadid)
            baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploadId="+uploadid
            headers = {'Date':my_date, \
                'Authorization':generate_auth_string("DELETE", '/'+bucketname+'/'+ mytestdata+"?uploadId="+uploadid, my_date, '')}
            res = requests.delete(baseurl,params={},headers=headers)
            print (res.status_code, "\n", res.headers, "\n", res.text)

        
        print ("\n\n upload parts")
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploadId="+uploadid+"&partNumber=1"
        headers = {'Date':my_date, 'Content-Type': 'application/octet-stream',\
            'Authorization':generate_auth_string("PUT", '/'+bucketname+'/'+ mytestdata+"?partNumber=1&uploadId="+uploadid, my_date, 'application/octet-stream')}
        res = requests.put(baseurl,params={},headers=headers, data=datamatrix)
        print (res.status_code, "\n", res.headers, "\n", res.text)
        tag1 = res.headers['ETag'].strip('\"')
        
        print("\n\n ...........")
        print(uploadid)

        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploadId="+uploadid+"&partNumber=2"
        headers = {'Date':my_date, 'Content-Type': 'application/octet-stream',\
            'Authorization':generate_auth_string("PUT", '/'+bucketname+'/'+ mytestdata+"?partNumber=2&uploadId="+uploadid, my_date, 'application/octet-stream')}
        res = requests.put(baseurl,params={},headers=headers, data=datamatrix)
        print (res.status_code, "\n", res.headers, "\n", res.text)
        tag2 = res.headers['ETag'].strip('\"')
        print(tag1, tag2)

        if False:
            print("\n\n\n abort...........")
         
            baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploadId="+uploadid
            headers = {'Date':my_date, \
                'Authorization':generate_auth_string("DELETE", '/'+bucketname+'/'+ mytestdata+"?uploadId="+uploadid, my_date, '')}
            res = requests.delete(baseurl,params={},headers=headers)
            print (res.status_code, "\n", res.headers, "\n", res.text)
        if True:
            print("\n\n complete...........")

            baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/' + mytestdata+"?uploadId="+uploadid
            headers = {'Date':my_date, \
                'Authorization':generate_auth_string("POST", '/'+bucketname+'/'+ mytestdata+"?uploadId="+uploadid, my_date, '')}
            completexml = '<?xml version="1.0" encoding="utf-8"?><CompleteMultipartUpload><Part><PartNumber>1</PartNumber><ETag>&quot;'+tag1+'&quot;</ETag></Part><Part><PartNumber>2</PartNumber><ETag>&quot;' + tag2+'&quot;</ETag></Part></CompleteMultipartUpload>'

            res = requests.post(baseurl,params={},headers=headers, data=completexml)
            print (res.status_code, "\n", res.headers, "\n", res.text)
    if False:
        print("\n\ndelete bucket test.....")
        baseurl = 'http://' + host + ':'+str(port) + '/'  + bucketname + '/'
        headers = {'Date':my_date,'Authorization':generate_auth_string("DELETE", '/'+bucketname+'/',my_date)}
        res = requests.delete(baseurl,params={},headers=headers)
        print (res.status_code, "\n", res.headers, "\n", res.text)

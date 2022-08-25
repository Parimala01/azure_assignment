import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from flask import Flask, render_template

app = Flask(__name__)


def list_blobs():
    try:
       connection_string = "DefaultEndpointsProtocol=https;AccountName=storage7695;AccountKey=Yx7XmCGEFxME2+WMeh+hYD3nhPdJJzVieCY/v2yszWUlsDMs+k1yyqAoLw37AcrU0uw0I7xXVPz2+ASt0mMRtQ==;EndpointSuffix=core.windows.net"
       service = BlobServiceClient.from_connection_string(conn_str=connection_string)

    # Quick start code goes here
      
       container = ContainerClient.from_connection_string(conn_str=connection_string, container_name="container1")

       blob_list = container.list_blobs()
       for blob in blob_list:
          return("\t" + blob.name)

    except Exception as ex:
       return ex
       
@app.route('/')
def home():
   folder = list_blobs()
   return render_template('index.html',bucketlist=folder)
app.run(port=5000)

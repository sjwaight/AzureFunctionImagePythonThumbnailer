from io import BytesIO
from logging import FileHandler
import logging
import azure.functions as func
from PIL import Image

def main(msg: func.QueueMessage, inputblob: func.InputStream,
         outputblob: func.Out[func.InputStream]) -> None:

    blob_source_raw_name = msg.get_body().decode('utf-8')
    logging.info('Python queue trigger function processed a queue item: %s', blob_source_raw_name)

    # thumbnail filename
    local_file_name_thumb = blob_source_raw_name[:-4] + "_thumb.jpg"

    #####
    # Download file from Azure Blob Storage
    #####
    with open(blob_source_raw_name,"w+b") as local_blob:
        local_blob.write(inputblob.read())

    #####
    # Use PIL to create a thumbnail
    #####
    new_size = 200,200 
    im = Image.open(local_blob.name)
    im.thumbnail(new_size)
    im.save(local_file_name_thumb, quality=95)

    # write the stream to the output file in blob storage
    new_thumbfile = open(local_file_name_thumb,"rb")
    outputblob.set(new_thumbfile.read())
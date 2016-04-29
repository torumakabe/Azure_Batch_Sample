import os
import sys
import datetime
import pytz

from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions,
    BlobPermissions,
    PublicAccess,
)

if __name__ == '__main__':

    parms = sys.argv

    input_block_blob_service = BlockBlobService(account_name=parms[1], sas_token=parms[2], protocol='https')
    input_block_blob_service.get_blob_to_path(parms[3], parms[4], 'input.txt')

    input_file=open("input.txt","r")
    wordcount={}
    for word in input_file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    input_file.close()

    now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
    fmt = "%Y-%m-%d-%H-%M-%S-%Z"
    output_filename = now.strftime(fmt) + ".txt"

    output_file=open(output_filename,"w")
    for k,v in wordcount.items():
        output_file.writelines(k + " " + str(v) + "\n")

    output_file.close()

    output_block_blob_service = BlockBlobService(account_name=parms[5], sas_token=parms[7], protocol='https')
    output_block_blob_service.create_blob_from_path(parms[6], output_filename, output_filename)
import logging

import azure.functions as func

from azure.storage.blob import BlobClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    blob_client = BlobClient.from_blob_url("copy your Blob SAS URL here")
    download_stream = blob_client.download_blob()
    logging.info('=========below is content of test1')
    logging.info(download_stream.readall())
    logging.info('=========above is content of test1')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )

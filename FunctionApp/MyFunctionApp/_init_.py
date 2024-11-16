import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Log a simple message
    logging.info('Python HTTP trigger function processed a request.')

    # Get query parameter or body data
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # Return a response
    return func.HttpResponse(
        f"Hello, {name}!",
        status_code=200
    )

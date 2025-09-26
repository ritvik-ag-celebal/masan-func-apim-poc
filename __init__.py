import logging
import azure.functions as func
from azure.functions_openapi import OpenApiHttpTrigger

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Hello from Azure Function!", status_code=200)

# OpenAPI endpoint
openapi_trigger = OpenApiHttpTrigger()
app.register_functions(openapi_trigger.get_functions())

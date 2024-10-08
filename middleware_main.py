from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("my_middleware")

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Perform action before the request is processed
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.url}")

        # Process the request and get the response
        response = await call_next(request)

        # Perform action after the request is processed
        process_time = time.time() - start_time
        logger.info(f"Response status: {response.status_code} - Time taken: {process_time:.4f} seconds")

        return response

# Initialize FastAPI app
app = FastAPI()

# Add middleware to the app
app.add_middleware(LogMiddleware)

# Example route
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

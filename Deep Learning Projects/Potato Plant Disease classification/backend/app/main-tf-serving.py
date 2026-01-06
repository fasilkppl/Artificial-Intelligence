from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests

app = FastAPI() #initialize the FastAPI app

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

endpoint = "http://localhost:8501/v1/models/potatoes_model:predict"

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"] #Define class names for prediction, same as the .ipynb notebook.

# this is a health check endpoint, it returns a simple message to confirm the server is running
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# we want our API to accept an image file, process it, and return a prediction.
# also we have to convert image tensior to numpy array.
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


# Define the prediction endpoint
@app.post("/predict")
async def predict(
    file: UploadFile = File(...) # this indicates that the endpoint expects a file upload
):
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read()) #await is to manage delay for multiple requests.
    img_batch = np.expand_dims(image, 0) #expand dimensions to create a batch of size 1
    # Prepare the data in the format expected by TensorFlow Serving, which is a JSON.
    json_data = {
        "instances": img_batch.tolist()
    }

    # Make the request to TensorFlow Serving
    response = requests.post(endpoint, json=json_data)
    
    # Extract the prediction from the response
    prediction = np.array(response.json()["predictions"][0])
    
    # Get the class with the highest predicted probability and its confidence score
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    # Return the predicted class and confidence score as a JSON response
    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }


# Run the app with Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)


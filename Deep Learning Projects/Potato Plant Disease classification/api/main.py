

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI() #initialize the FastAPI app

origins = [ #list of allowed origins for CORS
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(   #this is to handle CORS
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the pre-trained model
MODEL = tf.keras.models.load_model("../saved_models/1")

# Define class names for prediction, same as the .ipynb notebook.
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping") #this is a health check endpoint, it returns a simple message to confirm the server is running
async def ping():
    return "Hello, I am alive"


# we want our API to accept an image file, process it, and return a prediction.
# also we have to convert image tensior to numpy array.
def read_file_as_image(data) -> np.ndarray: #function to read uploaded file as image.
    image = np.array(Image.open(BytesIO(data))) #this reads the image data from bytes and converts it to a numpy array
    return image

# Define the prediction endpoint
@app.post("/predict") # this endpoint will handle POST requests for predictions
async def predict( 
    file: UploadFile = File(...)# this indicates that the endpoint expects a file upload
):
    image = read_file_as_image(await file.read()) #read the uploaded file as an image, await is to manage delay for multiple requests.
    img_batch = np.expand_dims(image, 0) #expand dimensions to create a batch of size 1
    
    predictions = MODEL.predict(img_batch) #make prediction using the pre-trained model 

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])] #get the class with the highest predicted probability
    confidence = np.max(predictions[0]) #get the confidence score for the predicted class
    return {
        'class': predicted_class, #return the predicted class and confidence score as a JSON response
        'confidence': float(confidence)
    }
# Run the app with Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)


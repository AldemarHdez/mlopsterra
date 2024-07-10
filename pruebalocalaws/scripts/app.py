from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from mangum import Mangum

app = FastAPI()

# Load the trained model
model = tf.keras.models.load_model('s3://your-bucket/iris_model')

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
    prediction = model.predict(data)
    return {"prediction": np.argmax(prediction)}

# Create an adapter for AWS Lambda
handler = Mangum(app)

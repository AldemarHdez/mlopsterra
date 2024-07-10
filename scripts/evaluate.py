import tensorflow as tf
import pandas as pd
import mlflow

# Load the preprocessed data
X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv')

# Load the model
model = tf.keras.models.load_model('s3://your-bucket/iris_model')

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)

# Log metrics with MLflow
with mlflow.start_run() as run:
    mlflow.log_metric("loss", loss)
    mlflow.log_metric("accuracy", accuracy)

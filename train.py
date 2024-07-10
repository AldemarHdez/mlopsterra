import tensorflow as tf
import pandas as pd
import boto3

# Load the preprocessed data
X_train = pd.read_csv('s3://your-bucket/X_train.csv')
y_train = pd.read_csv('s3://your-bucket/y_train.csv')

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50)

# Save the model
model.save('s3://your-bucket/iris_model')

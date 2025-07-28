import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load and normalize data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(120, activation="relu"),
    layers.Dense(10, activation="softmax")  # fixed typo: "software" → "softmax"
])

# Compile model
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])  # fixed typos: "mtrics" → "metrics"

# Train model
model.fit(x_train, y_train, epochs=5)

# Evaluate model on test data (fixed incorrect use of x_train instead of x_test)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Show prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()

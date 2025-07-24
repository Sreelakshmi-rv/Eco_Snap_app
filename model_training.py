# Import necessary libraries
from bing_image_downloader import downloader
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Step 1: Download images for each category
categories = [
    "reusable shopping bag",
    "tree planting",
    "riding bicycle",
    "compost bin",
    "public transport",
    "cloth packaging over plastic"
]

for category in categories:
    print(f"Downloading images for: {category}")
    downloader.download(category, limit=30, output_dir='eco_dataset', adult_filter_off=True, force_replace=False, timeout=60)

# Step 2: Set image size and path
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
DATASET_DIR = "eco_dataset"

# Step 3: Prepare the dataset using ImageDataGenerator
datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2
)

train_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Step 4: Define a simple CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(train_generator.num_classes, activation='softmax')
])

# Step 5: Compile and train the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_generator, epochs=10, validation_data=val_generator)

# Step 6: Save the model in different formats
model.save("eco_model.keras")
model.save("eco_model.h5")

# Step 7: Convert and save as TensorFlow Lite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("eco_model.tflite", "wb") as f:
    f.write(tflite_model)

# Step 8: Save class labels
class_labels = list(train_generator.class_indices.keys())
with open("class_labels.txt", "w") as f:
    for label in class_labels:
        f.write(label + "\n")

print("✅ Training complete. Models and class labels saved!")

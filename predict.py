import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)

model = MobileNetV2(
    weights="imagenet"
)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    width, height = image.size
    crop_size = min(width, height)
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size
    image = image.crop(
        (
            left,
            top,
            right,
            bottom
        )
    )

    image = image.resize(
        (224,224)
    )
    image = np.array(image)
    image = preprocess_input(image)
    image = np.expand_dims(
        image,
        axis=0
    )
    return image

def predict_image(image_path):
    image = preprocess_image(
        image_path
    )
    predictions = model.predict(
        image,
        verbose=0
    )
    decoded = decode_predictions(
        predictions,
        top=3
    )[0]

    results = []

    for item in decoded:
        results.append(
            {
                "label":
                item[1]
                .replace("_"," ")
                .title(),
                "confidence":
                round(
                    item[2] * 100,
                    2
                )
            }
        )

    return {
        "prediction":
        results[0]["label"],
        "confidence":
        results[0]["confidence"],
        "top3":
        results
    }
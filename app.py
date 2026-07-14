from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

history = []


@app.route("/")
def home():

    return render_template(
        "index.html",
        history=history[:5]
    )


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    image = request.files["image"]

    if image.filename == "":
        return "No image selected."

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)

    from predict import predict_image

    result = predict_image(image_path)

    history.insert(
        0,
        {
            "image": image.filename,
            "prediction": result["prediction"],
            "confidence": result["confidence"]
        }
    )

    history[:] = history[:5]

    return render_template(
        "index.html",
        prediction=result["prediction"],
        confidence=result["confidence"],
        top3=result["top3"],
        image=image.filename,
        history=history
    )


if __name__ == "__main__":

    app.run(debug=True)
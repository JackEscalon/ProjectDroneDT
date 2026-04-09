from transformers import pipeline
from PIL import Image, ImageDraw

detector = pipeline("object-detection")


def analyze_image(image_path):
    image = Image.open(image_path).convert("RGB")

    results = detector(image)

    results = [obj for obj in results if obj["score"] > 0.7]
    results = sorted(results, key=lambda x: x["score"], reverse=True)[:1]

    draw = ImageDraw.Draw(image)

    detected_label = None
    detected_score = None

    for obj in results:
        label = obj["label"]
        score = round(obj["score"], 2)
        box = obj["box"]

        if label == "airplane":
            label = "drone"

        detected_label = label
        detected_score = score

        xmin = box["xmin"]
        ymin = box["ymin"]
        xmax = box["xmax"]
        ymax = box["ymax"]

        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
        draw.text((xmin, max(0, ymin - 12)), f"{label} {score}", fill="red")

    output_path = image_path.replace(".jpg", "_detected.jpg")
    image.save(output_path)

    return detected_label, detected_score, output_path
from transformers import pipeline
from PIL import Image, ImageDraw

detector = pipeline("object-detection")

image_path = "media/uploads/dron1.jpg"
image = Image.open(image_path).convert("RGB")

# 🔥 NAJWAŻNIEJSZE — uruchamiamy model
results = detector(image)

# 🔥 filtrujemy i bierzemy najlepszy wynik
results = [obj for obj in results if obj["score"] > 0.7]
results = sorted(results, key=lambda x: x["score"], reverse=True)[:1]

draw = ImageDraw.Draw(image)

for obj in results:
    label = obj["label"]
    score = round(obj["score"], 2)
    box = obj["box"]

    xmin = box["xmin"]
    ymin = box["ymin"]
    xmax = box["xmax"]
    ymax = box["ymax"]

    # 🔥 mapowanie labela
    if label == "airplane":
        label = "drone"

    print(f"{label} | score={score} | box={box}")

    draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
    draw.text((xmin, max(0, ymin - 12)), f"{label} {score}", fill="red")

output_path = "media/uploads/dron1_detected.jpg"
image.save(output_path)

print(f"\nZapisano obraz z ramkami: {output_path}")
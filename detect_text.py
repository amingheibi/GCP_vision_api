from google.cloud import vision
from google.cloud.vision_v1.types.image_annotator import AnnotateImageResponse
import json


def detect_text(file_path):
    print("Sending request for {}".format(file_path))
    client = vision.ImageAnnotatorClient()

    with open(file_path, "rb") as image:
        binary_image = image.read()

    base64_image = vision.Image(content=binary_image)

    response = client.text_detection(image=base64_image)
    texts = response.text_annotations
    list_of_texts = []

    for text in texts:
        vertices = [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
        list_of_texts.append((text.description, vertices))

    if response.error.message:
        print(response.error.message)
    else:
        with open("{}.json".format(file_path), "w") as response_file:
            json.dump(list_of_texts, response_file)

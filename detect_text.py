from google.cloud import vision


def detect_text(path):
    file_path = str(path)
    client = vision.ImageAnnotatorClient()

    with open(file_path, "rb") as image:
        binary_image = image.read()

    base64_image = vision.Image(content=binary_image)

    response = client.text_detection(image=base64_image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = [
            "({},{})".format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        print(response.error.message)

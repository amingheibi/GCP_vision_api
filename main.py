import detect_text
import os, json

for root, dirs, files in os.walk("data/"):
    print("{} files to process ...".format(len(files)))
    for file in files:
        detect_text.detect_text(os.path.join(root, file))

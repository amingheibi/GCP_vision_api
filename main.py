import detect_text
import os, json

for root, dirs, files in os.walk("data/"):
    for file in files:
        detect_text.detect_text(os.path.join(root, file))

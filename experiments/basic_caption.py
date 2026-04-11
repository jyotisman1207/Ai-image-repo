import torch

features = torch.load("image_features.pt")

def generate_caption(features):
    if features.mean() > 0.5:
        return "A bright image with objects"
    else:
        return "A dark or low contrast scene"

caption = generate_caption(features)

print("Generated Caption:", caption)

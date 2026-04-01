import torch

# Load saved features
features = torch.load("image_features.pt")

# Dummy caption generator
def generate_caption(features):
    # Simulating caption logic
    if features.mean() > 0.5:
        return "A bright image with objects"
    else:
        return "A dark or low contrast scene"

caption = generate_caption(features)

print("Generated Caption:", caption)

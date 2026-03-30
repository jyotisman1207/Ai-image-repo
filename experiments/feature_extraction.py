import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pretrained ResNet model
model = models.resnet18(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Load image
img = Image.open("sample.jpg").convert("RGB")
img = transform(img).unsqueeze(0)

# Extract features
with torch.no_grad():
    features = model(img)

print("Feature shape:", features.shape)

torch.save(features, "image_features.pt")

print("Features saved as image_features.pt")

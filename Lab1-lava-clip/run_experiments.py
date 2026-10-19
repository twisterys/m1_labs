import torch
import os
import glob
from PIL import Image
import pandas as pd
from transformers import CLIPProcessor, CLIPModel

device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

print("Loading CLIP...")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
print("CLIP loaded successfully.")

# Exercise 2 & 3
image = Image.open("image.jpg").convert("RGB")
print("Ex 2 - Image size:", image.size, "mode:", image.mode)

texts = [
    "a photo of a cat",
    "a photo of a dog",
    "a photo of a car",
    "a photo of a horse",
    "a photo of a person"
]

inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)
inputs = {k: v.to(device) for k, v in inputs.items()}
with torch.no_grad():
    outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)[0].cpu()

print("\n--- Exercise 3 Results ---")
for text, p in zip(texts, probs):
    print(f"{text:35s}: {p.item():.4f}")

# Exercise 4
def classify_image(img, classes):
    prompts = [f"a photo of a {c}" for c in classes]
    inp = processor(text=prompts, images=img, return_tensors="pt", padding=True)
    inp = {k: v.to(device) for k, v in inp.items()}
    with torch.no_grad():
        out = model(**inp)
    p = out.logits_per_image.softmax(dim=1)[0].cpu()
    idx = torch.argmax(p).item()
    return classes[idx], p[idx].item()

classes = ["cat", "dog", "car", "airplane", "horse", "bird"]
pred, prob = classify_image(image, classes)
print("\n--- Exercise 4 Zero-Shot ---")
print("Prediction:", pred, "Probability:", f"{prob:.4f}")

# Exercise 5: Evaluation
dataset = [
    ("dog1.jpg", "dog"),
    ("dog2.jpg", "dog"),
    ("cat1.jpg", "cat"),
    ("cat2.jpg", "cat"),
    ("car1.jpg", "car"),
    ("car2.jpg", "car"),
    ("horse1.jpg", "horse"),
    ("horse2.jpg", "horse"),
    ("bird1.jpg", "bird"),
    ("airplane1.jpg", "airplane")
]

eval_results = []
correct = 0
for img_path, actual in dataset:
    im = Image.open(img_path).convert("RGB")
    p_class, p_prob = classify_image(im, classes)
    is_corr = (p_class == actual)
    if is_corr:
        correct += 1
    eval_results.append({
        "Image": img_path,
        "Actual": actual,
        "Predicted": p_class,
        "Probability": f"{p_prob:.4f}",
        "Correct": is_corr
    })

accuracy = correct / len(dataset)
df_eval = pd.DataFrame(eval_results)
print("\n--- Exercise 5 Evaluation ---")
print(df_eval.to_string(index=False))
print(f"Accuracy: {accuracy:.2f} ({correct}/{len(dataset)})")

# Exercise 6: Prompt engineering
prompts_ex6 = [
    "a cat",
    "a photo of a cat",
    "a photograph showing a cat",
    "an image containing a cat",
    "a domestic animal called a cat"
]
cat_img = Image.open("cat1.jpg").convert("RGB")
inp6 = processor(text=prompts_ex6, images=cat_img, return_tensors="pt", padding=True)
inp6 = {k: v.to(device) for k, v in inp6.items()}
with torch.no_grad():
    out6 = model(**inp6)
probs6 = out6.logits_per_image.softmax(dim=1)[0].cpu()
print("\n--- Exercise 6 Prompt Engineering (on cat image) ---")
for pr, val in zip(prompts_ex6, probs6):
    print(f"{pr:35s}: {val.item():.4f}")

# Exercise 7 & 8: Retrieval
image_files = sorted([os.path.join("images", f) for f in os.listdir("images") if f.endswith(('.jpg', '.png', '.jpeg'))])
print(f"\nFound {len(image_files)} images for retrieval database.")

image_embeddings = []
for p in image_files:
    im = Image.open(p).convert("RGB")
    inp = processor(images=im, return_tensors="pt")
    inp = {k: v.to(device) for k, v in inp.items()}
    with torch.no_grad():
        emb = model.get_image_features(**inp)
        emb = emb / emb.norm(dim=-1, keepdim=True)
        image_embeddings.append(emb.cpu())

image_embeddings = torch.cat(image_embeddings, dim=0)

QUERY = "a person playing football"
inp_text = processor(text=[QUERY], return_tensors="pt")
inp_text = {k: v.to(device) for k, v in inp_text.items()}
with torch.no_grad():
    text_emb = model.get_text_features(**inp_text)
    text_emb = text_emb / text_emb.norm(dim=-1, keepdim=True)
    text_emb = text_emb.cpu()

sims = (image_embeddings @ text_emb.T).squeeze(1)
topk = torch.topk(sims, k=5)

print("\n--- Exercise 8 Top-5 Retrieval for Query:", QUERY, "---")
for rank, (idx, score) in enumerate(zip(topk.indices, topk.values), 1):
    print(f"Rank {rank}: {image_files[idx.item()]:25s} | Cosine Similarity: {score.item():.4f}")
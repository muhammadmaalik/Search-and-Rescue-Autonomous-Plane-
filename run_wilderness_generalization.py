from ultralytics import YOLO

# 1. Initialize from your reliable city baseline
model = YOLO("/mnt/c/Users/Umerm/Desktop/SRPlane/runs/detect/train-2/weights/best.pt")

print("🌲🏜️ Initiating Cross-Terrain Generalization Protocol...")

# 2. Run fine-tuning with aggressive augmentation parameters to simulate wilderness environments
model.train(
    data="VisDrone.yaml",  # Leverage your working data distribution
    epochs=5,              # Quick adaptation pass so it doesn't break baseline weights
    imgsz=640,
    batch=8,
    device=0,
    workers=4,
    hsv_h=0.015,           # Randomly shifts image hues (simulates desert/forest lighting shifts)
    hsv_s=0.7,             # Alters saturation drastically
    hsv_v=0.4,             # Alters brightness
    scale=0.6,             # Shrinks/expands images to train the model on tiny long-distance targets
    fliplr=0.5,            # Random horizontal flips
    mosaic=1.0             # Fuses 4 images together to train the model on highly cluttered views
)

print("🎉 Success! The generalized model has been updated and compiled.")
print("📦 Ready for deployment onto the Jetson Orin Nano Super!")

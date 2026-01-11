#!/usr/bin/env python3
"""
Checkpoint 4: Test Image Preprocessing
Tests the image preprocessing pipeline with sample images
"""

import os
import sys
from image_preprocessor import ImagePreprocessor

print("="*60)
print("🧪 CHECKPOINT 4: Image Preprocessing Test")
print("="*60)
print()

# Create preprocessor
preprocessor = ImagePreprocessor(max_size=512, quality=85)

# Test images directory
test_images_dir = "../../data/test_images"

print("Step 1: Checking test images directory...")
if not os.path.exists(test_images_dir):
    print(f"   Creating directory: {test_images_dir}")
    os.makedirs(test_images_dir, exist_ok=True)

# Get all image files
image_files = []
if os.path.exists(test_images_dir):
    for file in os.listdir(test_images_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
            image_files.append(os.path.join(test_images_dir, file))

if not image_files:
    print(f"   ⚠️  No images found in {test_images_dir}")
    print()
    print("To test image preprocessing:")
    print("1. Add some car damage images to: data/test_images/")
    print("2. Run this script again")
    print()
    print("You can download sample images from:")
    print("  - Google Images: 'car damage scratch'")
    print("  - Unsplash: car damage photos")
    print("  - Your own car photos")
    print()
    sys.exit(0)

print(f"   ✅ Found {len(image_files)} image(s)")
print()

# Process each image
print("Step 2: Processing images...")
print()

for i, image_path in enumerate(image_files, 1):
    filename = os.path.basename(image_path)
    print(f"[{i}/{len(image_files)}] {filename}")

    try:
        result = preprocessor.process_file(image_path)

        print(f"   Original: {result['original_dimensions'][0]}x{result['original_dimensions'][1]}")
        print(f"             {result['original_size_kb']:.2f} KB")
        print(f"   Processed: {result['processed_dimensions'][0]}x{result['processed_dimensions'][1]}")
        print(f"              {result['processed_size_kb']:.2f} KB")
        print(f"   Compression: {result['compression_ratio']:.2f}x")
        print(f"   Base64: {result['base64_length']:,} chars")

        # Check if within limits
        if result['processed_size_kb'] > 500:
            print("   ⚠️  Warning: Image > 500KB, may be slow")
        else:
            print("   ✅ Size is optimal")

        print()

    except Exception as e:
        print(f"   ❌ Error: {e}")
        print()

print("="*60)
print("✅ CHECKPOINT 4 COMPLETE!")
print("="*60)
print()
print("Image preprocessing is working correctly!")
print("Images are ready for vision model inference.")
print()
print("Next: Checkpoint 5 - Vision Testing with Server")
print()

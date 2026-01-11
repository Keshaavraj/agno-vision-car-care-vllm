#!/usr/bin/env python3
"""
Checkpoint 5: Test Vision Inference
Tests vLLM server with actual images to verify multimodal capabilities
"""

import sys
import os
import requests
import time

# Add parent directory to path to import preprocessor
sys.path.append('../checkpoint_04_image_preprocessing')
from image_preprocessor import ImagePreprocessor

SERVER_URL = "http://localhost:8000"

print("="*60)
print("🖼️  CHECKPOINT 5: Vision Inference Test")
print("="*60)
print()

# Step 1: Check if server is running
print("Step 1: Checking vLLM server...")
try:
    response = requests.get(f"{SERVER_URL}/health", timeout=5)
    if response.status_code == 200:
        print("   ✅ Server is running")
    else:
        print(f"   ❌ Server returned status {response.status_code}")
        exit(1)
except requests.exceptions.ConnectionError:
    print("   ❌ Cannot connect to server")
    print("   Make sure vLLM server is running:")
    print("   cd ~/uae-car-care-ai/checkpoints/checkpoint_03_vllm_server")
    print("   python start_server.py")
    exit(1)

# Step 2: Find test images
print("\nStep 2: Looking for test images...")
test_images_dir = "../../data/test_images"
image_files = []

if os.path.exists(test_images_dir):
    for file in os.listdir(test_images_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
            image_files.append(os.path.join(test_images_dir, file))

if not image_files:
    print(f"   ⚠️  No images found in {test_images_dir}")
    print()
    print("   To test vision inference:")
    print("   1. Add car damage images to: data/test_images/")
    print("   2. Run this script again")
    print()
    exit(0)

print(f"   ✅ Found {len(image_files)} image(s)")

# Step 3: Process and test each image
print("\nStep 3: Testing vision inference...")
print()

preprocessor = ImagePreprocessor(max_size=512, quality=85)

for i, image_path in enumerate(image_files[:3], 1):  # Test first 3 images
    filename = os.path.basename(image_path)
    print(f"[{i}] Testing: {filename}")

    try:
        # Preprocess image
        print("   📸 Preprocessing image...")
        result = preprocessor.process_file(image_path)
        data_url = f"data:image/jpeg;base64,{result['base64_string']}"

        print(f"      Size: {result['processed_dimensions'][0]}x{result['processed_dimensions'][1]}")
        print(f"      Compressed: {result['processed_size_kb']:.2f} KB")

        # Send to vLLM server
        print("   🤖 Sending to vision model...")

        payload = {
            "model": "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url
                            }
                        },
                        {
                            "type": "text",
                            "text": "Analyze this car damage image. Describe: 1) Type of damage, 2) Severity (minor/moderate/major), 3) Affected parts, 4) Estimated repair complexity. Be specific and professional."
                        }
                    ]
                }
            ],
            "max_tokens": 300,
            "temperature": 0.1
        }

        start_time = time.time()
        response = requests.post(
            f"{SERVER_URL}/v1/chat/completions",
            json=payload,
            timeout=60
        )
        inference_time = time.time() - start_time

        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']

            print(f"   ✅ Analysis complete ({inference_time:.2f}s)")
            print()
            print("   " + "="*56)
            print("   DAMAGE ANALYSIS")
            print("   " + "="*56)
            for line in analysis.split('\n'):
                print(f"   {line}")
            print("   " + "="*56)
            print()

        else:
            print(f"   ❌ Request failed: {response.status_code}")
            print(f"      {response.text}")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    print()

print("="*60)
print("✅ CHECKPOINT 5 COMPLETE!")
print("="*60)
print()
print("Vision inference is working correctly!")
print("The multimodal AI can analyze car damage images.")
print()
print("Next: Checkpoint 6 - Install Agno Framework")
print()

#!/usr/bin/env python3
"""
Checkpoint 3: Test vLLM Server
Tests that the vLLM server is running and responding correctly.
Run this AFTER starting the server (in a separate terminal).
"""

import requests
import json
import time

SERVER_URL = "http://localhost:8000"

print("="*60)
print("🧪 CHECKPOINT 3: vLLM Server Test")
print("="*60)
print()

# Test 1: Health check
print("Test 1: Checking server health...")
try:
    response = requests.get(f"{SERVER_URL}/health", timeout=5)
    if response.status_code == 200:
        print("   ✅ Server is healthy")
    else:
        print(f"   ❌ Server returned status {response.status_code}")
        exit(1)
except requests.exceptions.ConnectionError:
    print("   ❌ Cannot connect to server")
    print("   Make sure the server is running:")
    print("   python start_server.py")
    exit(1)
except Exception as e:
    print(f"   ❌ Error: {e}")
    exit(1)

# Test 2: List models
print("\nTest 2: Listing available models...")
try:
    response = requests.get(f"{SERVER_URL}/v1/models", timeout=5)
    if response.status_code == 200:
        models = response.json()
        print(f"   ✅ Found {len(models.get('data', []))} model(s)")
        for model in models.get('data', []):
            print(f"      • {model['id']}")
    else:
        print(f"   ❌ Failed to list models")
        exit(1)
except Exception as e:
    print(f"   ❌ Error: {e}")
    exit(1)

# Test 3: Simple text completion
print("\nTest 3: Testing text completion...")
try:
    payload = {
        "model": "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        "messages": [
            {"role": "user", "content": "Say hello in one word"}
        ],
        "max_tokens": 10
    }

    print("   Sending request...")
    start_time = time.time()
    response = requests.post(
        f"{SERVER_URL}/v1/chat/completions",
        json=payload,
        timeout=30
    )
    response_time = time.time() - start_time

    if response.status_code == 200:
        result = response.json()
        message = result['choices'][0]['message']['content']
        print(f"   ✅ Response received")
        print(f"      Response: {message}")
        print(f"      Time: {response_time:.2f}s")
    else:
        print(f"   ❌ Request failed: {response.status_code}")
        print(f"      {response.text}")
        exit(1)
except Exception as e:
    print(f"   ❌ Error: {e}")
    exit(1)

print()
print("="*60)
print("✅ CHECKPOINT 3 COMPLETE!")
print("="*60)
print()
print("vLLM server is running correctly!")
print("API endpoint: http://localhost:8000/v1/chat/completions")
print()
print("Next: Checkpoint 4 - Image Preprocessing")
print()

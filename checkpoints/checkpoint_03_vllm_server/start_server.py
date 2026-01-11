#!/usr/bin/env python3
"""
Checkpoint 3: Start vLLM Server
Simple Python script to start vLLM as OpenAI-compatible API server
"""

import subprocess
import sys
import os
from datetime import datetime

print("="*60)
print("🚀 CHECKPOINT 3: Starting vLLM Server")
print("="*60)
print()

# Configuration
MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4"
HOST = "0.0.0.0"
PORT = 8000
LOG_DIR = "../../logs"

# Step 1: Check GPU
print("Step 1: Checking GPU...")
try:
    result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'],
                          capture_output=True, text=True, check=True)
    print(f"   ✅ GPU: {result.stdout.strip()}")
except FileNotFoundError:
    print("   ❌ nvidia-smi not found!")
    sys.exit(1)
except subprocess.CalledProcessError:
    print("   ❌ GPU check failed!")
    sys.exit(1)

# Step 2: Check if port is free
print("\nStep 2: Checking port 8000...")
try:
    result = subprocess.run(['lsof', '-ti', f':{PORT}'],
                          capture_output=True, text=True)
    if result.stdout.strip():
        print(f"   ⚠️  Port {PORT} is in use")
        print(f"   Kill it? (y/n): ", end='')
        response = input()
        if response.lower() == 'y':
            pid = result.stdout.strip()
            subprocess.run(['kill', '-9', pid], check=False)
            print("   ✅ Process killed")
        else:
            print("   ❌ Cannot start server")
            sys.exit(1)
    else:
        print(f"   ✅ Port {PORT} is free")
except FileNotFoundError:
    print(f"   ⚠️  Cannot check port (lsof not found), continuing anyway...")

# Step 3: Check vLLM
print("\nStep 3: Checking vLLM installation...")
try:
    import vllm
    print(f"   ✅ vLLM {vllm.__version__} is installed")
except ImportError:
    print("   ❌ vLLM not installed!")
    print("   Run: pip install vllm")
    sys.exit(1)

# Step 4: Create logs directory
print("\nStep 4: Setting up logs...")
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"vllm_server_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
print(f"   ✅ Logs will be saved to: {log_file}")

# Step 5: Start server
print("\nStep 5: Starting vLLM server...")
print(f"   Model: {MODEL_NAME}")
print(f"   Endpoint: http://localhost:{PORT}/v1")
print(f"   API Docs: http://localhost:{PORT}/docs")
print()
print("   Configuration:")
print("   • Quantization: gptq_marlin")
print("   • Max context: 1024 tokens")
print("   • GPU memory: 75% utilization")
print("   • Max sequences: 1")
print()
print("   Press Ctrl+C to stop the server")
print("="*60)
print()

# Build command
cmd = [
    'python', '-m', 'vllm.entrypoints.openai.api_server',
    '--model', MODEL_NAME,
    '--host', HOST,
    '--port', str(PORT),
    '--quantization', 'gptq_marlin',
    '--max-model-len', '1024',
    '--gpu-memory-utilization', '0.75',
    '--enforce-eager',
    '--max-num-seqs', '1',
    '--dtype', 'float16',
    '--trust-remote-code'
]

# Run server (this will block until Ctrl+C)
try:
    # Open log file for writing
    with open(log_file, 'w') as log:
        # Start server and stream output to both console and log file
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        # Stream output
        for line in process.stdout:
            print(line, end='')
            log.write(line)
            log.flush()

        process.wait()

except KeyboardInterrupt:
    print("\n\n⚠️  Stopping server (Ctrl+C pressed)...")
    process.terminate()
    process.wait()
    print("✅ Server stopped")
except Exception as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)

#!/usr/bin/env python3
"""
Checkpoint 2: Test Qwen2-VL-2B Model Download & Loading
This script downloads and loads the model into GPU memory.
"""

import torch
from vllm import LLM
import time

def main():
    print("="*60)
    print("🚀 CHECKPOINT 2: Qwen2-VL-2B Model Loading Test")
    print("="*60)
    print()

    # Check CUDA availability
    print("📊 Checking GPU availability...")
    if not torch.cuda.is_available():
        print("❌ ERROR: CUDA not available!")
        print("   Make sure PyTorch was installed with CUDA support")
        exit(1)

    print(f"✅ CUDA Available: {torch.cuda.is_available()}")
    print(f"✅ GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"✅ GPU Count: {torch.cuda.device_count()}")
    print()

    # Model configuration
    MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4"

    print("📥 Downloading and loading model...")
    print(f"   Model: {MODEL_NAME}")
    print(f"   Size: ~2GB (GPTQ Int4 quantized)")
    print()
    print("⏳ This will take 5-10 minutes on first run (downloading)")
    print("   Subsequent runs will be faster (cached)")
    print()

    # Start timer
    start_time = time.time()

    try:
        # Load model with optimized settings for 4GB VRAM
        # Using gptq_marlin (recommended by vLLM, faster than gptq)
        llm = LLM(
            model=MODEL_NAME,
            quantization='gptq_marlin',    # GPTQ Marlin (faster & more stable)
            max_model_len=1024,            # Limit context length
            gpu_memory_utilization=0.75,  # Use 75% of VRAM (safe for 4GB)
            enforce_eager=True,            # Disable CUDA graphs (saves VRAM)
            trust_remote_code=True,        # Required for Qwen2-VL
            dtype='float16',               # FP16 precision
            max_num_seqs=1,                # Process 1 request at a time
        )

        load_time = time.time() - start_time

        print()
        print("="*60)
        print("✅ MODEL LOADED SUCCESSFULLY!")
        print("="*60)
        print(f"⏱️  Loading time: {load_time:.2f} seconds")
        print()

        # Check GPU memory usage
        if torch.cuda.is_available():
            allocated = torch.cuda.memory_allocated(0) / 1024**3  # GB
            reserved = torch.cuda.memory_reserved(0) / 1024**3    # GB
            print(f"📊 GPU Memory Usage:")
            print(f"   Allocated: {allocated:.2f} GB")
            print(f"   Reserved:  {reserved:.2f} GB")
            print(f"   Total VRAM: 4.00 GB")
            print()

            if allocated > 3.5:
                print("⚠️  WARNING: VRAM usage is high!")
                print("   You may encounter OOM errors during inference")
            else:
                print("✅ VRAM usage is within safe limits")

        print()
        print("="*60)
        print("🎯 CHECKPOINT 2 COMPLETE!")
        print("="*60)
        print()
        print("Next steps:")
        print("  1. Check VRAM usage with: nvidia-smi")
        print("  2. Continue to Checkpoint 3 (vLLM server)")
        print()

    except Exception as e:
        print()
        print("="*60)
        print("❌ ERROR LOADING MODEL")
        print("="*60)
        print(f"Error: {str(e)}")
        print()
        print("Common issues:")
        print("1. Out of memory: Reduce gpu_memory_utilization to 0.7")
        print("2. Model not found: Check internet connection")
        print("3. CUDA error: Restart terminal and try again")
        print("4. WSL multiprocessing: This script should fix it")
        print()
        exit(1)

if __name__ == '__main__':
    # Required for multiprocessing on Windows/WSL
    main()

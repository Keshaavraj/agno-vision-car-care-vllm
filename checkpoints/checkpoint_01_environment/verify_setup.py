#!/usr/bin/env python3
"""
Checkpoint 1: Verify Environment Setup
Quick verification that all dependencies are installed correctly.
"""

import sys

print("="*60)
print("🔍 CHECKPOINT 1: Environment Verification")
print("="*60)
print()

# Check Python version
print("1. Checking Python version...")
if sys.version_info < (3, 11):
    print(f"   ❌ Python {sys.version_info.major}.{sys.version_info.minor} is too old")
    print(f"   Need Python 3.11+")
    sys.exit(1)
else:
    print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

# Check PyTorch
print("\n2. Checking PyTorch...")
try:
    import torch
    print(f"   ✅ PyTorch {torch.__version__}")

    if torch.cuda.is_available():
        print(f"   ✅ CUDA Available: {torch.cuda.is_available()}")
        print(f"   ✅ GPU: {torch.cuda.get_device_name(0)}")
        print(f"   ✅ CUDA Version: {torch.version.cuda}")
    else:
        print("   ❌ CUDA not available!")
        sys.exit(1)
except ImportError:
    print("   ❌ PyTorch not installed")
    sys.exit(1)

# Check vLLM
print("\n3. Checking vLLM...")
try:
    import vllm
    print(f"   ✅ vLLM {vllm.__version__}")
except ImportError:
    print("   ❌ vLLM not installed")
    sys.exit(1)

# Check other dependencies
print("\n4. Checking supporting libraries...")
deps = ['PIL', 'numpy', 'psutil', 'requests', 'fastapi', 'uvicorn']
for dep in deps:
    try:
        if dep == 'PIL':
            import PIL
            print(f"   ✅ Pillow {PIL.__version__}")
        else:
            mod = __import__(dep)
            print(f"   ✅ {dep} {getattr(mod, '__version__', 'installed')}")
    except ImportError:
        print(f"   ⚠️  {dep} not installed (optional)")

print()
print("="*60)
print("✅ CHECKPOINT 1 COMPLETE!")
print("="*60)
print()
print("All dependencies are installed correctly.")
print("Next: Run checkpoint 2 to download the model")
print()

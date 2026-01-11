# ⏳ Checkpoint 3: vLLM Server Setup

## What This Does
Starts vLLM as an OpenAI-compatible API server:
- Serves Qwen2-VL-2B on http://localhost:8000
- OpenAI-compatible endpoints (/v1/chat/completions)
- Optimized for 4GB VRAM
- Can handle image + text inputs

## Status
⏳ **READY TO RUN**

## How to Run
```bash
cd checkpoints/checkpoint_03_vllm_server
chmod +x start_server.sh
./start_server.sh
```

## What It Does
1. Checks GPU availability
2. Checks if port 8000 is free
3. Activates virtual environment
4. Starts vLLM server with optimized flags
5. Logs output to `../../logs/vllm_server_*.log`

## Server Configuration
```bash
--model Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
--quantization gptq_marlin
--max-model-len 1024
--gpu-memory-utilization 0.75
--enforce-eager
--max-num-seqs 1
--dtype float16
--trust-remote-code
```

## API Endpoints (Once Running)
- **Chat Completions:** http://localhost:8000/v1/chat/completions
- **Models List:** http://localhost:8000/v1/models
- **API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health

## Test the Server
After starting, open a new terminal and run:
```bash
python test_server.py
```

## Files
- `start_server.sh` - Server startup script
- `test_server.py` - Server health check script
- `README.md` - This file

## Expected Output
```
========================================
  vLLM Server for Qwen2-VL-2B (GPTQ)
  Optimized for RTX 500 (4GB VRAM)
========================================

[1/5] Checking GPU availability...
GPU detected: NVIDIA RTX 500 Ada Generation Laptop GPU, 4096 MiB, 573.76

[2/5] Checking if port 8000 is available...
✓ Port 8000 is free

[3/5] Activating virtual environment...
✓ Virtual environment activated

[4/5] vLLM environment ready
Python: Python 3.12.3
vLLM: 0.13.0

[5/5] Starting vLLM server...
Model: Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
Endpoint: http://localhost:8000/v1
API Docs: http://localhost:8000/docs

Server Configuration:
  • Quantization: gptq_marlin
  • Max context: 1024 tokens
  • GPU memory: 75% utilization
  • CUDA graphs: Disabled (saves VRAM)
  • Max sequences: 1 (stable memory)

Press Ctrl+C to stop the server
========================================

INFO: Started server process [12345]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## Troubleshooting

### Port already in use
```bash
# Find and kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

### Out of memory
Edit `start_server.sh` and reduce:
```bash
--gpu-memory-utilization 0.7  # Instead of 0.75
```

### Model not found
Model should already be cached from Checkpoint 2.
If not, it will auto-download on first start.

## Next Step
Continue to Checkpoint 4: Image Preprocessing

# 🚀 Checkpoint 3: vLLM Server - Instructions

## What You'll Do
Start the vLLM server as an OpenAI-compatible API on port 8000.

---

## Step-by-Step Instructions

### **Step 1: Activate virtual environment**
```bash
cd ~/uae-car-care-ai
source venv/bin/activate
```
**Important:** You must see `(venv)` in your terminal prompt!

### **Step 2: Navigate to checkpoint folder**
```bash
cd checkpoints/checkpoint_03_vllm_server
```

### **Step 3: Start the server**
```bash
python start_server.py
```

**What will happen:**
1. ✅ Checks GPU availability
2. ✅ Checks if port 8000 is free
3. ✅ Verifies vLLM is installed
4. ✅ Creates log file
5. 🚀 Starts vLLM server

**Expected output:**
```
============================================================
🚀 CHECKPOINT 3: Starting vLLM Server
============================================================

Step 1: Checking GPU...
   ✅ GPU: NVIDIA RTX 500 Ada Generation, 4096 MiB

Step 2: Checking port 8000...
   ✅ Port 8000 is free

Step 3: Checking vLLM installation...
   ✅ vLLM 0.13.0 is installed

Step 4: Setting up logs...
   ✅ Logs will be saved to: ../../logs/vllm_server_*.log

Step 5: Starting vLLM server...
   Model: Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
   Endpoint: http://localhost:8000/v1
   API Docs: http://localhost:8000/docs

   Configuration:
   • Quantization: gptq_marlin
   • Max context: 1024 tokens
   • GPU memory: 75% utilization
   • Max sequences: 1

   Press Ctrl+C to stop the server
============================================================

[... server logs will appear here ...]

INFO: Started server process [12345]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

⏱️ **Time:** Server starts in 15-30 seconds

---

### **Step 3: Test the server (in a NEW terminal)**

**Open a new terminal and run:**
```bash
cd ~/uae-car-care-ai/checkpoints/checkpoint_03_vllm_server
source ../../venv/bin/activate
python test_server.py
```

**Expected output:**
```
============================================================
🧪 CHECKPOINT 3: vLLM Server Test
============================================================

Test 1: Checking server health...
   ✅ Server is healthy

Test 2: Listing available models...
   ✅ Found 1 model(s)
      • Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4

Test 3: Testing text completion...
   Sending request...
   ✅ Response received
      Response: Hello
      Time: 2.34s

============================================================
✅ CHECKPOINT 3 COMPLETE!
============================================================

vLLM server is running correctly!
API endpoint: http://localhost:8000/v1/chat/completions

Next: Checkpoint 4 - Image Preprocessing
```

---

## Summary

**Terminal 1 (Server):**
```bash
cd ~/uae-car-care-ai/checkpoints/checkpoint_03_vllm_server
python start_server.py
# Keep this running...
```

**Terminal 2 (Testing):**
```bash
cd ~/uae-car-care-ai/checkpoints/checkpoint_03_vllm_server
source ../../venv/bin/activate
python test_server.py
```

---

## Troubleshooting

### Port already in use
The script will ask if you want to kill it. Say 'y'.

### Out of memory error
Edit `start_server.py` and change:
```python
'--gpu-memory-utilization', '0.7',  # Instead of 0.75
```

### Server won't start
Check the log file in `../../logs/vllm_server_*.log`

---

## Files in This Checkpoint
- `start_server.py` - Starts the vLLM server
- `test_server.py` - Tests the server
- `INSTRUCTIONS.md` - This file
- `README.md` - Detailed information

---

## Next Step
When tests pass, continue to Checkpoint 4!

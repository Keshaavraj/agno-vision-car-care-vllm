# 🖼️ Checkpoint 5: Vision Testing - Instructions

## Prerequisites

### **1. vLLM Server MUST be running**

**Check if it's running:**
```bash
curl http://localhost:8000/health
```

If you get an error, start the server:
```bash
cd ~/uae-car-care-ai/checkpoints/checkpoint_03_vllm_server
python start_server.py
# Keep this running in another terminal
```

### **2. Test images needed**

Add 2-3 car damage images to:
```
~/uae-car-care-ai/data/test_images/
```

---

## Step-by-Step Instructions

### **Step 1: Navigate to checkpoint folder**
```bash
cd ~/uae-car-care-ai
source venv/bin/activate
cd checkpoints/checkpoint_05_vision_test
```

### **Step 2: Run vision test**
```bash
python test_vision_inference.py
```

**Expected output:**
```
============================================================
🖼️  CHECKPOINT 5: Vision Inference Test
============================================================

Step 1: Checking vLLM server...
   ✅ Server is running

Step 2: Looking for test images...
   ✅ Found 3 image(s)

Step 3: Testing vision inference...

[1] Testing: car_scratch.jpg
   📸 Preprocessing image...
      Size: 512x384
      Compressed: 48.23 KB
   🤖 Sending to vision model...
   ✅ Analysis complete (8.45s)

   ════════════════════════════════════════════════════════
   DAMAGE ANALYSIS
   ════════════════════════════════════════════════════════
   Type of damage: Horizontal scratch on front bumper

   Severity: Minor (2/10)
   - Cosmetic damage only
   - No structural issues
   - Paint layer affected

   Affected parts:
   - Front bumper (center section)
   - Paint clear coat damaged
   - Possible primer exposure

   Repair complexity: Low to Medium
   - Surface preparation required
   - Paint matching needed
   - Clear coat application
   - Estimated time: 2-3 hours
   - Suitable for local body shop repair
   ════════════════════════════════════════════════════════

[2] Testing: dent.png
   ...

============================================================
✅ CHECKPOINT 5 COMPLETE!
============================================================

Vision inference is working correctly!
The multimodal AI can analyze car damage images.

Next: Checkpoint 6 - Install Agno Framework
```

---

## What This Proves

✅ **vLLM server works** with vision models
✅ **Multimodal inference** processes images correctly
✅ **Qwen2-VL-2B** understands car damage
✅ **Image preprocessing** optimizes for inference
✅ **End-to-end pipeline** is functional

---

## Troubleshooting

### Server not running
```
❌ Cannot connect to server
```
**Solution:** Start vLLM server in another terminal

### No images found
```
⚠️  No images found in data/test_images/
```
**Solution:** Add car damage images to the folder

### Slow inference (>20s)
**Causes:**
- Large images (should be <500KB after preprocessing)
- CPU inference instead of GPU
- High system load

**Check GPU usage:**
```bash
nvidia-smi
```

### Error: Out of memory
**Solution:** Reduce image quality in preprocessing:
```python
preprocessor = ImagePreprocessor(max_size=384, quality=75)  # Smaller
```

---

## Performance Notes

**Expected times (RTX 500 4GB):**
- Image preprocessing: <1 second
- Vision inference: 5-15 seconds
- Total per image: 6-16 seconds

**Token usage:**
- 512x512 image ≈ 500-800 tokens
- Text prompt ≈ 50-100 tokens
- Response ≈ 200-300 tokens
- Total ≈ 750-1200 tokens (within 1024 limit ✅)

---

## Next Step

Once vision inference works, continue to **Checkpoint 6** to install Agno framework!

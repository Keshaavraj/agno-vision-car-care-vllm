# 📸 Checkpoint 4: Image Preprocessing - Instructions

## What You'll Do
Create and test image preprocessing utilities for the vision model.

---

## Step-by-Step Instructions

### **Step 1: Add test images** (if you don't have any yet)

**Option A: Download sample car damage images**
1. Go to Google Images and search: "car scratch damage"
2. Download 2-3 images
3. Save them to: `~/uae-car-care-ai/data/test_images/`

**Option B: Use your own car photos**
- Any car damage photos will work
- Scratches, dents, broken parts, etc.

---

### **Step 2: Navigate to checkpoint folder**
```bash
cd ~/uae-car-care-ai
source venv/bin/activate
cd checkpoints/checkpoint_04_image_preprocessing
```

---

### **Step 3: Test the preprocessor**
```bash
python test_preprocessing.py
```

**Expected output:**
```
============================================================
🧪 CHECKPOINT 4: Image Preprocessing Test
============================================================

Step 1: Checking test images directory...
   ✅ Found 3 image(s)

Step 2: Processing images...

[1/3] car_scratch.jpg
   Original: 4032x3024
             2456.78 KB
   Processed: 512x384
              48.23 KB
   Compression: 50.93x
   Base64: 66,234 chars
   ✅ Size is optimal

[2/3] dent.png
   Original: 1920x1080
             856.45 KB
   Processed: 512x288
              35.67 KB
   Compression: 24.01x
   Base64: 48,956 chars
   ✅ Size is optimal

[3/3] broken_light.jpg
   Original: 3264x2448
             1893.22 KB
   Processed: 512x384
              52.11 KB
   Compression: 36.33x
   Base64: 71,589 chars
   ✅ Size is optimal

============================================================
✅ CHECKPOINT 4 COMPLETE!
============================================================

Image preprocessing is working correctly!
Images are ready for vision model inference.

Next: Checkpoint 5 - Vision Testing with Server
```

---

### **Step 4: Test with a single image (optional)**
```bash
python image_preprocessor.py
```

This runs the example in the preprocessor script.

---

## What Just Happened?

✅ **Image Resizing:** All images scaled to max 512x512
✅ **Compression:** Images reduced by 20-50x
✅ **Base64 Encoding:** Ready for API transmission
✅ **Validation:** All images < 500KB

---

## Troubleshooting

### No images found
```
⚠️  No images found in data/test_images/
```
**Solution:** Add some car damage images to the folder

### Image too large warning
```
⚠️  Warning: Image > 500KB, may be slow
```
**Solution:** The preprocessor will still work, but you can:
- Reduce quality: Edit `test_preprocessing.py`, change `quality=85` to `quality=75`
- Reduce size: Change `max_size=512` to `max_size=384`

### Import error
```
ModuleNotFoundError: No module named 'PIL'
```
**Solution:**
```bash
pip install Pillow
```

---

## Next Step

Once preprocessing works, continue to **Checkpoint 5** where we'll test vision inference with the vLLM server!

---

## Files Created
- `image_preprocessor.py` - Preprocessing utility class
- `test_preprocessing.py` - Test script
- Sample processed images ready for inference

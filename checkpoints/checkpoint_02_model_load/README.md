# ✅ Checkpoint 2: Model Download & Load Test

## What This Does
Downloads and tests the Qwen2-VL-2B-GPTQ-Int4 model:
- Downloads model from Hugging Face (~2.48GB)
- Loads model into GPU memory
- Verifies VRAM usage is within limits
- Tests model initialization

## Status
✅ **COMPLETED**

## What Happened
```bash
python test_model_load.py
```

## Results
- ✅ Model: Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
- ✅ Download size: 2.48GB
- ✅ Download time: ~1:47
- ✅ Model loading: 2.35 GB VRAM
- ✅ KV cache: 0.46 GB VRAM
- ✅ Total VRAM: ~2.8-3 GB (out of 4GB)
- ✅ Quantization: gptq_marlin (faster kernel)
- ✅ Loading time: 152.96 seconds

## Configuration Used
```python
LLM(
    model='Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4',
    quantization='gptq_marlin',
    max_model_len=1024,
    gpu_memory_utilization=0.75,
    enforce_eager=True,
    dtype='float16',
    max_num_seqs=1
)
```

## Files
- `test_model_load.py` - Model download & load test script

## Next Step
Continue to Checkpoint 3: vLLM Server Setup

# 🏗️ UAE Car Care AI - Architecture (Agno + vLLM + Qwen)

## 🎯 **100% FREE Open-Source Tech Stack**

### **Goal:** Impress recruiters with modern AI architecture using completely free, on-premise tools

---

## 🔥 **Core Architecture**

```
┌──────────────────────────────────────────────────────┐
│         React + Vite Frontend (Mobile-First)         │
│  ┌────────────┐  ┌─────────────┐  ┌──────────────┐  │
│  │  Camera    │  │   Results   │  │  Workshop    │  │
│  │  Upload    │  │   Display   │  │    List      │  │
│  └────────────┘  └─────────────┘  └──────────────┘  │
│         http://localhost:5173 (Dev) / 3000 (Prod)    │
└───────────────────────┬──────────────────────────────┘
                        │
                  (REST API Call)
                        │
              http://localhost:8000/api
                        │
┌───────────────────────▼──────────────────────────────┐
│         Agno Multi-Agent System (Python)             │
│  ┌────────────┐  ┌─────────────┐  ┌──────────────┐  │
│  │  Vision    │  │   Price     │  │  Workshop    │  │
│  │   Agent    │  │   Agent     │  │   Agent      │  │
│  └─────┬──────┘  └──────┬──────┘  └──────┬───────┘  │
│        │                │                │           │
│        └────────────────┴────────────────┘           │
│                       │                              │
│              ┌────────▼────────┐                     │
│              │  Coordinator    │                     │
│              │     Agent       │                     │
│              └────────┬────────┘                     │
└───────────────────────┼──────────────────────────────┘
                        │
                  (HTTP Request)
                        │
              http://localhost:8000/v1
                        │
┌───────────────────────▼──────────────────────────────┐
│           vLLM Server (OpenAI-Compatible API)        │
│  - Serves: Qwen2-VL-2B-Instruct-GPTQ-Int4            │
│  - GPU-Accelerated (NVIDIA RTX 500)                  │
│  - Optimized for 4GB VRAM                            │
└───────────────────────┬──────────────────────────────┘
                        │
              ┌─────────▼─────────┐
              │  Qwen2-VL-2B      │
              │  (GPTQ Int4)      │
              │  Multimodal Model │
              └───────────────────┘
```

---

## 💎 **Tech Stack (100% Free & Open-Source)**

### **1. Frontend: React + Vite**
- **What:** Modern React framework with lightning-fast build tool
- **Why:** Vite is 10x faster than Webpack, instant hot-reload
- **Cost:** FREE (MIT License)
- **Features:**
  - Mobile-first responsive design
  - Native camera access
  - Real-time image preview
  - Fast builds (~5 seconds)
  - Instant hot module replacement (HMR)

### **2. Multi-Agent Framework: Agno**
- **What:** Modern Python framework for building coordinated AI agents
- **Why:** 36k GitHub stars, production-ready, built-in state management
- **Cost:** FREE (Apache 2.0 License)
- **GitHub:** https://github.com/agno-agi/agno

### **3. Inference Server: vLLM**
- **What:** High-performance LLM inference engine with OpenAI-compatible API
- **Why:** 2-5x faster than standard inference, optimized for GPU
- **Cost:** FREE (Apache 2.0 License)
- **Features:**
  - PagedAttention (efficient memory)
  - GPTQ quantization support
  - Continuous batching
  - OpenAI-compatible endpoints

### **4. Model: Qwen2-VL-2B-Instruct-GPTQ-Int4**
- **What:** Multimodal vision-language model (Alibaba Cloud)
- **Why:** Excellent vision understanding, fits in 4GB VRAM
- **Size:** ~2GB (Int4 quantized)
- **Cost:** FREE (Apache 2.0 License)
- **Capabilities:**
  - Image understanding
  - Text generation
  - Visual reasoning

### **5. Hardware: NVIDIA RTX 500 (4GB VRAM)**
- **Your GPU:** RTX 500 Ada Generation
- **VRAM:** 4GB dedicated
- **Why it works:** GPTQ Int4 quantization fits perfectly
- **Optimization:** 75% GPU memory utilization (leaves room for OS)

---

## 🎨 **Agent Architecture**

### **Agent 1: Vision Agent (Damage Analyzer)**
```python
Name: "Car Damage Analyzer"
Model: Qwen2-VL-2B via vLLM (local)
API Endpoint: http://localhost:8000/v1/chat/completions

Input: Car damage image (Base64 encoded)
Output:
  - Damage type (scratch, dent, broken part)
  - Severity (minor, moderate, major)
  - Affected parts (bumper, door, etc.)
  - Repair complexity

Tools: None (pure multimodal inference)
```

### **Agent 2: Price Estimation Agent**
```python
Name: "Repair Cost Estimator"
Model: Qwen2-VL-2B via vLLM (text mode)
API Endpoint: http://localhost:8000/v1/chat/completions

Input: Damage analysis from Vision Agent
Output:
  - Parts needed
  - Labor hours
  - Cost estimate in AED (min-max range)

Tools: SQLite MCP (pricing database)
Knowledge: UAE market repair costs
```

### **Agent 3: Workshop Finder Agent**
```python
Name: "Workshop Locator"
Model: Qwen2-VL-2B via vLLM (text mode)
API Endpoint: http://localhost:8000/v1/chat/completions

Input: Location, car brand, damage type
Output:
  - Top 5 workshops
  - Ratings, distance, specialization
  - Price comparison

Tools: Google Maps MCP (optional), SQLite MCP
Knowledge: Workshop database (UAE)
```

### **Agent 4: Coordinator Agent**
```python
Name: "Multi-Agent Coordinator"
Model: Qwen2-VL-2B via vLLM (text mode)

Role: Orchestrates all agents
Flow:
  1. Receives user image + location
  2. Sends to Vision Agent → damage analysis
  3. Sends to Price Agent → cost estimate
  4. Sends to Workshop Agent → locations
  5. Combines all results → final report
```

---

## 🔧 **vLLM Configuration (Optimized for 4GB VRAM)**

### **Server Launch Flags:**
```bash
python -m vllm.entrypoints.openai.api_server \
  --model "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4" \
  --host "0.0.0.0" \
  --port 8000 \
  --quantization gptq \
  --max-model-len 1024 \
  --gpu-memory-utilization 0.75 \
  --enforce-eager \
  --max-num-seqs 1 \
  --dtype float16 \
  --trust-remote-code
```

### **Flag Explanations:**
| Flag | Purpose | Why Important |
|------|---------|---------------|
| `--quantization gptq` | Use GPTQ Int4 quantization | Model fits in 4GB VRAM |
| `--max-model-len 1024` | Limit context length | Prevents OOM errors |
| `--gpu-memory-utilization 0.75` | Use only 75% VRAM | Leaves room for Windows OS |
| `--enforce-eager` | Disable CUDA graphs | Saves ~1GB VRAM |
| `--max-num-seqs 1` | Process 1 request at a time | Minimizes memory spikes |
| `--dtype float16` | FP16 precision | Memory efficient |

---

## 🌐 **API Integration (Agno ↔ vLLM)**

### **Agno Configuration:**
```python
from agno import Agent
from agno.models.openai import OpenAI

# Configure Agno to use LOCAL vLLM server (not OpenAI cloud!)
vision_agent = Agent(
    name="Car Damage Analyzer",
    model=OpenAI(
        id="Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        api_key="not-needed",  # vLLM doesn't require auth
        base_url="http://localhost:8000/v1"  # LOCAL vLLM endpoint
    ),
    description="UAE car repair expert",
    instructions=[
        "Analyze car damage from photos",
        "Identify damage type, severity, parts",
        "Be specific and professional"
    ],
    markdown=True
)
```

### **Why This Works:**
- ✅ vLLM mimics OpenAI API format
- ✅ Agno thinks it's talking to OpenAI
- ✅ Actually uses YOUR local Qwen model
- ✅ NO cloud API, NO internet needed for inference
- ✅ 100% FREE, 100% on-premise

---

## 📊 **Data Flow**

### **User Journey:**
```
1. User opens React app (http://localhost:5173)
        ↓
2. Clicks "Take Photo" → Opens camera (mobile) or file picker
        ↓
3. Captures/uploads car damage photo
        ↓
4. React preprocesses image (resize to 512x512, Base64 encode)
        ↓
5. Frontend → Agno Backend API (POST /api/analyze)
        ↓
3. Coordinator Agent receives request
        ↓
4. Vision Agent:
   - Encodes image to Base64
   - Sends to vLLM: POST /v1/chat/completions
   - vLLM runs Qwen2-VL-2B on GPU
   - Returns damage analysis
        ↓
5. Price Agent:
   - Takes damage analysis
   - Queries SQLite via MCP
   - Sends to vLLM for reasoning
   - Returns cost estimate
        ↓
6. Workshop Agent:
   - Takes location + damage type
   - Queries workshop database
   - Sends to vLLM for recommendations
   - Returns top 5 workshops
        ↓
7. Coordinator combines all results
        ↓
8. Backend → Frontend (JSON response)
        ↓
9. React renders comprehensive report:
   - Damage analysis card
   - Cost breakdown
   - Workshop list with map
   - Insurance advice
```

---

## 🚀 **Performance Expectations**

### **On Your Hardware (RTX 500 + 32GB RAM):**

| Task | Expected Time |
|------|---------------|
| Model Loading (cold start) | 10-15 seconds |
| Image Analysis (Vision Agent) | 5-10 seconds |
| Text Generation (Price/Workshop) | 2-5 seconds |
| Full Pipeline (all agents) | 15-25 seconds |
| VRAM Usage | 3-3.5 GB (out of 4GB) |
| System RAM Usage | 8-10 GB (out of 32GB) |

### **Performance Optimizations:**
- ✅ GPTQ Int4 quantization (4x memory reduction)
- ✅ Image preprocessing (resize to 512x512)
- ✅ Eager execution (no CUDA graph overhead)
- ✅ Single sequence processing (stable memory)

---

## 🔐 **Why Recruiters Will Be Impressed**

### **1. Modern AI Framework (Agno)**
> "I used Agno, a cutting-edge multi-agent framework with 36k GitHub stars. It's production-ready with built-in state management and agent coordination."

### **2. High-Performance Inference (vLLM)**
> "I deployed vLLM for GPU-accelerated inference, achieving 2-5x speedup compared to standard inference. It's optimized for production workloads."

### **3. Multimodal AI (Qwen2-VL)**
> "The system uses Qwen2-VL-2B, a state-of-the-art multimodal model that understands both images and text. Perfect for car damage assessment."

### **4. Resource Optimization**
> "I optimized the entire stack to run on a 4GB GPU using GPTQ quantization and memory-efficient configurations. This shows understanding of production constraints."

### **5. 100% Free & Open-Source**
> "The entire tech stack is open-source and runs on-premise. No API costs, no vendor lock-in, full control over the system."

### **6. Multi-Agent Architecture**
> "I built a coordinated multi-agent system where specialized agents (Vision, Pricing, Workshop) work together. This mirrors enterprise AI architectures."

---

## 📝 **Repository Structure**

```
uae-car-care-ai/
├── frontend/                    # React + Vite UI (NEW!)
│   ├── src/
│   │   ├── components/
│   │   │   ├── CameraUpload.jsx     # Photo capture
│   │   │   ├── DamageReport.jsx     # Results display
│   │   │   ├── WorkshopCard.jsx     # Workshop list item
│   │   │   ├── LoadingSpinner.jsx   # Loading state
│   │   │   └── ErrorBoundary.jsx    # Error handling
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx             # Landing page
│   │   │   └── Results.jsx          # Analysis results
│   │   │
│   │   ├── services/
│   │   │   └── api.js               # Backend API calls
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js (optional)
│
├── vllm_server/
│   ├── start_server.sh          # Launch vLLM with optimized flags
│   ├── test_server.py           # Health check script
│   └── config.yaml              # Server configuration
│
├── backend/
│   ├── agents/
│   │   ├── vision_agent.py      # Multimodal damage analyzer
│   │   ├── price_agent.py       # Cost estimator (MCP + vLLM)
│   │   ├── workshop_agent.py    # Location finder (MCP + vLLM)
│   │   └── coordinator.py       # Orchestrates all agents
│   │
│   ├── api/
│   │   ├── routes.py            # FastAPI endpoints
│   │   └── middleware.py        # CORS, error handling
│   │
│   ├── app.py                   # Main Agno application
│   ├── server.py                # FastAPI server
│   └── requirements.txt
│
├── client/
│   ├── test_vision.py           # Test vision agent
│   ├── test_full_pipeline.py   # End-to-end test
│   └── performance_monitor.py  # TTFT, TPS metrics
│
├── utils/
│   ├── image_preprocessor.py   # Resize/compress images
│   └── monitor_vram.py         # GPU memory monitoring
│
├── data/
│   ├── test_images/             # Sample car damage photos
│   ├── workshops.db             # SQLite database
│   └── pricing.db               # Repair cost data
│
├── logs/                        # vLLM server logs
├── docs/
│   ├── ARCHITECTURE_VLLM.md     # This file
│   ├── SETUP_GUIDE.md           # Step-by-step installation
│   └── DEMO_SCRIPT.md           # How to demo to recruiters
│
└── README.md                    # Main documentation
```

---

## 🎯 **Key Differentiators (vs Generic Projects)**

| Feature | This Project | Typical Projects |
|---------|--------------|------------------|
| Framework | Agno (modern multi-agent) | LangChain (common) |
| Inference | vLLM (production-grade) | Direct model calls |
| Model | Qwen2-VL (multimodal) | Text-only LLMs |
| Architecture | Multi-agent coordination | Single agent |
| Optimization | GPTQ, memory-tuned | Default settings |
| Cost | 100% free, on-premise | Often uses paid APIs |

---

## 📚 **Technical Terms for Resume/Interviews**

**When describing this project, use:**
- Multi-agent orchestration
- GPU-accelerated inference
- GPTQ quantization (Int4)
- OpenAI-compatible API endpoints
- Multimodal vision-language models
- Production-optimized deployment
- Resource-constrained optimization
- Agent-to-agent communication (A2A)
- Model Context Protocol (MCP)
- FastAPI asynchronous runtime

---

## 🔗 **Resources**

- **Agno:** https://github.com/agno-agi/agno
- **vLLM:** https://github.com/vllm-project/vllm
- **Qwen2-VL:** https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
- **GPTQ:** https://arxiv.org/abs/2210.17323

---

**This architecture demonstrates:**
✅ Modern AI frameworks
✅ Production inference optimization
✅ Multimodal AI capabilities
✅ Resource-efficient deployment
✅ Enterprise-grade multi-agent systems
✅ 100% open-source approach

**Perfect for impressing technical recruiters!** 🚀

# 🚀 UAE Car Care AI - Build Guide with Checkpoints

## 🎯 **Goal:** Build Agno + vLLM + Qwen2-VL multimodal AI system (100% FREE)

**Timeline:** 7-10 days
**Hardware:** NVIDIA RTX 500 (4GB VRAM) + 32GB RAM ✅

---

## ✅ **CHECKPOINT 1: Environment Setup** (Day 1)

### **Objective:** Get Python, vLLM, and GPU working

### **Steps:**

**1.1 Navigate to project & activate venv**
```bash
cd ~/uae-car-care-ai
source venv/bin/activate
```

**1.2 Verify GPU is accessible**
```bash
nvidia-smi
```
✅ **Expected:** See "NVIDIA RTX 500 Ada Generation"

**1.3 Upgrade pip**
```bash
pip install --upgrade pip
```

**1.4 Install PyTorch with CUDA 12.1**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
⏱️ **Time:** 3-5 minutes

**1.5 Verify PyTorch sees GPU**
```bash
python -c "import torch; print('CUDA:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0))"
```
✅ **Expected:** `CUDA: True` and `GPU: NVIDIA RTX 500...`

**1.6 Install vLLM**
```bash
pip install vllm
```
⏱️ **Time:** 2-3 minutes

**1.7 Verify vLLM installation**
```bash
python -c "import vllm; print('vLLM version:', vllm.__version__)"
```
✅ **Expected:** Version number (e.g., 0.6.x)

**1.8 Install supporting libraries**
```bash
pip install Pillow numpy psutil gputil requests python-dotenv
```

**1.9 Freeze requirements**
```bash
pip freeze > requirements.txt
```

### **✅ Checkpoint 1 Complete When:**
- [x] `nvidia-smi` shows your GPU
- [x] PyTorch `torch.cuda.is_available()` returns `True`
- [x] vLLM imports without errors
- [x] `requirements.txt` created

### **🎯 Test Command:**
```bash
python -c "import torch, vllm; print('✅ Ready for Checkpoint 2')"
```

---

## ✅ **CHECKPOINT 2: Download & Test Qwen2-VL Model** (Day 1-2)

### **Objective:** Get Qwen2-VL-2B model and verify vLLM can load it

### **Steps:**

**2.1 Create model cache directory**
```bash
mkdir -p ~/.cache/huggingface
```

**2.2 Download Qwen2-VL-2B-GPTQ-Int4 model**
```bash
# This will auto-download on first use, or you can pre-download:
huggingface-cli download Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
```
⏱️ **Time:** 10-20 minutes (model is ~2GB)

**Alternative:** Let vLLM auto-download on first start (easier)

**2.3 Test vLLM can load the model (dry run)**
```bash
python -c "
from vllm import LLM
print('Loading Qwen2-VL-2B...')
llm = LLM(
    model='Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4',
    quantization='gptq',
    max_model_len=1024,
    gpu_memory_utilization=0.75,
    enforce_eager=True,
    trust_remote_code=True
)
print('✅ Model loaded successfully!')
"
```
⏱️ **Time:** 10-15 seconds (first time loading)

✅ **Expected:** Model loads without OOM errors

### **✅ Checkpoint 2 Complete When:**
- [x] Model downloaded to cache
- [x] vLLM loads model without errors
- [x] No CUDA OOM errors
- [x] GPU shows ~3-3.5GB VRAM usage

### **🎯 Test Command:**
```bash
nvidia-smi  # Check VRAM usage
```

---

## ✅ **CHECKPOINT 3: vLLM Server Setup** (Day 2)

### **Objective:** Start vLLM as OpenAI-compatible API server

### **Steps:**

**3.1 Create server launch script**
```bash
touch vllm_server/start_server.sh
chmod +x vllm_server/start_server.sh
```

**3.2 Add startup script content**
(I'll provide this in the next step - it's the bash script with all flags)

**3.3 Start vLLM server**
```bash
cd ~/uae-car-care-ai
./vllm_server/start_server.sh
```
⏱️ **Time:** 10-15 seconds to start

✅ **Expected:** Server logs show "Uvicorn running on http://0.0.0.0:8000"

**3.4 Test server health (in new terminal)**
```bash
curl http://localhost:8000/v1/models
```
✅ **Expected:** JSON response with model info

**3.5 Test simple text completion**
```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
    "messages": [{"role": "user", "content": "Say hello"}]
  }'
```
✅ **Expected:** JSON response with "Hello" or similar

### **✅ Checkpoint 3 Complete When:**
- [x] vLLM server starts without errors
- [x] `/v1/models` endpoint returns model info
- [x] `/v1/chat/completions` returns text responses
- [x] Server runs stably (no crashes)

### **🎯 Test Command:**
```bash
curl http://localhost:8000/health
```

---

## ✅ **CHECKPOINT 4: Image Preprocessing Utility** (Day 2-3)

### **Objective:** Create utility to resize/compress images before sending to model

### **Steps:**

**4.1 Create image preprocessor**
```bash
touch utils/image_preprocessor.py
```

**4.2 Add preprocessing logic**
(Resize to 512x512, compress to <500KB, convert to Base64)

**4.3 Test with sample image**
```bash
python utils/image_preprocessor.py data/test_images/sample_car.jpg
```
✅ **Expected:** Processed image < 500KB, 512x512 dimensions

### **✅ Checkpoint 4 Complete When:**
- [x] Can process images of any size
- [x] Output is always < 500KB
- [x] Base64 encoding works
- [x] Maintains aspect ratio

---

## ✅ **CHECKPOINT 5: Test Multimodal Vision** (Day 3)

### **Objective:** Verify Qwen2-VL can analyze car damage images

### **Steps:**

**5.1 Download sample car damage images**
```bash
# Add 3-5 sample images to data/test_images/
```

**5.2 Create vision test script**
```bash
touch client/test_vision.py
```

**5.3 Test image analysis via API**
```bash
python client/test_vision.py data/test_images/car_scratch.jpg
```
✅ **Expected:** Model describes the damage in the image

**5.4 Measure performance**
- Time to First Token (TTFT)
- Tokens Per Second (TPS)
- VRAM usage

### **✅ Checkpoint 5 Complete When:**
- [x] Model correctly identifies car damage
- [x] Response time < 10 seconds
- [x] VRAM stays under 4GB
- [x] No OOM errors

### **🎯 Success Criteria:**
```
Input: car_scratch.jpg
Output: "The image shows a horizontal scratch on the front bumper..."
TTFT: < 2 seconds
TPS: > 10 tokens/second
VRAM: 3.2-3.5 GB
```

---

## ✅ **CHECKPOINT 6: Install Agno Framework** (Day 3-4)

### **Objective:** Set up Agno for multi-agent orchestration

### **Steps:**

**6.1 Install Agno**
```bash
pip install agno
```

**6.2 Verify installation**
```bash
python -c "import agno; print('Agno version:', agno.__version__)"
```

**6.3 Create project structure**
```bash
mkdir -p backend/agents
touch backend/agents/__init__.py
touch backend/agents/vision_agent.py
touch backend/agents/price_agent.py
touch backend/agents/workshop_agent.py
touch backend/agents/coordinator.py
touch backend/app.py
```

**6.4 Test Agno can connect to local vLLM**
```python
from agno import Agent
from agno.models.openai import OpenAI

agent = Agent(
    name="Test Agent",
    model=OpenAI(
        id="Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        api_key="not-needed",
        base_url="http://localhost:8000/v1"
    )
)

response = agent.run("Say hello")
print(response.content)
```
✅ **Expected:** Agent responds via local vLLM

### **✅ Checkpoint 6 Complete When:**
- [x] Agno installed
- [x] Can create Agent instances
- [x] Agent connects to local vLLM (not OpenAI cloud)
- [x] Agent.run() returns responses

---

## ✅ **CHECKPOINT 7: Build Vision Agent** (Day 4-5)

### **Objective:** Create Agno agent that analyzes car damage images

### **Steps:**

**7.1 Implement Vision Agent**
```python
# backend/agents/vision_agent.py
from agno import Agent
from agno.models.openai import OpenAI

vision_agent = Agent(
    name="Car Damage Analyzer",
    model=OpenAI(
        id="Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        api_key="not-needed",
        base_url="http://localhost:8000/v1"
    ),
    description="UAE car repair expert - analyzes damage photos",
    instructions=[
        "Analyze car damage from photos",
        "Identify damage type, severity, affected parts",
        "Estimate repair complexity",
        "Be specific and professional"
    ],
    markdown=True
)
```

**7.2 Test Vision Agent**
```bash
python -c "
from backend.agents.vision_agent import vision_agent
result = vision_agent.run('Analyze this car damage', images=['data/test_images/car_scratch.jpg'])
print(result.content)
"
```

**7.3 Test with 5 different damage types**
- Front bumper scratch
- Side door dent
- Broken headlight
- Rear bumper damage
- Hood scratch

### **✅ Checkpoint 7 Complete When:**
- [x] Vision Agent correctly identifies damage type
- [x] Describes severity accurately
- [x] Lists affected parts
- [x] Works with 5+ different images
- [x] Response time < 10 seconds

### **🎯 Success Output:**
```
Input: car_scratch.jpg

Output:
"DAMAGE ANALYSIS
Type: Front bumper scratch
Severity: Minor (cosmetic)
Affected Parts:
  - Front bumper (paint layer)
  - No structural damage
Repair Complexity: Low
Estimated Time: 2-3 hours"
```

---

## ✅ **CHECKPOINT 8: Build Price Agent** (Day 5-6)

### **Objective:** Create agent that estimates repair costs in AED

### **Steps:**

**8.1 Create SQLite pricing database**
```bash
touch data/pricing.db
```

**8.2 Seed pricing data**
(20-30 common repair scenarios with UAE market prices)

**8.3 Implement Price Agent with MCP**
```python
# backend/agents/price_agent.py
from agno import Agent
from agno.models.openai import OpenAI
from agno.tools.mcp import MCPClient

price_agent = Agent(
    name="Repair Cost Estimator",
    model=OpenAI(
        id="Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        api_key="not-needed",
        base_url="http://localhost:8000/v1"
    ),
    tools=[MCPClient("sqlite", db_path="data/pricing.db")],
    instructions=[
        "Calculate repair costs based on damage analysis",
        "Query pricing database for parts and labor",
        "Provide min-max cost range in AED",
        "Break down: parts + labor + total"
    ]
)
```

**8.4 Test Price Agent**
```bash
python -c "
from backend.agents.price_agent import price_agent
result = price_agent.run('Estimate cost for front bumper scratch')
print(result.content)
"
```

### **✅ Checkpoint 8 Complete When:**
- [x] Pricing database has 20+ scenarios
- [x] Price Agent queries database correctly
- [x] Returns cost breakdown (parts + labor)
- [x] Costs are in AED currency
- [x] Min-max ranges are realistic

---

## ✅ **CHECKPOINT 9: Build Workshop Agent** (Day 6)

### **Objective:** Create agent that finds workshops in UAE

### **Steps:**

**9.1 Create workshop database**
```bash
touch data/workshops.db
```

**9.2 Seed workshop data**
(20-30 workshops in Abu Dhabi, Dubai, Sharjah)

**9.3 Implement Workshop Agent**
```python
# backend/agents/workshop_agent.py
from agno import Agent
from agno.models.openai import OpenAI
from agno.tools.mcp import MCPClient

workshop_agent = Agent(
    name="Workshop Locator",
    model=OpenAI(
        id="Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4",
        api_key="not-needed",
        base_url="http://localhost:8000/v1"
    ),
    tools=[MCPClient("sqlite", db_path="data/workshops.db")],
    instructions=[
        "Find workshops based on location and car brand",
        "Filter by specialization and ratings",
        "Return top 5 matches with details"
    ]
)
```

**9.4 Test Workshop Agent**
```bash
python -c "
from backend.agents.workshop_agent import workshop_agent
result = workshop_agent.run('Find Toyota workshops in Abu Dhabi')
print(result.content)
"
```

### **✅ Checkpoint 9 Complete When:**
- [x] Workshop database has 20+ entries
- [x] Agent filters by location
- [x] Returns top 5 results
- [x] Includes name, address, rating, phone

---

## ✅ **CHECKPOINT 10: Build Coordinator Agent** (Day 7)

### **Objective:** Orchestrate all agents to work together

### **Steps:**

**10.1 Implement Coordinator**
```python
# backend/agents/coordinator.py
from agno import Team
from backend.agents.vision_agent import vision_agent
from backend.agents.price_agent import price_agent
from backend.agents.workshop_agent import workshop_agent

coordinator = Team(
    name="UAE Car Care Team",
    agents=[vision_agent, price_agent, workshop_agent],
    instructions=[
        "Coordinate damage analysis workflow",
        "1. Vision Agent analyzes image",
        "2. Price Agent estimates cost",
        "3. Workshop Agent finds locations",
        "4. Compile comprehensive report"
    ]
)
```

**10.2 Test full pipeline**
```bash
python -c "
from backend.agents.coordinator import coordinator
result = coordinator.run(
    'Analyze this car damage and find workshops',
    images=['data/test_images/car_scratch.jpg'],
    location='Abu Dhabi'
)
print(result.content)
"
```

### **✅ Checkpoint 10 Complete When:**
- [x] All agents work together
- [x] Coordinator orchestrates flow correctly
- [x] Final report includes all sections
- [x] End-to-end time < 30 seconds

---

## ✅ **CHECKPOINT 11: Performance Monitoring** (Day 7)

### **Objective:** Add metrics and monitoring

### **Steps:**

**11.1 Create performance monitor**
```bash
touch client/performance_monitor.py
```

**11.2 Measure key metrics**
- Time to First Token (TTFT)
- Tokens Per Second (TPS)
- Total Inference Time
- VRAM Usage
- System RAM Usage

**11.3 Create monitoring dashboard**
```bash
python client/performance_monitor.py
```

### **✅ Checkpoint 11 Complete When:**
- [x] Can measure TTFT and TPS
- [x] VRAM monitoring works
- [x] Logs saved to `logs/` directory
- [x] Performance meets targets (TTFT < 2s, TPS > 10)

---

## ✅ **CHECKPOINT 12: Setup React + Vite Frontend** (Day 8-9)

### **Objective:** Create mobile-first React frontend

### **Steps:**

**12.1 Install Node.js (if not installed)**
```bash
# Check if Node.js is installed
node --version
npm --version

# If not, install Node.js 18+ from https://nodejs.org
```

**12.2 Create React + Vite project**
```bash
cd ~/uae-car-care-ai
npm create vite@latest frontend -- --template react
cd frontend
npm install
```
⏱️ **Time:** 2-3 minutes

**12.3 Install additional dependencies**
```bash
npm install axios
npm install -D tailwindcss postcss autoprefixer  # Optional: for styling
npx tailwindcss init -p  # If using Tailwind
```

**12.4 Test development server**
```bash
npm run dev
```
✅ **Expected:** Opens at http://localhost:5173

**12.5 Configure Vite for API proxy**
```javascript
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

### **✅ Checkpoint 12 Complete When:**
- [x] Vite dev server runs on port 5173
- [x] Can see default React page
- [x] Hot reload works (edit App.jsx and see changes)
- [x] API proxy configured

---

## ✅ **CHECKPOINT 13: Build Frontend Components** (Day 9-10)

### **Objective:** Create UI components for car damage analysis

### **Steps:**

**13.1 Create CameraUpload component**
```bash
touch frontend/src/components/CameraUpload.jsx
```

**13.2 Add camera capture logic**
```jsx
// frontend/src/components/CameraUpload.jsx
import { useState } from 'react'

function CameraUpload({ onImageCapture }) {
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleCapture = (e) => {
    const file = e.target.files[0]
    if (file) {
      setLoading(true)
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result)
        onImageCapture(reader.result) // Base64
        setLoading(false)
      }
      reader.readAsDataURL(file)
    }
  }

  return (
    <div className="camera-upload">
      <input
        type="file"
        accept="image/*"
        capture="environment"
        onChange={handleCapture}
        id="camera-input"
        className="hidden"
      />
      <label htmlFor="camera-input" className="btn-primary">
        📷 Take Photo
      </label>
      {preview && <img src={preview} alt="Preview" />}
    </div>
  )
}

export default CameraUpload
```

**13.3 Create DamageReport component**
```bash
touch frontend/src/components/DamageReport.jsx
```

**13.4 Create API service**
```bash
mkdir -p frontend/src/services
touch frontend/src/services/api.js
```

```javascript
// frontend/src/services/api.js
import axios from 'axios'

const API_BASE = '/api' // Proxied to http://localhost:8000

export const analyzeDamage = async (imageBase64, location = 'Abu Dhabi') => {
  const response = await axios.post(`${API_BASE}/analyze`, {
    image: imageBase64,
    location: location
  })
  return response.data
}

export const healthCheck = async () => {
  const response = await axios.get(`${API_BASE}/health`)
  return response.data
}
```

**13.5 Update App.jsx**
```jsx
// frontend/src/App.jsx
import { useState } from 'react'
import CameraUpload from './components/CameraUpload'
import DamageReport from './components/DamageReport'
import { analyzeDamage } from './services/api'

function App() {
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleImageCapture = async (imageBase64) => {
    setLoading(true)
    setError(null)
    try {
      const data = await analyzeDamage(imageBase64)
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <h1>🚗 UAE Car Care AI</h1>
      <CameraUpload onImageCapture={handleImageCapture} />
      {loading && <p>Analyzing damage...</p>}
      {error && <p className="error">{error}</p>}
      {result && <DamageReport data={result} />}
    </div>
  )
}

export default App
```

**13.6 Test frontend locally**
```bash
npm run dev
```

### **✅ Checkpoint 13 Complete When:**
- [x] Camera upload component works
- [x] Can capture/upload images
- [x] API calls work (connects to backend)
- [x] Loading states display correctly
- [x] Results render properly

---

## ✅ **CHECKPOINT 14: Mobile Optimization** (Day 10-11)

### **Objective:** Make UI mobile-responsive and production-ready

### **Steps:**

**14.1 Add responsive styling**
- Use Tailwind CSS or CSS Grid
- Test on mobile viewport (Chrome DevTools)
- Ensure touch-friendly buttons (min 44px)

**14.2 Add loading spinner**
```bash
touch frontend/src/components/LoadingSpinner.jsx
```

**14.3 Add error handling**
```bash
touch frontend/src/components/ErrorBoundary.jsx
```

**14.4 Test on mobile device**
```bash
# Find your local IP
ifconfig | grep inet  # Or `ip addr` on Linux

# Access from phone on same WiFi:
http://YOUR_IP:5173
```

**14.5 Build for production**
```bash
npm run build
```
✅ **Expected:** Creates `dist/` folder with optimized build

**14.6 Preview production build**
```bash
npm run preview
```

### **✅ Checkpoint 14 Complete When:**
- [x] UI works on mobile screens
- [x] Camera opens on mobile devices
- [x] Touch interactions work smoothly
- [x] Production build successful
- [x] No console errors

---

## ✅ **CHECKPOINT 15: Documentation & Demo** (Day 11-12)

### **Objective:** Create professional documentation for recruiters

### **Steps:**

**15.1 Create comprehensive README**
- Project overview
- Architecture diagram
- Tech stack explanation
- Installation guide
- Demo video/screenshots

**15.2 Add code documentation**
- Docstrings for all agents
- Inline comments
- API documentation

**15.3 Create demo script**
```bash
touch demo.py
```

**15.4 Record demo video**
- Show frontend camera capture
- Show damage analysis
- Show multi-agent coordination
- Show performance metrics
- Explain architecture

**15.5 Take screenshots**
- Frontend UI (desktop + mobile)
- Terminal output
- Performance metrics
- Multi-agent logs
- Final report

### **✅ Checkpoint 15 Complete When:**
- [x] README is comprehensive
- [x] Demo script works end-to-end
- [x] Screenshots captured
- [x] Demo video recorded (optional)
- [x] GitHub repo ready

---

## 🎯 **FINAL SUCCESS CRITERIA**

### **Technical Achievements:**
- ✅ vLLM server running stably on 4GB GPU
- ✅ Qwen2-VL-2B analyzing images accurately
- ✅ Agno multi-agent system coordinating 3+ agents
- ✅ OpenAI-compatible API working locally
- ✅ 100% free, on-premise deployment
- ✅ Response time < 30 seconds end-to-end

### **Portfolio Readiness:**
- ✅ Professional README with architecture
- ✅ Clean, documented code
- ✅ Working demo script
- ✅ Performance metrics documented
- ✅ Screenshots/video showing results
- ✅ GitHub repo organized

---

## 📊 **Progress Tracking**

**Daily Targets:**
- Day 1: Checkpoints 1-2 (Environment + Model)
- Day 2-3: Checkpoints 3-5 (vLLM Server + Vision Test)
- Day 3-4: Checkpoint 6 (Agno Setup)
- Day 4-5: Checkpoint 7 (Vision Agent)
- Day 5-6: Checkpoints 8-9 (Price + Workshop Agents)
- Day 7: Checkpoints 10-11 (Coordinator + Monitoring)
- Day 8-9: Checkpoint 12 (React + Vite Setup)
- Day 9-10: Checkpoint 13 (Frontend Components)
- Day 10-11: Checkpoint 14 (Mobile Optimization)
- Day 11-12: Checkpoint 15 (Documentation + Demo)

---

## 🚀 **Ready to Start?**

**Begin with Checkpoint 1!**

```bash
cd ~/uae-car-care-ai
source venv/bin/activate
nvidia-smi
```

**Let's build this! 🔥**

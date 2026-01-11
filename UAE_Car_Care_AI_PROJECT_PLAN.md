# 🚗 UAE Car Care AI - Complete Project Plan

## 📋 Project Overview

**Name:** UAE Car Care AI Assistant
**Purpose:** Multimodal AI agent system for car damage assessment, workshop finder, and repair guidance in UAE
**Framework:** Agno v2 (Apache 2.0 - Free)
**Deployment:** Mobile-first web app with free hosting

---

## 🎯 Core Features

### 1. **Car Damage Assessment (Vision AI)**
- Upload car damage photos
- AI identifies damage type, severity, parts affected
- Estimates repair cost in AED (UAE market rates)
- Multimodal: Llama 3.2 Vision 11B

### 2. **Workshop Finder & Price Comparison**
- Find workshops in Abu Dhabi/Dubai/Sharjah
- Compare prices, ratings, locations
- Google Maps integration via MCP
- Filter by car brand specialization

### 3. **Insurance Advisor Agent**
- Analyze if damage should be claimed
- Compare excess vs repair cost
- Explain UAE insurance claim process
- Step-by-step guidance

### 4. **Emergency Guide**
- Nearest hospitals in case of accidents
- Emergency numbers (999, ambulance)
- UAE accident scene procedure
- Voice-enabled for hands-free use

### 5. **Voice Integration**
- Text-to-speech for all responses
- Speech-to-text for queries
- Hands-free operation (while driving)

---

## 🛠️ Tech Stack

### **Backend - Agno Framework**
```yaml
Framework: Agno v2
Runtime: AgentOS (pre-built FastAPI)
Models:
  - Llama 3.2 Vision 11B (multimodal - damage analysis)
  - Llama 3.1 8B (conversational AI)
LLM Runtime: Ollama (local, free)
```

### **MCP Servers (Model Context Protocol)**
```yaml
Maps: @modelcontextprotocol/server-google-maps
Filesystem: @modelcontextprotocol/server-filesystem
Database: @modelcontextprotocol/server-sqlite
Web Scraping: @modelcontextprotocol/server-fetch
```

### **Database**
```yaml
Vector DB: ChromaDB (workshop knowledge, repair guides)
Structured: SQLite (pricing, insurance rules)
```

### **Frontend**
```yaml
Framework: React 18 + Vite
Mobile-First: Responsive design, PWA-ready
Camera: Native camera access for damage photos
Voice: Web Speech API + gTTS
```

### **Hosting (FREE Options)**
```yaml
Backend Options:
  1. Render.com (Free tier - 750 hours/month)
  2. Railway.app (Free $5 credit/month)
  3. Fly.io (Free tier available)

Frontend Options:
  1. Vercel (Free, unlimited projects)
  2. Netlify (Free tier)
  3. GitHub Pages (Free)

Model Hosting:
  - Challenge: Llama 3.2 Vision 11B needs ~8GB RAM
  - Solutions:
    Option A: Use smaller model (Llama 3.2 Vision 3B) for free hosting
    Option B: Local development, deploy with API-based models
    Option C: Ollama on Render.com (limited free tier)
```

---

## 🏗️ Project Structure

```
uae-car-care-ai/
│
├── backend/                      # Agno + FastAPI backend
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── vision_agent.py      # Car damage analyzer (Vision)
│   │   ├── price_agent.py       # Cost estimator
│   │   ├── workshop_agent.py    # Workshop finder (Google Maps)
│   │   ├── insurance_agent.py   # Claim advisor
│   │   └── emergency_agent.py   # Hospital guide
│   │
│   ├── knowledge/                # Agno knowledge bases
│   │   ├── workshops/
│   │   │   ├── abu_dhabi.json
│   │   │   ├── dubai.json
│   │   │   └── sharjah.json
│   │   ├── pricing/
│   │   │   └── repair_costs.json
│   │   └── insurance/
│   │       └── uae_rules.json
│   │
│   ├── tools/                    # Custom tools & MCP integrations
│   │   ├── google_maps_tool.py
│   │   ├── damage_analyzer.py
│   │   ├── price_calculator.py
│   │   └── voice_handler.py
│   │
│   ├── database/
│   │   ├── init_db.py           # Initialize SQLite + ChromaDB
│   │   └── seed_data.py         # Load workshop/pricing data
│   │
│   ├── app.py                    # Main Agno application
│   ├── server.py                 # FastAPI server wrapper
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                     # React mobile-first UI
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Landing.jsx      # Home page
│   │   │   ├── DamageAssessment.jsx
│   │   │   ├── WorkshopFinder.jsx
│   │   │   └── Emergency.jsx
│   │   │
│   │   ├── components/
│   │   │   ├── CameraUpload.jsx  # Photo capture
│   │   │   ├── VoiceInput.jsx    # Speech-to-text
│   │   │   ├── DamageReport.jsx  # Results display
│   │   │   └── WorkshopCard.jsx
│   │   │
│   │   ├── services/
│   │   │   ├── api.js           # Backend API calls
│   │   │   └── voice.js         # TTS/STT handlers
│   │   │
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── data/                         # Raw data files
│   ├── workshops_scraped.csv
│   ├── repair_prices.csv
│   └── sample_damage_images/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   └── API.md
│
├── .env.example
├── .gitignore
├── docker-compose.yml           # Optional: local development
└── README.md
```

---

## 🤖 Agent Architecture

### **Agent 1: Vision Agent (Damage Analyzer)**
```python
Name: "UAE Car Damage Analyzer"
Model: Llama 3.2 Vision 11B (via Ollama)
Input: Car damage image
Output:
  - Damage type (dent, scratch, broken part)
  - Severity (minor, medium, major)
  - Affected parts (bumper, door, headlight, etc.)
  - Estimated cost range in AED

Tools: None (pure vision model)
Knowledge: UAE car part terminology, common damage patterns
```

### **Agent 2: Price Estimation Agent**
```python
Name: "Repair Cost Estimator"
Model: Llama 3.1 8B
Input: Damage analysis from Vision Agent
Output: Detailed price breakdown
  - Labor cost
  - Parts cost
  - Total estimate (min-max range)

Tools: SQLite pricing database
Knowledge: UAE market rates, workshop pricing patterns
```

### **Agent 3: Workshop Finder Agent**
```python
Name: "Workshop Locator"
Model: Llama 3.1 8B
Input: User location, car brand, damage type
Output: List of 5-10 workshops
  - Name, address, phone
  - Distance from user
  - Ratings
  - Specialization
  - Price comparison for the repair

Tools: Google Maps MCP server
Knowledge: Workshop database, specializations
```

### **Agent 4: Insurance Advisor Agent**
```python
Name: "Insurance Claim Advisor"
Model: Llama 3.1 8B
Input: Damage severity, repair cost, user's excess amount
Output: Claim recommendation
  - Should you claim? (Yes/No + reasoning)
  - Cost comparison (excess vs repair)
  - Claim process steps
  - Required documents

Tools: None
Knowledge: UAE insurance laws, claim procedures
```

### **Agent 5: Emergency Guide Agent**
```python
Name: "Emergency Response Guide"
Model: Llama 3.1 8B
Input: Accident location, injury status
Output:
  - Emergency numbers (999)
  - Nearest hospital with directions
  - What to do at scene (UAE law)
  - Police report requirements

Tools: Google Maps MCP server
Knowledge: UAE traffic law, emergency procedures
```

---

## 📊 Data Requirements

### **1. Workshop Database** (Manual Collection + Web Scraping)
```json
{
  "workshops": [
    {
      "name": "Al Futtaim Auto Center",
      "location": "Abu Dhabi, Mussafah",
      "coordinates": {"lat": 24.35, "lng": 54.50},
      "brands": ["Toyota", "Lexus", "Honda"],
      "rating": 4.5,
      "phone": "+971-2-xxx-xxxx",
      "services": ["body_repair", "paint", "mechanical"],
      "price_tier": "medium"
    }
  ]
}
```

**Data Sources:**
- Google Maps scraping (20-30 top workshops)
- Manual research (authorized dealers)
- Dubizzle workshop listings

### **2. Pricing Database**
```json
{
  "repairs": [
    {
      "damage_type": "bumper_scratch",
      "severity": "minor",
      "parts_needed": ["paint"],
      "labor_hours": 2,
      "cost_aed": {"min": 400, "max": 600},
      "description": "Small scratch on bumper, requires sanding and repainting"
    }
  ]
}
```

**Data Sources:**
- Workshop website estimates
- Dubizzle auto parts prices
- Manual research (call 5-10 workshops for quotes)

### **3. Insurance Knowledge Base**
```json
{
  "uae_insurance_rules": {
    "comprehensive_coverage": {
      "typical_excess": {"min": 500, "max": 2000},
      "claim_threshold": "Claim if repair > excess + 500 AED",
      "process": [
        "Contact insurance within 24 hours",
        "Get police report if needed",
        "Take damage photos",
        "Get repair quotes",
        "Submit claim form"
      ]
    }
  }
}
```

---

## 🌐 Free Hosting Strategy

### **Option A: Hybrid Deployment (RECOMMENDED for FREE)**

**Backend (Agno + Ollama):**
- **Local Development**: Run on your machine for testing
- **Demo Mode**: Use lighter models or mock responses for live demo
- **Alternative**: Use Groq API (free tier) for fast inference instead of local Ollama

**Frontend:**
- **Vercel** (Free): Deploy React app
- **Mobile PWA**: Add manifest.json for "install to home screen"

**Database:**
- **Supabase** (Free tier): PostgreSQL for workshops/pricing
- **Turso** (Free tier): SQLite in the cloud

**Cost:** $0/month ✅

---

### **Option B: Full Cloud Deployment (Limited Free)**

**Platform: Render.com (Free Tier)**
- 750 hours/month free
- Deploys Docker containers
- Custom domains
- Auto-sleep after 15min inactivity (wake on request)

**Challenge:**
- Free tier: 512MB RAM (not enough for Llama 3.2 Vision 11B ~8GB)
- **Solution:** Use **Llama 3.2 Vision 3B** (smaller model, ~2GB RAM)

**Cost:** $0/month (with limitations) ✅

---

### **Option C: API-Based Models (Easiest for FREE Mobile)**

**Instead of Ollama, use FREE API providers:**
- **Groq**: Free API, super fast Llama models
- **Together AI**: Free tier available
- **Replicate**: Pay-per-use (very cheap)

**Frontend:** Vercel (Free)
**Backend:** Vercel Serverless Functions (Free tier)

**Pros:**
- Actually works on free hosting
- Mobile accessible immediately
- No server management

**Cons:**
- Not 100% on-premise (but APIs are free)
- Demonstrates API integration skills (good for portfolio!)

**Cost:** $0-5/month ✅

---

## 🎯 Recommended Path for YOU

### **Phase 1: Local Development (This Week)**
1. Build everything locally with Agno + Ollama
2. Use full Llama 3.2 Vision 11B (best quality)
3. Test all agents thoroughly
4. Create demo videos (record locally)

### **Phase 2: Mobile-Accessible Demo (Next Week)**
5. Deploy frontend to **Vercel** (free, mobile-ready)
6. Backend: Use **Groq API** (free, fast) instead of Ollama
7. Database: **Supabase** (free PostgreSQL)
8. Result: **Fully working mobile app, $0 cost**

### **Phase 3: Portfolio Showcase**
9. GitHub repo (show local Ollama version)
10. Live demo link (Vercel + Groq API version)
11. Demo video showing damage analysis
12. README with architecture diagrams

**Best of Both Worlds:**
- ✅ Local version shows "on-premise" capabilities
- ✅ Live version shows "production deployment" skills
- ✅ Both are free!

---

## 📱 Mobile-First Considerations

### **PWA Features**
```json
// manifest.json
{
  "name": "UAE Car Care AI",
  "short_name": "CarCare AI",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#1e3a8a",
  "theme_color": "#3b82f6",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}
```

### **Mobile UX**
- **Large touch targets** (min 44px)
- **Camera integration** for damage photos
- **Voice input** for hands-free (while parked!)
- **Offline mode** (cache workshop data)
- **Fast loading** (< 3 seconds)

---

## 📸 Screenshot Plan for Portfolio

1. **Landing page** (mobile view)
2. **Camera capture** damage photo
3. **AI analysis** showing damage + cost
4. **Workshop results** with map
5. **Insurance advice** screen
6. **Voice interface** demo

---

## 🚀 Development Timeline

### **Week 1: Core Setup**
- Day 1-2: Install Agno, Ollama, project structure
- Day 3-4: Build Vision Agent + test with sample images
- Day 5-7: Build Price Agent + create pricing database

### **Week 2: Multi-Agent System**
- Day 1-3: Workshop Finder Agent + Google Maps MCP
- Day 4-5: Insurance Advisor Agent
- Day 6-7: Emergency Guide Agent

### **Week 3: Frontend + Voice**
- Day 1-3: React mobile UI (camera, upload, results)
- Day 4-5: Voice integration (TTS/STT)
- Day 6-7: Testing, bug fixes

### **Week 4: Deployment + Polish**
- Day 1-2: Deploy to Vercel (frontend) + Groq API (backend)
- Day 3-4: Mobile testing, PWA setup
- Day 5-6: Create demo video, screenshots
- Day 7: GitHub README, portfolio update

---

## 💡 Key Success Metrics

**For Recruiters:**
- ✅ Multimodal AI (vision + text + voice)
- ✅ Multi-agent architecture (5 specialized agents)
- ✅ Real-world problem solving (UAE market)
- ✅ Mobile-first design
- ✅ Production deployment (live link!)
- ✅ Modern tech stack (Agno, React, MCP)

**For Users:**
- ✅ Fast damage assessment (< 30 seconds)
- ✅ Accurate cost estimates (within 20% of actual)
- ✅ Useful workshop recommendations
- ✅ Clear insurance guidance

---

## 📝 Next Immediate Steps

When you're ready to start coding:

1. **Read this plan**: `cat /home/kesavan/UAE_Car_Care_AI_PROJECT_PLAN.md`
2. **Create project directory**: `mkdir -p ~/uae-car-care-ai && cd ~/uae-car-care-ai`
3. **Install Agno**: Follow installation commands
4. **Pull models**: `ollama pull llama3.2-vision:11b`
5. **Build Vision Agent**: Start with car damage analyzer
6. **Test with sample image**: Upload car damage photo

---

## 🔗 Useful Resources

- Agno Docs: https://docs.agno.com
- Agno GitHub: https://github.com/agno-agi/agno
- Ollama Models: https://ollama.com/library
- MCP Servers: https://github.com/modelcontextprotocol
- Groq API (Free): https://console.groq.com
- Vercel Deployment: https://vercel.com

---

**PLAN SAVED!** You can always refer back to this document.
When ready to continue, just say: "Let's continue from [step]"

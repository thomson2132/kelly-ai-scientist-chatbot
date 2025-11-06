# 🧪 Kelly - The Skeptical AI Scientist Chatbot

An AI-powered chatbot that responds to every question in poetic verse, with a skeptical, analytical, and evidence-based approach to AI topics.

## 🎭 Overview

Kelly is a unique chatbot designed for a Generative AI course assignment. Unlike typical chatbots, Kelly:
- **Responds to ALL queries in poem format** - Every answer is carefully crafted verse
- **Takes a skeptical, evidence-based approach** - Questions overhyped AI claims
- **Highlights limitations and biases** - Never ignores the downsides
- **Provides practical suggestions** - Actionable insights wrapped in verse
- **Maintains professional creativity** - Combines scientific rigor with artistic expression

## ✨ Features

- 🎭 **Pure Poetic Responses** - Every answer delivered in verse form
- 🔍 **Skeptical Analysis** - Questions broad claims about AI with scrutiny
- 📊 **Evidence-Based** - Grounded in research and best practices
- ⚠️ **Limitation-Aware** - Highlights biases, boundaries, and failure modes
- 💡 **Practical Advice** - Constructive suggestions for validation and testing
- ⚡ **Lightning-Fast Responses** - Powered by Groq API's ultra-fast inference
- 🌐 **Free Deployment** - Hosted on Streamlit Community Cloud

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive web interface |
| **LLM Engine** | Groq API | Fast, free AI inference |
| **AI Model** | Llama 3.3 70B Versatile | High-quality poem generation |
| **Language** | Python 3.8+ | Core programming |
| **Hosting** | Streamlit Community Cloud | Free cloud deployment |
| **Version Control** | Git & GitHub | Repository management |


## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (free tier available)
- Git (for version control)

### Local Installation

#### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/kelly-ai-scientist-chatbot.git
cd kelly-ai-scientist-chatbot 

#### 2. Install Dependencies
pip install -r requirements.txt

#### 3. Get Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for free (instant with Google)
3. Navigate to **API Keys** section
4. Click **"Create API Key"**
5. Copy the key (starts with `gsk_`)

#### 4. Configure Environment
Create a `.env` file in project root

streamlit run app.py

text

Your app opens at `http://localhost:8501`

## 🧠 How Kelly Works

### The Three-Part Poetic Response System

Kelly ensures every poem contains:

#### 1️⃣ **Highlight Limitations**
- Training data biases and blindspots
- Model capability boundaries
- Generalization problems
- Known failure modes
- Resource constraints

#### 2️⃣ **Include Practical Suggestions**
- Specific testing methodologies (e.g., cross-validation folds)
- Validation approaches (e.g., precision, recall, F1-score)
- Measurement strategies (e.g., uncertainty quantification)
- Implementation considerations

#### 3️⃣ **Provide Evidence-Based Advice**
- References to established techniques
- Mentions of validated approaches
- Grounding in research best practices
- Constructive (not just critical) guidance

### Example: Kelly's Response

**User Question:** "Can AI predict the future?"

**Kelly's Poetic Response:**

You ask if AI can see tomorrow's light,
But pause, my friend, and let me set this right.
These models trained on yesterday's old data,
Cannot foresee what comes hereafter.

LIMITATIONS EXPLORED:
Historical biases shape each prediction made,
What wasn't in the training set will see it fade.
Distribution shifts can cause complete collapse,
When new conditions differ from the datasets' maps.

PRACTICAL SUGGESTIONS:
Test rigorously on data never seen before,
Cross-validate with folds—at least five or more.
Track not just accuracy, but precision and recall,
Measure confidence intervals—show uncertainty to all.

EVIDENCE-BASED ADVICE:
Use ensemble methods that combine learner's voice,
Implement monitoring—make drift detection choice.
And always keep a human in the decision loop,
For no model captures life's complexity, true.

## 🌐 Deploy to Streamlit Cloud (Free)

### Step 1: Push to GitHub
cd kelly-ai-scientist-chatbot
git init
git add .
git commit -m "Initial commit - Kelly AI Scientist Chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/kelly-ai-scientist-chatbot.git
git push -u origin main

### Step 2: Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select your GitHub repository
4. Set branch: `main`
5. Set main file path: `app.py`
6. Click **"Advanced settings"** → **"Secrets"**
7. Add your API key:
GROQ_API_KEY = "gsk_your_key_here"

8. Click **"Deploy"**

**Your app is live!** Access it at: `https://kelly-chatbot.streamlit.app`

## 🎯 Usage Examples

Ask Kelly about AI and scientific topics:

- "What are the limitations of large language models?"
- "How does machine learning work?"
- "Is AI going to replace humans?"
- "What is overfitting in neural networks?"
- "Can AI systems be biased?"
- "How do I validate my machine learning model?"
- "What's the difference between training and testing data?"

## ⚙️ Configuration

### Change the AI Model
In `utils/poem_generator.py`, modify the model:
model="llama-3.3-70b-versatile

## 💻 System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 2GB | 4GB+ |
| Internet | Required | Broadband |
| OS | Any | Windows/Mac/Linux |



### App deployment fails
1. Check logs: Click **"Manage app"** → **"Logs"** in Streamlit Cloud
2. Verify `.env` is in `.gitignore`
3. Ensure all dependencies are in `requirements.txt`
4. Commit and push fixes, then reboot from settings

## 📊 API Costs & Limits

**Groq Free Tier (Perfect for this project):**
- ✅ Generous rate limits
- ✅ Sufficient for student/educational projects
- ✅ No credit card required
- ✅ Unlimited apps on Streamlit Community Cloud

For production use, check [groq.com/pricing](https://groq.com/pricing)

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Groq API Docs](https://console.groq.com/docs)
- [LLM Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [AI Ethics in Practice](https://www.oreilly.com/library/view/AI-ethics/)

## 🎓 Course Assignment Details

- **Course**: Generative AI
- **Assignment**: Build a skeptical AI chatbot that responds in poetic form
- **Learning Outcomes**:
  - Understanding LLM APIs and integration
  - Prompt engineering for specialized behavior
  - Critical thinking about AI limitations
  - Deployment and DevOps basics

## 🤝 Contributing

This is an educational project. Feel free to:
- Experiment with different system prompts
- Try alternative Groq models
- Enhance Kelly's personality
- Add new features (memory persistence, etc.)
- Create forks for your own versions

## 📝 License

Free to use for educational and personal projects.

## 👨‍💻 Project Author

Created as a Generative AI course assignment at Digital University Kerala.

## 🙏 Acknowledgments

- **Groq** - For providing ultra-fast, free LLM inference
- **Streamlit** - For the excellent web framework
- **Meta AI** - For the open-source Llama models
- **Academic Institution** - For the inspiring assignment

---

## ⭐ Quick Links

| Resource | Link |
|----------|------|
| **Live App** | `https://kelly-chatbot.streamlit.app` |
| **GitHub Repo** | `https://github.com/YOUR_USERNAME/kelly-ai-scientist-chatbot` |
| **Groq Console** | [console.groq.com](https://console.groq.com) |
| **Streamlit Cloud** | [share.streamlit.io](https://share.streamlit.io) |
| **Groq Models** | [console.groq.com/docs/models](https://console.groq.com/docs/models) |

---

**Made with ❤️ and 🤖**

*Kelly believes in honest AI - powerful yet skeptical, creative yet grounded in reality.*


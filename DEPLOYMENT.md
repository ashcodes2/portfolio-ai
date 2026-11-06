# 🚀 Portfolio AI Assistant Deployment Guide

Ashwani Upadhyay's AI Portfolio Chatbot & JD Matcher (Chainlit + Groq LLM).

---

## 🛠️ Option 1: Hugging Face Spaces (Recommended - Free & 24/7)

Hugging Face Spaces supports Chainlit / Docker natively and gives a free public URL with no sleep timeouts.

### Steps:
1. Go to [huggingface.co/new-space](https://huggingface.co/new-space).
2. Set Space Name: `ashwani-ai-portfolio` (or your choice).
3. Select **Space SDK**: **Docker** (Blank template).
4. Select **Public**.
5. Once created, clone the space repo locally or push your `Portfolio` files to it:
   ```bash
   cd Portfolio
   git init
   git remote add origin https://huggingface.co/spaces/<your-username>/<space-name>
   git add .
   git commit -m "Deploy Ashwani Portfolio AI"
   git push -u origin main --force
   ```
6. **Set Secret Key in Settings**:
   - Go to your Space -> **Settings** -> **Variables and secrets**.
   - Add a **New secret**:
     - Key: `GROQ_API_KEY`
     - Value: `<your_groq_api_key>`
7. Your app will automatically build and become live!

---

## 🌐 Option 2: Render.com (Free Web Service)

1. Push the `Portfolio` folder to a GitHub repository (e.g. `https://github.com/<your-username>/portfolio-ai`).
2. Log in to [render.com](https://render.com) and click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Settings:
   - **Environment**: `Python 3` (or `Docker`)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `chainlit run app.py --host 0.0.0.0 --port $PORT --headless`
5. Under **Environment Variables**:
   - Add `GROQ_API_KEY` with your key.
6. Click **Deploy Web Service**.

---

## 💻 Local Run

To run locally on your machine:
```bash
cd Portfolio
chainlit run app.py -w
```
Open your browser at `http://localhost:8000`.

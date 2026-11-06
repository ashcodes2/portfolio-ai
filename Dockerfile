FROM python:3.11-slim

WORKDIR /app

# Install system utilities if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set default ports
EXPOSE 7860 8000

ENV HOST=0.0.0.0
ENV PORT=7860

# Run Chainlit with dynamic PORT support for Hugging Face Spaces / Render
CMD ["sh", "-c", "chainlit run app.py --host 0.0.0.0 --port ${PORT:-7860} --headless"]

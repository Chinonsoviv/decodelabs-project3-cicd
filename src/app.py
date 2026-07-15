from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>DecodeLabs CI/CD Pipeline</h1><p>Deployed automatically via GitHub Actions to AWS EC2.</p>"

@app.route('/health')
def health():
    return {"status": "healthy", "message": "Pipeline is running"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

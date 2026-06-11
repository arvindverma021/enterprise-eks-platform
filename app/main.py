from fastapi import FastAPI

app = FastAPI(
    title="Enterprise EKS Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "healthy",
        "project": "enterprise-eks-platform"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }

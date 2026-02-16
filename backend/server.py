from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import os

app = FastAPI(title="CMC Portfolio - Martina Caputo")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Site directory
SITE_DIR = "/app/site"

# Health check
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "CMC Portfolio is running"}

# Serve static files under /api/site
app.mount("/api/site/assets", StaticFiles(directory=f"{SITE_DIR}/assets"), name="assets")
app.mount("/api/site/images", StaticFiles(directory=f"{SITE_DIR}/images"), name="images")
app.mount("/api/site/css", StaticFiles(directory=f"{SITE_DIR}/css"), name="css")
app.mount("/api/site/js", StaticFiles(directory=f"{SITE_DIR}/js"), name="js")

# Serve HTML pages
@app.get("/api/site/index.html")
@app.get("/api/site/")
@app.get("/api/site")
async def serve_index():
    return FileResponse(f"{SITE_DIR}/index.html", media_type="text/html")

@app.get("/api/site/chi-sono.html")
async def serve_chi_sono():
    return FileResponse(f"{SITE_DIR}/chi-sono.html", media_type="text/html")

@app.get("/api/site/progetti.html")
async def serve_progetti():
    return FileResponse(f"{SITE_DIR}/progetti.html", media_type="text/html")

@app.get("/api/site/cv.html")
async def serve_cv():
    return FileResponse(f"{SITE_DIR}/cv.html", media_type="text/html")

@app.get("/api/site/contatti.html")
async def serve_contatti():
    return FileResponse(f"{SITE_DIR}/contatti.html", media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

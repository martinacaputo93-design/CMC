from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

# Serve static files from the site directory
SITE_DIR = "/app/site"

# Mount static directories
app.mount("/assets", StaticFiles(directory=f"{SITE_DIR}/assets"), name="assets")
app.mount("/images", StaticFiles(directory=f"{SITE_DIR}/images"), name="images")
app.mount("/css", StaticFiles(directory=f"{SITE_DIR}/css"), name="css")
app.mount("/js", StaticFiles(directory=f"{SITE_DIR}/js"), name="js")

@app.get("/")
async def serve_index():
    return FileResponse(f"{SITE_DIR}/index.html")

@app.get("/index.html")
async def serve_index_html():
    return FileResponse(f"{SITE_DIR}/index.html")

@app.get("/chi-sono.html")
async def serve_chi_sono():
    return FileResponse(f"{SITE_DIR}/chi-sono.html")

@app.get("/chi-sono")
async def serve_chi_sono_clean():
    return FileResponse(f"{SITE_DIR}/chi-sono.html")

@app.get("/progetti.html")
async def serve_progetti():
    return FileResponse(f"{SITE_DIR}/progetti.html")

@app.get("/progetti")
async def serve_progetti_clean():
    return FileResponse(f"{SITE_DIR}/progetti.html")

@app.get("/cv.html")
async def serve_cv():
    return FileResponse(f"{SITE_DIR}/cv.html")

@app.get("/cv")
async def serve_cv_clean():
    return FileResponse(f"{SITE_DIR}/cv.html")

@app.get("/contatti.html")
async def serve_contatti():
    return FileResponse(f"{SITE_DIR}/contatti.html")

@app.get("/contatti")
async def serve_contatti_clean():
    return FileResponse(f"{SITE_DIR}/contatti.html")

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "CMC Portfolio is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

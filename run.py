import os
import sys

# Add lib folder to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_root, "lib"))

import uvicorn

if __name__ == "__main__":
    # Use PORT environment variable if provided (for Render), default to 8003
    port = int(os.environ.get("PORT", 8003))
    host = os.environ.get("HOST", "0.0.0.0")
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        log_level="info"
    )

# main.py
import uvicorn
from server.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "server.server:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )

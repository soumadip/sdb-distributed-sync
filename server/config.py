# server/config.py

class Settings:
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True
    DEBUG: bool = True

settings = Settings()

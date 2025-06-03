import os
from datetime import datetime

try:
    from django.conf import settings
    LOG_DIR = getattr(settings, "LOG_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs"))
except ImportError:
    # Fallback if settings not available (e.g., running standalone)
    LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

def _write_log(level: str, message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {level.upper()}: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

class SimpleLogger:
    def info(self, message): _write_log("INFO", message)
    def warning(self, message): _write_log("WARNING", message)
    def error(self, message): _write_log("ERROR", message)
    def debug(self, message): _write_log("DEBUG", message)
    def critical(self, message): _write_log("CRITICAL", message)

log = SimpleLogger()

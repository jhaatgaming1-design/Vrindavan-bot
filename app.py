
import threading
from dashboard import run_dashboard
from bot import start_bot

if __name__ == "__main__":
    threading.Thread(target=run_dashboard).start()
    start_bot()

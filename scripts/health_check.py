
import os
import time
import logging
import psutil
from datetime import datetime

# Project directories
BASE_DIR = os.path.expanduser("~/cloudops")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "health_check.log")

# Alert thresholds (percent)
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 80

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print("\n--- CloudOps System Health ---")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU usage: {cpu:.1f}%")
    print(f"RAM usage: {memory.percent:.1f}%")
    print(f"Disk usage: {disk.percent:.1f}%")

    logging.info(
        "CPU=%.1f%% | RAM=%.1f%% | Disk=%.1f%%",
        cpu,
        memory.percent,
        disk.percent,
    )

    if cpu >= CPU_THRESHOLD:
        logging.warning("High CPU usage: %.1f%%", cpu)
        print("WARNING: High CPU usage!")

    if memory.percent >= RAM_THRESHOLD:
        logging.warning("High RAM usage: %.1f%%", memory.percent)
        print("WARNING: High RAM usage!")

    if disk.percent >= DISK_THRESHOLD:
        logging.warning("High disk usage: %.1f%%", disk.percent)
        print("WARNING: High disk usage!")

if __name__ == "__main__":
    check_system_health()

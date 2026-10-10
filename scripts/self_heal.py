
#!/usr/bin/env python3

import logging
import subprocess
from datetime import datetime
from pathlib import Path

LOG_DIR = Path.home() / "cloudops" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "self_heal.log"
SERVICE = "cloudops-demo.service"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)

def service_is_active():
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", SERVICE],
        check=False,
    )
    return result.returncode == 0

def main():
    if service_is_active():
        message = f"{SERVICE} is healthy."
        print(message)
        logging.info(message)
        return

    message = f"{SERVICE} is down. Attempting recovery."
    print(message)
    logging.warning(message)

    result = subprocess.run(
        ["sudo", "-n", "systemctl", "start", SERVICE],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode == 0 and service_is_active():
        message = f"Recovery successful: {SERVICE} is running."
        print(message)
        logging.info(message)
    else:
        message = f"Recovery failed: {SERVICE} did not start."
        print(message)
        logging.error("%s Details: %s", message, result.stderr.strip())

if __name__ == "__main__":
    main()

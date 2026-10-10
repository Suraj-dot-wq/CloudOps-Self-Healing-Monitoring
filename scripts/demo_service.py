#!/usr/bin/env python3

import time
from datetime import datetime

while True:
    print(f"CloudOps demo service is running: {datetime.now()}", flush=True)
    time.sleep(10)

# System Resource Monitor

A lightweight Python script that monitors real-time system performance (CPU, Memory, Disk, and Network usage) using the `psutil` library. It acts as an automated system, tracking metrics and throwing instant alerts if resource usage exceeds defined thresholds.
At first I used a lot of if-elif-else statements than with the help of AI i improved made it more efficient it now it look a lot better it has
## Features

* **Live Monitoring:** Continuously tracks core system components.
* **Automated Threshold Alerts:** Prints warning logs if resource consumption spikes too high.
* **Network Tracking:** Calculates and normalizes byte transfer rates over short intervals.

## Thresholds

| Component | Default Alert Limit |
| :--- | :--- |
| **CPU** | > 80% |
| **Memory** | > 80% |
| **Disk** | > 80% |
| **Network** | > 5 MB/s |

## Requirements

* Python 3.x
* `psutil` library

Install the dependencies via pip:
```bash
pip install psutil

# CloudOps — Automated Monitoring & Self-Healing

## Overview
An AWS EC2-based project that monitors Linux system resources and automatically recovers a stopped demo service.

## Technologies
- AWS EC2 and Ubuntu
- Python and psutil
- Linux cron and systemd
- Prometheus
- Node Exporter
- Grafana
- Alertmanager

## Features
- Automated CPU, memory, and disk health checks
- Scheduled monitoring scripts
- Self-healing of a stopped systemd service
- Prometheus metrics collection and alert rules
- Grafana infrastructure dashboard

## Logging

Runtime logs are stored locally on the EC2 instance under `logs/`.

- `health_check.log` — CPU, memory, and disk health-check results.
- `self_heal.log` — Service failure detection and recovery events.

Generated logs are excluded from Git to avoid committing continuously changing runtime data.

## Project Structure
- `scripts/` — Health checks, self-healing, and demo service
- `monitoring/` — Monitoring configuration files
- `logs/` — Runtime logs generated on the EC2 instance

## Recovery Test
Stopped the demo service manually and verified that the scheduled recovery script restarted it.

## Security
Monitoring services should remain private. SSH access should be restricted to trusted IP addresses.

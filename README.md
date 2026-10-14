# CloudOps — Self-Healing Infrastructure Monitoring

A hands-on Cloud & DevOps project that combines AWS infrastructure provisioning, Linux system monitoring, visualization, and automated service recovery.

## 📌 Project Overview

CloudOps demonstrates how to provision cloud infrastructure using Terraform, monitor Linux server health with Prometheus and Grafana, and automate service recovery using Python and systemd.

The project focuses on infrastructure monitoring, resource visibility, health checks, and basic self-healing automation.

## 🏗️ Architecture

```text
                AWS Cloud
                    |
               EC2 Instance
                    |
             Ubuntu Linux Server
                    |
          +---------+---------+
          |                   |
      Prometheus          Node Exporter
          |                   |
          +---- Metrics ------+
                    |
                 Grafana
                    |
           Dashboards & Alerts

       Python Health-Check Script
                    |
          systemd Service Recovery
```

## 🛠️ Tech Stack

- **Cloud:** AWS EC2, VPC, Subnets, Internet Gateway, Security Groups
- **Infrastructure as Code:** Terraform
- **Operating System:** Ubuntu Linux
- **Monitoring:** Prometheus, Node Exporter
- **Visualization & Alerting:** Grafana
- **Automation:** Python, Bash, Cron, systemd
- **Version Control:** Git and GitHub

## ⚙️ Key Implementations

### 1. Infrastructure Provisioning
- Provisioned AWS infrastructure using Terraform.
- Configured networking resources, including a VPC, subnet, Internet Gateway, route table, and Security Group.
- Deployed an Ubuntu EC2 instance for monitoring and automation.

### 2. Infrastructure Monitoring
- Installed and configured Prometheus to collect monitoring metrics.
- Configured Node Exporter to expose Linux host metrics.
- Created Grafana dashboards to visualize CPU, memory, and disk utilization.
- Configured a high-CPU alert rule.

### 3. Health Checks and Self-Healing
- Developed Python automation for system health checks and logging.
- Used Linux systemd to manage services.
- Implemented a self-healing script to restart a demo service when it becomes inactive.
- Tested service recovery by manually stopping the service and verifying that the recovery script restarted it.

## 📸 Project Screenshots

### 1. Grafana Monitoring Dashboard

<img width="400" alt="CloudOps Project Screenshot" src="https://github.com/user-attachments/assets/55dc4f5d-f958-489b-b9b0-f87b1f5d22df" />
<img width="400" alt="Screenshot 2026-10-14 230519" src="https://github.com/user-attachments/assets/4b6c09cb-d0f9-4714-aef8-9722c425cf56" />


### 3. CloudOps Project Screenshot

<img width="400" alt="Grafana Monitoring Dashboard" src="https://github.com/user-attachments/assets/583ac00f-9692-43fd-a3a8-7f3a157d08e7" />

## 🎯 Key Learnings

- Provisioning AWS infrastructure using Terraform.
- Configuring Linux monitoring with Prometheus and Node Exporter.
- Building Grafana dashboards and alert rules.
- Writing Python scripts for health checks and service recovery.
- Troubleshooting Linux services and verifying recovery behavior.

## 🚀 Future Improvements

- Configure and test end-to-end alert notifications.
- Improve automated recovery with retry limits and failure logging.
- Add additional monitoring and alerting scenarios.
- Automate infrastructure deployment through a CI/CD pipeline.

## 👨‍💻 Author

**Suraj Ghadage**

Aspiring Cloud & DevOps Engineer | AWS | Linux | Terraform | Prometheus | Grafana

- GitHub: https://github.com/Suraj-dot-wq
- CloudOps Repository: https://github.com/Suraj-dot-wq/CloudOps-Self-Healing-Monitoring

# Automated Cloud Monitoring and Auto-Remediation System

## 📌 Overview
This project implements an **event-driven cloud monitoring and auto-remediation system** using AWS services. The system continuously monitors an EC2 instance for performance issues and automatically triggers remediation logic when predefined thresholds are breached.

The project simulates a real-world **incident detection and response workflow**, commonly used in cloud infrastructure and SRE environments, while remaining fully compatible with AWS free-tier and student subscriptions.

---

## 🧠 Problem Statement
In cloud environments, manual monitoring of infrastructure performance can lead to delayed incident response, service degradation, and increased operational overhead. There is a need for an automated mechanism that can detect performance anomalies and initiate remediation actions without human intervention.

---

## 🎯 Solution
This project uses **Amazon CloudWatch**, **SNS**, and **AWS Lambda** to create an automated monitoring pipeline:

- EC2 performance metrics are continuously collected
- CloudWatch alarms detect sustained high CPU utilization
- Alerts are published to an SNS topic
- A Lambda function is triggered to execute remediation logic
- All actions are logged for observability and auditing

---

## 🏗 Architecture

EC2 Instance--➡️CloudWatch Metrics--➡️CloudWatch Alarm (High CPU)--➡️SNS Topic--➡️AWS Lambda (Auto-Remediation) --➡️CloudWatch Logs


---

## ⚙️ AWS Services Used
- **Amazon EC2 (Ubuntu)** – Compute resource being monitored
- **Amazon CloudWatch** – Metrics, alarms, and logs
- **Amazon SNS** – Event notification and message delivery
- **AWS Lambda (Python 3.10)** – Serverless remediation logic
- **AWS IAM** – Secure, least-privilege access control

---

## 🔐 Security Considerations
- SSH access to EC2 restricted to personal IP addresses
- Lambda uses **AWSLambdaBasicExecutionRole**
- No destructive permissions granted during initial validation
- Follows the **principle of least privilege**

---

## 🧪 Testing & Validation
To validate the system:
1. High CPU usage is simulated on the EC2 instance using a stress utility
2. CloudWatch alarm transitions from `OK` to `ALARM`
3. SNS publishes an alert message
4. Lambda function is automatically triggered
5. Remediation activity is verified through CloudWatch Logs

This confirms end-to-end automation without manual intervention.

---

## 📈 Key Outcomes
- Automated detection of infrastructure performance issues
- Event-driven remediation using serverless architecture
- Improved observability through centralized logging
- Reduced need for manual monitoring and response

---

## 🚀 Future Enhancements
- Add automated EC2 reboot or stop actions
- Integrate email or Slack notifications
- Extend monitoring to memory and disk metrics
- Implement Infrastructure as Code using Terraform
- Add cost monitoring and budget alerts

---

## 🧑‍💻 Author
 Syamanth
Computer Science Student | Cloud & DevOps Enthusiast
---

# Automated EC2 Health Monitor

## Project Overview
This project is a Python-based automation tool designed for Cloud Engineers to monitor the health and status of AWS EC2 instances in real-time. Instead of manually checking the AWS Management Console, this script provides an automated report of your infrastructure.

## Key Features
- **Real-time Status Tracking:** Automatically fetches the status (Running/Stopped) of all EC2 instances in your account.
- **Detailed Reporting:** Generates a clear summary of your infrastructure health directly in the terminal.
- **Root Cause Analysis (In Progress):** The project is being expanded to identify the reason why an instance has stopped (e.g., scheduled maintenance, user-initiated shutdown, or system failure).

## Technologies Used
- **Python:** For writing the automation logic.
- **Boto3:** The AWS SDK for Python to interact with EC2 services.
- **AWS EC2:** Cloud infrastructure monitoring.

## How it Works
1. The script uses the `boto3` library to communicate with the AWS API.
2. It filters through your EC2 instances to retrieve their current state.
3. Future updates will include logs to detect specific "Stop" events to help in troubleshooting infrastructure issues.

## Why this Project?
This tool helps in reducing manual overhead and enables proactive infrastructure management, which is a core requirement for DevOps and Cloud Architecture roles.

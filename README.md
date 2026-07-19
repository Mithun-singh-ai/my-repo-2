# Automated EC2 Health & Audit Monitor

## Project Overview
This project is an advanced Python-based automation tool designed for Cloud Engineers to monitor the health and audit the status of AWS EC2 instances in real-time. It replaces manual console checks with an automated, audit-ready report of your infrastructure.

## Key Features
- **Real-time Status Tracking:** Automatically fetches the status (Running/Stopped) of all EC2 instances in your account.
- **Root Cause Analysis:** Automatically identifies *who* stopped an instance and *when* by integrating with AWS CloudTrail.
- **Detailed Reporting:** Generates a clear summary of infrastructure health directly in the terminal.

## Technologies Used
- **Python:** Core automation logic.
- **Boto3:** AWS SDK for Python to interact with EC2 and CloudTrail APIs.
- **AWS EC2:** Cloud compute infrastructure monitoring.
- **AWS CloudTrail:** Used to track and audit API activity for infrastructure changes.

## How it Works
1. The script uses the `boto3` library to communicate with the AWS EC2 API to identify instance states.
2. If an instance is found in a `stopped` state, the script triggers a `cloudtrail.lookup_events` call.
3. It parses the CloudTrail logs to display the specific user identity and timestamp associated with the stop event.
4. The final status and audit details are printed clearly in the terminal.

## Why this Project?
This tool mimics real-world DevOps practices by moving from manual monitoring to automated auditing. It demonstrates the ability to interact with multiple AWS services (EC2 + CloudTrail) to improve operational visibility and security compliance.
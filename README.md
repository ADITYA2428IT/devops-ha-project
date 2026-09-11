# 🚀 Highly Available DevOps Web Application

A simple DevOps project demonstrating a **Highly Available Web Application on AWS** with **EC2, Application Load Balancer, Multi-AZ deployment, GitHub, and GitHub Actions CI/CD**.

---

## 📌 Project Overview

This project deploys a Flask web application on two AWS EC2 instances located in different Availability Zones.

An **Application Load Balancer (ALB)** distributes incoming traffic between the EC2 instances.

GitHub Actions is used to automatically deploy the latest code to both EC2 instances whenever changes are pushed to the `main` branch.

---

## 🏗️ Architecture

```text
                    Internet
                       |
                       v
              Application Load Balancer
                       |
              +--------+--------+
              |                 |
              v                 v
          EC2 Instance 1    EC2 Instance 2
          Availability Zone  Availability Zone
              |                 |
              +--------+--------+
                       |
                       v
                  Flask App
                    :5000

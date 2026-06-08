# 🛡️ NetGuard Security Center
**Live Demo:** [View NetGuard on Render](https://netguard-api-91fg.onrender.com)

## Overview
NetGuard is a secure RESTful API and simulated Network Operations Center (NOC) dashboard. It generates, categorizes, and serves simulated TCP/IP packet data while demonstrating robust backend security practices.

## 🚀 Key Features
* **API Key Authentication:** Features a custom Python decorator that intercepts HTTP requests, explicitly blocking unauthorized access (returning `401 Unauthorized`) unless a valid `x-api-key` is detected in the headers.
* **Network Protocol Simulation:** Accurately models data structures for TCP, UDP, ICMP, and HTTPS traffic, assigning simulated threat-assessment weights to varying payload sizes.
* **Asynchronous Dashboard:** Includes an integrated frontend interface that utilizes JavaScript `fetch()` to securely pass API credentials and render backend JSON data in real-time.

## 🛠️ Technical Stack
* **Backend & API:** Python 3, Flask
* **Security:** Custom Header Authentication 
* **Cloud Deployment:** Render, Gunicorn WSGI
* **Frontend:** Responsive HTML/CSS, Asynchronous JavaScript

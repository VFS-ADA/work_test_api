# Visma Amili - Work Test API

### Prerequisite (Ubuntu)

> [Download and install MongoDb on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

> [Download MongoDb Compass](https://www.mongodb.com/products/compass)

> Install PyCharm Community Edition via Software App

# Plan for Developing a "Public Transport Driver Deployment" Application

## 1. API Endpoint Design
- Structure well-defined API endpoints to facilitate communication between the frontend, backend, and any external services.
- Include endpoints for:
  - Driver Management
  - Route Scheduling
  - Assignment Operations
  - Notifications
  - Reporting Functionalities

## 2. Development Task Breakdown
- Develop a comprehensive plan outlining the specific development tasks required to build the application.
- Key tasks include implementing core features such as:
  - Authentication
  - Driver Management
  - Route Scheduling
  - Assignment Automation
  - Real-Time Monitoring
  - Reporting

# "Public Transport Driver Deployment" application
## Overview
The "Public Transport Driver Deployment" application is designed to manage the assignment of drivers to various public transport routes effectively. The system should optimize scheduling, handle driver requests, accommodate last-minute changes, and ensure clear communication between transport managers and drivers.

## Core Functionalities

### Driver Management:
- Maintain a roster of available drivers with their skills, certifications, and scheduling preferences.
- Allow drivers to update their availability and preferences via a user interface or mobile application.

### Route and Schedule Management:
- Define and manage transport routes and schedules.
- Allow dynamic scheduling based on factors like driver availability, route demand, and operational needs.

### Assignment and Deployment:
- Automatically assign drivers to routes based on criteria such as availability, route familiarity, and seniority.
- Allow manual overrides and adjustments by transport managers.

### Communication:
- Send notifications to drivers regarding assignments, changes, and alerts via SMS or push notifications.
- Provide a feedback loop for drivers to confirm or request changes to assignments.

### Real-Time Monitoring and Adjustments:
- Offer a dashboard for managers to monitor current deployments and make real-time adjustments.
- Handle disruptions such as driver sick leave or route changes efficiently.

### Historical Data and Reporting:
- Keep logs of driver assignments for audit and analysis.
- Generate reports to assess driver utilization and operational efficiency.


## We will evaluate the application development based on the following criteria:

- **Readability:** 
  - Clarity and understandability of the code, including comments and straightforward logic.

- **Code Formatting:** 
  - Adherence to PEP8 standards and Pythonic principles for backend code, and appropriate style guides for Vue 3 in frontend development.

- **Code Reusability:** 
  - Effective reuse of code components and functions to minimize redundancy.

- **Design Patterns:** 
  - Utilization of recognized programming patterns, such as MVC (Model-View-Controller) and others relevant to both backend and frontend development.

- **Project Structure:** 
  - Logical and organized structuring of files and directories in both the backend and frontend parts of the application.

- **Optimal Use of Frameworks:** 
  - Efficient and effective use of open-source frameworks like Python Eve for the backend and Vue 3 for the frontend, showcasing best practices and advanced features.

- **Innovation and Improvement:** 
  - Feel free to add additional functionalities or refactor existing code to demonstrate your skills, creativity, and understanding of systematizing a complex application.


---
---

### Sub Task #1

    Add encyption on user password (one way encryption) using the package passlib

### Sub Task #2

    Add access control to all endpoints except "/authenticate" using Event Hooks in Python EVE

## Documentation

> [Password Library](https://passlib.readthedocs.io/en/stable/)

> [Event hooks](https://docs.python-eve.org/en/stable/features.html#eventhooks)

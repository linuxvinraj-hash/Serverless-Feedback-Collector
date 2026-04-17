# Serverless-Feedback-Collector

# 🚀 Serverless Feedback Collector

## 📌 Overview
A lightweight serverless application to collect user feedback via a web form and display submissions in an admin dashboard.

Built using AWS services with a production-style architecture.

---

## 🏗 Architecture

- **Frontend:** S3 Static Website (HTML/JS)
- **API Layer:** API Gateway (HTTP API)
- **Compute:** AWS Lambda (Python)
- **Database:** DynamoDB

  <img width="1296" height="710" alt="image" src="https://github.com/user-attachments/assets/ba423cf4-797d-4e01-8e7a-0d2f77a934ba" />


---

## 🔄 Workflow

1. User submits feedback via form
2. API Gateway forwards request to Lambda
3. Lambda stores feedback in DynamoDB
4. Admin page fetches and displays feedback

---

## 📡 API Endpoints
https://dphkf5s57d.execute-api.ap-southeast-2.amazonaws.com

## DynamoDB Schema

TableName - FeedbackCollector

| Attribute  | Type                 | Description                                                  |
| ---------- | -------------------- | ------------------------------------------------------------ |
| feedbackId | String (Primary Key) | Unique identifier (UUID) for each feedback submission        |
| name       | String               | Name of the user providing feedback                          |
| message    | String               | Feedback content submitted by the user                       |
| timestamp  | Number               | Submission time stored as Unix Epoch (for sorting/filtering) |

## 🌐 Live Demo

FeedBackCollecter - https://feedback-app-collec.s3.ap-southeast-2.amazonaws.com/index.html

AdminLogs - https://feedback-app-collec.s3.ap-southeast-2.amazonaws.com/admin.html


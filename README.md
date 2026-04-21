# LeetCode Daily Email Alert

This project fetches the daily problem using the LeetCode GraphQL API and sends an email notification using SMTP.  
It runs automatically using **GitHub Actions**, so your laptop does not need to be running.

---

## Features

- Fetches the LeetCode Daily Challenge
- Sends formatted email notification
- Runs automatically every day
- Secure credential management with GitHub Secrets
- Simple Python implementation

---

## Project Structure

```
leetcode-daily-email-alert
│
├── .github
│   └── workflows
│       └── daily_leetcode.yml
│
├── src
│   └── send_leetcode_email.py
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## Setup Guide

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/leetcode-daily-email-alert.git
cd leetcode-daily-email-alert
```

---

### 2. Create Gmail App Password

1. Go to Google Account Security
2. Enable **2‑Factor Authentication**
3. Generate **App Password**
4. Copy the password

You will use this instead of your Gmail password.

---

### 3. Add GitHub Secrets

Go to:

```
Repository → Settings → Secrets → Actions
```

Add the following secrets:

| Secret Name    | Value                  |
| -------------- | ---------------------- |
| EMAIL_ADDRESS  | your gmail             |
| EMAIL_PASSWORD | gmail app password     |
| TO_EMAIL       | email to receive alert |

---

### 4. Push Code

Once the code is pushed to GitHub, the automation will start running.

You can also trigger it manually:

```
Actions → Run Workflow
```

---

## Automation Schedule

The GitHub Action runs daily using cron:

```
0 3 * * *
```

This means:

**Every day at 03:00 UTC**.

---

## Example Email

```
LeetCode Daily Problem

Title: Two Sum
Difficulty: Easy

Solve here:
https://leetcode.com/problems/two-sum
```

---

## License

MIT License


import requests
import smtplib
import os
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL_ADDRESS"]
PASSWORD = os.environ["EMAIL_PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

url = "https://leetcode.com/graphql"

query = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    question {
      title
      difficulty
      titleSlug
    }
  }
}
"""

response = requests.post(url, json={"query": query}).json()

data = response["data"]["activeDailyCodingChallengeQuestion"]["question"]

title = data["title"]
difficulty = data["difficulty"]
slug = data["titleSlug"]

link = f"https://leetcode.com/problems/{slug}"

message = f"""
LeetCode Daily Problem

Title: {title}
Difficulty: {difficulty}

Solve here:
{link}
"""

msg = MIMEText(message)
msg["Subject"] = "🚀 LeetCode Daily Problem"
msg["From"] = EMAIL
msg["To"] = TO_EMAIL

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(EMAIL, PASSWORD)
server.send_message(msg)
server.quit()

print("Email sent successfully!")

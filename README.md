
# 🗣️ ChatBot with Rasa

This project is a conversational chatbot built with **Rasa (Open Source)** in **Python**, capable of:

- Listing menu items from a JSON config file
- Answering restaurant opening hours
- Taking food orders (with special requests)
- Summarizing the order
- Asking for delivery or pick-up
- Integrating with Slack

---

## 🚀 Features

- ✅ Natural language understanding with Rasa NLU
- ✅ Reads menu and hours from `menu.json` and `opening_hours.json`
- ✅ Tracks multiple user intents like `order_meal`, `ask_menu`, `ask_hours`
- ✅ Handles custom logic in `actions.py`
- ✅ Works with **Slack** (via webhook + ngrok)

---

## 📦 Requirements

- Python 3.8–3.11
- pip
- virtualenv (recommended)
- Rasa >= 3.0

---

## ⚙️ Setup Guide

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Python-chatbot-with-rasa.git
cd Python-chatbot-with-rasa/ChatBot
```

---

### 2. 🧪 Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

---

### 3. 📥 Install Dependencies

```bash
pip install rasa
pip install -r requirements.txt  # If you have a custom list
```

---

### 4. 🧠 Train the Bot

```bash
rasa train
```

---

### 5. ⚙️ Run Action Server

```bash
rasa run actions
```

> Keep this terminal open.

---

### 6. ▶️ Start the Rasa Server

In a new terminal (in the same folder):

```bash
rasa run --enable-api --cors "*" --debug
```

---

### 7. 🌐 Expose Localhost with Ngrok

In another terminal:

```bash
ngrok http 5005
```

Copy the `https://...` URL (e.g. `https://abcd1234.ngrok.io`)

---

## 💬 Slack Integration (Optional)

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Create a new app
3. Add these scopes under **OAuth & Permissions**:
   - `chat:write`
   - `im:read`, `im:write`, `im:history`
   - `channels:history`
   - `app_mentions:read`
4. Under **Event Subscriptions**, enable events:
   - Add `https://<your-ngrok-url>/webhooks/slack/webhook` as the **Request URL**
   - Subscribe to: `message.im`, `message.channels`, `app_mention`
5. Install the app to your workspace
6. Copy your **Bot Token** and **Signing Secret**
7. Update your `credentials.yml`:

```yaml
slack:
  slack_token: "xoxb-..."
  slack_signing_secret: "..."
```

8. Restart the `rasa run` process

---

## 📂 Project Structure

```bash
ChatBot/
├── actions/
│   └── actions.py
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── models/
├── menu.json
├── opening_hours.json
├── domain.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── README.md
```

---

## 🧪 Testing Locally

You can talk to your bot locally using:

```bash
rasa shell
```

---

## ❓ Troubleshooting

- **`rasa: command not found`** — Activate your virtual environment and ensure Rasa is installed
- **Slack 403 or 500** — Verify ngrok URL and `credentials.yml`
- **Bot not responding?** — Check terminal logs for errors

---

## 🧾 License

MIT License

---

## 👥 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## ✨ Author

Created by [Nikita Zinchenko](https://github.com/yourusername)

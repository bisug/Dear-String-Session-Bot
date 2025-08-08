# 🎵 Dear String Session Bot

[![GitHub Stars](https://img.shields.io/github/stars/bisug/Dear-String-Session-Bot?style=flat&color=gold)](https://github.com/bisug/Dear-String-Session-Bot/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/bisug/Dear-String-Session-Bot?style=flat&color=brightgreen)](https://github.com/bisug/Dear-String-Session-Bot/network/members)
[![Views](https://komarev.com/ghpvc/?username=bisug-Dear-String-Session-Bot&label=Views&color=blue&style=flat)](https://github.com/bisug/Dear-String-Session-Bot)
[![License](https://img.shields.io/github/license/bisug/Dear-String-Session-Bot?color=orange)](LICENSE)

A powerful and easy-to-use Telegram bot for generating **Pyrogram** and **Telethon** string sessions, managing **force subscriptions**, and **broadcasting messages** — all in one place.

---

## ✨ Features

- 🎯 **Generate Pyrogram Session**  
- 🤖 **Generate Pyrogram Bot Session**  
- 📜 **Generate Telethon Session**  
- 🤖 **Generate Telethon Bot Session**  
- 📌 **Force Subscribe**: Add a mandatory subscription channel before users can use the bot.  
- 📢 **Broadcast Messages**: Send messages to all bot users (owner only).  

---

## 🚀 1-Click Deployment

Easily deploy this bot to your favorite hosting service:

| Platform | Deploy |
|----------|--------|
| **Render** | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/bisug/Dear-String-Session-Bot) |

---

## 📜 Commands

| Command       | Description |
|---------------|-------------|
| `/start`      | ✅ Check if the bot is alive. |
| `/generate`   | 📝 Generate a string session. |
| `/broadcast`  | 📢 Broadcast a message to all users (owner only). |

---

## ⚙️ Environment Variables

| Variable      | Description |
|---------------|-------------|
| `API_ID`      | Your API ID from [my.telegram.org](https://my.telegram.org/apps). |
| `API_HASH`    | Your API Hash from [my.telegram.org](https://my.telegram.org/apps). |
| `BOT_TOKEN`   | Your bot token from [@BotFather](https://t.me/BotFather). |
| `OWNER_ID`    | Telegram ID of the bot owner (for broadcasting). |
| `F_SUB`       | *(Optional)* ID of the force-subscribe channel (bot must be admin there). |
| `MONGO_DB_URI`| MongoDB database URI from [MongoDB](https://mongodb.com) — [Video Guide](https://youtu.be/DAHRmFdw99o). |

---

## 🖥 Local Setup

```bash
# Clone the repository
git clone https://github.com/bisug/Dear-String-Session-Bot.git
cd Dear-String-Session-Bot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python ssgen.py

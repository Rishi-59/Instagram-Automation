# Instagram Auto Follower Bot

A Python automation project built with **Selenium WebDriver** that logs into Instagram, opens a target user's followers list, loads all followers by scrolling, and automatically follows eligible accounts while handling common Instagram pop-ups.

> **Disclaimer:** This project is intended for educational purposes only. Automating interactions on Instagram may violate Meta's Terms of Service. Use responsibly and at your own risk.

---

## Features

* 🔐 Automated Instagram login
* 👥 Opens any public user's followers list
* 📜 Automatically scrolls through the followers modal to load more users
* ➕ Clicks **Follow** on eligible accounts
* 🚫 Detects and dismisses confirmation pop-ups (e.g., private account prompts)
* ⏳ Uses explicit waits for reliable element interaction
* 🔄 Retries intercepted clicks automatically
* 🧩 Modular, object-oriented code structure

---

## Tech Stack

* Python 3
* Selenium WebDriver
* ChromeDriver
* python-dotenv

---

## Project Structure

```text
.
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/instagram-auto-follower.git
cd instagram-auto-follower
```

### 2. Create a virtual environment

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
USERNAME=your_instagram_username
PASSWORD=your_instagram_password
BASE_URL=https://www.instagram.com
```

---

## Configuration

Specify the Instagram account whose followers you want to browse.

```python
t_username = "chefsteps"
```

Replace it with any public Instagram username.

---

## Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Log into Instagram.
2. Dismiss login and notification pop-ups.
3. Open the target profile.
4. Load the complete followers list by scrolling.
5. Automatically click **Follow** on available accounts.

---

## How It Works

* Logs in using Selenium.
* Waits for elements using explicit waits.
* Opens the followers modal.
* Scrolls until no additional followers are loaded.
* Finds all visible follow buttons.
* Clicks each button.
* Handles intercepted clicks by dismissing confirmation dialogs and retrying.

---

## Requirements

* Python 3.10+
* Google Chrome
* Matching ChromeDriver version

---

## Dependencies

```text
selenium
python-dotenv
```

---

## Future Improvements

* Add random delays to mimic human behavior
* Configurable follow limit
* Logging and progress tracking
* Headless browser support
* Automatic unfollow functionality
* Better handling of Instagram rate limits
* CLI arguments for target username

---

## License

This project is intended for educational and learning purposes.

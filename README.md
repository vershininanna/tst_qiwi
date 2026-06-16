QIWI API Test Framework

Automated API tests for **QIWI Wallet API** using Python, Pytest and Playwright.

Tech Stack

- Python 3.13+
- Pytest
- Playwright (API requests)
- Allure Reports

---

## ⚙️ Setup Instructions

### 1. Clone repository

git clone https://github.com/vershininanna/tst_qiwi.git
cd tst_qiwi

### 2. Create virtual environment

python -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run all tests

python3 -m pytest

### 5. Report

allure serve reports
# Automated Video Scraper & Downloader

## Overview

This project automates the process of logging into an online learning platform, scraping video URLs from lesson pages, and downloading them for offline access. It utilizes **Selenium** for web automation and **Requests** for downloading the videos. Additionally, the script is converted into an executable (`.exe`) for easy execution without requiring Python installation.

## Features

- **Automated Login**: Uses Selenium to log into the website with provided credentials.
- **Video Scraping**: Extracts video URLs from multiple lesson pages.
- **Bulk Downloading**: Saves all video files locally.
- **Headless Execution**: Runs without opening the browser for faster performance.
- **EXE Conversion**: The script is compiled into an executable file.

## Prerequisites

### 1. Install Required Dependencies

Ensure you have **Python 3.x** installed. Then, install the necessary Python libraries:

```bash
pip install selenium webdriver-manager requests pyinstaller
```
### 2. Install Google Chrome & ChromeDriver

Ensure you have Google Chrome installed, and ChromeDriver is available. The script automatically downloads the correct version using webdriver-manager.

# Usage

## Run the Python Script
```bash
python main.py
```

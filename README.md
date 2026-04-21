# Xunter — Advanced VPN Config Tester

> **[English](./README.md)** | **[فارسی](./README_FA.md)**

---

## Introduction

**Xunter** is a powerful and modular VPN configuration tester built on top of **Xray Core**.
It allows you to test both **link-based** and **file-based** VPN configs with high accuracy and real network validation.

The tool is designed to be:

- Fast (multi-threaded)
- Accurate (real connection testing)
- Modular (easy to extend)
- Reliable (stable & clean output)

---

## Features

- Supports multiple protocols (vmess, vless, trojan, ss, etc.)
- Works with both links and config files
- Live terminal output (real-time results)
- Clean & colored table UI
- Smart scoring system
- Multi-threaded engine
- Cross-platform (Windows / Linux / macOS)
- Uses Xray Core for real connection testing
- Saves working configs automatically

---

## Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Installation

### Method 1: Download ZIP

1. Download the project as ZIP
2. Extract it
3. Open terminal in project folder
4. Run:

```bash
python hunterx.py
```

---

### Method 2: Clone with Git

```bash
git clone https://github.com/your-repo/xunter.git
cd xunter
pip install -r requirements.txt
python hunterx.py
```

---

## settings.json

```json
{
    "timeout": 2,
    "test_url": "https://google.com",
    "workers": 3,
    "socks_port_start": 1080
}
```

### Workers Tip

- Few configs → use lower workers (e.g. 5)
- Many configs → increase workers (e.g. 20+)

> ⚠️ High values may increase CPU usage

---

## Adding Configs

### Method 1: Manual (JSON)

Edit `configs.json`:

```json
{
    "configs": [
        {
            "name": "My VPN",
            "type": "vless",
            "raw": "vless://..."
        }
    ]
}
```

---

### Method 2: adding one by one

```bash
python add_configs.py
```

✔ No JSON knowledge required
✔ Beginner-friendly

---

### Method 3: Easy Mode (Recommended)

**Run the file and enter your .txt path.**

```bash
python add_configs_by_txt.py
```

✔ No JSON knowledge required
✔ Beginner-friendly
✔ Adding configs by `.txt` file
✔ Adding name automaticly
✔ Detecting type automaticly


---

## File Configs

Place your config files inside:

```
configs/
```

---

## Run

```bash
python hunterx.py
```

---

## Output Files

Working configs are saved in:

```
actives.json
```

---

## Cross Platform

Works on:

- Windows
- Linux
- macOS

---

## Extending Protocols

To add a new protocol:

1. Create a file in `protocols/`
2. Implement:

```python
class Protocol:
    def build(self, config, port):
        ...
```

---

## Final Notes

Xunter is built for developers and advanced users who need:

- Fast bulk config testing
- Accurate validation
- Clean CLI output

---

If you find this project useful you can join to my telegram channel.

[A Hunter](https://t.me/ahunter0)

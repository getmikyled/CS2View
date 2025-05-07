# CS2 View

CS2 View is a lightweight GUI application for analyzing Counter-Strike 2 demo files. It provides detailed statistical breakdowns of player and team performance, including:

- ADR (Average Damage per Round)
- KAST (Kill, Assist, Survive, Trade percentage)
- HLTV-style Rating
- Round End Reasons (elimination, bomb defusal, etc.)

The application is designed to simplify parsing `.dem` files and surface competitive insights with a clean, intuitive interface.

---

## Features

- Supports CS2 demo files parsed locally
- Interactive table of player stats
- Aggregated round outcomes and filters
- Easily switch between sides
- Fast loading and responsive interface

---

## Requirements

- Python 3.11 or later

---

## Installation

### Option 1: Use `setup.sh` (Recommended)

- If you have python3 installed:

```bash
git clone https://github.com/yourusername/CS2View.git
cd CS2View
chmod +x setup.sh
./setup.sh
```

### Option 2:

- Manually create your environment and install dependencies

```
# once you have created a python env with python 3.11 or later
pip install -r requirements.txt
```

## Running

- Running is as simple as `python main.py` in your terminal

## Example Demo

- An example demo can be downloaded at https://drive.google.com/file/d/1gNhNMjm5WK0cMVgDBav_CEKb5sT_rGsY/view 

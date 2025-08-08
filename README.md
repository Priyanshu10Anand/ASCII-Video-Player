# 🎞️ ASCII Video Player

Convert videos into animated ASCII art and play them in your terminal using Python!

> Inspired by the viral “Indonesian Aura Kid” video, now rendered in ASCII ✨

---

## 📁 Project Structure

```
.
├── .venv/              # Virtual environment (optional)
├── ascii_frames/       # Stores .txt ASCII frames (generated)
├── frames/             # Stores extracted video frames (generated)
├── aura.mp4.webm       # Input video
├── converter.py        # Converts PNG frames to ASCII
├── player.py           # Plays ASCII frames in terminal
└── README.md           # This file
```

---

## ⚙️ Requirements

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html)
- Pillow (`pip install Pillow`)

---

## 🧰 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Priyanshu10Anand/ascii-video-player.git
cd ascii-video-player
```

### 2. (Optional) Set up a virtual environment

```bash
python -m venv .venv
# Activate it:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install Pillow
```

---

## 🎬 Convert Video to ASCII

### Step 1: Extract frames using FFmpeg

Make sure `ffmpeg` is installed and accessible via terminal.

```bash
ffmpeg -i aura.mp4.webm -vf "fps=10,scale=140:-1" frames/frame_%03d.png
```

- `fps=10`: sets frame rate (adjust for speed)
- `scale=140:-1`: resizes width to 140 pixels while maintaining aspect ratio

### Step 2: Convert PNG frames to ASCII

Run the converter:

```bash
python converter.py
```

This creates an `ascii_frames/` directory with `.txt` files for each frame.

---

## 📽️ Play ASCII Video in Terminal

After converting, run:

```bash
python player.py
```

Enjoy the video in full ASCII glory.

---

## 🧠 How It Works

- Frames are extracted from the video (`frames/*.png`)
- Each frame is converted to grayscale and mapped to ASCII characters
- The terminal prints them in sequence at a set frame rate

---

## 🚫 .gitignore (Suggested)

Add this to your `.gitignore` to avoid uploading heavy/generated files:

```
# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/

# Output folders
frames/
ascii_frames/

# Media files
*.mp4
*.webm
*.avi
*.mov

# OS
.DS_Store
Thumbs.db
```

---

## 🌟 Credits

- Original idea: [Indonesian Aura Kid](https://youtube.com/shorts/vnJs7ODTvNU?si=mK5jNmOs6kYCZKtZ)

Made with ❤️ by Priyanshu Anand

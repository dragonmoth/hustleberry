# 🍓 HustleBerry

HustleBerry is a cute, floating **Pomodoro timer widget** built with **PyQt6**, styled with strawberry shortcake vibes — rounded, transparent, draggable, and sound-enabled! 🎀

![Screenshot_2025-06-17_171741-removebg-preview](https://github.com/user-attachments/assets/1a61e7f9-e093-45c6-8b61-439113db3bd3)

---

## 🧠 Features

- 🍰 Minimal transparent widget (280x340)
- ⏱️ Pomodoro logic: Work → Short Break → Work → Long Break
- 🔔 Sound alert on each session (plays `alarm.wav`)
- 💗 Aesthetic UI with image buttons and Kranky font
- 🍓 Auto-switches between sessions
- 📌 Drag to move, stays on top, frameless

---

## 🎮 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/dragonmoth/hustleberry.git
cd hustleberry
```

### 2. Install dependencies
```bash
pip install PyQt6
```

### 3. Run it!
```bash
python main.py
```

---

## 🎨 Assets

| File              | Purpose                         |
|-------------------|---------------------------------|
| `background.png`  | Widget background (rounded)     |
| `heart.png`       | Start/Pause toggle              |
| `reset.png`       | Reset timer                     |
| `short_break.png` | Start short break               |
| `long_break.png`  | Start long break                |
| `work.png`        | Start work session              | 
| `alarm.wav`       | Sound played when session ends  | 

---

## ⚙️ Customize

You can change durations in `pomodoro.py`:

```python
"Work": 25 * 60,
"Short Break": 5 * 60,
"Long Break": 10 * 60
```

Or use test mode with `10s` blocks for debugging.

---

## 📦 Packaging as .exe (optional)

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed main.py
```

Then find it in `dist/main.exe`

---

## 💖 Made with love

By [@dragonmoth](https://github.com/dragonmoth) — for focus, fun, and productivity 🍓

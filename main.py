from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QFrame
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtMultimedia import QSoundEffect
import sys
import os
from pomodoro import PomodoroTimer

class HustleBerry(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HustleBerry")
        self.setFixedSize(280, 340)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.drag_position = None

        # Background
        self.bg_label = QLabel(self)
        pixmap = QPixmap("background.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, 280, 340)

        # Timer logic
        self.timer = PomodoroTimer()
        self.is_running = False
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.countdown)

        # Sound setup
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("alarm.wav"))  # ← Levelup.wav renamed to alarm.wav
        self.sound.setLoopCount(1)
        self.sound.setVolume(0.9)

        # Timer Frame
        self.timer_frame = QFrame(self)
        self.timer_frame.setStyleSheet(
            "background-color: #ABA78E; border-radius: 12px; border: 2px solid white;"
        )

        # Timer Label
        self.timer_label = QLabel(self.timer.get_time(), self.timer_frame)
        self.timer_label.setFont(QFont("Kranky", 30))
        self.timer_label.setStyleSheet("color: #EBAFAB; background: transparent;")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        self.add_button("heart.png", 126, 255, self.toggle_timer, 35, 34)
        self.add_button("reset.png", 182, 255, self.reset_timer, 77, 24)
        self.add_button("work.png", 25, 257, lambda: self.set_mode("Work"), 77, 24)
        self.add_button("short_break.png", 180, 27, lambda: self.set_mode("Short Break"), 77, 24)
        self.add_button("long_break.png", 180, 74, lambda: self.set_mode("Long Break"), 77, 24)

        self.set_mode("Short Break")

    def add_button(self, filename, x, y, callback, w, h):
        if not os.path.exists(filename):
            print(f"⚠️ Missing image: {filename}")
        btn = QPushButton(self)
        pixmap = QPixmap(filename).scaled(w, h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        btn.setIcon(QIcon(pixmap))
        btn.setIconSize(pixmap.size())
        btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0);
                border: none;
                outline: none;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0);
            }
            QPushButton:pressed {
                background-color: rgba(0, 0, 0, 0);
            }
        """)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        btn.setGeometry(x, y, w, h)
        btn.clicked.connect(callback)

    def set_mode(self, mode):
        self.timer.set_mode(mode)
        self.is_running = False
        self.qtimer.stop()
        self.update_timer()

    def toggle_timer(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.qtimer.start(1000)
        else:
            self.qtimer.stop()

    def countdown(self):
        if self.timer.tick():
            self.update_timer()
        else:
            self.qtimer.stop()
            self.is_running = False
            self.sound.play()               # 🔔 Play alarm
            self.timer.next_mode()         # Auto switch mode
            self.update_timer()
            self.qtimer.start(1000)        # Auto start next session

    def update_timer(self):
        time_text = self.timer.get_time()
        self.timer_label.setText(time_text)

        font_metrics = self.timer_label.fontMetrics()
        text_width = font_metrics.boundingRect(time_text).width() + 30
        text_height = font_metrics.boundingRect(time_text).height() + 5

        self.timer_frame.setFixedSize(text_width, text_height)
        self.timer_label.setGeometry(0, 0, text_width, text_height)

        self.timer_frame.move((self.width() - text_width) // 2 + 5, 125)

    def reset_timer(self):
        self.timer.reset()
        self.update_timer()
        self.is_running = False
        self.qtimer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HustleBerry()
    window.show()
    sys.exit(app.exec())

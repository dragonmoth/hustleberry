class PomodoroTimer:
    def __init__(self, mode="Work"):
        self.session_count = 0
        self.set_mode(mode)

    def set_mode(self, mode):
        self.mode = mode
        if mode == "Work":
            self.total_seconds = 25 * 60
        elif mode == "Short Break":
            self.total_seconds = 5 * 60
        elif mode == "Long Break":
            self.total_seconds = 10 * 60
        else:
            raise ValueError("Unknown mode")

    def tick(self):
        if self.total_seconds > 0:
            self.total_seconds -= 1
            return True
        return False  # Time's up

    def get_time(self):
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def reset(self):
        self.set_mode(self.mode)

    def next_mode(self):
        if self.mode == "Work":
            self.session_count += 1
            if self.session_count % 3 == 0:
                self.set_mode("Long Break")
            else:
                self.set_mode("Short Break")
        else:
            self.set_mode("Work")

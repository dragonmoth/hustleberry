from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class AppReloader(FileSystemEventHandler):
    def __init__(self, app_file):
        self.app_file = os.path.abspath(app_file)
        self.process = None
        self.restart_app()

    def restart_app(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        print("🔁 Reloading app...")
        self.process = subprocess.Popen(["python", self.app_file])

    def on_modified(self, event):
        # Ignore temporary and cache files
        if (
            event.is_directory or
            not event.src_path.endswith(".py") or
            os.path.abspath(event.src_path) != self.app_file
        ):
            return

        print(f"Detected change in {event.src_path}")
        self.restart_app()

if __name__ == "__main__":
    app_file = "main.py"
    event_handler = AppReloader(app_file)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
            event_handler.process.wait()
    observer.join()

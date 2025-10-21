from PySide6.QtWidgets import QApplication
import sys
from launcher.views.main_window import MainWindow
from launcher.utils.paths import DATA_DIR

def main():
    app = QApplication(sys.argv)
    DATA_DIR.mkdir(exist_ok=True, parents=True)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

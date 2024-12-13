import sys
from PySide6.QtWidgets import QApplication
from auth_window import AuthWindow
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow(app)
    AuthWindow(main)
    sys.exit(app.exec())

from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QImage, QPixmap

from ..uis.ui_check import Ui_CheckWindow
from app.views.main_menu_view import MainMenu

import cv2


class CheckWindow(QMainWindow, Ui_CheckWindow):
    def __init__(self, student_id, student_name, main_menu_window=None):
        super().__init__()

        self.student_name = student_name
        self.student_id = student_id
        self.main_menu_window = main_menu_window

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | Check")

        self.modifyWindow()

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

    def modifyWindow(self):
        self.btnBackMainMenu.clicked.connect(self.back_to_main_menu)
        self.integrate_camera_to_frame()

    def integrate_camera_to_frame(self):
        self.cameraFrame_layout = self.cameraFrame.layout()

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        self.cameraFrame_layout.addWidget(self.video_label)

        self.video_capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    @Slot()
    def update_frame(self):
        ret, frame = self.video_capture.read()

        if ret:
            # Convert the OpenCV frame to a QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(
                frame.data, width, height, bytes_per_line, QImage.Format_RGB888
            ).rgbSwapped()

            # Convert QImage to QPixmap and display it in the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)

    def closeCamera(self):
        # Release the video capture when the application is closed
        self.video_capture.release()

    def back_to_main_menu(self):
        self.closeCamera()
        self.main_menu_window = MainMenu(
            self.student_name,
            self.student_id,
        )
        self.main_menu_window.show()
        self.hide()

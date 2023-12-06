from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtGui import QImage, QPixmap

from ..uis.ui_check import Ui_CheckWindow
from app.controllers.check_controller import CheckController
from app.models.test import Test
from app.views.main_menu_view import MainMenu

import cv2
import os


class CheckWindow(QMainWindow, Ui_CheckWindow):
    def __init__(self, student_name, student_id, main_menu_window=None):
        super().__init__()

        self.student_name = student_name
        self.student_id = student_id
        self.main_menu_window = main_menu_window
        self.check_controller = CheckController()
        self.check_controller.create_paths()
        self.test = Test()

        self.setupUi(self)
        self.setWindowTitle(f"WattWise | Check")

        self.modifyWindow()

        self.showMaximized()
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

    def modifyWindow(self):
        self.btnBackMainMenu.clicked.connect(self.back_to_main_menu)
        self.btnCapture.clicked.connect(self.capture_image)
        self.btnCheck.clicked.connect(self.check_answer_sheet)
        self.btnProfile.clicked.connect(self.open_profile_window)
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

    def validate_test_id(self, test_id):
        if self.test.is_test_checked(test_id):
            self.error_validation("The answer sheet has been already checked!")
        elif not self.test.test_belong_to_current_user(test_id, self.student_id):
            self.error_validation(
                "The answer sheet does not belong to the current user!"
            )
        else:
            self.success_validation()

    def error_validation(self, text):
        msg = self.message_box_creator(text, True)
        msg.exec()

        self.back_to_main_menu()

    def success_validation(self):
        # Disable the capture button after one click
        self.btnCapture.setEnabled(False)

        # Change its appearance
        self.btnCapture.setStyleSheet(
            """
            QPushButton {
                background-color: #DDDDDD;
            }
            """
        )

        msg = self.message_box_creator(
            f"The answer sheet with Test ID of {self.test_id} has been successfully captured!",
            False,
        )

        msg.exec()

        self.setup_answers()

    def setup_answers(self):
        self.answers = self.check_controller.get_answers_from_captured_answer_sheet()

        self.label_items = [
            self.labelItem1,
            self.labelItem2,
            self.labelItem3,
            self.labelItem4,
            self.labelItem5,
            self.labelItem6,
            self.labelItem7,
            self.labelItem8,
            self.labelItem9,
            self.labelItem10,
            self.labelItem11,
            self.labelItem12,
            self.labelItem13,
            self.labelItem14,
            self.labelItem15,
            self.labelItem16,
            self.labelItem17,
            self.labelItem18,
            self.labelItem19,
            self.labelItem20,
        ]

        count = 1
        for label, answer in zip(self.label_items, self.answers):
            label.setText(f"{count}. {answer}")
            count += 1

    def check_answer_sheet(self):
        correct_answers_str = self.test.get_correct_answers_of_test_from_db(
            self.test_id
        )
        self.correct_answers = [
            element.strip()
            for element in correct_answers_str.strip(",").split(",")
            if element.strip()
        ]

        self.show_score()

    def show_score(self):
        score = 0
        count = 1
        for label, (answer, correct_answer) in zip(
            self.label_items, zip(self.answers, self.correct_answers)
        ):
            if answer == correct_answer:
                label.setStyleSheet(
                    "background-color: #04AA6D; color: white; padding-left: 3px"
                )
                score += 1
            else:
                label.setText(f"{count}. {answer} - {correct_answer}")
                label.setStyleSheet(
                    "background-color: #B22222; color: white; padding-left: 3px"
                )
            count += 1

        self.labelResults.setText(f"{score}/20")

        # Update the tests table in the database
        self.test.update_score_of_tests_in_db(score, self.test_id)

        # Disable the capture button after one click
        self.btnCheck.setEnabled(False)

        # Change its appearance
        self.btnCheck.setStyleSheet(
            """
            QPushButton {
                background-color: #DDDDDD;
            }
            """
        )

    def capture_image(self):
        ret, frame = self.video_capture.read()

        if ret:
            current_directory = "C:/Users/caber/OneDrive/Documents/Coding/WattWise/app/"
            output_folder = "print_check"
            image_path = os.path.normpath(
                os.path.join(
                    current_directory, output_folder, "captured_answer_sheet.jpg"
                )
            )

            # cv2.imwrite(image_path, frame)  # Save the captured image
            self.timer.stop()  # Stop the timer (camera feed)

            # Release the video capture
            self.video_capture.release()

        self.test_id = self.check_controller.scan_qrcode()

        if self.test_id is None:
            self.error_validation("No QR Code available in the image captured!")
        else:
            self.validate_test_id(self.test_id)

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

    def open_profile_window(self):
        from app.views.profile_view import ProfileWindow

        self.profile_window = ProfileWindow(
            self.student_name, self.student_id, main_menu_window=self.main_menu_window
        )
        self.profile_window.show()
        self.hide()

    def message_box_creator(self, text, is_error):
        # Prompt the user that the randomization is succesful
        msg = QMessageBox()
        msg.setWindowTitle("Success" if not is_error else "Error")
        msg.setIcon(QMessageBox.Information if not is_error else QMessageBox.Warning)
        msg.setText(text)

        return msg

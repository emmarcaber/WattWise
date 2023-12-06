import cv2
from pyzbar.pyzbar import decode
import os
from app.controllers import tries
import numpy as np


class CheckController:
    def create_paths(self):
        # Get the current working directory
        current_directory = (
            "C:/Users/caber/OneDrive/Documents/Coding/WattWise/app/controllers"
        )
        output_folder = "../print_check"

        # Construct the relative path
        self.captured_answer_sheet_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "captured_answer_sheet.jpg")
        )

    def scan_qrcode(self):
        # Read the image
        image = cv2.imread(self.captured_answer_sheet_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use the pyzbar library to decode the QR code
        decoded_objects = decode(gray)

        # Print information about the QR code
        for obj in decoded_objects:
            if obj.data.decode("utf-8"):
                return obj.data.decode("utf-8")

    def get_answers_from_captured_answer_sheet(self):
        detected_options = []

        def process_option(img, option_contour):
            pt1 = np.float32(option_contour)
            pt2 = np.float32(
                [[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]]
            )
            matrix = cv2.getPerspectiveTransform(pt1, pt2)
            img_warp_colored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

            img_warp_gray = cv2.cvtColor(img_warp_colored, cv2.COLOR_BGR2GRAY)
            img_thresh = cv2.threshold(img_warp_gray, 170, 255, cv2.THRESH_BINARY_INV)[
                1
            ]

            boxes = tries.splitBoxes(img_thresh)

            my_pixels_val = np.zeros((questions, choices))
            count_c = 0
            count_r = 0

            for image in boxes:
                total_pixels = cv2.countNonZero(image)
                my_pixels_val[count_r][count_c] = total_pixels
                count_c += 1
                if count_c == choices:
                    count_r += 1
                    count_c = 0

            for x in range(questions):
                arr = my_pixels_val[x]
                my_index_val = np.where(arr == np.amax(arr))
                option = chr(ord("A") + my_index_val[0][0])
                detected_options.append(option)

            return img_warp_colored, detected_options

        path = self.captured_answer_sheet_path
        widthImg = 500
        heightImg = 650
        questions = 10
        choices = 5

        img = cv2.imread(path)
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        img = cv2.resize(img, (widthImg, heightImg))
        img_contours = img.copy()
        img_biggest_contours = img.copy()

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
        img_canny = cv2.Canny(img_blur, 10, 50)

        contours, hierarchy = cv2.findContours(
            img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 10)

        rect_contours = tries.rectCountour(contours)
        first_contour = tries.getCornerPoints(rect_contours[0])
        second_contour = tries.getCornerPoints(rect_contours[1])

        if first_contour.size != 0 and second_contour.size != 0:
            cv2.drawContours(img_biggest_contours, first_contour, -1, (0, 255, 0), 20)
            cv2.drawContours(img_biggest_contours, second_contour, -1, (255, 0, 0), 20)

            process_option(img, tries.reorder(first_contour))
            process_option(img, tries.reorder(second_contour))

        return detected_options

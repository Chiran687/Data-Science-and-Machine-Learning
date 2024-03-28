import cv2
import math
import numpy as np
import pyautogui
from PIL import Image
import keyboard

# Constants
red = [255, 0, 0]


# # Function to calculate distance
# def calculate_distance(x1, y1, x2, y2):
#     return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# # Function to calculate angle
# def calculate_angle(x1, y1, x2, y2):
#     angle_radians = math.atan2(y2 - y1, x2 - x1)
#     angle_degrees = math.degrees(angle_radians)
#     angle_degrees = (angle_degrees + 360) % 360
#     return angle_degrees


# Function to get HSV limits of a color
def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    lower_limit = (
        hsvC[0][0][0] - 10,
        100,
        100,
    )  # Broadened range for more robust color detection
    upper_limit = hsvC[0][0][0] + 10, 255, 255
    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)
    return lower_limit, upper_limit


# Main processing function
def process_frames_and_click():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        if not ret:
            break

        HSVImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_limit, upper_limit = get_limits(color=red)
        mask = cv2.inRange(HSVImage, lower_limit, upper_limit)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            # Find the largest contour (assumed to be the red object)
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Calculate the center of the red object
            center_x = x + w // 2
            center_y = y + h // 2

            # Simulate a mouse click at the red object's center
            # Ensure the screen size matches or scales to your video frame size
            screen_width, screen_height = pyautogui.size()

            pyautogui.click(
                screen_width * center_x / frame.shape[1],
                screen_height * center_y / frame.shape[0],
            )
            print("pressed")
            # Optionally, draw a rectangle around the detected object
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if keyboard.read_key() == "a":
                break
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    process_frames_and_click()

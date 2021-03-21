import cv2


# trained_data = cv2.CascadeClassifier('data.xml')

wcam = cv2.VideoCapture(0)

while True:
    _ , frame = wcam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(1)

    if key == 113 or key == 81:
        break
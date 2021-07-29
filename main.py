import cv2
import numpy as np

# input
Video_in = "formwork.mp4"

# output
Video_out = "XY.mp4"

# Video Settings
winName = 'output'

# cv2.resizeWindow(winName, 500, 500)
cap = cv2.VideoCapture(Video_in)

# Font to write over the image
font = cv2.FONT_HERSHEY_SIMPLEX

fps = int(cap.get(cv2.CAP_PROP_FPS))
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(3))
height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(Video_out, fourcc, fps, (width, height))

n_frame = 0
frames = []
dim = (500, 500)
dim1 = (720, 1280)
while cap.isOpened():
    # get frame from video
    ret, frame = cap.read()
    print('video_progress: ', round(n_frame * 100 / length_video, 1), '%')

    # Do something

    if ret:
        # Crop the image to proces only the relevant part
        cropped = frame[305:571, 291:662]

        # BGR range for Yellow color
        YELLOW_MIN = np.array([50, 100, 170], np.uint8)
        YELLOW_MAX = np.array([130, 200, 255], np.uint8)

        # using in range to detect relevent pixels and count them
        dst = cv2.inRange(cropped, YELLOW_MIN, YELLOW_MAX)
        yellow_pixels = cv2.countNonZero(dst)

        # Function call to write the value of number of pixels over the image
        # frame = writeOverImage(frame,"Yellow Color",no_brown)
        cv2.putText(frame, 'Yellow Color:' + str(yellow_pixels), (10, 650), font, 2, (0, 255, 100), 2, cv2.LINE_AA)
        out.write(frame)
        cv2.imwrite('ConcreteImages/' + str(n_frame) + '.bmp', frame)
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
        # cv2.resizeWindow(winName, 500, 500)
        # cv2.imshow('output', frame)
        if cv2.waitKey(1) == ord('q'):
            print("going here")
            break
    else:
        break
    n_frame += 1

cap.release()
out.release()
cv2.destroyAllWindows()
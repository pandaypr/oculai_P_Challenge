import cv2
import numpy as np

# input
Video_in = "data/formwork.mp4"

# output
Video_out = "output/formworkOut.mp4"

# Video Settings
winName = 'output'

# cv2.resizeWindow(winName, 500, 500)   #gives error if used here, must be used after creating a window using cv2.namedWindow

cap = cv2.VideoCapture(Video_in)

# Font to write over the image
font = cv2.FONT_HERSHEY_SIMPLEX

# Capture basic video meta data
fps = int(cap.get(cv2.CAP_PROP_FPS))
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(3))
height = int(cap.get(4))

# To write o/p video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(Video_out, fourcc, fps, (width, height))

# Variables
n_frame = 0
frames = []
# dim = (500, 500)
# Input frame shape = (720, 1280)


while cap.isOpened():
    # get frame from video
    ret, frame = cap.read()
    print('video_progress: ', round(n_frame * 100 / length_video, 1), '%')

    # Do something
    # Verifying that the frame is there before applying any techniques, so the code is operational
    # code is kept inside if loop to stop "NoneType' object is not subscriptable"

    if ret:
        # Crop the image to proces only the relevant part
        cropped = frame[310:560, 300:655]

        # BGR range for Yellow color
        YELLOW_MIN = np.array([50, 100, 170], np.uint8)
        YELLOW_MAX = np.array([130, 200, 255], np.uint8)

        # using in range to detect relevent pixels and count them
        dst = cv2.inRange(cropped, YELLOW_MIN, YELLOW_MAX)
        yellow_pixels = cv2.countNonZero(dst)

        # frame = writeOverImage(frame,"Yellow Color",yellow_pixels)    #Function call to write over frames [REMOVED]
        cv2.putText(frame, 'Yellow Colored Pixels:' + str(yellow_pixels), (10, 650), font, 1.5, (0, 255, 100), 2,
                    cv2.LINE_AA)  # write over frames
        out.write(frame)  # Save the video
        # cv2.imwrite('ConcreteImages/'+str(n_frame)+'.bmp', frame)                  #Save individual Images
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)  # Define the window
        # cv2.resizeWindow(winName, 500, 500)   #To resize window if needed
        cv2.imshow('output', frame)  # To display image if needed
        if cv2.waitKey(100) == ord('q'):
            break
    else:
        break
    n_frame += 1

# Releasing video and destroying all windows after use
cap.release()
out.release()
cv2.destroyAllWindows()
""" Show how to work with video-data using OpenCV 

Note that the package OpenCV has to be installed for this program to work.
"""

# Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Set the video file, and open it
video_file = r'..\Data\Pleasure.mp4'
cap = cv2.VideoCapture(video_file)

# Set the parameters
out_base =  r'..\Data\Pleasure_out'
dt = 25 # [msec]
counter = 0

# Show the movie
while(cap.isOpened()):
    ret, frame = cap.read()     # Get the next frame

    if ret == True:
        # Convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the frame for 'dt' msec, or until the user hits 'q'
        cv2.imshow('frame',gray)
        if cv2.waitKey(dt) & 0xFF == ord('q'):
            break

        # Save every 50-th frame
        if not np.remainder(counter, 50):
            out_file = out_base + str(counter) + '.jpg'
            plt.imshow(gray, cmap='gray')
            plt.savefig(out_file)
            plt.close()
            print(f'{out_file} saved')

        counter += 1

    else:
        # Return after the end of the movie
        break

# Clean things up
cap.release()
cv2.destroyAllWindows()

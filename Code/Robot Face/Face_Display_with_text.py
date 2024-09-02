import cv2

video = True

# Set desired width and height for the video frames
frame_width = 1280
frame_height = 720

while (video):
    vid = cv2.VideoCapture('Luna1.mp4')

    if not vid.isOpened():
        print("Error opening video file.")
        break

    # Create a named window
    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)

    # Set the window to fullscreen
    cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while video:
        ute, pic_fr = vid.read()
        if ute:
            # Resize the frame to the desired dimensions
            pic_fr = cv2.resize(pic_fr, (frame_width, frame_height))

            # Add text "Talking" to the frame
            text = 'Talking'
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 2
            color = (0, 255, 0)  # Green text
            thickness = 3
            position = (500, 700)  # (x, y) position for text on the frame

            cv2.putText(pic_fr, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

            # Display the frame
            cv2.imshow('Frame', pic_fr)

            # Check for 'u' key press to break loop
            key = cv2.waitKey(25) & 0xFF
            if key == ord('u'):
                break

            # Check for 'a' key press to stop the video
            if key == ord('a'):
                video = False
                break
        else:
            break

print("End")
vid.release()
cv2.destroyAllWindows()

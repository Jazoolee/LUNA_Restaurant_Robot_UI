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
    
    
    cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    

    while video:
        ute, pic_fr = vid.read()
        if ute:
            # Resize the frame to the desired dimensions
            pic_fr = cv2.resize(pic_fr, (frame_width, frame_height))
            
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

import cv2
# Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Reading from webcam
    ret, back = cap.read() 
    if ret:
        # 'back' is what the camera is reading
        cv2.imshow('image', back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
#import libraries
import cv2

#import classifier for face and eye detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Import Classifier for Face and Eye Detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier ('haarcascade_eye.xml')

def face_detector (img, size=0.5):
# Convert Image to Grayscale
    gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # Given coordinates to detect face and eyes location from ROI
    for (x, y, w, h) in faces:
        x = x - 100
        w = w + 100
        y = y - 100
        h = h + 100
        cv2.rectangle (img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y: y+h, x: x+w]
        roi_color = img[y: y+h, x: x+w]
        eyes = eye_classifier.detectMultiScale (roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            roi_color = cv2.flip (roi_color, 1)
        return roi_color


# Webcam setup for Face Detection
cap = cv2.VideoCapture (0)
while True:
    ret, frame = cap.read ()
    cv2.imshow ('Our Face Extractor', face_detector(frame))
    if cv2.waitKey (1) == 13: #13 is the Enter Key
        break

# When everything done, release the capture
cap.release ()
cv2.destroyAllWindows ()
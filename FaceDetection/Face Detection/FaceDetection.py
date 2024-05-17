import cv2

image = cv2.imread("./img.jpg")
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = classifier.detectMultiScale(image, 1.3, 5)
for face in faces:
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]

    cv2.rectangle(image, (x, y), (x+w, y+h), (139, 75, 123), 2)

while True:
    cv2.imshow("My Image", image)
#   Press q to close the image
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
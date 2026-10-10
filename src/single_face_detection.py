import cv2

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Load the input image
image = cv2.imread("test2.jpg")

# Check if image loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        2
    )

# Display number of detected faces
print("Number of faces detected:", len(faces))

# Display the output
cv2.imshow("AI-Based Face Detection System", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

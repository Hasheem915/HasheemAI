import cv2
import numpy as np


image_path = r'C:\Users\farya\OneDrive\Desktop\AI Codigal\Filters\image3.jpg'  
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found or unable to load.")
    exit()


image = cv2.resize(image, (600, 400))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def apply_sepia(img):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, sepia_filter)
    sepia = np.clip(sepia, 0, 255)
    return sepia.astype(np.uint8)

sepia = apply_sepia(image)


edges = cv2.Canny(gray, threshold1=100, threshold2=200)


cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("Sepia", sepia)
cv2.imshow("Canny Edge Detection", edges)

print("Press any key to close the images.")
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

def nothing(x):
    pass


image_path = r"C:\Users\farya\OneDrive\Desktop\AI Codigal\Fun with filters\ev-22_1.webg"  
original = cv2.imread(image_path)

if original is None:
    print("Error: Image not found.")
    exit()


max_width = 800
if original.shape[1] > max_width:
    scale = max_width / original.shape[1]
    original = cv2.resize(original, None, fx=scale, fy=scale)


cv2.namedWindow("Image Filter")


cv2.createTrackbar("R", "Image Filter", 0, 255, nothing)
cv2.createTrackbar("G", "Image Filter", 0, 255, nothing)
cv2.createTrackbar("B", "Image Filter", 0, 255, nothing)
cv2.createTrackbar("Intensity", "Image Filter", 0, 100, nothing)

while True:
    # Get RGB and intensity from sliders
    r = cv2.getTrackbarPos("R", "Image Filter")
    g = cv2.getTrackbarPos("G", "Image Filter")
    b = cv2.getTrackbarPos("B", "Image Filter")
    intensity = cv2.getTrackbarPos("Intensity", "Image Filter") / 100.0

    
    filter_layer = np.full(original.shape, (b, g, r), dtype=np.uint8)

    
    blended = cv2.addWeighted(original, 1 - intensity, filter_layer, intensity, 0)

    
    cv2.imshow("Image Filter", blended)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite("filtered_image.jpg", blended)
        print("Image saved as 'filtered_image.jpg'.")

cv2.destroyAllWindows()

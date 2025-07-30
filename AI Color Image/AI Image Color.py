import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\farya\OneDrive\Desktop\AI Codigal\AI Color Image\ev-22_1.webp")

image_rbg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rbg)
plt.title("RBG Image")
plt.show()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.show()


cropped_image = image[100:300, 200:400]
cropped_rbg = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rbg)
plt.title("Cropped Region")
plt.show()
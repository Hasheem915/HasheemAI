import cv2


image_path = r'C:\Users\farya\OneDrive\Desktop\AI Codigal\CV project\ev-22_1.webp'  
image = cv2.imread(image_path)


if image is None:
    print("Error: Image not found or cannot be loaded.")
    exit()


sizes = {
    "Small (150x150)": (150, 150),
    "Medium (300x300)": (300, 300),
    "Large (600x600)": (600, 600)
}


for label, size in sizes.items():
    resized = cv2.resize(image, size)
    cv2.imshow(label, resized)


cv2.waitKey(0)
cv2.destroyAllWindows()

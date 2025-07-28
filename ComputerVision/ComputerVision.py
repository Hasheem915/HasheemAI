import cv2
image = cv2.imread(r"C:\Users\farya\OneDrive\Desktop\AI Codigal\ComputerVision\917df29fabeca6b6641fcc58685ccb22.jpg")
cv2.namedWindow("Loaded image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded image", 800, 500)
cv2.imshow("Loaded image", image)
cv2.waitKey(0)
cv2.destoryAIwindows()
print(f"Image Dimension: {image.shape}")


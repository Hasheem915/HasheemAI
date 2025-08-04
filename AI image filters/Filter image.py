import cv2
import numpy as np


image_path = r'C:\Users\farya\OneDrive\Desktop\AI Codigal\AI image filters\images.jpeg' 
img_original = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def nothing(x):
    pass


cv2.namedWindow("Edge Detection")


cv2.createTrackbar("Filter: 0=None 1=Gaussian 2=Median", "Edge Detection", 0, 2, nothing)
cv2.createTrackbar("Kernel Size (odd)", "Edge Detection", 1, 15, nothing)


cv2.createTrackbar("Method: 0=Sobel 1=Canny 2=Laplacian", "Edge Detection", 0, 2, nothing)


cv2.createTrackbar("Canny Thresh1", "Edge Detection", 50, 500, nothing)
cv2.createTrackbar("Canny Thresh2", "Edge Detection", 150, 500, nothing)

while True:
    img = img_original.copy()

    filter_type = cv2.getTrackbarPos("Filter: 0=None 1=Gaussian 2=Median", "Edge Detection")
    ksize = cv2.getTrackbarPos("Kernel Size (odd)", "Edge Detection")
    ksize = max(1, ksize if ksize % 2 == 1 else ksize + 1)

    method = cv2.getTrackbarPos("Method: 0=Sobel 1=Canny 2=Laplacian", "Edge Detection")

    
    if filter_type == 1:
        img = cv2.GaussianBlur(img, (ksize, ksize), 0)
    elif filter_type == 2:
        img = cv2.medianBlur(img, ksize)

    
    if method == 0:  
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=ksize)
        sobel = cv2.magnitude(sobelx, sobely)
        result = cv2.convertScaleAbs(sobel)
    elif method == 1:  
        thresh1 = cv2.getTrackbarPos("Canny Thresh1", "Edge Detection")
        thresh2 = cv2.getTrackbarPos("Canny Thresh2", "Edge Detection")
        result = cv2.Canny(img, thresh1, thresh2)
    elif method == 2:  
        laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=ksize)
        result = cv2.convertScaleAbs(laplacian)

    
    cv2.imshow("Edge Detection", result)

    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Image not found or path is incorrect.")
    return image

def crop_image(image, x, y, width, height):
    return image[y:y+height, x:x+width]

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

def adjust_brightness(image, value=30):
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.clip(v + value, 0, 255).astype(np.uint8)
    final_hsv = cv2.merge((h, s, v))
    bright_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bright_img

def main():
    image_path = r"C:\Users\farya\OneDrive\Desktop\AI Codigal\Manupulation Challenge\bugatti-chiron-pur-sport-tech_026-1280.jpg" 
    image = load_image(image_path)

    
    cropped = crop_image(image, x=100, y=50, width=200, height=200)

    
    rotated = rotate_image(cropped, angle=45)

    
    brightened = adjust_brightness(rotated, value=40)

    
    cv2.imshow("Original", image)
    cv2.imshow("Cropped", cropped)
    cv2.imshow("Rotated", rotated)
    cv2.imshow("Brightened", brightened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

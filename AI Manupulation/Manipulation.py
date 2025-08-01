import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    """Load an image from file."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError("Image not found.")
    print("Image loaded successfully.")
    return img

def rotate_image(img, angle):
    """Rotate image around center by given angle (degrees)."""
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))
    return rotated

def crop_image(img, x, y, width, height):
    """Crop image using top-left (x, y) and size."""
    return img[y:y+height, x:x+width]

def adjust_brightness(img, factor):
    """
    Adjust brightness.
    factor > 1.0: brighter, factor < 1.0: darker
    """
    img = img.astype(np.float32) * factor
    img = np.clip(img, 0, 255)
    return img.astype(np.uint8)

def show_image(img, title="Image"):
    """Display image using Matplotlib (in RGB format)."""
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_image(img, path):
    """Save image to disk."""
    cv2.imwrite(path, img)
    print(f"Saved to {path}")

# ---------- MAIN ----------
if __name__ == "__main__":
    img_path = r"C:\Users\farya\OneDrive\Desktop\AI Codigal\AI Manupulation\ev-22_1.webp"
    img = load_image(img_path)

    rotated = rotate_image(img, 45)
    cropped = crop_image(rotated, 50, 50, 200, 200)
    brightened = adjust_brightness(cropped, 1.5)

    show_image(brightened, "Final Result")
    save_image(brightened, "output.jpg")

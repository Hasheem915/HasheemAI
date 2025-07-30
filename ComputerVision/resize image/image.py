import cv2
import os

# Predefined sizes
sizes = {
    'small': (200, 200),
    'medium': (400, 400),
    'large': (800, 800)
}

def resize_image(image, size):
    return cv2.resize(image, size)

def load_and_prepare(image_path, view_type):
    print(f"Trying to load image: {image_path}")
    if not os.path.isfile(image_path):
        print("File does not exist.")
        return None
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load image. Check file format or path.")
        return None
    if view_type == "gray":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def display_resized_versions(image, label_prefix):
    for size_label, size in sizes.items():
        resized = resize_image(image, size)
        window_name = f"{label_prefix} - {size_label}"
        cv2.imshow(window_name, resized)

def main():
    interior_path = input(r"C:\Users\farya\OneDrive\Desktop\AI Codigal\ComputerVision\resize image\interior.jpeg").strip().strip('"')
    exterior_path = input(r"C:\Users\farya\OneDrive\Desktop\AI Codigal\ComputerVision\resize image\outer.jpg").strip().strip('"')
    view_type = input("Choose image type (colored/gray): ").strip().lower()
    region_choice = input("Which to display? (interior/exterior/both): ").strip().lower()

    if region_choice in ['interior', 'both']:
        interior_image = load_and_prepare(interior_path, view_type)
        if interior_image is not None:
            print("Displaying interior image...")
            display_resized_versions(interior_image, "Interior")
        else:
            print("Skipping interior image due to load failure.")

    if region_choice in ['exterior', 'both']:
        exterior_image = load_and_prepare(exterior_path, view_type)
        if exterior_image is not None:
            print("Displaying exterior image...")
            display_resized_versions(exterior_image, "Exterior")
        else:
            print("Skipping exterior image due to load failure.")

    print("Press any key in image windows to close them.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

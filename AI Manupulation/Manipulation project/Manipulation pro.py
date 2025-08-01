import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_bidirectional_arrow(img, pt1, pt2, color=(0, 255, 0), thickness=2, line_type=cv2.LINE_AA):
    cv2.line(img, pt1, pt2, color, thickness, line_type)

    
    arrow_size = 10
    angle = np.arctan2(pt1[1]-pt2[1], pt1[0]-pt2[0])
    

    p1 = (int(pt2[0] + arrow_size * np.cos(angle + np.pi/6)),
          int(pt2[1] + arrow_size * np.sin(angle + np.pi/6)))
    p2 = (int(pt2[0] + arrow_size * np.cos(angle - np.pi/6)),
          int(pt2[1] + arrow_size * np.sin(angle - np.pi/6)))
    cv2.line(img, pt2, p1, color, thickness, line_type)
    cv2.line(img, pt2, p2, color, thickness, line_type)

    
    p3 = (int(pt1[0] - arrow_size * np.cos(angle + np.pi/6)),
          int(pt1[1] - arrow_size * np.sin(angle + np.pi/6)))
    p4 = (int(pt1[0] - arrow_size * np.cos(angle - np.pi/6)),
          int(pt1[1] - arrow_size * np.sin(angle - np.pi/6)))
    cv2.line(img, pt1, p3, color, thickness, line_type)
    cv2.line(img, pt1, p4, color, thickness, line_type)

def annotate_image_width(image_path, pt_left, pt_right):
    
    img = cv2.imread(image_path)
    img_copy = img.copy()


    draw_bidirectional_arrow(img_copy, pt_left, pt_right)

    
    width_px = int(np.linalg.norm(np.array(pt_right) - np.array(pt_left)))
    mid_point = ((pt_left[0] + pt_right[0]) // 2, (pt_left[1] + pt_right[1]) // 2)
    cv2.putText(img_copy, f'Width: {width_px}px', (mid_point[0]+10, mid_point[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    
    img_rgb = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 6))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("Width Measurement Annotation")
    plt.show()

image_path = r'C:\Users\farya\OneDrive\Desktop\AI Codigal\AI Manupulation\Manipulation project\ev-22_1.webp'
pt_left = (100, 200)  
pt_right = (400, 200)  

annotate_image_width(image_path, pt_left, pt_right)

import cv2
import numpy as np
import math

def count_fingers(contour, drawing):
    hull = cv2.convexHull(contour, returnPoints=False)
    if hull is None or len(hull) < 3:
        return 0
    defects = cv2.convexityDefects(contour, hull)
    if defects is None:
        return 0

    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        
        a = math.dist(start, end)
        b = math.dist(start, far)
        c = math.dist(end, far)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 180 / math.pi

        
        if angle <= 90:
            finger_count += 1
            cv2.circle(drawing, far, 5, [0, 255, 0], -1)
    
    return finger_count + 1  

def main():
    cap = cv2.VideoCapture(0)

    
    lower_color = np.array([100, 150, 0])
    upper_color = np.array([140, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        roi = frame[100:400, 100:400]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        
        mask = cv2.inRange(hsv, lower_color, upper_color)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        mask = cv2.dilate(mask, None, iterations=2)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(max_contour) > 1000:
                drawing = np.zeros(roi.shape, np.uint8)
                cv2.drawContours(drawing, [max_contour], -1, (0, 255, 0), 2)
                fingers = count_fingers(max_contour, drawing)

                
                text = f"Fingers: {fingers}"
                cv2.putText(frame, text, (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                
                
                if fingers == 1:
                    cv2.putText(frame, "Action: Volume Up", (50, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif fingers == 2:
                    cv2.putText(frame, "Action: Volume Down", (50, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif fingers == 5:
                    cv2.putText(frame, "Action: Pause/Play", (50, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                
                frame[100:400, 100:400] = cv2.addWeighted(roi, 0.5, drawing, 0.5, 0)

        
        cv2.rectangle(frame, (100, 100), (400, 400), (255, 0, 0), 2)
        cv2.imshow("Gesture Control", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2

# Try opening the default camera (index 0)

cap = cv2.VideoCapture(0)

if not cap.isOpened():

  print("Error: Could not open camera.")

  exit()

while True:

  ret, frame = cap.read()

  if not ret:

    print("Error: Failed to read frame.")

    break

   # Show the live feed

  cv2.imshow("Webcam Test - Press q to Quit", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

    

  

cap.release()

cv2.destroyAllWindows()
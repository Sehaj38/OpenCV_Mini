import cv2
# open webcam --> 0 or change to a video file path
cap = cv2.Videocapture(0)
# my screen resolution is 1920x1080
screen_width = 1920
screen_height = 1080

target_width = screen_width / 4
target_height = screen_height / 4

print(f"Rescaled to : {target_width} x {target_height}")

while True :
  ret, frame = cap.read()
  if not ret:
    break
  # convert to grayscale  
  gray = cv2.cvtColor(frame,cv2.COLOR_BRG2GRAY)
  # resize to 1/4th screen size
  resized_gray = cv2.resize(gray,(target_width,target_height))
  # show output
  cv2.imshow('1/4th screen Grayscale Video',resized_gray)
  # q to quit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

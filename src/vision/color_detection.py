import cv2
import numpy as np

image = cv2.imread("squares.jpeg")

cv2.imshow('Original Image', image)
white_low = np.array([200, 200, 200])
white_high = np.array([255, 255, 255])
black_low = np.array([0, 0, 0]) 
black_high = np.array([60, 60, 60])

coral_mask = cv2.inRange(image, white_low, white_high)

obstacle_mask = cv2.inRange(image, black_low, black_high)

contours, hierarchy = cv2.findContours(coral_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around contours
coral_center_points = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if cv2.contourArea(contour) > 100:  # optional condition to filter small contours
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cx = int(x + w/2)
        cy = int(y + h/2)
        cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)
        coral_center_points.append((cx, cy))


# Show result
cv2.imshow('boxes', image)

cv2.imshow('cor', coral_mask)
cv2.imshow('obs', obstacle_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()




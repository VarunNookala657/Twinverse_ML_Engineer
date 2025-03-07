import cv2
import mediapipe as mp
import numpy as np

# Initialize Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Start webcam
cap = cv2.VideoCapture(0)

def draw_bar_with_text(frame, x, y, width, height, label, condition):
    color = (0, 255, 0) if condition else (0, 0, 255)  # Green if true, Red if false
    cv2.rectangle(frame, (x, y), (x + width, y + height), color, -1)
    text_color = (255, 255, 255)
    cv2.putText(frame, label, (x + 5, y + int(height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb_frame)

    # Default values for conditions
    facing_camera = False
    hands_relaxed = False

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        # Extract key landmarks
        nose = landmarks[mp_pose.PoseLandmark.NOSE]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]

        # Position Check - Nose should be centered between shoulders
        shoulder_width = abs(left_shoulder.x - right_shoulder.x)
        nose_centered = abs(nose.x - (left_shoulder.x + right_shoulder.x) / 2) < shoulder_width * 0.1
        facing_camera = nose_centered and 0.3 < nose.y < 0.7  # Nose at reasonable vertical level

        # Pose Check - Hands relaxed at sides (wrist should be below hip)
        hands_relaxed = left_wrist.y > left_hip.y

        # Draw landmarks
        mp.solutions.drawing_utils.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Lighting Check - Based on frame brightness
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    lighting_ok = brightness > 100

    # Draw all 3 bars (at top of screen, horizontally side by side)
    bar_width, bar_height = 120, 40
    start_y = 10

    # Lighting Bar
    draw_bar_with_text(frame, 10, start_y, bar_width, bar_height, "Lighting", lighting_ok)

    # Pose Bar
    draw_bar_with_text(frame, 140, start_y, bar_width, bar_height, "Pose", hands_relaxed)

    # Position Bar
    draw_bar_with_text(frame, 270, start_y, bar_width, bar_height, "Position", facing_camera)

    # Show frame
    cv2.imshow('Twinverse Pose Estimation', frame)

    # Press 'q' to quit
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


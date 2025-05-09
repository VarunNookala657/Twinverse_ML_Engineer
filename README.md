# Pose Estimation Assignment - Twinverse Technology ML Engineer Coding Round 01

## Objective
This project implements a Pose Estimation Model using Python and Mediapipe to verify:
- Lighting condition (well-lit room)
- Pose condition (standing straight with hands relaxed at sides)
- Position condition (facing the camera directly)

---

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Programming Language |
| OpenCV | Computer Vision (Webcam Capture & Drawing) |
| Mediapipe | Pose Estimation Model |
| Numpy | Numerical Processing |

---

## How to Run
1. Activate your virtual environment.
2. Run:
    ```bash
    python main.py
    ```
3. Webcam opens. Top of screen shows 3 bars:
    - **Lighting** (Green = Good, Red = Bad)
    - **Pose** (Green = Hands relaxed, Red = Hands raised)
    - **Position** (Green = Facing camera, Red = Not centered)
4. Press `q` to quit.

---

##  Folder Structure

```
pose_estimation/
├── main.py
├── requirements.txt
├── README.md
```



| Condition   | Description                                                |
|-------------|------------------------------------------------------------|
| Lighting    | Turns Green when environment is well-lit                    |
| Pose        | Turns Green when standing upright with hands relaxed        |
| Position    | Turns Green when subject is facing the camera directly      |




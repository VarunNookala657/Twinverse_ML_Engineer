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

pose_estimation/
├── main.py
├── requirements.txt
├── README.md
├── Pose red.png
├── Lightning Green.png
├── All Green.png
├── Lightning Red.png
├── Position Green.png


| Condition   | Description                                                |
|-------------|------------------------------------------------------------|
| Lighting    | Turns Green when environment is well-lit                    |
| Pose        | Turns Green when standing upright with hands relaxed        |
| Position    | Turns Green when subject is facing the camera directly      |

## Sample Output Screenshots

### 1. Lighting Green, Pose Red, Position Red
![Lighting Green, Pose red, Position Red](lightning Green.png)

### 2. Pose Red, Lighting Green, Position Green
![Pose red, Lighting Green, Position Green](Pose red.png)

### 3. All Green (Ideal Condition)
![All Green](All Green.png)

### 4. Lighting Red, Position Green, Pose Green
![Lighting Red, Position Green, Pose Green](Lightning Red.png)

### 5. Position Green, Lighting Red, Pose Red
![Position Green, Lighting Red, Pose red](Position Green.png)


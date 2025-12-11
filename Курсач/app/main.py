import numpy as np
import cv2
import mediapipe as mp

def get_camera_list(max_cameras : int = 5) -> list[int]:
    cameras = []
    for camera_id in range(max_cameras):
        cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)

        if not cap.read()[0]:
            print(f"[DEBUG] Could not access camera #{camera_id}")
            continue
        cap.release()
        cameras.append(camera_id)

    return cameras


if __name__ == '__main__':
    print("Запускаемся...")
    print(get_camera_list())

    # TEST
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open camera")

        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Something went wrong...")
            break
        
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
import cv2
import numpy as np
from pathlib import Path


video_path = '4.2 dog.mp4.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()


output_dir = Path('PythonProject/webcam_output.avi')
output_dir.mkdir(parents=True, exist_ok=True)


file_name = output_dir / "webcam_output.avi"
codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
frame_rate = cap.get(cv2.CAP_PROP_FPS)
resolution = (640, 480)


video_file_output = cv2.VideoWriter(str(file_name), codec, frame_rate, resolution)


frames_dir = output_dir / 'frames'
frames_dir.mkdir(parents=True, exist_ok=True)
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video bitti veya bir hata oluştu.")
        break

    frame = cv2.flip(frame, 1)


    cv2.imshow("Video Playback", frame)


    key = cv2.waitKey(1) & 0xFF


    if key == ord('s'):
        frame_filename = frames_dir / f'frame_{frame_count}.jpg'
        cv2.imwrite(str(frame_filename), frame)
        print(f"Frame {frame_count} kaydedildi!")
        frame_count += 1


    elif key == ord('u'):
        print("Ekran kapatiliyor...")
        break


    video_file_output.write(frame)

cap.release()
video_file_output.release()
cv2.destroyAllWindows()


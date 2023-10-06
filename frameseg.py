import cv2
input_video_path = '/Users/nam/Desktop/동국대학교/산업공학회/sample.mp4'
output_video_path = '/Users/nam/Desktop/동국대학교/산업공학회/111111111.mp4'
target_fps = 1
cap = cv2.VideoCapture(input_video_path)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
original_fps = int(cap.get(5))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter(output_video_path, fourcc, target_fps, (frame_width, frame_height))
frame_interval = int(original_fps / target_fps)
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frame_interval == 0:
        out.write(frame)
    frame_count += 1
cap.release()
out.release()

print(f'동영상을 {target_fps} FPS로 변경하여 {output_video_path}에 저장했습니다.')

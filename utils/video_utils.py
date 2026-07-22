import cv2

def read_video(video_path, max_width=1280):
    """Read video frames, optionally downscaling wide footage for Mac CPU/RAM."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if max_width and frame.shape[1] > max_width:
            scale = max_width / frame.shape[1]
            frame = cv2.resize(frame, (max_width, int(frame.shape[0] * scale)))
        frames.append(frame)
    cap.release()
    return frames, fps

def save_video(output_video_frames, output_video_path, fps=24):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()
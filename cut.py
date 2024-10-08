import os
from moviepy.editor import VideoFileClip

def get_latest_video_file(directory):
    video_files = [f for f in os.listdir(directory) if f.endswith(('.mp4', '.mov', '.avi', '.mkv', '.flv'))]
    if not video_files:
        raise FileNotFoundError("No video files found in the directory")
    latest_file = max(video_files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    return os.path.join(directory, latest_file)

def compress_video(input_path, output_path, target_size_mb, start_time, end_time):
    clip = VideoFileClip(input_path).subclip(start_time, end_time)
    target_size_bytes = target_size_mb * 1024 * 1024
    duration = clip.duration
    target_bitrate = target_size_bytes / duration
    target_bitrate_kbps = target_bitrate * 8 / 1000
    clip.write_videofile(output_path, bitrate=f"{int(target_bitrate_kbps)}k")
    clip.close()

def parse_time(time_str):
    parts = list(map(int, time_str.split(':')))
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    else:
        raise ValueError("Time must be in HH:MM:SS or MM:SS format")

if __name__ == "__main__":
    directory = '.'  # Current directory
    input_path = get_latest_video_file(directory)
    output_path = 'output.mp4'
    target_size_mb = float(input("Enter the target size in MB: "))
    start_time = parse_time(input("Enter the start timestamp (HH:MM:SS or MM:SS): "))
    end_time = parse_time(input("Enter the end timestamp (HH:MM:SS or MM:SS): "))
    if start_time >= end_time:
        raise ValueError("End time must be greater than start time")
    compress_video(input_path, output_path, target_size_mb, start_time, end_time)

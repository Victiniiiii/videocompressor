import os
from moviepy.editor import VideoFileClip

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

def get_latest_video(folder_path):
    video_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.mov', '.avi', '.mkv'))]
    if not video_files:
        raise FileNotFoundError("No video files found in the directory")
    latest_file = max(video_files, key=lambda f: os.path.getctime(os.path.join(folder_path, f)))
    return os.path.join(folder_path, latest_file)

def split_video(input_path, num_parts, target_size_mb):
    clip = VideoFileClip(input_path)
    duration = clip.duration
    part_duration = duration / num_parts
    
    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration if i != num_parts - 1 else duration
        output_path = f"output_part_{i+1}.mp4"
        compress_video(input_path, output_path, target_size_mb, start_time, end_time)
    
    clip.close()

if __name__ == "__main__":
    folder_path = '.'
    input_path = get_latest_video(folder_path)
    target_size_mb = 20.0
    num_parts = int(input("Enter the number of parts to split the video into: "))
    split_video(input_path, num_parts, target_size_mb)

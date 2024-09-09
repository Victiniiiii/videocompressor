from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("video1.mp4")
clip2 = VideoFileClip("video2.mp4")

final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile("merged_video.mp4")

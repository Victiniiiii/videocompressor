from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

video = VideoFileClip("input.mp4")
subtitle_y_position = (video.h / 2 + video.h * 0.9) / 2

subtitle_1 = ImageClip("subtitle1.png").set_duration(5).set_position(("center", subtitle_y_position)).set_start(0)
subtitle_2 = ImageClip("subtitle2.png").set_duration(3).set_position(("center", subtitle_y_position)).set_start(5)
subtitle_3 = ImageClip("subtitle3.png").set_duration(4).set_position(("center", subtitle_y_position)).set_start(8)

result = CompositeVideoClip([video, subtitle_1, subtitle_2, subtitle_3])
result.write_videofile("output_video_with_subtitles.mp4", codec="libx264")

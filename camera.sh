rm image.jpg
rm output.mp4
fswebcam -r 1920x1080 --jpeg 85 -D 1 image.jpg
ffmpeg -t 10 -f v4l2 -framerate 60 -video_size 640x480 -i /dev/video0 output.mp4
# https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/
# http://www.ffmpeg.org/documentation.html

ffmpeg -framerate 1 -i img%05d.jpg -i The_Boys_of_Summer.mp3 -acodec copy video.mp4

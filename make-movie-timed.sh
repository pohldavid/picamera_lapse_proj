# https://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/
# http://www.ffmpeg.org/documentation.html

echo "`date`"
ffmpeg -framerate 1 -i img%05d.jpg video.mp4
echo "`date`"

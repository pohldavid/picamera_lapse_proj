2023-01-01

# Timelapse Project Notes

- begin time lapse on boot 


- automate audio fade

- %05d.xyz provides for > 24hrs duration at lapse 1/sec, fr 1/sec 

- script ffmpeg movie w/ optinal audio


> `ffmpeg -framerate 1 -i img%05d.jpg -i The_Boys_of_Summer.mp3 -acodec copy video.mp4`
> 
> [ffmpeg Documentation](https://ffmpeg.org/ffmpeg.html)

> - timer for video create

> - multiple streams -> ffmpeg?


- option for overlay

> - in picamera script
> - in ffmpeg script


- Make a pySimpleGUI








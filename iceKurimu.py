import os
import yt_dlp
import mpv


fileName = 'iceKurimu.m4a'

if( fileName not in os.listdir()):

    iceCurimu = "https://www.youtube.com/watch?v=OXCQV2q9B4Y"
    ytdlOptions = {'outtmpl': fileName , 'format': '139'}
    with yt_dlp.YoutubeDL(ytdlOptions) as ydl:
        ydl.download(iceCurimu)
        
player = mpv.MPV();
player.play(f'./{fileName}')
player.wait_for_playback()
from pytube import YouTube
from pathlib import Path
import subprocess

FFMPEG_PATH = "ffmpeg" #Si no tienes el path de ffmpg en tu variable de entorno, añadela o escribe aqui el path completo

def download_video(url, path):
    ''' 
    Dado un url o una lista de urls de videos de youtube, descarga el video/s en la ubicacion path
    Input: list o string de urls
    '''
    if isinstance(url, list):
        for video in url:
            yt = YouTube(video)
            yt.streams.filter(progressive=True, file_extension='mp4',).order_by('resolution').desc().first().download(output_path=path) 
    else:       
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4',).order_by('resolution').desc().first().download(output_path=path)




def cortar_video(video_path, tiempo_inicio, tiempo_final, path_video_output):
    '''
    Corta un video dada la ruta del archivo y los tiempos de inicio y final
    Input:
        video_path = Video a cortar
        tiempo_inicio = formato hh:mm:ss
        tiempo_final = formato hh:mm:ss
        path_video_output = path del video de salida

    '''
    command = f"{FFMPEG_PATH} -i {video_path} -ss {tiempo_inicio} -to {tiempo_final} -c:v copy -c:a copy {path_video_output}"
    subprocess.check_output(command, shell=True)


def normalizar_audio(video_input, video_output):
    '''
        Normaliza el audio de un video dada su ruta
        Input:
            video_input = Video a normalizar
            video_output = path del video de salida

    '''
    command = f"{FFMPEG_PATH} -i {video_input} -af loudnorm=I=-23:LRA=8:tp=-2:print_format=json -c:v copy {video_output}"
    subprocess.check_output(command, shell=True)


def extrae_imagenes_video(video, output_path, segundos):
    '''
    Extrae imagenes de un video dada una frecuencia en segundos.
    Input:
        - Video = path al archivo de video
        - output_path
        - segundos = frecuencia en segundos de video en que se extraeran imagenes
    '''
    output_path = str(Path(output_path)).replace("\\", "/") + "/"
    command = f"{FFMPEG_PATH} -i {video} -vf fps={1/segundos} -y {output_path}image_%3d.jpg"
    print(command)
    subprocess.check_output(command, shell=True)
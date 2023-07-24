# picorlib
Esta es una libreria que pretende contener un conjunto de librerias utiles para el podcast de PicorTV
Para muchas de estas utilidades se utilizará las herramientas de video ffmpeg, ffprobe o ffplay. 
Se puede encontrar documentacion de estos comandos [aqui](https://ffmpeg.org/documentation.html)

## Funciones en esta libreria

  - **download_video**(url, path): Dado un url o una lista de urls de videos de youtube, descarga el video/s en la ubicacion path
    Input: list o string de urls
  - **cortar_video**(video_path, tiempo_inicio, tiempo_final, path_video_output): Corta un video dada la ruta del archivo y los tiempos de inicio y final
    Input:
        video_path = Video a cortar
        tiempo_inicio = formato hh:mm:ss
        tiempo_final = formato hh:mm:ss
        path_video_output = path del video de salida
  - **normalizar_audio**(video_input, video_output): Normaliza el audio de un video dada su ruta
        Input:
            video_input = Video a normalizar
            video_output = path del video de salida
  - **extrae_imagenes_video**(video, output_path, segundos): Extrae imagenes de un video dada una frecuencia en segundos.
    Input:
        - Video = path al archivo de video
        - output_path
        - segundos = frecuencia en segundos de video en que se extraeran imagenes

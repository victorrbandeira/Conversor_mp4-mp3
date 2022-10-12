from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Digite o link e o local para salvar o mp3
link = input("Link para conversão: ")
path = input("Digite o nome da pasta que deseja salvar: ")
yt = YouTube(link)

# Começa o download
print("Download...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download finalizado!")

# Converte mp4 para mp3
print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucesso!')

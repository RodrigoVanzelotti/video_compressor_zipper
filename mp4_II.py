import os
import ffmpeg
import time
import numpy as np
import shutil

dirname = 'Compressed'

EXTERNAL_PATH = '/Volumes/EXTERNALSSD/Asimov Academy/Cursos/Python/Raw Videos'
RAW_PATH = EXTERNAL_PATH

RAW_PATH = os.getcwd() + "/"
COMPRESSED_PATH = os.getcwd() + f"/{dirname}/"

if not os.path.isdir(COMPRESSED_PATH): os.mkdir(dirname)

raw_video_files = [i for i in  os.listdir(RAW_PATH) if (".MP4" in i or ".mp4" in i)]
already_compressed = [i for i in  os.listdir(COMPRESSED_PATH) if (".MP4" in i or ".mp4" in i)]
video_list = np.setdiff1d(raw_video_files, already_compressed)
# video_list = [i for i in video_list if i[1] == '.' and len(i) > 3]


def compress_video(video):
    t1 = time.time()
    print("Compressing {}...".format(video))
    stream = ffmpeg.input(RAW_PATH + video)
    stream = ffmpeg.output(stream, COMPRESSED_PATH + video)
    ffmpeg.run(stream)
    print("{} Done. Total time: {}".format(video, time.time() - t1))


for video in video_list:
    compress_video(video)

shutil.make_archive(dirname + '_zipped', 'zip', COMPRESSED_PATH)
    




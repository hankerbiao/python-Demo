import os
from multiprocessing import Pool
import sys
from pydub import AudioSegment
ifile = sys.argv[1]
ofile = sys.argv[2]




def mp3_to_wav(mp3_paths):
    for mp3_path in mp3_paths:
        print(mp3_path)
        try:
            song = AudioSegment.from_mp3(ifile + "/" + mp3_path).set_channels(1).set_frame_rate(16000)
            song.export(ofile+"/" + mp3_path.replace(".mp3", ".wav"), format="wav", bitrate='16k')
        except:
            pass


if __name__ == '__main__':
    mp3_list = os.listdir(ifile)
    bat = []
    tmp = []
    for i in mp3_list:
        tmp.append(i)
        if len(tmp) == 100:
            bat.append(tmp)
            tmp = []
            if len(bat) == 5:
                pool = Pool()
                pool.map(mp3_to_wav, bat)
                pool.close()
                pool.join()
                bat = []
    bat.append(tmp)
    pool = Pool()
    pool.map(mp3_to_wav, bat)
    pool.close()
    pool.join()

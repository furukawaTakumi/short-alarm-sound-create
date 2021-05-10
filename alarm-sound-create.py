import os

from pydub import AudioSegment
import fire

def done(in_file, start_at, end_at, out_file, padding_seconds):
    if not os.path.exists(in_file):
        print('input file is not exists.')
        exit()

    music = AudioSegment.from_file(in_file)
    music = music[start_at * 1000:end_at * 1000]

    padding = AudioSegment.silent(1000 * padding_seconds)
    (music + padding).export(out_file)
    
    print('end.')

if '__main__' == __name__:
    fire.Fire(done)
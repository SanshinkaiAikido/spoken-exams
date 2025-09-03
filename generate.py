#!/usr/bin/env python3
"""Generate spoken Japanese from hiragana with text-to-speech."""

from datetime import datetime
from pathlib import Path
from re import search
import sys
from typing import TextIO

import ffmpeg
from gtts import gTTS

# pylint:disable=unspecified-encoding


TRACKS = {
    'rokkyu': ('1', '2'),
    'gokyu': ('3', '4'),
    'yonkyu': ('5', '6'),
    'sankyu': ('7', '8'),
    'nikyu': ('9', '10'),
    'ikkyu': ('11', '12'),
    'shodan': ('13', '14'),
    'nidan': ('15', '16'),
    'sandan': ('17', '18'),
    'yondan': ('19', '20'),
    'hojonokata': ('1', '2'),
    'tonokata': ('3', '4'),
    'kodachinokata': ('5', '6'),
    'x': ('7', '8'),
    'y': ('9', '10'),
}


def silence(seconds: int) -> None:
    """Generate silent audio file."""
    path = Path(f'tmp/silence_{seconds:02}.mp3')
    if not path.is_file():
        ffmpeg.input(
            'anullsrc=r=24000:cl=mono',
            f='lavfi',
            t=seconds
        ).output(
            str(path),
            acodec='libmp3lame',
            audio_bitrate='64k'
        ).global_args('-v', 'quiet').run()


def write(base: str, text: str) -> None:
    """Generate and write audio file."""
    path = Path(f'{base}_fast.mp3')
    if not path.is_file():
        res = gTTS(text, lang='ja')
        res.save(path)
    path = Path(f'{base}_normal.mp3')
    if not path.is_file():
        res = gTTS(text, lang='ja', slow=True)
        res.save(path)


def playlists(plf: TextIO, pln: TextIO, exam: str, number: int) -> None:
    """Write playlists."""
    plf.write(f"file '../tmp/{exam}_{number:02}_fast.mp3'\n")
    if not exam.endswith('nokata'):
        plf.write("file '../tmp/silence_03.mp3'\n")
        plf.write("file '../tmp/haidouzo_fast.mp3'\n")
        plf.write("file '../tmp/silence_30.mp3'\n")
        plf.write("file '../tmp/matte_fast.mp3'\n")
        plf.write("file '../tmp/silence_02.mp3'\n")

    pln.write(f"file '../tmp/{exam}_{number:02}_normal.mp3'\n")
    if not exam.endswith('nokata'):
        pln.write("file '../tmp/silence_03.mp3'\n")
        pln.write("file '../tmp/haidouzo_normal.mp3'\n")
        pln.write("file '../tmp/silence_75.mp3'\n")
        pln.write("file '../tmp/matte_normal.mp3'\n")
        pln.write("file '../tmp/silence_06.mp3'\n")


def generate(cache: bool = True) -> None:
    """Generate artwork for website and social media."""
    Path('tmp').mkdir(exist_ok=True)
    Path('playlists').mkdir(exist_ok=True)
    Path('mp3').mkdir(exist_ok=True)
    silence(2)
    silence(3)
    silence(6)
    silence(30)
    silence(75)
    write('tmp/haidouzo', 'はい、どうぞ。')
    write('tmp/matte', 'まって。')

    warnings = ('（）', '：。', '、。', '　　', '。。')
    pattern = r'[ ,\.:()a-zA-Z0-9]'
    paths = Path('hiragana').glob('*.txt')
    for path in paths:
        exam = path.stem
        print(path.stem)
        plfn = f'playlists/{exam}_fast'
        plnn = f'playlists/{exam}_normal'
        with open(path) as txt, \
             open(plfn, 'w') as plf, \
             open(plnn, 'w') as pln:
            for number, line in enumerate(txt, start=1):
                line = line[:-1]
                valid = True
                for warning in warnings:
                    if warning in line:
                        print(f'WARNING: Found "{warning}" on line'
                              f' {number:02}: {line}')
                        valid = False
                if search(pattern, line):
                    print(f'WARNING: Found "{pattern}" on line {number:02}:'
                          f' {line}')
                    valid = False
                if valid:
                    p = f'tmp/{exam}_{number:02}'
                    write(p, line)
                    playlists(plf, pln, exam, number)
#         cover_input = ffmpeg.input('cover.png')
#         audio_input = ffmpeg.input(plfn, f='concat', safe=0)
#         print(plfn)
#         ffmpeg.output(
#             audio_input, cover_input,
#             f'mp3/{TRACKS[exam][0]:02}_{exam}_fast.mp3',
#             c='copy',
#             id3v2_version=3,
#             **{
#                 'map': '0:a',
#                 'map:1': '1:v',
#                 'metadata:s:v': 'title=Album cover',
#                 'metadata:s:v:1': 'comment=Cover (front)',
#                 # 'metadata:artist': 'artist=Sanshinkai Aikido',
#                 # 'metadata:s:a': 'album_artist=Sanshinkai Aikido',
#                 # 'metadata:s:a': 'album=Shiken',
#                 # 'metadata:date': f'{datetime.now().year}',
#                 # 'metadata:genre': 'Spoken',
#                 # 'metadata:track': TRACKS[exam][0],
#             }
#             # extra_args=[
#             #     '-map', '0:a',
#             #     '-map', '1:v',
#             #     '-metadata:s:v', 'title=Album cover',
#             #     '-metadata:s:v', 'comment=Cover (front)',
#             #     '-metadata', f'title={TRACKS[exam][0]} {exam}',
#             #     '-metadata', 'artist=Sanshinkai Aikido',
#             #     '-metadata', 'album_artist=Sanshinkai Aikido',
#             #     '-metadata', 'album=Shiken',
#             #     '-metadata', f'date={datetime.now().year}',
#             #     '-metadata', 'genre=Spoken',
#             #     '-metadata', 'TRACK_TOTAL=20',
#             #     '-metadata', f'track={TRACKS[exam][0]}',
#             #     ],
#         ).overwrite_output().run()
# #        .global_args('-v', 'quiet')\
#         exit(0)
#         audio_input = ffmpeg.input(plnn, f='concat', safe=0)
#         ffmpeg.output(
#             audio_input, cover_input,
#             f'mp3/{TRACKS[exam][1]:02}_{exam}_normal.mp3',
#             c='copy',
#             id3v2_version=3,
#             metadata=f'title={TRACKS[exam][1]} {exam}',
#             **{
#                 'map': '0:a',
#                 'map:1': '1:v',
#                 'metadata:s:v': 'title=Album cover',
#                 'metadata:s:v:1': 'comment=Cover (front)',
#                 'metadata:artist': 'Sanshinkai Aikido',
#                 'metadata:album_artist': 'Sanshinkai Aikido',
#                 'metadata:date': f'{datetime.now().year}',
#                 'metadata:genre': 'Spoken',
#                 'metadata:album': 'Shiken',
#                 'metadata:TRACK_TOTAL': 'TRACK_TOTAL=20',
#                 'metadata:track': TRACKS[exam][1],
#             }
#         ).overwrite_output().run()
#         # .global_args('-v', 'quiet')
#         exit(0)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'nocache':
        generate(False)
    generate()

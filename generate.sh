#!/usr/bin/env sh
set -e

mkdir -p tmp playlists mp3

FILE=tmp/silence_002.mp3
if [ ! -e $FILE ]; then
    ffmpeg -v quiet -f lavfi -i anullsrc=r=24000:cl=mono -t 2 -c:a libmp3lame -b:a 64k $FILE
fi
FILE=tmp/silence_003.mp3
if [ ! -e $FILE ]; then
    ffmpeg -v quiet -f lavfi -i anullsrc=r=24000:cl=mono -t 3 -c:a libmp3lame -b:a 64k $FILE
fi
FILE=tmp/silence_006.mp3
if [ ! -e $FILE ]; then
    ffmpeg -v quiet -f lavfi -i anullsrc=r=24000:cl=mono -t 6 -c:a libmp3lame -b:a 64k $FILE
fi
FILE=tmp/silence_030.mp3
if [ ! -e $FILE ]; then
    ffmpeg -v quiet -f lavfi -i anullsrc=r=24000:cl=mono -t 30 -c:a libmp3lame -b:a 64k $FILE
fi
FILE=tmp/silence_075.mp3
if [ ! -e $FILE ]; then
    ffmpeg -v quiet -f lavfi -i anullsrc=r=24000:cl=mono -t 75 -c:a libmp3lame -b:a 64k $FILE
fi

FILE=tmp/haidouzo_fast.aac
if [ ! -e $FILE ]; then
    gtts-cli -l ja -o $FILE はい、どうぞ。
fi
FILE=tmp/haidouzo_normal.aac
if [ ! -e $FILE ]; then
    gtts-cli -s -l ja -o $FILE はい、どうぞ。
fi
FILE=tmp/matte_fast.aac
if [ ! -e $FILE ]; then
    gtts-cli -l ja -o $FILE まって。
fi
FILE=tmp/matte_normal.aac
if [ ! -e $FILE ]; then
    gtts-cli -s -l ja -o $FILE まって。
fi

for exam in $(ls hiragana/*); do
    EXAM=$(basename $exam .txt)
    case $EXAM in
      rokkyu)
        TRACKn=01
        TRACKs=02
        ;;
      gokyu)
        TRACKn=03
        TRACKs=04
        ;;
      4kyu)
        TRACKn=05
        TRACKs=06
        ;;
      sankyu)
        TRACKn=07
        TRACKs=08
        ;;
      2kyu)
        TRACKn=09
        TRACKs=10
        ;;
      1kyu)
        TRACKn=11
        TRACKs=12
        ;;
      shodan)
        TRACKn=13
        TRACKs=14
        ;;
      nidan)
        TRACKn=15
        TRACKs=16
        ;;
      sandan)
        TRACKn=17
        TRACKs=18
        ;;
      yondan)
        TRACKn=19
        TRACKs=20
        ;;
    esac
    CNT=0
    for i in $(cat $exam); do
        CNT=$((CNT+1))
        BASE=$EXAM\_$(printf "%02d" $CNT)
        echo $BASE $i
        # fast speed
        FILE=tmp/$BASE\_fast.aac
        if [ $exam -nt $FILE ]; then
            gtts-cli -l ja -o $FILE $i
        fi
        # normal speed
        FILE=tmp/$BASE\_normal.aac
        if [ $exam -nt $FILE ]; then
            gtts-cli -s -l ja -o $FILE $i
        fi
    done
    # fast speed
    PLAYLIST=playlists/$EXAM\_fast
    rm -f $PLAYLIST
    for i in tmp/$EXAM\_??_fast.aac; do
        echo "file '../"$i"'" >> $PLAYLIST
        echo "file '../tmp/silence_003.mp3'" >> $PLAYLIST
        echo "file '../tmp/haidouzo_fast.aac'" >> $PLAYLIST
        echo "file '../tmp/silence_030.mp3'" >> $PLAYLIST
        echo "file '../tmp/matte_fast.aac'" >> $PLAYLIST
        echo "file '../tmp/silence_002.mp3'" >> $PLAYLIST
    done
    MP3=mp3/$EXAM\_fast.mp3
    if [ $PLAYLIST -nt $MP3 ]; then
        ffmpeg -v quiet -f concat -safe 0 -i $PLAYLIST -i cover.png -map 0:a -map 1:v -c:a copy -c:v copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" -metadata title=$TRACKn" "$EXAM -metadata album="Shiken" -metadata artist="Sanshinkai Aikido" -metadata album_artist="Sanshinkai Aikido" -metadata date=$(date +%Y) -metadata TRACK_TOTAL=20 -metadata genre="Spoken" -metadata track=$TRACKn $MP3 -y
    fi
    # normal speed
    PLAYLIST=playlists/$EXAM\_normal
    rm -f $PLAYLIST
    for i in tmp/$EXAM\_??_normal.aac; do
        echo "file '../"$i"'" >> $PLAYLIST
        echo "file '../tmp/silence_003.mp3'" >> $PLAYLIST
        echo "file '../tmp/haidouzo_normal.aac'" >> $PLAYLIST
        echo "file '../tmp/silence_075.mp3'" >> $PLAYLIST
        echo "file '../tmp/matte_normal.aac'" >> $PLAYLIST
        echo "file '../tmp/silence_006.mp3'" >> $PLAYLIST
    done
    MP3=mp3/$EXAM\_normal.mp3
    if [ $PLAYLIST -nt $MP3 ]; then
        ffmpeg -v quiet -f concat -safe 0 -i $PLAYLIST -i cover.png -map 0:a -map 1:v -c:a copy -c:v copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" -metadata title=$TRACKs" "$EXAM -metadata album="Shiken" -metadata artist="Sanshinkai Aikido" -metadata album_artist="Sanshinkai Aikido" -metadata date=$(date +%Y) -metadata TRACK_TOTAL=20 -metadata genre="Spoken" -metadata track=$TRACKs $MP3 -y
    fi
done

# Spoken exams

Spoken exams in MP3 format to practice by yourself. All the exam requirements are read in the same way an examinator would during an exam in Sanshinkai Aikido.

This repository generates with text-to-speech what an examinator would say when you are doing an exam in Sanshinkai Aikido. Each exam is written out in hiragana. With the use of [gTTS](https://pypi.org/project/gTTS/) and [FFmpeg](https://ffmpeg.org/) MP3 files are generated.

The average use will use these files from links elsewhere. The links currently available are:

| Grade    | Romaji | Fast | Normal |
|----------|--------|------|--------|
| 4th dan  | yondan |
| 3rd dan  | sandan | 
| 2nd dan  | niddan |
| 1st dan  | shodan |
| 1st kyu  | ikkyu  |
| 2nd kyu  | nikyu  |
| 3rd kyu  | sankyu |
| 4th kyu  | yonkyu |
| 5th kyu  | gokyu  |
| 6th kyu  | rokkyu |
| 7th kyu  | 
| 8th kyu  | 
| 9th kyu  | yukyu
| 10th kyu | jyukyu
| 11th kyu | jyuichikyu
| 12th kyu | jyunikyu

# Requirements

Install

    sudo apt-get -y install ffmpeg
    pip install gtts

# Usage

Edit the TXT scripts with a text editor. Use only hiragana and CJK punctation in those files. Generate the MP3 files with `./generate.sh`.

# Development

Install

    sudo apt-get -y install devscripts

and run `./linst.sh` to lint the shell scripts.

# Searching

For searching in hiragana, the following is practical:

| Type      | Romaji                | Hiragana |
|-----------|-----------------------|---|
| position  | suwariwaza            |  |
| position  | tachiwaza             | たちわざ |
| attack    | katatedori aihanmi    | かたてどり　あいはんみ |
| attack    | katatedori gyakuhanmi | かたてどり　ぎゃくはんみ |
| attack    | shomenuchi            | しょうめんうち |
| attack    | ryotedori             | りょうてどり |
| attack    | katate ryotedori      | かたてりょうてどり |
| attack    | ushiro ryotedori      | うしろ　りょうてどり |
| attack    | katadori menuchi      | かたどり　めんうち |
| attack    | chudantsuki           | ちゅうだんつき |
| attack    | yokomenuchi           | よこめんうち |
| technique | ikkyo                 | いっきょう |
| technique | nikyo                 | にきょう |
| technique | sankyo                | さんきょう |
| technique | yonkyo                | よんきょう |
| technique | kotegaeshi |  |
| technique | iriminage |  |
| technique | shihonage |  |
| technique | koshinage |  |
| technique | jiyuwaza | じゆうわざ |
| direction | omote          | おもて |
| direction | ura            | うら |
| movement  | tenkan         | てんかん |
| movement  | tenshin        | てんしん |
| movement  | irimi tenkan   | いりみ　てんかん |
| movement  | irimi          | いりみ |
| movement  | tenkan tenshin | てんかん　てんしん |
| movement  | sabaki |  |
| side      | uchinote |  |
| side      | katanote |  |


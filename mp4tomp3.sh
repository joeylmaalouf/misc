#!/bin/sh
vlc="/usr/bin/vlc"

if [ ! -e "$vlc" ]; then
    echo "Command '$vlc' does not exist"
    exit 1
fi

for file in "$@"; do
    echo "=> Transcoding '$file'... "

    dst=`dirname "$file"`
    new=`basename "$file" | sed 's/mp4/mp3/'`

    $vlc -I dummy -q "$file" \
       --sout "#transcode{vcodec=dummy,acodec=mp3}:standard{access=file,mux=raw,dst=\"$dst/$new\"}" \
       vlc://quit
done

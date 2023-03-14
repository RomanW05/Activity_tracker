#!/bin/bash

while true
do
    file_name=$(date +%F)
    SCRIPT_DIR="$(dirname "$0")"
    FILE="$SCRIPT_DIR/logs/$file_name.log"

    nows_time=$(date "+%F %T")
    active_windows=$(xdotool getwindowfocus getwindowname)
    command_to_show="$nows_time | $active_windows"

    if [ ! -f "$FILE" ]; then
        cat > $FILE
        echo "file ${dir_name} created"
    fi

    echo "$command_to_show" >> $FILE
    sleep 1

done

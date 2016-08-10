#!/bin/bash

if [ $(condor_q $1 | wc -l) = 7 ]; then
    echo "Waiting for job $1 to finish."
    while [ true ]; do
        if [ $(condor_q $1 | wc -l) = 6 ]; then
            if [ ! -z $2 ]; then
                mail -s "$2" "kroffo@oswego.edu" <<EOF
Your job with ID $1 has completed.
EOF
            else
                mail -s "$1 Finished" "kroffo@oswego.edu" <<EOF
Your job with ID $1 has completed.
EOF
            fi
            break
        fi
        sleep 10
    done
else
    echo "Job $1 does not exist."
fi

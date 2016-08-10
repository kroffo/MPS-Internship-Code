#!/bin/bash

cp -R $MESA_DIR/star/work track
(cd track; ./mk)

cd mass

for i in $(ls); do
    echo "Analyzing $i..."
    cd $i
    if [ -d "bumpTrack" ]; then
        rm -rf bumpTrack
    fi
    cd LOGS/Analysis
    if [ -d "gyre" ]; then
        rm -rf gyre
    fi
    mkdir gyre
    cp ../../../../grabRelevantProfiles.py .
    NUMPROFILES=$(ls -l ../profile*.data | wc -l)
    cp -r ../../../../track bumpTrack
    python grabRelevantProfiles.py $NUMPROFILES
    cd bumpTrack
    echo "    Setting up track..."
    MAXAGE=$(cat maxAge.dat)
    cp ../../../../../inlist_project_model_start ./inlist_project
    sed -i.bak "s/max_age = /max_age = $MAXAGE/g" inlist_project
    cd ..
    mv bumpTrack ../..
    cd ../../
    if [ $1 == "true" ]; then
        cd bumpTrack
        cp ../../../maybe_sub.sh .
        cp ../../../profile_columns.list
        ./maybe_sub.sh ./rn
        cd ..
    fi
    cd ..
    echo "    Finished."
done

cd ..
rm -rf track


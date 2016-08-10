#!/bin/bash

#! Originally written by Earl Bellinger. Modified by Kenny Roffo.

if [ -d "mass" ]; then
    rm -rf mass
fi

cp -R $MESA_DIR/star/work .
(cd work; ./mk)
mkdir mass
for i in $(seq 0.7 0.1 2.2); do 
    cp -R work mass/$i
    cp inlist_project mass/$i/inlist_project
    cp maybe_sub.sh mass/$i/maybe_sub.sh
    cd mass/$i
    sed -i.bak "s/initial_mass = 1/initial_mass = $i/g" inlist_project
    ./maybe_sub.sh ./rn
    cd -
done
rm -rf work


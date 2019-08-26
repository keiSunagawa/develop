#!/bin/bash

for scriptpath in $(ls ./*.sh); do
    echo ${scriptpath}
    scriptname=$(basename ${scriptpath})
    thisfilename=$(basename ${0})
    if [ ${scriptname} != ${thisfilename} ] ; then
        commandname=$(echo ${scriptname} | sed "s/.sh//")
        cp ./${scriptname} /usr/local/bin/${commandname}
    fi
done

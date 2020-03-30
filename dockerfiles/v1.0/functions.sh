#!/bin/bash
# MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>
# Description: Common Function File
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#

source /opt/cra/scripts/env_file.sh

DATE=$(date +%Y%m%d-%H%M%S)
LOGFILE="cra_${DATE}.log"
export logfile=/tmp/${LOGFILE}
touch $logfile
export logdir=/tmp
export STD_OUT_FILE="/proc/1/fd/1"
export STD_ERR_FILE="/proc/1/fd/2"
export TOP_PID=$$

###### Function Related to printing messages and exit the script if error occurred ##################
error_exit() {
local NOW=$(date +"%m-%d-%Y %T %Z")
        # Display error message and exit
#       echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
        echo "${NOW} : ${PROGNAME}: ${1:-"Unknown Error"}" | tee -a $logfile > $STD_OUT_FILE 
        kill -s TERM $TOP_PID
}

print_message ()
{
        local NOW=$(date +"%m-%d-%Y %T %Z")
        # Display  message and return
        echo "${NOW} : ${PROGNAME} : ${1:-"Unknown Message"}" | tee -a $logfile > $STD_OUT_FILE
        return $?
}

#####################################################################################################

#!/bin/bash
# MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>
# Description: Common Function File
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#

source /opt/cra/scripts/env_file.sh
source "$SCRIPT_DIR/functions.sh"

######  FIREWALL BLOCKS ENDS HERE ############

######  FIREWALL BLOCKS ENDS HERE ############

######  PYTHON VERSION CHANGE ############
alias python='/usr/bin/python3'
######  PYTHON VERSION CHANGE END ############

######## CLONE PROJECT BLOCK BEGIN HERE #############
print_message "Project clone"
cd /opt
git clone https://github.com/psaini2018/Cloud-Resource-Analyzer

######## CLONE PROJECT BLOCK BEGIN HERE #############
print_message "Create Python Virtual env"
cd /opt/Cloud-Resource-Analyzer/
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

print_message "Create Python Virtual env Completed"

print_message "Starting the application"
python ./src/application.py &
######## CLONE PROJECT BLOCK BEGIN HERE #############

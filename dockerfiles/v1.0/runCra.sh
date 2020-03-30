#!/bin/bash
# MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>
# 
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
# 

source /opt/cra/scripts/env_file.sh
source "$SCRIPT_DIR/functions.sh"

print_message "Running runCra.sh for APP"
$SCRIPT_DIR/$USER_SCRIPTS_FILE  $APP_SCRIPTS_ROOT $SCRIPTS_TYPE

print_message "Running runCra.sh for ML"
$SCRIPT_DIR/$USER_SCRIPTS_FILE  $ML_SCRIPTS_ROOT $SCRIPTS_TYPE


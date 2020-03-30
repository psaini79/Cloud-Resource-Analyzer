#!/bin/bash
# MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
# 

source /opt/cra/scripts/env_file.sh

source "$SCRIPT_DIR/functions.sh"

SCRIPTS_ROOT="$1";
SCRIPTS_TYPE="$2";

if [ -z "$SCRIPTS_ROOT" ]; then
   print_message "$0: No SCRIPTS_ROOT passed on, no scripts will be run";
else

if [ "${SCRIPTS_TYPE}" == "APP" ] && [ -d "$SCRIPTS_ROOT" ] && [ -n "$(ls -A $SCRIPTS_ROOT)" ]; then

  print_message "";
  print_message "Executing user defined scripts for ${SCRIPTS_TYPE}"

  for f in $SCRIPTS_ROOT/*; do
      case "$f" in
          *.sh)     print_message "$0: running $f"; . "$f" ;;
          *)        print_message "$0: ignoring $f" ;;
      esac
      print_message "";
  done
  
  print_message "DONE: Executing user defined scripts for ${SCRIPTS_TYPE}"
  print_message "";

fi;

fi;
 
if [ -z "$SCRIPTS_ROOT" ]; then
   print_message "$0: No SCRIPTS_ROOT passed on, no scripts will be run";

else

if [ "${ML_SCRIPTS_TYPE}" == "ML" ] && [ -d "$SCRIPTS_ROOT" ] && [ -n "$(ls -A $SCRIPTS_ROOT)" ]; then

  print_message "";
  print_message "Executing user defined scripts for ${SCRIPTS_TYPE}"

  for f in $SCRIPTS_ROOT/*; do
      case "$f" in
          *.sh)     print_message "$0: running $f"; . "$f" ;;
          *)        print_message "$0: ignoring $f" ;;
      esac
      print_message "";
  done

  print_message "DONE: Executing user defined scripts for ${SCRIPTS_TYPE}"
  print_message "";

fi;

fi;

#!/bin/bash
# MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>
# Description: Common Function File
#
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#

source /opt/cra/scripts/env_file.sh
source "$SCRIPT_DIR/functions.sh"




######## FIREWALL BLOCK BEGIN HERE #############


systemctl stop firewalld

systemctl disable firewalld


######  FIREWALL BLOCKS ENDS HERE ############






###### NGINX SERVER BLOCK BENGINS HERE  ###################
print_message "Installing Nginx"

touch /etc/yum.repos.d/nginx.repo

echo "[nginx]" > /etc/yum.repos.d/nginx.repo
echo "name=nginx repo"  >> /etc/yum.repos.d/nginx.repo
echo "baseurl=http://nginx.org/packages/rhel/7/\$basearch/" >> /etc/yum.repos.d/nginx.repo
echo "gpgcheck=0" >> /etc/yum.repos.d/nginx.repo
echo "enabled=1" >> /etc/yum.repos.d/nginx.repo

print_message "Doing yum install for nginx"
yum -y install nginx | tee -a $logfile
print_message "Checking nginx status"
systemctl status nginx | tee -a $logfile
print_message "Starting nginx server"
systemctl start nginx.service | tee -a $logfile
print_message "Checking nginx Status"
systemctl status nginx | tee -a $logfile

######### NGINX SERVER BLOCK ENDS HERE ###########

######## GARAFNA BLOCK BEGIN HERE #############

print_message "Setting up Grafana"

mv grafana-6.6.2-1.x86_64.rpm /opt/cra/software/ 

######  GRAFANA BLOCKS ENDS HERE ############




######## PROMETHEUS BLOCK BEGIN HERE #############

print_message "Setting up Prometheus"
print_message "Untar Prometheus"
tar -xvf /opt/cra/software/prometheus-2.11.2.linux-amd64.tar.gz

 

######  PROMETHEUS BLOCKS ENDS HERE ############

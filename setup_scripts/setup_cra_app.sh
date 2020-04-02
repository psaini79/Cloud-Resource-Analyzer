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

print_message "Copy config file"
cp /Cloud-Resource-Analyzer/configs/nginx.conf /etc/nginx/ 

print_message "Starting nginx server"
systemctl start nginx.service | tee -a $logfile
print_message "Checking nginx Status"
systemctl status nginx | tee -a $logfile

######### NGINX SERVER BLOCK ENDS HERE ###########




######## GARAFNA BLOCK BEGIN HERE #############

print_message "Setting up Grafana"
mv grafana-6.6.2-1.x86_64.rpm /opt/cra/software/ 

print_message "Install Grafana"
yum install /opt/cra/software/grafana-6.6.2-1.x86_64.rpm

print_message "Open port"
echo "http_port = 3000" >> /etc/grafana/grafana.ini

print_message "Allow Embedding"
echo "allow_embedding = true" >> /etc/grafana/grafana.ini

print_message "Reload systemd"
systemctl daemon-reload

print_message "Start Grafana"
systemctl start grafana-server

print_message "Enable Grafana Server"
systemctl enable grafana-server





######  GRAFANA BLOCKS ENDS HERE ############




######## PROMETHEUS BLOCK BEGIN HERE #############

print_message "Setting up Prometheus"
print_message "Untar Prometheus"
tar -xvf /opt/cra/software/prometheus-2.11.2.linux-amd64.tar.gz -C /opt/cra/software/

print_message "Start Prometheus"
/opt/cra/software/prometheus-2.11.2.linux-amd64/./prometheus --config.file=/opt/cra/software/prometheus-2.11.2.linux-amd64/prometheus.yml
 

######  PROMETHEUS BLOCKS ENDS HERE ############




######## NODE INSTALLATION BLOCK BEGIN HERE #############

print_message "Node installation"
curl -sL https://rpm.nodesource.com/setup_10.x | bash -

yum install -y nodejs

 

######  NODE INSTALLATION BLOCKS ENDS HERE ############



######## CLONE PROJECT BLOCK BEGIN HERE #############

print_message "Project clone"
git clone https://github.com/psaini2018/Cloud-Resource-Analyzer

print_message "Install node modules"
cd /Cloud-Resource-Analyzer/application/frontend
npm install

npm install @material-ui/core
npm install @material-ui/icons
npm install material-ui-dialogs


print_message "Build React app"
npm run build


rm -rf /usr/share/nginx/html/*

print_message "Move build files to nginx"
cp -R build/* /usr/share/nginx/html

print_message "Move config files to nginx"



print_message "Move to root directory"
cd / 

######  CLONE PROJECT BLOCK ENDS HERE ############






######## MAVEN INSTALLATION BLOCK BEGIN HERE #############

print_message "Maven installation"
cd /opt/cra/software/

print_message "Download maven"
wget https://downloads.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz

print_message "Untar maven"
tar -xvf apache-maven-3.6.3-bin.tar.gz


#vi ~/.bashrc

#echo "export PATH=/opt/cra/software/apache-maven-3.6.3/bin:$PATH" >> ~/.bashrc

#source ~/.bashrc 
 

######  MAVEN INSTALLATION BLOCKS ENDS HERE ############




######## SPRINGBOOT APPLICATION BLOCK BEGIN HERE #############

print_message "Start application"
cd /Cloud-Resource-Analyzer/application/backend/target
java -jar backend-0.0.1-SNAPSHOT.jar


print_message "Move to root directory"
cd / 

######  SPRINGBOOT APPLICATION BLOCKS ENDS HERE ############



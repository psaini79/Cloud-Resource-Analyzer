# CRA  DOCKERFILES PROJECT
# --------------------------
# This is the Dockerfile for Cloud Resource Analyzer
# 
# REQUIRED FILES TO BUILD THIS IMAGE
# ----------------------------------
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run: 
#      $ docker build -t cra/app-ml:latest . 
#
# Pull base image
# ---------------
FROM oraclelinux:7-slim

# Maintainer
# ----------
MAINTAINER Paramdeep Saini <paramdeep.saini@sjsu.edu> Rajalakshmi Babu <rajalakshmi.babu@sjsu.edu> Julian Simon <julian.soosaimanickamsimon@sjsu.edu> Viswa <viswanathsingh.kambam@sjsu.edu>

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
# Linux Env Variable
ENV PATH=/bin:/usr/bin:/sbin:/usr/sbin:$PATH \
    SCRIPT_DIR=/opt/cra/scripts \
    USER_SCRIPTS_FILE="runUserScripts.sh" \
    FUNCTIONS="functions.sh" \ 
    ENVFILE="env_file.sh" \
    RUN_FILE="runCra.sh"

   
COPY $RUN_FILE $FUNCTIONS $USER_SCRIPTS_FILE $ENVFILE $SCRIPT_DIR/

RUN yum-config-manager --enable ol7_developer_EPEL && \
yum -y groupinstall "Server with GUI" && \
yum -y install systemd net-tools which nginx wget zip unzip tar openssl expect e2fsprogs openssh-server openssh-client vim-minimal passwd which sudo install python36 python36-devel  python-pip git tigervnc-server xorg-x11-fonts-Type1 @development  && \
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
yum -y install ./google-chrome-stable_current_*.rpm && \
easy_install-3.6 pip && \
pip3 install --upgrade pip && \
pip3 install Flask && \
pip3 install flask_restful && \
pip3 install request && \
pip3 install flask_jwt && \
pip3 install jupyter && \
pip3 install numpy  && \
pip3 install pandas &&  \
pip3 install matplotlib && \
pip3 install seaborn && \
pip3 install statsmodels && \
pip3 install scikit-learn && \
pip3 install tqdm && \
yum clean all && \
useradd -ms /bin/bash appuser && \ 
mkdir -p /opt/cra/software && \
wget https://github.com/prometheus/prometheus/releases/download/v2.11.2/prometheus-2.11.2.linux-amd64.tar.gz && \
mv prometheus-2.11.2.linux-amd64.tar.gz /opt/cra/software && \
wget https://dl.grafana.com/oss/release/grafana-6.6.2-1.x86_64.rpm && \
yum -y --disablerepo=* localinstall grafana-6.6.2-1.x86_64.rpm && \
chmod 755 $SCRIPT_DIR/*.sh && \ 
echo "nohup $SCRIPT_DIR/runCra.sh &" >> /etc/rc.local && \
chmod +x /etc/rc.d/rc.local  && \
sync

USER root
WORKDIR /root 

VOLUME ["/opt/cra/scripts"]

CMD ["/usr/sbin/init"]

#!/usr/bin/python

import os
import sys
import re
import subprocess

fname='/opt/cra/software/prometheus-2.11.2.linux-amd64/prometheus.yml'
pm_template='/scripts_app/prometheus_template.yml'
port="9100"

def restart_pm():
  """
   This function restart the premoethous
  """

  ## Killing Promethous 
  try:
    cmd='''kill  -9 `ps -ef | grep prometheus.yml | grep -v "grep --color=auto prometheus.yml" | awk '{ print $2 }'`'''
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output,error),retcode = out.communicate(),out.returncode
  except:
    error_msg=sys.exc_info()

  ## Starting promethous server
  try:
    cmd='''kill  -9 `ps -ef | grep prometheus.yml | grep -v "grep --color=auto prometheus.yml" | awk '{ print $2 }'`'''
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output,error),retcode = out.communicate(),out.returncode
  except:
    error_msg=sys.exc_info()
   
 
def main(argv):

    n = len(argv) 
    print("Total arguments passed:", n)

    if n > 1:
       ec2_inst = argv[1]
    else:
       ec2_inst= None

    if not ec2_inst:
       sys.exit(127)

    f1 = open(fname, 'r')
    fdata = f1.read()
    f1.close()      
    matched_output=re.findall("(?:static_configs:\n)(?:.+\n)+",fdata) 
    print(matched_output[1])
    if (matched_output[0]):
       contents_re = re.search(r'\[(.*?)\]',matched_output[1]).group(1)
       new_ec2=''' ,\'{0}:9100\''''.format(ec2_inst)       
       contents_re += new_ec2
       print(contents_re)
       f1 = open(pm_template, 'r')
       fdata_template = f1.read()
       f1.close() 
       fdata=fdata_template.replace("###EC2_STRING###",contents_re)
       ### Write to original file
       f1 = open(fname, 'w')
       print(fdata)
       f1.write(fdata)
       f1.close()

    restart_pm()        
       
if __name__ == '__main__':
   main(sys.argv)

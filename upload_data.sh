#!/bin/bash
# Upload data to ENA with webin-cli.
# Expects Webin user and password in env variables WEBINUSER and WEBINPASSWORD.
# Fredrik Boulund 2022
set -eou pipefail

for manifest in *manifest.txt; do
  sample_name=$(awk '/NAME/{print $2}' ${manifest})
  if [ ! -d "reads/${sample_name}" ];then 
	  java -jar webin-cli-*.jar \
	  	-context=reads \
	  	-userName $WEBINUSER \
	  	-password $WEBINPASSWORD \
	  	-manifest ${manifest} \
	  	-submit
  else
	  echo "INFO: directory reads/${sample_name} already exists, skipping!"
  fi
done 

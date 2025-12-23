#!/bin/bash
# Upload data to ENA with webin-cli.
# Expects Webin user and password in env variables WEBINUSER and WEBINPASSWORD.
# Fredrik Boulund 2022
set -eou pipefail

for manifest in *manifest.txt; do
  if [ ! -e ${manifest}.report ];then 
	  java -jar webin-cli-*.jar \
	  	-context=reads \
	  	-userName $WEBINUSER \
	  	-password $WEBINPASSWORD \
	  	-manifest ${manifest} \
	  	-submit
	  cp ./webin-cli.report "${manifest}.report"
  else
	  echo "INFO: ${manifest}.report already exists, skipping!"
  fi
done 

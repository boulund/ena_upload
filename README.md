# ENA Upload
Scripts for generating manifests and uploading paired raw read data to ENA.

## Step 1 - Register study and samples
 * https://ena-docs.readthedocs.io/en/latest/submit/study.html
 * https://ena-docs.readthedocs.io/en/latest/submit/samples.html

Manually create an appropriate sample registration sheet as per instructed in
"Register Samples using spreadsheet template" on the Webin platform.

## Step 2 - Generate manifests for FASTQ files
The `generate_manifests.py` script expects a CSV file generated from the
"Samples Report" function in the Webin submissions portal. It is important that
the file contains a table with columns `alias` and `id`. The script produces a
manifest file for each input fq.gz pair. The ENA study ID must be provided
using `--study STUDY_ID`. Also take an opportunity to review the other
manifest information to confirm that the INSTRUMENT and LIBRARY details are
correct. Modify the script to add/remove manifest properties if needed.

## Step 3 - Upload the data using Webin-CLI
Download the latest version of Webin-CLI from
[Webin-CLI Github](https://github.com/enasequence/webin-cli/releases/latest).

The `upload_data.sh` script runs `webin-cli-*.jar` (expected to be in the
same folder) to upload the reads to ENA using the Webin user account and
password specified in the environment variables `WEBINUSER` and
`WEBINPASSWORD`. 


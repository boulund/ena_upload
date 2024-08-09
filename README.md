# ENA Upload
Scripts for generating manifests and uploading paired raw read data to ENA.

The `generate_manifests.py` script expects a file called `ENA_samples.csv`,
containing a csv table with columns `alias` and `id`. It produces a manifest
file for each input fq.gz pair. The ENA study ID must be entered on line 11.
Also take an opportunity to review the manifest information to confirm that the
INSTRUMENT and LIBRARY details are correct.

The `upload_data.sh` script runs `webin-cli-4.3.0.jar` (expected to be in the
same folder) to upload the reads to ENA using the Webin user account and
password specified in the environment variables `WEBINUSER` and
`WEBINPASSWORD`. 


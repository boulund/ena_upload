#!/usr/bin/env python
""" Generate ENA manifest files for paired reads.
"""
__author__ = "Fredrik Boulund"
__date__ = "2022-04-27"

import pathlib
import textwrap
import csv

study = ""

samples = dict()
with open("ENA_samples.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        samples[row["alias"]] = row["id"]

for file_ in pathlib.Path(".").glob("*1.fq.gz"):
    _, sample_name, _, _ = file_.name.split("__")

    sample_id = samples[sample_name]
    fastq_1 = file_.name
    fastq_2 = file_.name.replace("1.fq.gz", "2.fq.gz")

    manifest = textwrap.dedent(f"""\
    STUDY {study}
    SAMPLE {sample_id}
    NAME {sample_name}
    INSTRUMENT DNBSEQ-G400
    LIBRARY_SELECTION RANDOM
    LIBRARY_SOURCE METAGENOMIC
    LIBRARY_STRATEGY WGS
    FASTQ {fastq_1}
    FASTQ {fastq_2}
    """)

    manifest_filename = file_.name.rstrip("1.fq.gz") + "manifest.txt"
    with open(manifest_filename, "w") as manifest_file:
        manifest_file.write(manifest)


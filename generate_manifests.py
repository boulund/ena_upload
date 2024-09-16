#!/usr/bin/env python
""" Generate ENA manifest files for paired reads.
"""
__author__ = "Fredrik Boulund"
__date__ = "2022-04-27"

from sys import argv, exit
import pathlib
import textwrap
import csv
import argparse


def parse_args():
    desc = ("Generate manifest files for FASTQ files, intended for use with Webin-CLI. "
            "Refer to https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html "
            "for valid options for instrument and library properties.")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-i", "--instrument", required=True,
            default="",
            help="Instrument, e.g. 'DNBSEQ-G400', 'DNBSEQ-T7', or 'Illumina Hiseq 2500'.")
    parser.add_argument("-s", "--sample-csv", required=True,
            default="ENA_samples.csv",
            help="ENA samples CSV containing 'alias' and 'id' columns.")
    parser.add_argument("-S", "--study", required=True,
            default="",
            help="ENA Study accession number.")
    parser.add_argument("--library-selection",
            default="RANDOM",
            help="Library selection [%(default)s].")
    parser.add_argument("--library-source",
            default="METAGENOMIC",
            help="Library source [%(default)s].")
    parser.add_argument("--library-strategy",
            default="WGS",
            help="Library strategy [%(default)s].")

    if len(argv) < 2:
        print("ERROR: Need arguments")
        parser.print_usage()
        exit(1)

    return parser.parse_args()


def generate_manifests(sample_csv, instrument, study, library_selection,
        library_source, library_strategy):

    samples = dict()
    with open(sample_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            samples[row["alias"]] = row["id"]

    for file_ in pathlib.Path(".").glob("*1.fq.gz"):
        if instrument in ("DNBSEQ-G400", "DNBSEQ-T7"):
            _, sample_name, _, _ = file_.name.split("__")
        else:
            # Assuming simple filenames like Sample123_1.fq.gz
            sample_name = file_.name.split(".")[0][:-2]

        sample_id = samples[sample_name]
        fastq_1 = file_.name
        fastq_2 = file_.name.replace("1.fq.gz", "2.fq.gz")

        manifest = textwrap.dedent(f"""\
        STUDY {study}
        SAMPLE {sample_id}
        NAME {sample_name}
        INSTRUMENT Illumina HiSeq 2500
        LIBRARY_SELECTION {library_selection}
        LIBRARY_SOURCE {library_source}
        LIBRARY_STRATEGY {library_strategy}
        FASTQ {fastq_1}
        FASTQ {fastq_2}
        """)

        manifest_filename = file_.name.rstrip("1.fq.gz") + "manifest.txt"
        with open(manifest_filename, "w") as manifest_file:
            manifest_file.write(manifest)


args = parse_args()

generate_manifests(
    args.sample_csv,
    args.instrument,
    args.study,
    args.library_selection,
    args.library_source,
    args.library_strategy,
)


"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    read_bed_file, print_line, BedLine
)

from boundsquery import (
    lower_bound, upper_bound
)


def extract_region(features: list[BedLine],
                   start: int, end: int, outfile) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""

    starts = [x[1] for x in features]
    lower_bound_index = lower_bound(starts,start,end)
    
   
    ends = [x[2] for x in features]
    upper_bound_index = upper_bound(ends,start, end)

    if upper_bound_index is None and lower_bound_index is None:
        return []
    elif upper_bound_index is None:
        return features[lower_bound_index:] 
    elif lower_bound_index is None:
        return features[:upper_bound_index]
    else:
        return features[lower_bound_index:upper_bound_index+1] 
 


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features = read_bed_file(args.bed)
    for query in args.query:
        chrom, start, end = query.split()
        # Extract the region from the chromosome, using your extract_region()
        # function. If you did your job well, this should give us the features
        # that we want.
        region = extract_region(
            features.get_chrom(chrom), int(start), int(end),args.outfile)
        for line in region:
            print_line(line, args.outfile)


if __name__ == '__main__':
    main()

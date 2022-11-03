# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from query_bed import extract_region
from bed import *


def test_extract_region():
    #we design a query from chrom0
    start = 0
    end = 200
    
    features= [BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='bar'),
               BedLine(chrom='chr1', chrom_start=199, chrom_end=200, name='qax'),
               BedLine(chrom='chr1', chrom_start=200, chrom_end=201, name='qux'),
               BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')]
    
    assert features[0:2] == extract_region(features,start,end,"")


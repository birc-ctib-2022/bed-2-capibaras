# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from merge_bed import (merge,read_bed_file)
from bed import *

def test_merge():
    
    f1= [BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='bar'),
          BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')]
    
    f2= [BedLine(chrom='chr1', chrom_start=199, chrom_end=200, name='qax'),
        BedLine(chrom='chr1', chrom_start=200, chrom_end=201, name='qux')]
    
    solution= [BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='bar'),
               BedLine(chrom='chr1', chrom_start=199, chrom_end=200, name='qax'),
               BedLine(chrom='chr1', chrom_start=200, chrom_end=201, name='qux'),
               BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')]
    
    ##create test file
    test_file_path= "data/test_merge.txt"
    merge(f1, f2, open(test_file_path, "w"))
    test_open = open(test_file_path,"r")
    sorted_test = read_bed_file(test_open)
    
    for chrom, features in sorted_test.items():
        #assert total length
        assert len(features) == len(solution)
        #assert if it is sorted
        for i in range(0,len(features)):
            assert features[i] == solution[i]



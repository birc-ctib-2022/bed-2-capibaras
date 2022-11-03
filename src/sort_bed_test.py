# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import *
from sort_bed import sort_file

def test_sort():
    
    sorted_bedlines = [ BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='bar'),
                        BedLine(chrom='chr1', chrom_start=199, chrom_end=200, name='qax'),
                        BedLine(chrom='chr1', chrom_start=200, chrom_end=201, name='qux'),
                        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')]
    
    unsorted_bedlines = [BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz'),
                        BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='bar'),
                        BedLine(chrom='chr1', chrom_start=200, chrom_end=201, name='qux'),
                        BedLine(chrom='chr1', chrom_start=199, chrom_end=200, name='qax')]
    
    #we create the table to test sort_file in sort_bed.py
    test_table = Table()
    for line in unsorted_bedlines:
        test_table.add_line(line)
    
    #sort the table
    sort_file(test_table)
    
    #check if the result is as expected
    for chrom, features in test_table.items():
        assert features == sorted_bedlines

test_sort()
    
    

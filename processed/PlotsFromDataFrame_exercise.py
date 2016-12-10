
# coding: utf-8

# In[18]:

# script for making plots from a dataframe

#import libraries: pandas, matplotlib.pyplot
import pandas as pd;
import matplotlib.pyplot as plt;

#import sys allows command line arguments
import sys

#assigns file specified in command line input
filename = sys.argv[1]
print("you are analyzing file:");
print(filename);

#%matplotlib inline

#import data using pandas
human_chr21 = pd.read_csv(filename, sep = "\t");

#calculate proportions
#save them as new columns in existing dataframe
human_chr21['gc_content'] = human_chr21['gc_bases'] / (human_chr21['win_end']-human_chr21['win_start']);
human_chr21['gene_content'] = human_chr21['exon_bases'] / (human_chr21['win_end'] - human_chr21['win_start']);

#plot gc_content vs. gene_content
plt.plot(human_chr21['gc_content'],human_chr21['gene_content'],'.',color = 'red');
plt.xlabel('GC Content');
plt.ylabel('Gene Content');
#plt.show();

#save figure to a file
plt.savefig(filename + '.plot.png')




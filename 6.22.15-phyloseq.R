# 1/13/15 Sequence analysis 
# wb: Jim Griffin
# updated 6/22 and renamed to 6.22.
# I want to get all of the basic data analysis steps completed ASAP so I can choose futher directions.
# goal is to use as many phyloseq wrapper functions as possible to save space and time.

library(phyloseq)
library(ggplot2)
library(vegan)
library("doParallel")
library("foreach")
library(plyr)
library(ape)
# I moved this and broke the shit out of it. 
source("Desktop/16s_methods_dev/vuono_work/R_scripts/phyloseq_wrappers.R")


# import qiime can take otu, biom, tree, map, ref-set 
biom = "/Users/jimbo/Desktop/6.9.15_seq_data/open_ref_otus/tax2/L6json.biom"
new_biom = "/Users/jimbo/Desktop/6.9.15_seq_data/jsonbiom.biom"

lvl6biom = "/Users/jimbo/Desktop/6.9.15_seq_data/open_ref_otus/tax2/lvl6jsonbiom2.biom"


ref_seqs = "/Users/jimbo/Desktop/6.9.15_seq_data/open_ref_otus/rep_set.fna"
tree = "/Users/jimbo/Desktop/6.9.15_seq_data/open_ref_otus/rep_set.tre"
map_file = "/Users/jimbo/Desktop/6.9.15_seq_data/map/map_v2.txt"

# make the phyloseq object
biom6.30 = import_biom(BIOMfilename = lvl6biom, "greengenes") # By default, all otus that were present in the biom file are passed as separate entities even if they have the same taxonomic rank. I'm trying to undo this. This level of detail could eventually be useful if I want to look at sub-OTU level dynamics at some point but for now I want to kill it. 
mapfile = "/Users/jimbo/Desktop/6.9.15_seq_data/map/map_v2_filtered.txt"
map = import_qiime_sample_data(mapfile)


biom6.30

biom6.9v3
#biom_from_biom = import_biom(BIOMfilename = new_biom, 

# this line just removes the NTC and the 2 that didn't work. 
biom6.9.pruned = prune_samples(sample_sums(biom6.9v3)>=1000, biom6.9v2)
biom6.9.pruned

# total observations before agglomeration
x = sample_sums(biom6.9.pruned)
totalsum = sum(x)
# after agglomeration - throws away >50% of data
y = sum(sample_sums(glom_taxa))
glom_taxa
names = tax_table(glom_taxa)
write.table(names, file = "/Users/jimbo/Desktop/names", sep = "\t")
abundance = otu_table(glom_taxa)
write.table(abundance, file = "/Users/jimbo/Desktop/abundance", sep = "\t")

# conclusion from above is that agglomerating OTUs based on taxonomy is a really bad idea right now because it discards any OTU that isn't classified at a given level. 

plot_richness(biom6.9.pruned, measures = "Observed", x="Description")
sample_data(biom6.9.pruned)
plot_richness(biom6.9.pruned, measures = "Observed", x="Month")

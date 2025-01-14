# TAMAP Package

The rapid evolution of technology has equipped researchers with the means to estimate metabolite abundance, thereby unlocking potential paths to understand their critical roles in cellular processes, including intercellular communication. Despite this progress, a need remains for enhanced methodologies capable of accurately quantifying all metabolites within a single cell due to the vast metabolomic diversity present. The dataset provided by Sarah et al., which encompasses 180 pan-cancer cell lines, each with six replicates, offers information on the abundance of a limited set of 1809 metabolites. Simultaneously, RNA-based Next-generation sequencing (NGS) techniques enable the profiling of hundreds of thousands of cells in one run. This juxtaposition raises a crucial question: Can gene expressions serve as reliable predictors for metabolite abundance? Given the limited metabolite data available for the 180 cell lines and our understanding of metabolic reactions, this study proposes a regression-based analysis with the objective of formulating a regression model predicated on gene expression data to predict metabolite abundance. This study scrutinizes the correlation between gene expressions and the roles of enzymes in substrate and product formation, aspiring to reveal the predictive capability of gene expressions in determining metabolite abundance. Collectively, this research aims to bridge the gap between gene expressions and metabolite abundance, highlighting the potential of gene expression data in predicting metabolite levels.

# Instructions

## How to install?
1. These are are required packages: 
   
	numpy, pandas, pickle, os, pkg_resources

2. To install these packages use below command
   	
	!pip install numpy, pandas, pickle, os, pkg_resources

3. Get latest version of GEMAP from the link given below:
   	
	https://pypi.org/project/TAMAP

4. Install it using below command.
   	
	pip install GEMAP

## How to use?
1. from GEMAP import GEMAP
   
   GEMAP("gene expression file name") 
   
   For example: 

   metaboplites=GEMAP("NIHMS1530136Simple.xlsx")
   
   print(metaboplites.head)

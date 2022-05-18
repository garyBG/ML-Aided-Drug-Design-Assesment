# Machine-Learning Aided Drug Design: An Extensive Assessment of the e-LEA3D Web Server

## Authors:

Gary Guiragossian

Seleen Jaber 

Esthela Cruz Mendez 

Dylan Thibault

Manasa Yadavalli 

## Description
Two-part research project whose aims were to evaluate computational tools for bio-medical drug discovery. The first part consisted of an analysis of four scoring functions (used for predicting binding affinity), so that we can accurataly asses generated drug molecules. After training on .mol protein-drug complexes from the PDBind database, the ML NNScore function significantly outperformed the other scoring fuctions. The second part then was to generate twenty ligands and simulate binding each of them on the 2P7G protein. Of these, ten of them met the pharmacokinetics, druglikeness, and binding affinity thresholds to assess their potential of being a plausible drugs. Research was done under the supervision of Dr. Zaneveld of the University of Washington, Bothell's Biology department.

### Workflow
![Workflow](/workflowDiagram.png "Research Workflow")

## Results

Through the E-LEA3D and PLANTS bioinformatic web servers we were able to combine techniques that allowed pharmacophore mapping, predict binding sites, and compare algorithms in scoring functions that evaluate the binding abilities of multiple ligand conformations. Based on the benchmark assessment, NNScore has promising acquired results that can replace PLANTS to increase the quality of ligands as shown by the strong positive relationship between the computed binding affinity values, and the experimental binding affinity values.

![Binding Affinity Results](/bindingaffinityResults.png "bindingaffinityResults")

A Pie Chart Depicting the Percent of Generated Ligands Satisfied the Binding
Affinity Threshold. Out of the twenty generated ligands, 80% of them had a binding
affinity less than 1000nm. 

### Example Visualization
![Example Visualization](/protein-ligand10.png "Ligand10Visualization")

Protein-Ligand Complex for Ligand 10, and the Estrogen-Related Receptor
Γ. The ligand is the blue structure, and the binding affinity of this protein-ligand complex
is 0.0044 nM, indicating that the ligand is able to form a strong interaction with the
protein. Visualization done through PyMol after PLANTS binding and Autodock format
conversion. The ligand is visualized in the pose and pocket with the highest binding
affinity as given by PLANTS.

## Python Scripts




## Acknowledgments

[E-LEA3D Drug Design Server](https://www.hsls.pitt.edu/obrc/index.php?page=URL1275672987)
[NNScore 2.0](https://pubs.acs.org/doi/10.1021/ci2003889)
[PLANTS](https://link.springer.com/chapter/10.1007/11839088_22)

## Affiliations:
1 University of Washington, Bothell, School of Science, Technology, Engineering, and
Mathematics, Division of Biological Sciences, UWBB-277, Bothell, WA 98011,
USA
* All authors contributed equally


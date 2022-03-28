import os
import subprocess
# import MvdWrapper
import sys

cd = 'D:\\Desktop\\UWB\\BIOFINAL'
vina = '"\\Program Files (x86)\\The Scripps Research Institute\\Vina\\vina.exe" ' \
          r'--config config.txt --log log.txt --out output'
nnScore = 'python NNScore2.py '
nnVina = ' -vina_executable C:\\Vina\\vina.exe'

i = 15
configPath = 'C:\\Users\\garyl\\Desktop\\UWB\\SPR\\BIO\\bioP1\\formatted\\config.txt'

while i < 20:

    nnRecep = "-receptor 2p7g_receptor.pdbqt"
    nnLig = " -ligand ligand_" + str(i) + ".pdbqt" 
    nnF = nnScore + nnRecep + nnLig + nnVina
    
    subprocess.call(nnF, shell=True)
    i += 1
# prepare_dpf4.py -l pdbqt_file -r pdbqt_file
# complex = '1hvr'
#
# mvd = MvdWrapper.MvdWrapper("C:/Program Files (x86)/Molegro/MVD/bin/mvdconsole.exe", gui=True)
# mvd.info("testing")
# mvd.cd(cd)  # change to output path
# mvd.waitUntilReady()
# mvd.download(complex, complex + ".pdb")  # download from pdb.org
# mvd.importFrom("All", complex + ".pdb")  # import into workspace
# mvd.rmsd("ligand[0]")  # set a ligand as a rmsd reference
# mvd.dock("")  # start the docking
# mvd.exit()

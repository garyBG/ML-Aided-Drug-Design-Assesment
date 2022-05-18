import os
import subprocess

cd = "B BIO 383\\Project2"
plantsCmd = "./PLANTS1.2_64bit --mode screen <CONFIG>"

os.chdir(cd)
configFiles = os.listdir(cd + "\\configs")


for x in configFiles:
    nextCmd = plantsCmd.replace("<CONFIG>", x.replace(".file", ""))
    subprocess.call(nextCmd, shell=True)

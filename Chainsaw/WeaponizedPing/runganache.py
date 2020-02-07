import os,subprocess

FNULL = open(os.devnull, 'w')
subprocess.Popen(["ganache-cli -h '0.0.0.0' -p 9810"], shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

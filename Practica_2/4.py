evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""

title = evaluar.split('\n')[0].split(':')[1].split()
body = evaluar.split('\n')[1].split(':')[1].split('.')


easy = 0
aceptable = 0
hard = 0
very_hard = 0
for sentence in body:
    lenght =len(sentence.split())
    if(lenght > 25):
        very_hard += 1
    elif(lenght >= 18 and lenght <= 25):
        hard += 1
    elif(lenght >= 13 and lenght <= 17):
        aceptable+=1
    elif (len(sentence.split()) <= 12):
        easy+=1

if (len(title) > 10):
    print('Not ok')
else:
    print('ok')
print(f'There was {easy=} to read, {aceptable=} to read, {hard=} to read, {very_hard=} to read')       
# encoding = 'utf-8'

import argparse
import numpy

parser = argparse.ArgumentParser(description='Calculation for Atom Volume')

parser.add_argument('--band_path', type = str, default='./band.out', help='the file path for band.out')
parser.add_argument('--eigenvec_path', type = str, default='./eigenvec.out',help = "the file path for eigenvec.out")

parser.add_argument('--target_atom', type = str, default='all', help='a specific atom or "all" for all atoms')

args = parser.parse_args()
print(args)


def load_band(path):

    states = []
    with open(path,'r') as f:
        f.readline()
        for line in f:
            if line.strip():
                line = line.strip().split()[-1]
                states.append(line)
    states = numpy.array(states,dtype=float)
    return states

def load_eigenvec(path):
    '''

    :param path: the path of eigenvec.out
    :return:
        Eigenvectors: a list, each item is a dict {count+atom: [list of values]}
    '''
    Eigenvectors = []
    ev = {}
    count, atom, axis, eigenvalue = None, None, None, None
    with open(path,'r') as f:
        f.readline()
        for line in f:

            if line.strip():
                if line.startswith('Eigenvector'):
                    if ev!={}:
                        Eigenvectors.append(ev)
                    ev = {}
                    continue

                line = line.split()
                if len(line) == 5:
                    count = line[0]
                    atom = line[1]
                    axis = line[2]
                    eigenvalue = line[3]
                    ev[str(count+atom)]=[eigenvalue]
                elif len(line)==3:
                    count = count
                    atom = atom
                    axis = line[0]
                    eigenvalue = line[1]
                    ev[str(count+atom)].append(eigenvalue)
                else:
                    print("Wrong line?")
        if ev!={}:
            Eigenvectors.append(ev)
    return Eigenvectors


def AtomVolume(states, eigenvalues, target_atom):

    target_eigenvalues = []
    for item in eigenvalues:
        tmp =numpy.array(item[target_atom],dtype=float)
        value = numpy.dot(tmp.T,tmp)
        target_eigenvalues.append(value)
    target_eigenvalues = numpy.array(target_eigenvalues,dtype=float)

    atomvolume = numpy.dot(states.T,target_eigenvalues)
    print("The atom volume for {} is {}".format(target_atom,atomvolume))



if __name__ == '__main__':
    states = load_band(args.band_path)
    eigenvectors = load_eigenvec(args.eigenvec_path)

    try:
        assert len(states)==len(eigenvectors)
    except AssertionError:
        print("The band.out and eigenvec.out may not matched!!!")
        exit(0)

    if args.target_atom=='all':
        targets = eigenvectors[0].keys()
        for atom in targets:
            AtomVolume(states, eigenvectors,atom)
    else:
        AtomVolume(states, eigenvectors,args.target_atom)






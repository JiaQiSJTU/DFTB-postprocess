# Calculation for Atom Volume

### Requirements:
* argparse
* numpy

### Instruction: 

```python
python3 AtomVolume_Calculator.py [--band_path "the file path for band.out"] [--eigenvec_path "the file path for eigenvec.out"] [--target_atom "a specific atom or 'all' for all atoms"]
```

###Example-1:

* run: python3 AtomVolume_Calculator.py --target_atom all

* output:
```python
Namespace(band_path='./band.out', eigenvec_path='./eigenvec.out', target_atom='all')
The atom volume for 1O is 5.992598931196
The atom volume for 2H is 0.42254177520799996
The atom volume for 3H is 0.42254177520799996
```

### Example-2:

* run: python3 AtomVolume_Calculator.py --target_atom 1O

* output:
```python
Namespace(band_path='./band.out', eigenvec_path='./eigenvec.out', target_atom='1O')
The atom volume for 1O is 5.992598931196
```
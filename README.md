# EasierQM9
This is an implementation of the QM9 dataset in a pickled format. The data source is pytorch geometry library. Please refer to the original source for more details: https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html#torch_geometric.datasets.QM9

Although you can find multiple versions of QM9 data from different sources, you may encounter various types of problems inc. network, incompatibility to the extraction API etc.  Now you can directly use pickle to load it! With SMILES and coordinates which offers you more wider world to explore.

## Quick Start
```python
# You can load the QM9 dataset by running the following code:
from loadQM9 import EasyQM9
QM9 = EasyQM9() 
"""You can organize data files in a different directory by passing the path argument to EasyQM9, e.g., EasyQM9(path = './data_release'). However, never change the name of each data file"""
# You can observe one record of the QM9 dataset by running the following code:
QM9[-1]
```

#### Output:
```python
Loading QM9 data parts: 100%|██████████| 5/5 [00:06<00:00,  1.37s/it]
Load Complete! Found 133247 samples.
```
```python
{'mol_id': 'gdb_133885',
 'smiles': 'C1[N@@H+]2[C@H]3[C@@H]4[C@@H]5O[C@]13[C@H]2[C@@H]54',
 'xyz': [['C', np.float64(-1.4099), np.float64(1.3373), np.float64(0.41)],
  ['N', np.float64(-1.5646), np.float64(0.0991), np.float64(-0.5169)],
  ['C', np.float64(-0.8329), np.float64(-0.7076), np.float64(0.6043)],
  ['C', np.float64(0.271), np.float64(-1.6186), np.float64(0.1448)],
  ['C', np.float64(1.5285), np.float64(-0.7551), np.float64(0.3395)],
  ['O', np.float64(1.2502), np.float64(0.4586), np.float64(1.0471)],
  ['C', np.float64(-0.0574), np.float64(0.6112), np.float64(0.5411)],
  ['C', np.float64(-0.0959), np.float64(0.3804), np.float64(-0.9721)],
  ['C', np.float64(0.8167), np.float64(-0.8131), np.float64(-1.0224)]],
 'attr': array([ 3.64015000e+00,  2.21764000e+00,  1.93793000e+00,  8.62600000e-01,
         6.94800000e+01, -2.31600000e-01,  7.42000000e-02,  3.05800000e-01,
         7.56355700e+02,  1.27862000e-01, -4.00633052e+02, -4.00627892e+02,
        -4.00626948e+02, -4.00662186e+02,  2.34340000e+01, -1.60347187e+03,
        -1.61445516e+03, -1.62334508e+03, -1.49224715e+03])}
```

## Data Format
The complete set of 133,885 molecules is stored in a single pickled file named `qm9_data.pkl`. Each molecule is represented as a dictionary containing the following keys:
* `mol_id`: A unique identifier for the molecule (e.g., 'gdb_1').
* `smiles`: The SMILES string representation of the molecule (e.g., 'C'). Note: it's the canonical SMILES string and normally H atoms are not explicitly represented.
* `xyz`: A list of lists, where each inner list contains the atomic symbol and its corresponding x, y, z coordinates (e.g., [['C', -0.0127, 1.0858, 0.008]]).
* `attr`: A NumPy array containing 19 attributes of the molecule, including various energy levels, dipole moments, and other quantum chemical properties (e.g., array([ 1.57711800e+02,  1.57709970e+02,  1.57706990e+02,  0.00000000e+00,
         1.32100000e+01, -3.87700000e-01,  1.17100000e-01,  5.04800000e-01,
         3.53641000e+01,  4.47490000e-02, -4.04789300e+01, -4.04760620e+01,
        -4.04751170e+01, -4.04985970e+01,  6.46900000e+00, -3.95999595e+02,
        -3.98643290e+02, -4.01014647e+02, -3.72471772e+02]).
    * The attributes are ordered as follows:

    |Attribute Index| Attribute Name | Description |
    |---------------|----------------|-------------|
    | 0             | A              | X Axis rotational constants|
    | 1             | B              | Y Axis rotational constants|
    | 2             | C              | Z Axis rotational constants|
    | 3             | `mu`           | Dipole moment (Debye) |
    | 4             | `alpha`        | Isotropic polarizability (Bohr^3) |
    | 5             | `homo`         | Energy of the highest occupied molecular orbital (eV) |
    | 6             | `lumo`         | Energy of the lowest unoccupied molecular orbital (eV) |
    | 7             | `gap`          | Gap between HOMO and LUMO (eV) |
    | 8             | `r2`           | Radius of gyration (Bohr^2) |
    | 9             | `zpve`         | Zero-point vibrational energy (kcal/mol) |
    | 10            | `u0`           | Internal energy at 0 K (kcal/mol) |
    | 11            | `u298`         | Internal energy at 298.15 K (kcal/mol) |
    | 12            | `h298`         | Enthalpy at 298.15 K (kcal/mol) |
    | 13            | `g298`         | Gibbs free energy at 298.15 K (kcal/mol) |
    | 14            | `cv`           | Heat capacity at constant volume (cal/(mol·K)) |
    | 15            | `u0_atom`      | Atomic internal energy at 0 K (kcal/mol) |
    | 16            | `u298_atom`    | Atomic internal energy at 298.15 K (kcal/mol) |
    | 17            | `h298_atom`    | Atomic enthalpy at 298.15 K (kcal/mol) |
    | 18            | `g298_atom`    | Atomic Gibbs free energy at 298.15 K (kcal/mol) |

## Reference
### Original Paper:
Ramakrishnan, Raghunathan; Dral, Pavlo; Rupp, Matthias; Anatole von Lilienfeld, O. (2014). Quantum chemistry structures and properties of 134 kilo molecules. figshare. Collection. https://doi.org/10.6084/m9.figshare.c.978904.v5

### Pytorch Source:
Click icon to visit full official documentation: [![PyTorch Logo](https://raw.githubusercontent.com/pytorch/pytorch/master/docs/source/_static/img/pytorch-logo-dark.png)](https://pytorch-geometric.readthedocs.io/en/latest/modules/datasets.html#torch_geometric.datasets.QM9)
"The QM9 dataset from the ["MoleculeNet: A Benchmark for Molecular Machine Learning"](https://arxiv.org/abs/1703.00564) paper, consisting of about 130,000 molecules with 19 regression targets."





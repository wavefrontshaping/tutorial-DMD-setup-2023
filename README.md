# [_A practical guide to Digital Micro-mirror Devices (DMDs) for wavefront shaping_](https://arxiv.org/abs/XXXX)

<!-- [![DOI](https://zenodo.org/badge/DOI/10.48550/arXiv.2310.19337.svg)](https://doi.org/10.48550/arXiv.2310.19337) -->

## **S. M. Popoff [![](./ressources/logos//orcid.svg)](https://orcid.org/0000-0002-7199-9814) [![](./ressources/logos/gscholar.svg)](https://scholar.google.com/citations?user=2OuzjokAAAAJ), M. W. Matthès [![](./ressources/logos/gscholar.svg)](https://scholar.google.com/citations?user=daSSCjUAAAAJ), Y. Bromberg [![](./ressources/logos//orcid.svg)](https://orcid.org/0000-0003-2565-7394) [![](./ressources/logos/gscholar.svg)](https://scholar.google.com/citations?user=S5znnzoAAAAJ), and R. Gutiérrez-Cuevas [![](./ressources/logos/orcid.svg)](https://orcid.org/0000-0002-3451-6684) [![](./ressources/logos/gscholar.svg)](https://scholar.google.com/citations?user=7BSmVYkAAAAJ)**

```
@misc{popoff2023DMDtutorial,
      title={{A practical guide to Digital Micro-mirror Devices (DMDs) for wavefront shaping}},
      author={Popoff, Sébastien M. and Matthès, Maxime W. and Bromberg, Yaron and Gutiérrez-Cuevas, Rodrigo},
      year={2023},
      eprint={2310.19337},
      archivePrefix={arXiv},
      primaryClass={physics.optics}
}
```

## [/paper](paper/): Latex sources for the article

Download last PDF version of the article [here](./paper/main.pdf)

## [/python](python/): Python examples

### Global requirements

- scipy
- numpy
- matplotlib

Install with:

```bash
pip install scipy, numpy
```

or

```bash
conda install scipy, numpy
```

### 1. [DMD_diffraction_effects.ipynb.ipynb](python/DMD_diffraction_effects.ipynb.ipynb): Simulation of DMD diffraction effects

See also our online tool on [wavevrontshaping.net](https://www.wavefrontshaping.net/post/id/49)

### 2. [Experimental_aberration_correction.ipynb](python/Experimental_aberration_correction.ipynb): Data analysis of the experimental characterization of the DMD aberrations

### Requirements \[optional - for video\]

- cv2

```bash
pip install opencv-python
```

or

```bash
conda install -c anaconda opencv
```

### 3. [Simulation_aberration_correction.ipynb](python/Simulation_aberration_correction.ipynb): Simulation of aberration compensation optimization

### Additional requirements

- aotools (for Zernike polynomials)

```bash
pip install scipy, numpy, aotools
```

### Requirements \[optional\]

- EasyOptimization

```bash
pip install git+https://gitlab.institut-langevin.espci.fr/spopoff/EasyOptimization.git
```

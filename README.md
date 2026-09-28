# Forest Pest Dynamics Under Climate Variability

A reproducible Python modelling project exploring interactions among conifer foliage, spruce budworms, bark beetles, avian predators, and climate-driven changes in ecosystem resilience.

## Overview

This repository contains the computational work supporting the research project **Ecological Dynamics of Forest Pest Systems: Modelling Budworm–Bark Beetle Interactions with Climate-Driven Instabilities**. The model uses coupled ordinary differential equations (ODEs) to examine how pest growth, herbivory, predation, competition, foliage recovery, disease mortality, and climate variability can produce stable coexistence, progressive forest decline, or ecosystem collapse.

The project is designed for scientific exploration and education. Parameter values are illustrative unless explicitly calibrated to field observations; therefore, outputs should be interpreted as model experiments rather than site-specific forecasts.

## Research questions

- Under what conditions can budworms and forest foliage coexist sustainably?
- How does bark beetle introduction alter budworm–foliage dynamics?
- How do competition, predation, disease, and climate variability modify ecosystem resilience?
- Which simulated thresholds may serve as early-warning indicators of forest decline?

## Model formulation

The model tracks:

- `B(t)`: spruce budworm density.
- `C(t)`: bark beetle density.
- `S(t)` or `ES(t)`: foliage or effective foliage stock.
- `E(t)`: tree-health index, when included in an experiment.
- `t`: time in years.

### Stable budworm–foliage system

$$
\frac{dB}{dt} = r_B B\left(1 - \frac{B}{K_B ES}\right) - \beta\frac{B^2}{\alpha^2+B^2}
$$

$$
\frac{dES}{dt} = r_S ES\left(1 - \frac{ES}{K_S}\right) - \lambda ES - P_B B
$$

### Dual-pest system

$$
\frac{dB}{dt} = r_B B\left(1 - \frac{B}{K_B S}\right) - \delta BC - \beta\frac{B^2}{\alpha^2+B^2}
$$

$$
\frac{dC}{dt} = r_C C\left(1 - \frac{C}{K_C S}\right) - \delta BC
$$

$$
\frac{dES}{dt} = r_S ES\left(1 - \frac{ES}{K_S}\right) - \lambda ES - P_B B - P_C C
$$

### Climate forcing

Climate variability modifies foliage regrowth through a periodic forcing term:

$$
\frac{dES}{dt} = \left[r_S-A\sin\left(\frac{2\pi t}{T}\right)\right]ES\left(1-\frac{ES}{K_S}\right)-\lambda ES-P_BB-P_CC
$$

The implementation may also include disease mortality and linear bird predation, depending on the experiment.

## Repository structure

```text
forest-pest-dynamics/
├── README.md
├── LICENSE
├── requirements.txt
├── CITATION.cff
├── src/
│   └── model.py                  # Reusable ODE functions and parameters
├── scripts/
│   └── run_experiments.py        # Command-line simulation entry point
├── notebooks/
│   └── forest_pest_dynamics_original.ipynb
├── figures/                       # Generated figures and plots
├── data/                          # Input or processed data, if added later
├── docs/                          # Extended scientific notes
└── tests/                         # Validation and regression tests
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/pinkoom123/forest-pest-dynamics-under-climate-variability.git
cd forest-pest-dynamics-under-climate-variability
```

### 2. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebook

```bash
jupyter lab
```

Open `notebooks/forest_pest_dynamics_original.ipynb` and run the cells from top to bottom. The notebook contains exploratory simulations for stable dynamics, three-phase budworm–foliage interactions, bark beetle coexistence, dual-pest decline, and climate-driven collapse.

The original notebook contains the full exploratory simulations and figures. The src/ and scripts/ directories provide a refactored implementation of the core model and selected climate-forcing experiments. Exact reproduction of all notebook figures requires running the notebook or extending the refactored scripts to include each scenario.

### 5. Run the script

```bash
python scripts/run_experiments.py --scenario climate --years 102 --output-dir figures
```

## Scientific workflow

1. Define ecological parameters and initial conditions.
2. Specify the right-hand side of the ODE system.
3. Integrate the equations with `scipy.integrate.solve_ivp`.
4. Store time-series output for budworms, bark beetles, and foliage.
5. Diagnose thresholds and regime changes.
6. Produce labelled figures with units, legends, and reproducible settings.
7. Compare scenarios and document parameter changes.

## Interpretation of outputs

The simulations are interpreted in terms of qualitative regimes:

- **Stable coexistence:** Pest densities remain bounded and foliage recovery offsets losses.
- **Progressive decline:** Foliage decreases while pest pressure remains substantial.
- **Competitive restructuring:** Bark beetle introduction changes the relative abundance of the pest species.
- **Climate-driven collapse:** Reduced foliage recovery and cumulative pest damage push the system below a critical resource state.

A threshold identified in one parameterisation should not be treated as a universal ecological constant. It is a diagnostic of the particular model, parameter set, and initial conditions.

## Reproducibility and limitations

The current notebook contains exploratory and scenario-specific parameterisations. Some cells use manually specified phase-transition values to initialise later simulations. For publication-grade analysis, the model should be refactored into reusable functions, all parameters should be stored in version-controlled configuration files, and results should be validated against field observations or independent datasets.

Important limitations include the absence of spatial dispersal, forest age structure, host-species diversity, stochastic outbreak initiation, detailed predator dynamics, and site-specific temperature-response functions. Future improvements should include sensitivity analysis, uncertainty quantification, ensemble simulations, spatial extensions, and calibration with forest-inventory and pest-surveillance data.

## Related scientific background

The qualitative outbreak framing is informed by Ludwig, Jones, and Holling (1978), who analysed the spruce budworm and forest as a nonlinear insect outbreak system. The feedback perspective is also informed by Wood et al. (2008), who reviewed Daisyworld and the role of organism–environment feedbacks in Earth-system modelling.

## Citation

If you use this code or adapt the model, please cite the repository using the information in `CITATION.cff` and acknowledge the original research manuscript by Patrick Inkoom.

## Author

**Patrick Kobina Inkoom**  
Climate and environmental data researcher | Ecological and climate-system modelling

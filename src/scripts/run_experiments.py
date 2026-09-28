"""Run reproducible forest-pest simulations and save a figure."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.model import dual_pest_system

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", choices=["climate"], default="climate")
    parser.add_argument("--years", type=float, default=102)
    parser.add_argument("--output-dir", default="figures")
    args = parser.parse_args()
    p = {"r_B": .22, "r_C": .35, "r_S": .06, "K_B": 1.2, "K_C": 1.0, "K_S": 600, "beta": .4, "alpha": 30, "delta": .0002, "P_B": .004, "P_C": .003, "decay": .07, "mu": .01, "A": .015, "period": 1., "eps": 1e-8}
    t_eval=np.linspace(0,args.years,2000)
    sol=solve_ivp(lambda t,y: dual_pest_system(t,y,p),(0,args.years),[10,0,600],t_eval=t_eval,max_step=.1)
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(10,6)); ax.plot(sol.t,sol.y[0],label="Budworms (B)"); ax.plot(sol.t,sol.y[1],label="Bark beetles (C)"); ax.plot(sol.t,sol.y[2],label="Foliage (S)"); ax.set(xlabel="Time (years)",ylabel="Density / foliage",title="Forest pest dynamics under climate variability"); ax.legend(); ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(out/"climate_scenario.png",dpi=300); print(f"Saved {out/'climate_scenario.png'}")

if __name__ == "__main__": main()

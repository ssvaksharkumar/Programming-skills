from collections import Counter
from itertools import islice
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt

def extract_data_points(fname):
    #print(f"# parsing {fname}...")
    data = dict()
    current_series = 0
    current_i = -1
    current_j = 0
    
    with open(fname, 'rt') as ftext:
        distances = []
        forces = []
        inside_data = False
        
        for line in ftext:
            if line.startswith("#"):
                if "iIndex" in line:
                    if distances and forces and current_i >= 0:
                        data[(current_series, current_i, current_j)] = (np.array(distances), np.array(forces))
                        current_series = 1 - current_series
                    current_i = int(line.split()[-1])
                    distances = []
                    forces = []
                    inside_data = False
                elif "jIndex" in line:
                    current_j = int(line.split()[-1])
                elif "recorded-num-points" in line:
                    inside_data = True
            elif inside_data:
                values = line.split()
                if len(values) >= 2:
                    distances.append(float(values[0]))
                    forces.append(float(values[1]))
        
        if distances and forces:
            data[(current_series, current_i, current_j)] = (np.array(distances), np.array(forces))
    
    return data



def estimate_slope(distances, forces, series):

    
    # Selecting data for linear fitting
    def calc_slope(fs, fe):
        
        distances_fit = distances[fs:fe]
        forces_fit = forces[fs:fe]

        # Linear fit
        A = np.vstack([distances_fit, np.ones(len(distances_fit))]).T
        return np.linalg.lstsq(A, forces_fit, rcond=None)[0]
    
    if series == 0:
        # For Series 0, fit from local_min

        if len(forces) == 0:
            raise ValueError("Empty forces array")

        # Find local minimum and maximum force index
        f_index = np.argsort(forces)
        my_mid = forces[f_index[0]]+(forces[f_index[-1]]-forces[f_index[0]])/4
        choice = None
        for i in f_index[::-1]:
            if forces[i] < my_mid:
                choice = i
                slp, _ = calc_slope(choice, choice+50)
                print(slp)
                break
        

        # Setting fit_start at local minimum
        fit_start = choice

        # Set fit_end to maximum force index
        fit_end = choice+70 
        print(forces[fit_start])

    else:
        
        # Determine  threshold dynamically based on the data
        threshold = np.max(forces) * 0.05  

        # Finding index where forces exceed the threshold
        fit_start = np.argmin(forces > threshold)

        # Set fit_end to fit_start + 50 points
        fit_end = fit_start + 50

    #print(f"fit_start: {fit_start}, fit_end: {fit_end}")

    slope, intercept = calc_slope(fit_start, fit_end)
    return slope, intercept, fit_start, fit_end

def plot_curve(point, curve, slope, intercept,fit_start,fit_end, series, save=None):
    s, i, j = point
    d, f = curve
    plt.figure(figsize=[9, 6])
    plt.plot(d, f, label=f'data: push at ({i}, {j})')
    
    # Plot the extended fitted line
    fitted_line = slope * d + intercept
    plt.plot(d, fitted_line, 'r--', label=f'{slope:.5f} N/m')

    # Adding markers for fit start and end points
    if series==0:
        plt.scatter([d[fit_start+10], d[fit_end-50]], [f[fit_start+10], f[fit_end-50]], marker="x", color='red', zorder=5, label='Fit range')
    else:
        plt.scatter([d[fit_start+100], d[fit_end-20]], [f[fit_start+100], f[fit_end-20]], marker="x", color='red', zorder=5, label='Fit range')
    plt.title(f"Part II: curve-{s:01d}-{i:03d}-{j:03d}.png\npush at ({i}, {j}); number of records: {len(d)}")
    plt.xlabel("distance (m)")
    plt.ylabel("force (N)")
    if series ==0:
        plt.ylim(0.4e-9, 1.7e-9)
    
    plt.legend()
    plt.grid()
    
    if save is not None:
        plt.savefig(save, dpi=200, bbox_inches='tight')
    plt.close()

def main(args):
    data = extract_data_points(args.textfile)
    #print(f"# processing {len(data)} spectra...")
    
    for point, curve in data.items():
        s, i, j = point
        d, f = curve
        series=s
        slope, intercept,fit_start,fit_end = estimate_slope(d, f,series)
        print(f"{s} {i:03d} {j:03d} {slope:.5f}")
        
        if args.plotprefix:
            fname = f'{args.plotprefix}-{s:01d}-{i:03d}-{j:03d}.png'
            plot_curve(point, curve, slope, intercept, fit_start, fit_end, series, save=fname)

def get_argument_parser():
    p = ArgumentParser()
    p.add_argument("--textfile", "-t", default="sample.txt",
        help="name of the data file containing AFM curves for many points")
    p.add_argument("--plotprefix", default="test",
        help="non-empty path prefix of plot files (PNGs); do not save plots if not given")
    return p

if __name__ == "__main__":
    p = get_argument_parser()
    args = p.parse_args()
    main(args)
    
    

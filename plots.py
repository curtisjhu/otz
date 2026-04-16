import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description='Plot index vs Channel 1 voltage')
    parser.add_argument('csv', help='Path to CSV file')
    parser.add_argument('-o', '--output', default='channel1_plot.png', help='Output image file')
    args = parser.parse_args()

    try:
        import pandas as pd
        import matplotlib.pyplot as plt
    except Exception as e:
        print('Missing required packages: pandas and matplotlib')
        print('Install with: python -m pip install pandas matplotlib')
        raise

    df = pd.read_csv(args.csv)
    col_candidates = [c for c in df.columns if 'Channel 1' in c or 'channel 1' in c.lower()]
    if not col_candidates:
        print('CSV columns:', df.columns.tolist())
        raise SystemExit('Could not find a Channel 1 column in the CSV')

    col = col_candidates[0]
    y = df[col]
    x = df.index

    plt.figure(figsize=(10,4))
    plt.plot(x, y, '-', linewidth=0.8)
    plt.xlabel('Index')
    plt.ylabel(col)
    plt.title('Index vs ' + col)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out_path = args.output
    plt.savefig(out_path, dpi=150)
    print(f'Saved plot to {os.path.abspath(out_path)}')

if __name__ == '__main__':
    main()
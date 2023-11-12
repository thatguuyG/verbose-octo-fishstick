import argparse
from helpers.reconcile import reconcile_data


def main():
    parser = argparse.ArgumentParser(description="CSV Reconciliation Tool")

    parser.add_argument("-s", "--source", required=True, help="Path to the source CSV file.")
    parser.add_argument("-t", "--target", required=True, help="Path to the target CSV file.")
    parser.add_argument("-o", "--output", required=True, help="Path to save the output reconciliation report.")

    args = parser.parse_args()

    # Call the reconcile_data function
    reconcile_data(args.source, args.target, args.output)

if __name__ == "__main__":
    main()

import pandas as pd
import os


def is_csv_file(file_name):
    return file_name.endswith(".csv")


def reconcile_data(source_data, target_data, output_path):
    if not is_csv_file(source_data) or not is_csv_file(target_data):
        print("Source and target files must have a .csv extension.")
        return

    if not (os.path.exists(source_data) and os.path.exists(target_data)):
        print("Source and target files not found.")
        return

    # Load data
    source_df = pd.read_csv(source_data)
    target_df = pd.read_csv(target_data)

    missing_in_target = source_df[~source_df['ID'].isin(target_df['ID'])]
    missing_in_source = target_df[~target_df['ID'].isin(source_df['ID'])]

    # Create DataFrames with identical structures for comparison
    common_records = source_df.merge(target_df, on='ID', suffixes=('_source', '_target'))

    # output list
    report_data = []

    # append missing in source and target data
    for index, row in missing_in_target.iterrows():
        report_data.append({"Type": "Missing in Target", "Record Identifier": row['ID']})
    for index, row in missing_in_source.iterrows():
        report_data.append({"Type": "Missing in Source", "Record Identifier": row['ID']})

    # Compare "Date" and "Amount" fields for discrepancies
    # for column in common_records.columns.tolist():
    for column in ["Date", "Amount"]:
        common_records[f"{column}_discrepancy"] = common_records[f"{column}_source"] != common_records[f"{column}_target"]
        for index, row in common_records.iterrows():
            if row[f"{column}_discrepancy"]:
                report_data.append({
                    "Type": "Field Discrepancy",
                    "Record Identifier": row['ID'],
                    "Field": column,
                    "Source Value": row[f"{column}_source"],
                    "Target Value": row[f"{column}_target"]
                })

    # output dataframe
    reconciliation_report = pd.DataFrame(report_data, columns=["Type", "Record Identifier", "Field", "Source Value", "Target Value"])
    if isinstance(reconciliation_report, pd.DataFrame) and not reconciliation_report.empty:
        print(f"Reconciliation report saved to {output_path}")
        reconciliation_report.to_csv(output_path, index=False)
        return reconciliation_report

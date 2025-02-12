import csv

def to_table(file_path):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Determine column widths (max length of each column)
    col_width = [max(len(str(item)) for item in cols) for cols in zip(*data)] #zip data ensures single col value 

    # Create horizontal border
    border = "+-" + "-+-".join("-" * width for width in col_width) + "-+" #-+ this is used for separating
    print(border)

    for i, row in enumerate(data):  #enumerate gives both index and data 
        print("| " + " | ".join(f"{item:<{col_width[j]}}" for j, item in enumerate(row)) + " |") # < left aligned and takes col width space 
        print(border if i == 0 else border)  # Print border after the header and at the end

# Example CSV file path
file_path = "/home/diya/Documents/data1.csv"  # Replace with your actual CSV file path
to_table(file_path)
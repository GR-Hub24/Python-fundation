import csv

def del_col(csv_file, col_to_del):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        for col_index in sorted(col_to_del, reverse=True):
            del row[col_index]

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

csv_file = 'overnight.csv'
col_to_del = [2, 4, 6]
del_col(csv_file, col_to_del)

print(f"Congrats! All the stupid wavelength rows are beautifully deleted.")


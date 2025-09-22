import camelot

# replace with your actual PDF file path
tables = camelot.read_pdf("input.pdf", pages="all")

print(f"Total tables extracted: {len(tables)}")

# Export all tables into one Excel file
tables.export("output.xlsx", f="excel")

# Or save the first table separately
if len(tables) > 0:
    tables[0].to_excel("first_table.xlsx")
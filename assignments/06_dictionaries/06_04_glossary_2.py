glossary = {'Variable' : 'A name that stores data values', 'Comment' : 'Notes in the code', 'Loop' : 'Repeats the code', 'Dictionary' : 'Key-value pairs', 'If Statement' : 'Executes code based on conditions', 'List' : 'Ordered mutable collection', 'Tuple' : 'Ordered immutable collection', 'Module' : 'A file containing Python Code', 'Integer' : 'Whole numbers', 'Float' : 'Numbers with decimals'}
terms1 = glossary['Variable']
terms2 = glossary['Comment']
terms3 = glossary['Loop']
terms4 = glossary['Dictionary']
terms5 = glossary['If Statement']
terms6 = glossary['List']
terms7 = glossary['Tuple']
terms8 = glossary['Module']
terms9 = glossary['Integer']
terms10 = glossary['Float']
for key, value in glossary.items():
    print(f"\n{key}")
    print(f":{value}")
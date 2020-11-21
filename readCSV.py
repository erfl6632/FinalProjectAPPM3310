import csv 
def readCSV(csvname):
    with open(csvname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count=0
        totalContents = []
        for row in csv_reader:
            rowContent = []
            for x in row:
                rowContent.append(x)
            totalContents.append(rowContent)
        print(totalContents)
        '''
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
        '''



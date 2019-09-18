#!/usr/bin/python
import csv , json

csvFilePath = "/Users/svmss/Desktop/mywork/ContactList.csv"
oppcsv="/Users/svmss/Desktop/mywork/OpportunityList.csv"
jsonFilePath = "Output.json"
arr = []
arr1 = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile, open (oppcsv) as OpportunityCsv:
    csvReader = csv.DictReader(csvFile)
    oppReader = csv.DictReader(OpportunityCsv)
    for csvRow in csvReader:
        arr.append(csvRow)
        #print(csvRow['Name'])
        for oppRow in oppReader:
            arr1.append(oppRow)
            if( (csvRow['Name'] == oppRow['Contact1']) ):
                print("Contact 1 is  " +oppRow['Contact1']+ " and Contact2 is "+ oppRow['Contact2'] )


# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
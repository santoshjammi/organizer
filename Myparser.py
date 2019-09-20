#!/usr/bin/python
import csv , json

conCsvFilePath = "/Users/svmss/Desktop/mywork/ContactList.csv"
oppCsvFilePath = "/Users/svmss/Desktop/mywork/OpportunityList.csv"
tasCsvFilePath = "/Users/svmss/Desktop/mywork/TaskList.csv"
jsonFilePath1 = "Output1.json"
arr = []
arr1 = []
i=0
k=0
global_json =[]
opportunityFile = open(oppCsvFilePath,'r')
opportunityLines = opportunityFile.readlines()
taskFile = open(tasCsvFilePath,'r')
taskLines = taskFile.readlines()
#print(lines[0].split(','))

opportunityColumns = opportunityLines[0].split(',')
taskColumns = taskLines[0].split(',')

with open (conCsvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        for x,line in enumerate(opportunityLines):
            op_json={}
            opportunityLine = line.split(',')

            if (opportunityLine[4] or opportunityLine[6])!="" and (opportunityLine[4] or opportunityLine[6])==csvRow['Name']:
                op_json["id"]  = x
                op_json[opportunityColumns[0]] = opportunityLine[0]
                op_json[opportunityColumns[1]] = opportunityLine[1]
                op_json[opportunityColumns[2]] = opportunityLine[2]
                op_json[opportunityColumns[3]] = opportunityLine[3]
                op_json[opportunityColumns[4]] = opportunityLine[4]
                op_json[opportunityColumns[5]] = opportunityLine[5]
                op_json[opportunityColumns[6]] = opportunityLine[6]
                op_json[opportunityColumns[7]] = opportunityLine[7]
                op_json[opportunityColumns[8]] = opportunityLine[8]
                op_json[opportunityColumns[9]] = opportunityLine[9]
                op_json[opportunityColumns[10]] = opportunityLine[10]
                op_json[opportunityColumns[11]] = opportunityLine[11]
                global_json.append(op_json)
        csvRow['opportunities']=global_json
        global_json=[]

        for x,line in enumerate(taskLines):
            op_json={}
            taskLine = line.split(',')

            if taskLine[8]!="" and (taskLine[8])==csvRow['Name']:
                op_json["id"]  = x
                op_json[taskColumns[0]] = taskLine[0]
                op_json[taskColumns[1]] = taskLine[1]
                op_json[taskColumns[2]] = taskLine[2]
                op_json[taskColumns[3]] = taskLine[3]
                op_json[taskColumns[4]] = taskLine[4]
                op_json[taskColumns[5]] = taskLine[5]
                op_json[taskColumns[6]] = taskLine[6]
                op_json[taskColumns[7]] = taskLine[7]
                op_json[taskColumns[8]] = taskLine[8]
                op_json[taskColumns[9]] = taskLine[9]
                op_json[taskColumns[10]] = taskLine[10]
                op_json[taskColumns[11]] = taskLine[11]
                global_json.append(op_json)
        csvRow['tasks']=global_json
        global_json=[]

        arr.append(csvRow)        
print(global_json)

# write the data to a json file
with open(jsonFilePath1, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))

opportunityFile.close()
taskFile.close()

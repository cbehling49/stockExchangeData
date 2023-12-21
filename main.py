"""
Project Name: Stock Exchange Data
Author: Cody Behling
Due Date: 11/01/2020
Course: CS1400-X01

My program is to read through provided file data and sort out the highest/lowest values for each company.
It also must locate the overall highest and lowest values and identify which company those values belong to.
It will output this data in a new text file and print it to the console.
I learned to use optional parameters in functions and to use f-string formatting.
"""


import csv


# find the max for each company and the overall max
def findMax(maxList, company):
    maxValue = 0
    maxRow = []
    for findTheMax in maxList:
        if company == '':
            if float(findTheMax[2]) > maxValue:
                maxValue = float(findTheMax[2])
                maxRow = findTheMax
        else:
            if company == findTheMax[0]:
                if float(findTheMax[2]) > maxValue:
                    maxValue = float(findTheMax[2])
                    maxRow = findTheMax
    return maxValue, maxRow


# find the min for each company and the overall min
def findMin(minList, company):
    counter = 0
    minValue = 0
    minRow = []
    for findTheMin in minList:
        if company == '':
            if counter == 0:
                minValue = float(findTheMin[2])
                minRow = findTheMin
            elif float(findTheMin[2]) < minValue:
                minValue = float(findTheMin[2])
                minRow = findTheMin
            counter += 1
        else:
            if company == findTheMin[0]:
                if counter == 0:
                    minValue = float(findTheMin[2])
                    minRow = findTheMin
                elif float(findTheMin[2]) < minValue:
                    minValue = float(findTheMin[2])
                    minRow = findTheMin
                counter += 1
    return minValue, minRow


def main():
    companies = []
    dataList = []
    # read CSV file
    with open('stocks_data.csv', 'r') as stockData:
        stockReader = csv.reader(stockData, delimiter=',')
        if stockData != 'stocks_data.csv':
            print(f"file {stockData} does not exist.")
        # write TXT file
        with open('stock_summary.txt', 'w') as outputFile:
            for row in stockReader:
                company = row[0]
                dataList.append(row)
                if company not in companies:
                    companies.append(company)
            # format output
            companies.pop(0)
            dataList.pop(0)

            overallMax = []
            overallMin = []
            for company in companies:
                mean = 0
                counter = 0
                # call functions
                max, maxRow = findMax(dataList, company)
                min, minRow = findMin(dataList, company)
                # find the mean
                for data in dataList:
                    if company == data[0]:
                        counter += 1
                        mean += float(data[2])
                mean = mean / counter
                # write to text file
                overallMax.append(maxRow)
                overallMin.append(minRow)
                outputFile.write(company)
                outputFile.write('\n----\n')
                outputFile.write(f"Max: {max} {maxRow[1]}\n")
                outputFile.write(f"Min: {min} {minRow[1]}\n")
                outputFile.write(f"Ave: {mean}\n\n")
                # print to console
                print(company)
                print('----')
                print(f"Max: {max} {maxRow[1]}")
                print(f"Min: {min} {minRow[1]}")
                print(f"Ave: {mean}\n")
            # call functions
            maxValue, maxRow = findMax(overallMax, '')
            minValue, minRow = findMin(overallMin, '')
            # write to text file
            outputFile.write(f"Highest: {maxRow[0]} {maxRow[1]} {maxRow[2]}\n")
            outputFile.write(f"Lowest: {minRow[0]} {minRow[1]} {minRow[2]}")
            # print to console
            print(f"Highest: {maxRow[0]} {maxRow[1]} {maxRow[2]}")
            print(f"Lowest: {minRow[0]} {minRow[1]} {minRow[2]}")


if __name__ == "__main__":
    main()

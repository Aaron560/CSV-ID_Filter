"""
Date: 3/9/21
Program: Exam
"""
import csv, random
def Insertionsort(data):
            for i in range(1, len(data)): 
                    k = data[i]
                    j = i-1
                    while j >= 0 and k < data[j]: 
                            data[j + 1] = data[j] 
                            j -= 1
                    data[j + 1] = k

def binary_search(sequence, item):
            begin_index = 0
            end_index = len(sequence) - 1
            
            while begin_index <= end_index:
                midpoint = begin_index + (end_index - begin_index) // 2
                midpoint_value = sequence[midpoint][0]
                
                if midpoint_value == item:
                    return sequence[midpoint]

                elif item < midpoint_value:
                    end_index = midpoint - 1

                else:
                    begin_index = midpoint + 1

            return None

def main():
    try:
        with open('EmployeeList.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            arr = []
            for line in csv_reader:
                arr.append(line)
            Insertionsort(arr)
            print(arr)
        
        while (True):
            forward = input("Continue (Y)es or (N)o: ").upper()
            
            if forward == "N":
                break
            
            else:
                AskID = input("Enter a ID number you want to search for in the list: ")
                Item = AskID
                
                while len(AskID) != 7:
                    try:
                        ID = input("Please enter the customer's ID Number: ")
                    except ValueError:
                        item_list_a = ""
                    Item.append(ID)
                Employee = binary_search(arr, Item)
                rank = {'1': 'Intern', '2': 'New-Full-time hire', '3': 'Associate', '4': 'Assistant Manager', '5': 'Manager'}
                print("ID: " + Employee[0])
                print("Name: "+ Employee[1]+ " " + Employee[2])
                print("Phone: " + Employee[3])
                print("SSN: " + Employee[4])
                print("Address: " + Employee[5])
                print("Rank: " + rank[Employee[6]])
                print("Salary: " + Employee[7])
       
    except:
        print("Restarting.......")
        input("")
        main()

main()


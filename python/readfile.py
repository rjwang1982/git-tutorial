#open("employees.txt","r")
#open("employees.txt","w")
#open("employees.txt","a")
#open("employees.txt","r+")

employee_file = open("/Users/Ethan/BaiduYun/GeoSwift/SFTP/python/employees.txt","r")
print(employee_file.readable())
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines()[1])

employee_file.close()
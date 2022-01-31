#use database
use IT_Department;
Select * from employee;
#print Employee_Name four letter
select * from employee where  Employee_Name =(select Employee_Name from employee where Employee_Id="108");
#create database
create database IT_Department;
use IT_Department;
create table Employee(Employee_Name varchar(20),Employee_Id int, Employee_Dept varchar(20));
#describe scheme
describe Employee;
#insert into table
insert into Employee values("Vijay",108,"IT");
insert into Employee values("Ram",109,"CSE");
insert into Employee values("Suresh",1010,"Robo");
insert into Employee values("Mahesh",1082,"HR");
insert into Employee values("Kalpana",1089,"AU");
select * from Employee;
select distinct Employee_Name from Employee;

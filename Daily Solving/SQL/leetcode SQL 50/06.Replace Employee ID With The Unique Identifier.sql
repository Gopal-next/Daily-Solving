select UNI.unique_id, e.name from Employees as e
left join EmployeeUNI as UNI
on e.id = UNI.id;
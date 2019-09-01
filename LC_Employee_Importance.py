"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, ID):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        
        Approach:
        
        Have a dict to store all the employee information and recursively add them up if one particular employee has 
        a subordinate and that employee has a subordinate and so on.
        
        """
        if not employees:
            return(0)
        d = dict()
        sub = dict()
        total = 0
        
        for emp in employees:
            d[emp.id] = emp.importance
            sub[emp.id] = emp.subordinates
        
        def calc_total(ID):
            total = d[ID]
            for sub_id in sub[ID]:
                total += calc_total(sub_id)
            return(total)
        
        return(calc_total(ID))
                    
                    

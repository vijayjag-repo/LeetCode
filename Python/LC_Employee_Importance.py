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
# DFS Approach
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int

        Straightforward. If the class definition were to have a list of employees in subordinates, we needn't use dictionary.

        Time complexity: O(m), where m = total number of subordinates under a given employee
        Space complexity: O(n), where n = total number of employees (since we're storing all employees in a map)
        """
        def dfs(employee):
            subordinates_importance = 0

            if len(employee.subordinates) == 0:
                return employee.importance
            else:
                for reportee_id in employee.subordinates:
                    subordinates_importance += dfs(d[reportee_id])
            return subordinates_importance + employee.importance

        d = dict()
        for employee in employees:
            d[employee.id] = employee

        return dfs(d[id])

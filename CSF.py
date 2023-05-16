def solve_csp(variables, domains, constraints):
    assignment = {}

    def backtrack():
        if len(assignment) == len(variables):
            return assignment

        var = select_unassigned_variable()
        for value in order_domain_values(var):
            if is_consistent(var, value):
                assignment[var] = value
                result = backtrack()
                if result is not None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable():
        for var in variables:
            if var not in assignment:
                return var

    def order_domain_values(var):
        return domains[var]

    def is_consistent(var, value):
        for constraint in constraints:
            if var in constraint:
                other_var = constraint[0] if constraint[0] != var else constraint[1]
                if other_var in assignment and (assignment[other_var] == value or assignment[other_var] + value == 10):
                    return False
        return True

    return backtrack()


# Example usage
variables = ['A', 'B', 'C', 'D']
domains = {'A': [1, 2, 3, 4], 'B': [1, 2, 3, 4], 'C': [1, 2, 3, 4], 'D': [1, 2, 3, 4]}
constraints = [('A', 'B'), ('B', 'C'), ('C', 'D')]

solution = solve_csp(variables, domains, constraints)
if solution:
    print("Solution found:")
    for var, value in solution.items():
        print(var, "=", value)
else:
    print("No solution found.")

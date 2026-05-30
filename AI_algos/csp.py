jobs = ['J1', 'J2', 'J3'] 
workers = ['W1', 'W2', 'W3'] 
 
constraints = { 
    'W1': ['J3'], 
    'W2': ['J1'], 
    'W3': [] 
} 

def is_valid(assignment, workers, jobs): 
    if job in constraints.get(workers, []): 
        return False
    if job in assignment.values(): 
        return False
    return True 
 
def backtrack(assignment, workers, jobs, solutions): 
    if len(assignment) == len(workers): 
        solutions.append(assignment.copy()) 
        return 
 
    worker = workers[len(assignment)] 
    for job in jobs: 
        if is_valid(assignment, worker, job): 
            assignment[worker] = job 
            backtrack(assignment, workers, jobs, solutions) 
            del assignment[worker] 
 
def find_all_solutions(workers, jobs): 
    solutions = [] 
    assignment = {} 
    backtrack(assignment, workers, jobs, solutions) 
    return solutions 

#main
solutions = find_all_solutions(workers, jobs) 
 
if solutions: 
    print("All possible solutions:") 
    for solution in solutions: 
        print(solution) 
else: 
    print("No valid solution is possible.")








# other code
courses = ['C1', 'C2', 'C3', 'C4', 'C5'] 
time_slots = ['Morning', 'Afternoon', 'Evening'] 
 
constraints = { 
    'C1': ['C2'], 
    'C2': ['C1', 'C3'], 
    'C3': ['C2', 'C4'], 
    'C4': ['C3', 'C5'], 
    'C5': ['C4'] 
} 
 
def is_valid(assignment, course, slot): 
     
    for neighbor in constraints.get(course, []): 
        if neighbor in assignment and assignment[neighbor] == slot: 
            return False 
 
    count = 0 
    for c in assignment: 
        if assignment[c] == slot: 
            count += 1 
    if count >= 2: 
        return False 
 
    return True 
 
def backtrack(assignment): 
    if len(assignment) == len(courses): 
        return assignment 
 
    course = courses[len(assignment)] 
    for slot in time_slots: 
        if is_valid(assignment, course, slot): 
            assignment[course] = slot 
            result = backtrack(assignment) 
            if result: 
                return result 
            del assignment[course] 
 
    return None 
 
solution = backtrack({}) 
 
if solution: 
    print("Valid Exam Schedule:") 
    print(solution) 
else: 
    print("No valid schedule found.")

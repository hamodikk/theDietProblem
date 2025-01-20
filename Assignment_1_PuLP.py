from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Names of the five food items
foods = ["Devanco_Beef_Bacon", "Chicken_Breats", "Kerrygold_Butter", "O_Organics_Quinoa", "Cocoa_Puffs_Cereal"]

# Define the weekly nutritional requirements (daily values multiplied by 7)
weekly_requirements = {
    "sodium": ("max", 5000 * 7),   # mg/week
    "energy": ("min", 2000 * 7),   # kcal/week
    "protein": ("min", 50 * 7),    # g/week
    "vitamin_d": ("min", 20 * 7),  # mcg/week
    "calcium": ("min", 1300 * 7),  # mg/week
    "iron": ("min", 18 * 7),       # mg/week
    "potassium": ("min", 4700 * 7)   # mg/week
}

# Nutritional values of each packaged item
nutritional_data = {
    "sodium": [270, 74, 0, 0, 130],
    "energy": [45, 165, 100, 170, 140],
    "protein": [5, 31, 0, 6, 2],
    "vitamin_d": [0, 0, 0, 0, 4],
    "calcium": [2, 11, 0, 20, 130],
    "iron": [0, 1, 0, 2.1, 3.6],
    "potassium": [58, 0, 0, 250, 10]
}

# Define the cost per serving for each packaged item
costs = [0.85, 0.46, 0.37, 0.7, 0.85]

# Define the LP Problem
problem = LpProblem("Weekly_Diet_Minimum_Cost", LpMinimize)

# Define the decision variables
x = LpVariable.dicts("servings", foods, lowBound = 0)

# Define the objective function: Minimize the total cost
problem += lpSum(costs[i] * x[food] for i, food in enumerate(foods)), "Total_Cost"

# Add the constraints for each packaged item
for nutrient, (constraint_type, limit) in weekly_requirements.items():
    if constraint_type == "max":
        problem += lpSum(nutritional_data[nutrient][i] * x[food] for i, food in enumerate(foods)) <= limit, f"{nutrient}_constraint"
    elif constraint_type == "min":
        problem += lpSum(nutritional_data[nutrient][i] * x[food] for i, food in enumerate(foods)) >= limit, f"{nutrient}_constraint"
        
# Add the constraint that requires at least one serving for each packaged item
# These two lines of code are for the revised version with added constraint for non-zero servings
for food in foods:
    problem += x[food] >= 1, f"Min_Serving_{food}"

# Solve the problem
problem.solve()

print("Optimal servings for each food item for minimum cost:")
for food in foods:
    print(f"{food}: {x[food].value()} servings")
    
print(f"\nTotal weekly cost: ${problem.objective.value():.2f}")
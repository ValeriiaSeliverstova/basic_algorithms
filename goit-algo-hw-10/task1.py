from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
model = LpProblem("Production_Optimization", LpMaximize)

# Define variables
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Constraints based on available resources
model += 2 * lemonade + 1 * fruit_juice <= 100  # Water constraint
model += 1 * lemonade <= 50                     # Sugar constraint
model += 1 * lemonade <= 30                     # Lemon juice constraint
model += 2 * fruit_juice <= 40                  # Fruit puree constraint

# Objective: Maximize total production (lemonade + fruit juice)
model += lemonade + fruit_juice

# Solve the problem
model.solve()

# Results
print("Optimal Production Plan:")
print(f"Lemonade: {lemonade.varValue}")
print(f"Fruit Juice: {fruit_juice.varValue}")
print(f"Total Production: {lemonade.varValue + fruit_juice.varValue}")

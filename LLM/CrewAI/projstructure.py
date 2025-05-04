import os

structure = [
    "recipe_generator/.gitignore",
    "recipe_generator/pyproject.toml",
    "recipe_generator/README.md",
    "recipe_generator/.env",
    "recipe_generator/src/recipe_crew/__init__.py",
    "recipe_generator/src/recipe_crew/main.py",
    "recipe_generator/src/recipe_crew/crew.py",
    "recipe_generator/src/recipe_crew/tools/__init__.py",
    "recipe_generator/src/recipe_crew/tools/custom_tool.py",
    "recipe_generator/src/recipe_crew/config/agents.yaml",
    "recipe_generator/src/recipe_crew/config/tasks.yaml",
]

for path in structure:
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        pass
print("Project Structure Created Successfully")
    
    

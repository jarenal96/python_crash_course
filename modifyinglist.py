
# Start by creating a function to simulate printing each design.

def print_models(unprinted_designs, completed_designs):
    """Simulate printing each design until none are left."""

    # Simulate printing each design, until none are left
    # Move each design to complete_models after printing
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}...")
        completed_designs.append(current_design)


def show_completed_models(completed_designs):
    """ Show all the models that were printed"""
    # Display all completed models
    print("\nCompleted models:")

    for completed_design in completed_designs:
        print(completed_design)

# Define the designs

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []

print_models(unprinted_designs[:],completed_designs)
show_completed_models(completed_designs)
print(unprinted_designs)
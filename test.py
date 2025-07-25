import inspect

def test(first_argument, second_argument):
    print(first_argument)

# Get the first parameter name
sig = inspect.signature(test)
first_param_name = list(sig.parameters.keys())
print(f"First parameter name: '{first_param_name}'")  # Output: 'first_argument'

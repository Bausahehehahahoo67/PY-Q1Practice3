from pyscript import document, pyscript

def adding_numbers(e):
    document.getElementById('output').innerHTML = "" # clears previous output
    num1 = float(document.getElementById('neckhurts').value) # get 1st input
    num2 = float(document.getElementById('aurafarm').value)  # get 2nd input
    result = num1 + num2
    document.getElementById('outputs').innerHTML = f"The sum is: {result}"
from pyscript import document, display

def adding_numbers(e):
    document.getElementById('output').innerHTML = "" # clears previous output
    num1 = float(document.getElementById('neckhurts').value) # get 1st input
    num2 = float(document.getElementById('aurafarm').value)  # get 2nd input
    result = num1 + num2 # use operator to compute
    display(result, target = 'output') #display result
from pyscript import document, display

def adding_numbers(e):
    document.getElementById('output').innerHTML = "" # clears previous output
    num1 = float(document.getElementById('neckhurts').value) # get 1st input
    num2 = float(document.getElementById('aurafarm').value)  # get 2nd input
    result = num1 + num2 # use operator to compute
    display(result, target = 'output') #display result

def create_order(e): 
    prod1 = document.getElementById('item1')
    # Calculate
    subtotal = float(prod1.value) * prod1.checked
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)
    grandtotal = subtotal + size_price
    display(grandtotal, target = 'output2')

def create_order2(e):
    milo = document.getElementById('output3').innerHTML = "" #clears previous
    milo = document.getElementById('milo')
    milo_value = float(milo.value)
    display(milo_value, target = 'output3')
from pyscript import document, pyscript

        def adding_numbers(e):
        document.getElementById("input1").InnerHTML = ""
        num1 = float(document.getElementById("input1").value)
        num2 = float(document.getElementById("input2").value)
        result = num1 + num2
        display("result", target="output1")
        </script>
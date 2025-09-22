from pyscript import display, document

display()
def ave(e): #e for event handler
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)
#solution
    average = (num1 + num2) / 2

    if average >= 75:
        result = f"Average: {average:.2f}. Passed!"

    else:
        result = f"Average: {average:.2f}. Failed."     


    display(result, target="output1")

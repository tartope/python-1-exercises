def calc_total(arr, tax):
    # Create a variable for the result and set to zero
    # result = 0
    # Loop through the array
    # for num in arr:
        # Add number casted to float to result
        # result += float(num)
    # Add result and tax(remove the % sign) and divide by 10
    # result = result + float(tax[:-1]) / 10
    # result = result * (1+ float(tax[:-1])/100)
    # Return result


    # Sum all the numbers in the array
    total = sum(arr)
    # Find the tax percent by stripping the percent sign from the tax string
    tax_percent = float(tax.strip("%")) /100
    # Add total to total * 
    total_with_tax = total + (total * tax_percent)
    formatted_total = "${:,.2f}".format(total_with_tax)
    return formatted_total
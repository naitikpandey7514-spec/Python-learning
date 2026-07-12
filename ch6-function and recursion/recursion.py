#recursion

"""recursion is a programming technique in which function keep
 calling itself in simple and smaller part until the stopping
   condition, called base case is reched. """

#syntax of recursion

#def function_name(parameters):
#   if base_case_condition:
#       return base_case_value
#   else:
#       return function_name(modified_parameters)


#example of recursion

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
    
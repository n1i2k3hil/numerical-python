from scipy import integrate

result, error = integrate.quad(lambda x: x**2, 0, 3)

print("Integration:", result)

print()
print("* ENGINEERING TOOLKIT v1 *")
print()

# Fixed syntax typos like T' and missing closing brackets
conversions_available = [
    (1, 'km', 'mi'),
    (2, 'mi', 'km'),
    (3, 'kg', 'lbs'),
    (4, 'lbs', 'kg'),
    (5, '°F', '°C'),
    (6, '°C', '°F')
]

print('Conversions available:')
print()

# Fixed the f-string curly bracket syntax errors
for conversion_number, from_unit, to_unit in conversions_available:
    print(f'{conversion_number}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter the number of the conversion to use --> ')
conversion_index = int(conversion) - 1

# Pulling the chosen conversion details from the list
chosen_conversion = conversions_available[conversion_index]
conversion_number, from_unit, to_unit = chosen_conversion

print()
value_to_convert = float(input(f'Enter the value in {from_unit}: '))

# Performing calculations based on user selection
if conversion_number == 1:
    # Kilometers to Miles
    converted_value = value_to_convert * 0.621371
elif conversion_number == 2:
    # Miles to Kilometers
    converted_value = value_to_convert / 0.621371
elif conversion_number == 3:
    # Kilograms to Pounds
    converted_value = value_to_convert * 2.20462
elif conversion_number == 4:
    # Pounds to Kilograms
    converted_value = value_to_convert / 2.20462
elif conversion_number == 5:
    # Fahrenheit to Celsius
    converted_value = (value_to_convert - 32) * 5 / 9
elif conversion_number == 6:
    # Celsius to Fahrenheit
    converted_value = (value_to_convert * 9 / 5) + 32

print(f'{value_to_convert} {from_unit} is equal to {converted_value:.2f} {to_unit}')

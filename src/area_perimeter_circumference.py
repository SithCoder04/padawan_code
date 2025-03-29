import sys

while True:
	# import information from the user
	print('Which figure''s information whould you like to see : circle (C) or rectangle (R): ')
	print('Press:\nc for circle\nr fpr rectangle')
	user_input = input()
	user_input = user_input.lower()

	# see what information the user wants to view in the circle and rectangle
	# when the user wants to see the information of circle
	if user_input == 'c':
		# check if the user wants to view the circumference or area of the cicle and import the required information
		circle_input = input('Whould you like to see the circumference or area of the circle?')
		circle_input = str(circle_input)
		# import the radius from the user
		radius = input('Enter the radius of the circle : ')
		radius = int(radius)
		# declare that pi = 22 divided by 7
		pi = float(22) / 7
		# if the user wants to view the circumference of the circle
		if circle_input == 'circumference':
			circumference = 2 * pi * radius
			print('Circumference of the circle = {}'.format(circumference))
		# if the user wants to view the area of the circle
		else:
			area = pi * radius * radius
			print('Area of the circle = {}'.format(area))
	# when the user wants to see the information of rectangle
	elif user_input == 'r':
		# import the length from the user
		length = input('Enter the length of the rectangle : ')
		length = float(length)
		# import the breadth from the user
		breadth = input('Enter the breadth of the rectangle : ')
		breadth = float(breadth)
		rect_input = input('Whould you like to see the perimeter or area of the rectangle?')
		rect_input = str(rect_input)
		# when the user wants to see the perimeter of the rectangle
		if rect_input == 'perimeter':
			perimeter = 2 * (length + breadth)
			print('The perimeter of the rectangle is : {}'.format(perimeter))
		# when the user wants to see the area of the rectangle
		else:
			area = length * breadth
			print('The area of the rectangle is : {}'.format(area))
		# end if
	else:
		print('Unrecognised input')
	# end if
# end while


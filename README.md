This is a README file for calo_calculator

Calo_Calculator for calculating person's calrories needed per day based on the following:
1. Gender
2. Age
3. Weight
4. Height
5. Activity level

How to use it:
1. Import the package: from Calo import Calo
2. To define an object of type "Calo", you must provide Gender, Age, Weight, and Height as follow:
	person = Calo("female", 30, 55, 160)
    where:
    gender mush be either male or female.
    age must be an integer number from 10 to 100.
    weight and height are float numbers.
3. Then to use the calculator, call the following methos:
	person.calculate_calo(active_level)
    where:
    activity level is an integer from 1 to 5 representing person's activity lever
    	(1) for Sedentary (limited exercise)
        (2) for Lightly active (light exercise less than three days per week)
        (3) for Moderately active (moderate exercise most days of the week)
        (4) Very active (hard exercise every day)
        (5) Extra active (strenuous exercise two or more times per day)
        
What is next?
1. Calculating calories based on person's goal: healthy, diet, cutting, bulking
2. Calculating the macros (proties, carbs, and fats)
3. Calculating the ideal weight range for a person.
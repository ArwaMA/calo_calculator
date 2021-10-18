class Calo:
    """ Calo class for calculating daily calorie intake of a person
         based on his need.
        
        Attributes:
        genter (string) represnting the gender of a person (male or female)
        age (integer) representing the age of a person
        weight (float) represnting person's weight in kg
        height (float) represnting person's height in cm
    """
    
    def __init__(self, gender, age, weight, height):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        
        
    def calculate_bmr(self):
        """ Function to calculate person's BMR
        
        Args: 
			none
		
		Returns: 
			float: BMR - Basal Metabolic Rate
        """
        mbr = 0
        if self.gender.lower() == "male":
            mbr = (self.weight * 10) + (self.height * 6.25) - (self.age * 5) + 5
        else:
            mbr = (self.weight * 10) + (self.height * 6.25) - (self.age * 5) - 161
        
        return mbr
    
    def calculate_total_calo(self, bmr, activ_level):
        """ Function to calculate person's total calories 
            based on his/her activity level
        
        Args: 
            bmr (float) representing person's daily BMR
			active_level (integer) represening person's active level (from 1 to 4)
		
		Returns: 
			float: calo - person's daily total calories
        """
        if activ_level == 1:
            return bmr * 1.25
        elif activ_level == 2:
            return bmr * 1.375
        elif activ_level == 3:
            return bmr * 1.550
        elif activ_level == 4:
            return bmr * 1.725
        else:
            return 0
        
    def calculate_calo(self, active_level):
        
        """Function to calculate person's daily intake of food 
           based on Mifflin-St Jeor Equation
        
        Args: 
			active_level (integer) represening person's active level (from 1 to 4)
		
		Returns: 
			float: daily calories
        """
        #check_gender()
        #check_age()
        #check_weight()
        #check_height()
        bmr = self.calculate_bmr()
        calo = self.calculate_total_calo(bmr, active_level)
        
        return round(calo, 2)
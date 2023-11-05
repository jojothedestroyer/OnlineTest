from django.db import models
import random


def land_id():
    return str(random.randint(10000, 999999999999))

class crop(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class fullform(models.Model):

    trees = [
        ('', '--Select an option--'),

        ('Nutmeg', 'Nutmeg'),
        ('Coconut', 'Coconut'),
    ]
    farmer_ID = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    village = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True)
    GPS_location = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=50,null=True)
    age_range = [('A', '18-25'),('B', '26-35'),('C', '36-60'),('D', '61+'),]
    age = models.CharField(max_length=1, choices=age_range, default='A')
    titles = models.CharField(max_length=50, null=True)
    family = models.CharField(max_length=50, null=True)
    lease = models.CharField(max_length=100, null=True)
    caretaker = models.CharField(max_length=50, null=True)
    agent = models.CharField(max_length=50, null=True)
    comments = models.TextField(blank=True)
    Tree_types = models.CharField(max_length=50,choices=trees, default='A')
    Mature_trees = models.IntegerField(default= 0)
    Bearing_trees = models.IntegerField(default= 0)
    NonBearing_trees = models.IntegerField(default= 0)

    LAND_ELEVATION = [
        ('', '--Select an option--'),
        ('Low Belt', 'Low Belt'),
        ('Middle Belt', 'Middle Belt'),
        ('High Belt', 'High Belt'),        
    ]
    SOIL_TYPE = [
        ('', '--Select an option--'),
        ('Sandy Soil', 'Sandy Soil'),
        ('Clay Soil', 'Clay Soil'),
        ('Stilt Soil', 'Stilt Soil'),
        ('Peat Soil', 'Peat Soil'),
        ('Chalk Soil', 'Chalk Soil'),
        ('Loamy Soil', 'Loamy Soil'),
        ('Clay Loam Soil', 'Clay Loam Soil'),
        ('Sandy Loam Soil', 'Sandy Loam Soil'),

    ]
    RAINFALL_PATTERN = [
        ('', 'Select'),
        ('Persistent', 'Persistent'),
        ('Occasional', 'Occasional'),
        ('Mild', 'Mild'),
    ]
    land_elevation = models.CharField(max_length=100, choices=LAND_ELEVATION, default='P')
    soil_type = models.CharField(max_length=100, choices=SOIL_TYPE, default='P')
    rainfall_pattern = models.CharField(max_length=100, choices=RAINFALL_PATTERN, default='P')
    other_crops = models.ManyToManyField(crop)
    intercrop = models.CharField(max_length=50, null=True)
    pure_stand = models.CharField(max_length=50, null=True)
    norm_land = models.CharField(max_length=50, null=True)
    seas_land = models.CharField(max_length=50, null=True)
    aban_land = models.CharField(max_length=50, null=True)


    TREATED_WATER = [
        ('', 'Select'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    WATER_SOURCE = [
        ('', 'Was this water source is used?'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    road_access = models.CharField(max_length=50, null=True)
    land_slide = models.CharField(max_length=50, null=True)
    flooding = models.CharField(max_length=50, null=True)
    heavy_metals = models.CharField(max_length=50, null=True)
    chemical_spills = models.CharField(max_length=50, null=True)
    dumping = models.CharField(max_length=50, null=True)
    feedlot = models.CharField(max_length=50, null=True)
    pesticides = models.CharField(max_length=50, null=True)
    septic_tanks = models.CharField(max_length=50, null=True)
    manical = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    river = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    spring = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    well = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    harvested = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    treated = models.CharField(max_length=1, choices=TREATED_WATER, default='P')
    annual_production = models.CharField(max_length=50, null=True)
    peak_productions = models.CharField(max_length=50, null=True)
    inspected_by = models.DateField('Inspection Date',null=True)
    date = models.DateField('Current Date',null=True)


    def __str__(self):
        return self.farmer_ID







# class Moisture_Analysis_A(models.Model):

#     # Section A
#     DATE_OF_SAMPLING = models.DateField('Current Date',null=True)
#     STATION= models.CharField(max_length=50, null=True)
#     BATCH_CODE= models.IntegerField(default= 0)
#     Quantity_of_Bags= models.IntegerField(default= 0)
#     Quantity_of_Sample= models.IntegerField(default= 0)
#     Total_Weight = models.FloatField(default= 0)
#     Initial_Sample_Weight= models.FloatField(default= 0)
#     # Weight 
#     Insect_Damaged = models.FloatField(default= 0)
#     Broken= models.FloatField(default= 0)
#     Mould= models.FloatField(default= 0)
#     Final_Sample_Weight= models.FloatField(default= 0)


#     # MOISTURE CONTENT RESULTS (%)


#     # CRITERIA 

#     READING_1= models.CharField(max_length=50, null=True)
#     READING_2= models.CharField(max_length=50, null=True)
#     READING_3 = models.CharField(max_length=50, null=True)
#     AVERAGE= models.CharField(max_length=50, null=True)
#     DECISION = models.CharField(max_length=50, null=True)
#     Comments = models.TextField(blank=True)
#     TEST_PERFORMED_BY = models.CharField(max_length=50, null=True)
#     DATE= models.DateField('Current Date',null=True)
#     SIGNED_BY = models.CharField(max_length=50, null=True)
#     DATE_OF_REPORT= models.DateField('Current Date',null=True)

#     # CHECKED BY QA OFFICER

#     SIGNED_BY_QUALITY_ASSURANCE_OFFICER = models.CharField(max_length=50, null=True)
#     DATE= models.DateField('Current Date',null=True)




#     def __str__(self):
#         return self.BATCH_CODE



class Dried_Moisture_Analysis_A(models.Model):

    DECISION_MADE = [
        ('', 'What was the decision made?'),
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    ]


    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)





    # Section A
    DATE_OF_SAMPLING = models.DateField('Date of Sampling',null=True)
    STATION= models.CharField(max_length=50, null=True)
    BATCH_CODE= models.IntegerField(default= 0)
    Quantity_of_Bags= models.IntegerField(default= 0)
    Quantity_of_Sample= models.IntegerField(default= 0)
    Total_Weight = models.FloatField(default= 0)
    Initial_Sample_Weight= models.FloatField(default= 0)
    # Weight 
    Insect_Damaged = models.FloatField(default= 0)
    Broken= models.FloatField(default= 0)
    Mould= models.FloatField(default= 0)
    Final_Sample_Weight= models.DecimalField(default= 0,decimal_places=2,max_digits= 30)


    # MOISTURE CONTENT RESULTS (%)


    # CRITERIA 

    READING_1= models.CharField(max_length=50, null=True)
    READING_2= models.CharField(max_length=50, null=True)
    READING_3 = models.CharField(max_length=50, null=True)
    AVERAGE= models.CharField(max_length=50, null=True)
    DECISION = models.CharField(max_length=50,choices=DECISION_MADE,null=True)
    Comments = models.TextField(blank=True)
    TEST_PERFORMED_BY = models.CharField(max_length=50, null=True)
    DATE= models.DateField('Current Date',null=True)
    APPROVED_BY = models.CharField(max_length=50, null=True)
    DATE_OF_REPORT= models.DateField('Date of Report',null=True)

    # CHECKED BY QA OFFICER

    SIGNED_BY_QUALITY_ASSURANCE_OFFICER = models.CharField(max_length=50, null=True)
    DATE= models.DateField('Current Date',null=True)



    def __str__(self):
        return self.STATION



class Dried_Moisture_Analysis_B(models.Model):

    Stations = [
        ('', 'Select Station'),
        ('Beaulieu', 'Beaulieu'),
        ('Gouyave', 'Gouyave'),
        ('Grenville', 'Grenville'),
    ]

    DECISION_MADE = [
        ('', 'What was the decision made?'),
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    ]
    
    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)
    # Section B

    # Corrective Action for Nutmeg Above 10% Moisture Content
    # Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)

    DATE_OF_SAMPLING = models.DateField('Date of Sampling',null=True) 
    STATION = models.CharField(max_length=50, null=True)
    BATCH_CODE = models.IntegerField(default= 0)
    Total_Quantity_of_Bags_in_Non_Compliance = models.IntegerField(default= 0)
    Total_Weight_of_Nutmeg_in_Non_Compliance = models.IntegerField(default= 0)
    Additional_Drying_Period1 = models.CharField(max_length=50, null=True,blank=True)
    Additional_Drying_Period2 = models.CharField(max_length=50, null=True,blank=True)
    Additional_Drying_Period3 = models.CharField(max_length=50, null=True,blank=True)
    Initial_Sample_Weight = models.FloatField(default= 0)
    # Weight (oz/lbs)
    Insect_Damaged = models.FloatField(default= 0)
    Broken= models.FloatField(default= 0)
    Mould= models.FloatField(default= 0)
    Final_Sample_Weight= models.DecimalField(default= 0,decimal_places=2,max_digits= 30)

    # MOISTURE CONTENT RESULTS (%)     

    READING_1 = models.CharField(max_length=50, null=True)
    READING_2 = models.CharField(max_length=50, null=True)
    READING_3 = models.CharField(max_length=50, null=True)
    AVERAGE = models.DecimalField(default= 0,decimal_places=2,max_digits= 200)
    DECISION = models.CharField(max_length=50,choices=DECISION_MADE,null=True)
    Comments = models.TextField(blank=True) 
    TEST_PERFORMED_BY  = models.CharField(max_length=50, null=True)
    APPROVED_BY  = models.CharField(max_length=50, null=True)
    DATE_OF_REPORT = models.DateField('Date of Report',null=True)
    SIGNED_BY_QUALITY_ASSURANCE_OFFICER = models.CharField(max_length=50, null=True)
    DATE = models.DateField('Current Date',null=True)
        



    # def __str__(self):
    #     return self.STATION




class Floated_Moisture_Analysis_A(models.Model):


    DECISION_MADE = [
        ('', 'What was the decision made?'),
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    ]

    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)



    # Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)

    DATE_OF_SAMPLING_H = models.DateField('Date of Heavy Sampling',null=True) 
    DATE_OF_SAMPLING_L = models.DateField('Date of Light Sampling',null=True) 
    STATION = models.CharField(max_length=50, null=True)
    BATCH_CODE = models.IntegerField(default= 0)

    # HEAVIES
    Quantity_of_Sample_H = models.IntegerField(default= 0)
    Total_Weight_H = models.FloatField(default= 0)
    Initial_Sample_Weight_H = models.DecimalField(default= 0,decimal_places=2,max_digits= 30)

    # LIGHTS
    Quantity_of_Sample_L = models.IntegerField(default= 0)
    Total_Weight_L = models.FloatField(default= 0)
    Initial_Sample_Weight_L = models.DecimalField(default= 0,decimal_places=2,max_digits= 30)


    # Weight 

    # HEAVIES
    Insect_Damaged_H = models.FloatField(default= 0)
    Broken_H = models.FloatField(default= 0)
    Mould_H = models.FloatField(default= 0)
    Final_Sample_Weight_H= models.DecimalField(default= 0,decimal_places=2,max_digits= 30)


    # LIGHTS
    Insect_Damaged_L = models.FloatField(default= 0)
    Broken_L = models.FloatField(default= 0)
    Mould_L = models.FloatField(default= 0)
    Final_Sample_Weight_L = models.DecimalField(default= 0,decimal_places=2,max_digits= 30)



    # HEAVIES
    READING_1_H = models.FloatField(default= 0)
    READING_2_H = models.FloatField(default= 0)
    READING_3_H = models.FloatField(default= 0)
    AVERAGE_H = models.DecimalField(default= 0,decimal_places=2,max_digits= 200)
    DECISION_H  = models.CharField(max_length=50,choices=DECISION_MADE, null=True)
    Comments_H = models.TextField(blank=True) 
    TEST_PERFORMED_BY_H = models.CharField(max_length=50, null=True)
    DATE_H = models.DateField('Current Date',null=True) 


    # LIGHTS
    READING_1_L = models.FloatField(default= 0)
    READING_2_L = models.FloatField(default= 0)
    READING_3_L = models.FloatField(default= 0)
    AVERAGE_L = models.DecimalField(default= 0,decimal_places=2,max_digits= 200)
    DECISION_L = models.CharField(max_length=50, choices=DECISION_MADE, null=True)
    Comments_L = models.TextField(blank=True) 
    TEST_PERFORMED_BY_L = models.CharField(max_length=50, null=True)
    DATE_L = models.DateField('Current Date',null=True) 



    Approved_BY = models.CharField(max_length=50, null=True)
    Station_Manager = models.CharField(max_length=50, null=True)
    DATE_OF_REPORT = models.DateField('Date of Report',null=True) 

    # CHECKED BY QA OFFICER
    SIGNED_BY_Quality_Assurance_Officer= models.CharField(max_length=50, null=True)
    DATE = models.DateField('Current Date',null=True) 



    # def __str__(self):
    #     return self.STATION








class Floated_Moisture_Analysis_B(models.Model):


    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)


    # Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)

    # Corrective Action for Floated Nutmeg Above 10% Moisture Content
    DATE_OF_SAMPLING_H  = models.DateField('Date of Heavy Sampling',null=True) 
    DATE_OF_SAMPLING_L = models.DateField('Date of Light Sampling',null=True) 
    STATION = models.CharField(max_length=50, null=True)

    # HEAVIES
    Total_Quantity_of_Bags_in_Non_Compliance_H  = models.IntegerField(default= 0)
    Total_Weight_of_Nutmeg_in_Non_Compliance_H = models.FloatField(default= 0)
    Additional_Drying_Period_days_H = models.IntegerField(default= 0)
    Total_Weight_H = models.FloatField(default= 0)


    # LIGHTS

    Total_Quantity_of_Bags_in_Non_Compliance_L  = models.IntegerField(default= 0)
    Total_Weight_of_Nutmeg_in_Non_Compliance_L = models.FloatField(default= 0)
    Additional_Drying_Period_days_L = models.IntegerField(default= 0)
    Total_Weight_L = models.FloatField(default= 0)


    # Weight (oz/lbs)


    # HEAVIES
    Initial_Sample_Weight_H = models.FloatField(default= 0)
    Broken_H = models.FloatField(default= 0)
    Mould_H = models.FloatField(default= 0)
    Insect_Damaged_H = models.FloatField(default= 0)
    Final_Sample_Weight_H = models.FloatField(default= 0)



    # LIGHTS
    Initial_Sample_Weight_L = models.FloatField(default= 0)
    Broken_L = models.FloatField(default= 0)
    Mould_L = models.FloatField(default= 0)
    Insect_Damaged_L = models.FloatField(default= 0)
    Final_Sample_Weight_L = models.FloatField(default= 0)




    # HEAVIES

    READING_1_H = models.FloatField(default= 0)
    READING_2_H = models.FloatField(default= 0)
    READING_3_H = models.FloatField(default= 0)
    AVERAGE_H = models.FloatField(default= 0)
    DECISION_H = models.CharField(max_length=50, null=True)
    Comments_H = models.TextField(blank=True) 
    TEST_PERFORMED_BY_H = models.CharField(max_length=50, null=True)
    DATE_H = models.DateField('Current Date',null=True) 



    # LIGHTS
    READING_1_L = models.FloatField(default= 0)
    READING_2_L = models.FloatField(default= 0)
    READING_3_L = models.FloatField(default= 0)
    AVERAGE_L = models.FloatField(default= 0)
    DECISION_L = models.CharField(max_length=50, null=True)
    Comments_L = models.TextField(blank=True) 
    TEST_PERFORMED_BY_L = models.CharField(max_length=50, null=True)
    DATE_L = models.DateField('Current Date',null=True) 




    SIGNED_BY = models.CharField(max_length=50, null=True)
    Station_Manager = models.CharField(max_length=50, null=True)
    DATE_OF_REPORT = models.DateField('Date of Report',null=True) 


    # CHECKED BY QA OFFICER

    SIGNED_BY_Quality_Assurance_Officer = models.CharField(max_length=50, null=True)
    DATE = models.DateField('Signed On',null=True) 



class Quality_Control(models.Model):

    Stations = [
        ('', 'Select Station'),
        ('Beaulieu', 'Beaulieu'),
        ('Gouyave', 'Gouyave'),
        ('Grenville', 'Grenville'),
    ]

    RE= [
        ('', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),

    ]


    Sort= [
        ('', 'Select'),
        ('Sounds', 'Sounds'),
        ('Lights', 'Lights'),      
          ("110's","110's"),
        ('Other', 'Other'),

    ]

    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)


    # Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)

    DATE_1 = models.DateField(null=True) 
    STATION = models.CharField(max_length=50, choices=Stations,null=True)
    BATCH_NUMBER = models.IntegerField(default= 0)
    REWORK = models.CharField(max_length=50,choices=RE, null=True)
    SAMPLE_WEIGHT = models.FloatField(default= 0)

    # TOLERANCE LIMITS FOR DEFECTS

    # Free_of_extraneous matter - Inshell (Whole) and Shelled - 0.5%
    # Broken/damaged – Inshell Whole2%
    # Broken/damaged Shelled - 3%


    # WEIGHT (oz/lbs)
    Nutmeg_Assorted = models.CharField(max_length=50, choices=Sort, null=True)
    Nutmeg_Assorted2 = models.CharField(max_length=50, choices=Sort, null=True)
    Nutmeg_Assorted_cont = models.CharField(max_length=50, null=True)
    ASSORTOR1 = models.CharField(max_length=50, null=True)
    ASSORTOR2 = models.CharField(max_length=50, null=True)
    ASSORTOR3 = models.CharField(max_length=50, null=True)
    ASSORTOR4 = models.CharField(max_length=50, null=True)
    ASSORTOR5 = models.CharField(max_length=50, null=True)
    ASSORTOR6 = models.CharField(max_length=50, null=True)


    ASSORTOR1_A = models.CharField(max_length=50, null=True)
    ASSORTOR1_B = models.CharField(max_length=50, null=True)
    ASSORTOR1_C = models.CharField(max_length=50, null=True)
    ASSORTOR1_D = models.CharField(max_length=50, null=True)
    ASSORTOR1_E = models.CharField(max_length=50, null=True)





    ASSORTOR2 = models.CharField(max_length=50, null=True)


    ASSORTOR2_A = models.CharField(max_length=50, null=True)
    ASSORTOR2_B = models.CharField(max_length=50, null=True)
    ASSORTOR2_C = models.CharField(max_length=50, null=True)
    ASSORTOR2_D = models.CharField(max_length=50, null=True)
    ASSORTOR2_E = models.CharField(max_length=50, null=True)







    ASSORTOR3 = models.CharField(max_length=50, null=True)


    ASSORTOR3_A = models.CharField(max_length=50, null=True)
    ASSORTOR3_B = models.CharField(max_length=50, null=True)
    ASSORTOR3_C = models.CharField(max_length=50, null=True)
    ASSORTOR3_D = models.CharField(max_length=50, null=True)
    ASSORTOR3_E = models.CharField(max_length=50, null=True)


    ASSORTOR4 = models.CharField(max_length=50, null=True)


    ASSORTOR4_A = models.CharField(max_length=50, null=True)
    ASSORTOR4_B = models.CharField(max_length=50, null=True)
    ASSORTOR4_C = models.CharField(max_length=50, null=True)
    ASSORTOR4_D = models.CharField(max_length=50, null=True)
    ASSORTOR4_E = models.CharField(max_length=50, null=True)


    ASSORTOR5 = models.CharField(max_length=50, null=True)



    ASSORTOR5_A = models.CharField(max_length=50, null=True)
    ASSORTOR5_B = models.CharField(max_length=50, null=True)
    ASSORTOR5_C = models.CharField(max_length=50, null=True)
    ASSORTOR5_D = models.CharField(max_length=50, null=True)
    ASSORTOR5_E = models.CharField(max_length=50, null=True)

    SUPERVISOR_A = models.CharField(max_length=50, null=True)
    SUPERVISOR_B = models.CharField(max_length=50, null=True)
    SUPERVISOR_C = models.CharField(max_length=50, null=True)
    SUPERVISOR_D = models.CharField(max_length=50, null=True)
    SUPERVISOR_E = models.CharField(max_length=50, null=True)

    SOUNDS = models.FloatField(default= 0)
    PINHOLES = models.FloatField(default= 0)
    CRACKED = models.FloatField(default= 0)
    BROKEN = models.FloatField(default= 0)
    PIECES = models.FloatField(default= 0)
    FOREIGN_MATTER = models.FloatField(default= 0)


    SUPERVISOR = models.CharField(max_length=50, null=True)
    COMMENTS = models.TextField(blank=True) 


    Approved_BY = models.CharField(max_length=50, null=True)
    Station_Manager = models.CharField(max_length=50, null=True)      
    DATE_OF_REPORT = models.DateField(null=True) 

    # CHECKED BY QA OFFICER

    SIGNED_BY_QUALITY_ASSURANCE_OFFICER = models.CharField(max_length=50, null=True)
    DATE_2 = models.DateField(null=True) 

    def __str__(self):
        return self.COMMENTS





# class User_info(models.Model):

#     farmer_ID = models.CharField(max_length=50, unique=True, null=True)
#     name = models.CharField(max_length=50, null=True)
#     village = models.CharField(max_length=50, null=True)
#     parish = models.CharField(max_length=50, null=True) 
#     latitude = models.DecimalField(default=0.000000,max_digits=9, decimal_places=6)
#     longitude = models.DecimalField(default=0.000000,max_digits=9, decimal_places=6) 
#     phone = models.CharField(max_length=50,null=True)
#     photo = models.ImageField(upload_to='images/',null=True,blank=True)


#     age_range = [('A', '18-25'),('B', '26-35'),('C', '36-60'),('D', '61+'),]
#     age = models.CharField(max_length=1, choices=age_range, default='A')


#     def __str__(self):
#         return self.farmer_ID

# class Land_tenurship(models.Model):
#         TENURE_TYPE = [
#             ('', 'Select'),
#             ('Owned', 'Owned'),
#             ('Freehold', 'Freehold'),
#             ('Leased', 'Leased'),
#             ('Family Land', 'Family Land'),
#             ('ShareCrop', 'ShareCrop'),
#             ('Rent', 'Rent'),
#             ('Rented free', 'Rented free'),
#             ('Premission to work land', 'Premission to work land'),
#             ('Squatted', 'Squatted'),
#             ('Government Land', 'Government Land'),
#             ('Other', 'Other'),
#             ('Caretaker', 'Caretaker'),
#             ('Administrator', 'Administrator'),


#         ]

#         farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
#         tenure_status = models.CharField(max_length=50,choices=TENURE_TYPE, null=True)
#         # tenure_status = models.CharField(max_length=50, null=True)
#         family = models.CharField(max_length=50, null=True)
#         lease = models.CharField(max_length=100, null=True)
#         caretaker = models.CharField(max_length=50, null=True)
#         agent = models.CharField(max_length=50, null=True)
#         comments = models.TextField(blank=True)

#         # def __str__(self):
#         #     return self.farmer_ID
#         # objects = models.Manager()

# class tree(models.Model):
#     trees = [
#         ('', 'Select'),
#         ('Nutmeg', 'Nutmeg'),
#         ('Coconut', 'Coconut'),
#     ]

#     farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
#     Tree_types = models.CharField(max_length=50,choices=trees, default='A')
#     Mature_trees = models.IntegerField(default= 0)
#     Bearing_trees = models.IntegerField(default= 0)
#     NonBearing_trees = models.IntegerField(default= 0)

#     # def __str__(self):
#     #     return self.farmer_ID


# class farm(models.Model):
#     LAND_ELEVATION = [
#         ('', 'Select'),
#         ('Low Belt', 'Low Belt'),
#         ('Middle Belt', 'Middle Belt'),
#         ('High Belt', 'High Belt'),        
#     ]
#     SOIL_TYPE = [
#         ('', 'Select'),
#         ('Sandy Soil', 'Sandy Soil'),
#         ('Clay Soil', 'Clay Soil'),
#         ('Stilt Soil', 'Stilt Soil'),
#         ('Peat Soil', 'Peat Soil'),
#         ('Chalk Soil', 'Chalk Soil'),
#         ('Loamy Soil', 'Loamy Soil'),
#         ('Clay Loam Soil', 'Clay Loam Soil'),
#         ('Sandy Loam Soil', 'Sandy Loam Soil'),

#     ]
#     RAINFALL_PATTERN = [
#         ('', 'Select'),
#         ('Persistent', 'Persistent'),
#         ('Occasional', 'Occasional'),
#         ('Mild', 'Mild'),
#     ]

#     farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
#     land_elevation = models.CharField(max_length=100, choices=LAND_ELEVATION, default='P')
#     soil_type = models.CharField(max_length=100, choices=SOIL_TYPE, default='P')
#     rainfall_pattern = models.CharField(max_length=100, choices=RAINFALL_PATTERN, default='P')
#     other_crops = models.ManyToManyField(crop)
#     intercrop = models.CharField(max_length=50, null=True)
#     pure_stand = models.CharField(max_length=50, null=True)
#     norm_land = models.CharField(max_length=50, null=True)
#     seas_land = models.CharField(max_length=50, null=True)
#     aban_land = models.CharField(max_length=50, null=True)


#     # def __str__(self):
#     #     return self.farmer_ID

# class state(models.Model):
#     TREATED_WATER = [
#         ('', 'Select'),
#         ('Y', 'Yes'),
#         ('N', 'No'),
#     ]

#     WATER_SOURCE = [
#         ('', 'Was this water source is used?'),
#         ('Y', 'Yes'),
#         ('N', 'No'),
#     ]


#     farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
#     road_access = models.CharField(max_length=50, null=True)
#     land_slide = models.CharField(max_length=50, null=True)
#     flooding = models.CharField(max_length=50, null=True)
#     heavy_metals = models.CharField(max_length=50, null=True)
#     chemical_spills = models.CharField(max_length=50, null=True)
#     dumping = models.CharField(max_length=50, null=True)
#     feedlot = models.CharField(max_length=50, null=True)
#     pesticides = models.CharField(max_length=50, null=True)
#     septic_tanks = models.CharField(max_length=50, null=True)
#     manical = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     river = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     spring = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     well = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     harvested = models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
#     treated = models.CharField(max_length=1, choices=TREATED_WATER, default='P')
    
#     # def __str__(self):
#     #     return self.farmer_ID


# class symmary(models.Model):

#     farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
#     annual_production = models.CharField(max_length=50, null=True)
#     peak_productions = models.CharField(max_length=50, null=True)
#     inspected_by = models.DateField('Inspection Date',null=True)
#     date = models.DateField('Current Date',null=True)


#     # def __str__(self):
#     #     return self.farmer_ID

class Worker_Info(models.Model):

    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)



    def __str__(self):
        return self.Worker_ID_No



class Editors(models.Model):
    editor_name = models.CharField(max_length=200)
    num_users = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.editor_name, self.num_users) 











class Labour_support(models.Model):


    TYPE_OF_ASSISTANCE = [
        ('', '--Select an option--'),
        ('GCNA Farm Loan', 'GCNA Farm Loan'),
        ('GCNA Farm Assistance Program', 'GCNA Farm Assistance Program'),
        ('MOA Farm Assistance Program', 'MOA Farm Assistance Program'),        
        ('MOA ADAP Program', 'MOA ADAP Program'),
        ('GCNA Farm Loan', 'GCNA Farm Loan'),
        ('GCNA Assitance Program', 'GCNA Assitance Program'),        
        ('Grenada Development Bank Project', 'Grenada Development Bank Project'),
        ('Bank Loan', 'Bank Loan'),
        ('Grant Fund', 'Grant Fund'),        
        ('Other', 'Other'),        
    ]


    NATURE_OF_ASSISTANCE = [
        ('', '--Select an option--'),
        ('Land Clearing', 'Land Clearing'),
        ('Drainage', 'Drainage'),
        ('Weed Control', 'Weed Control'),
        ('Fertilizing', 'Fertilizing'),
        ('Pruning', 'Pruning'),
        ('Harvesting', 'Harvesting'),
        ('Planting/transplanting', 'Planting/transplanting'),
        ('Pest/Disease', 'Pest/Disease'),
        ('Management', 'Management'),


    ]



    OBJECTIVE_OF_THE_ASSITANCE = [
        ('', '--Select an option--'),
        ('Procurments of Farm inputs to increase farm productivity','Procurments of Farm inputs to increase farm productivity'),
        ('Farm labour support to increase production','Farm labour support to increase production'),
        ('Other', 'Other'),               
    ]


    FACILITATOR_OF_THE_ASSISTANCE = [
        ('', '--Select an option--'),
        ('Ministry of Agriculture(MOA)- World Bank', 'Ministry of Agriculture(MOA)- World Bank'),
        ('Grenada Development(GDB)', 'Grenada Development(GDB)'),
        ('GEF', 'GEF'),        
        ('GIDC', 'GIDC'),
        ('GCNA', 'GCNA'),
        ('GCA', 'GCA'),        
        ('Other', 'Other'),        
    ]
    
    
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)

    Type_of_Assistance= models.CharField(max_length=50, choices=TYPE_OF_ASSISTANCE,  null=True,  blank=True)

    Date_Recieved= models.DateField(max_length=50,  null=True)

    Nature_of_Assistance= models.CharField(max_length=50, choices=NATURE_OF_ASSISTANCE, null=True,  blank=True)

    Objective_of_the_Assistance= models.CharField(max_length=75, choices=OBJECTIVE_OF_THE_ASSITANCE,  null=True,  blank=True)

    Facilitator_of_the_Assistance= models.CharField(max_length=50, choices=FACILITATOR_OF_THE_ASSISTANCE,  null=True,  blank=True)

    Facilitator_of_the_Assistance_cont= models.CharField(max_length=50, null=True,  blank=True)



class Training_support(models.Model):

    TYPE_OF_TRAINING = [
        ('', '--Select an option--'),
        ('GAP', 'GAP'),
        ('GMP', 'GMP'),
        ('HACCP', 'HACCP'),  
        ('Use of small farming tools and equipment', 'Use of small farming tools and equipment'),
        ('Land Use', 'Land Use'),
        ('Pest and Disease', 'Pest and Disease'),  
        ('Management', 'Management'),
        ('Post Harvesting Handling', 'Post Harvesting Handling'),
        ('Harvesting', 'Harvesting'),  
        ('Grafting', 'Grafting'),
        ('Farm Management', 'Farm Management'),
        ('Other', 'Other'),



    ]




    OBJECTIVE_OF_THE_TRAINING = [
        ('', '--Select an option--'),
        ('Increase farm productivity', 'Increase farm productivity'),
        ('Improve the quality of produce', 'Improve the quality of produce'),
        ('Technical Knowledge', 'Technical Knowledge'),
        ('Increase from production', 'Increase from production'),
        ('Improve harvesting', 'Improve harvesting'),
        ('Farm Buisness Management', 'Farm Buisness Management'),  
        ('Improve the quality of plants', 'Improve the quality of plants'),
        ('Other', 'Other'),
    ]


    FACILITATOR_OF_THE_TRAINING = [
        ('', '--Select an option--'),
        ('GCNA', 'GCNA'),
        ('GCA', 'GCA'),
        ('MOA', 'MOA'),
        ('GIDC', 'GIDC'),
        ('Bureau of Standards', 'Bureau of Standards'),
        ('UNDP/SAEP', 'UNDP/SAEP'),
        ('Other', 'Other'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)

    Type_of_Training= models.CharField(max_length=50, choices=TYPE_OF_TRAINING, null=True)

    Type_of_Training_cont= models.CharField(max_length=50,null=True,  blank=True)

    Date_Recieved= models.DateField(max_length=50, null=True)

    Objective_of_the_Training= models.CharField(max_length=50, choices=OBJECTIVE_OF_THE_TRAINING, null=True)

    Objective_of_the_Training_cont= models.CharField(max_length=50,null=True,  blank=True)

    Facilitator_of_the_Training= models.CharField(max_length=50, choices=FACILITATOR_OF_THE_TRAINING, null=True)

    Facilitator_of_the_Training_cont= models.CharField(max_length=50,null=True,  blank=True)




class Farmer_Info(models.Model):
    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    age_range = [('A', '18-25'),('B', '26-35'),('C', '36-50'),('D', '51-65'),('D', '66+'),]
    age = models.CharField(max_length=1, choices=age_range, default='A')
    home_phone = models.CharField(max_length=50,null=True)
    mobile_phone = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)




    def __str__(self):
        return self.Nutmeg_ID_No




class visit(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)
    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    purpose_of_visit= models.CharField(max_length=50, null=True) 
    Date_of_visit = models.DateField('Visit Date',null=True)
    parish = models.CharField(max_length=50, null=True) 
    training = models.CharField(max_length=50, null=True) 
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    visit = models.CharField(max_length=50, null=True) 

    village = models.CharField(max_length=50, null=True)



class land_info(models.Model):




    LAND_ELEVATION = [
        ('', '--Select an option--'),
        ('Low Belt', 'Low Belt'),
        ('Middle Belt', 'Middle Belt'),
        ('High Belt', 'High Belt'),        
    ]
    SOIL_TYPE = [
        ('', '--Select an option--'),
        ('Sandy Soil', 'Sandy Soil'),
        ('Clay Soil', 'Clay Soil'),
        ('Stilt Soil', 'Stilt Soil'),
        ('Loamy Soil', 'Loamy Soil'),
        ('Clay Loam Soil', 'Clay Loam Soil'),
        ('Sandy Loam Soil', 'Sandy Loam Soil'),

    ]
    RAINFALL_PATTERN = [
        ('', '--Select an option--'),
        ('Persistent', 'Persistent'),
        ('Occasional', 'Occasional'),
        ('Mild', 'Mild'),
    ]


    FARM_TYPE = [
        ('', '--Select an option--'),
        ('Nutmeg', 'Nutmeg'),
        ('Coconut', 'Coconut'),
    ]


    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]

    farm_type = models.CharField(max_length=100, choices=FARM_TYPE, default='P')
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    training = models.CharField(max_length=50, null=True) 
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    visit = models.CharField(max_length=50, null=True) 

    village = models.CharField(max_length=50, null=True)
    latitude = models.DecimalField(default=0.000000,max_digits=9, decimal_places=6)
    longitude = models.DecimalField(default=0.000000,max_digits=9, decimal_places=6) 
    acreage = models.CharField(max_length=50, null=True)
    insurance_zone = models.CharField(max_length=50, null=True)
    land_elevation = models.CharField(max_length=100, choices=LAND_ELEVATION, default='Select')
    soil_type = models.CharField(max_length=100, choices=SOIL_TYPE, default='P')
    rainfall_pattern = models.CharField(max_length=100, choices=RAINFALL_PATTERN, default='P')


    Mature_trees_25_years_quantity = models.IntegerField('Number of Mature trees older than 25 years',default= 0,blank=True)
    Mature_trees_25_years_estimated_production = models.IntegerField('Estimated production for Mature older than 25 years',default= 0)
    Bearing_trees_16_24_years_quantity= models.IntegerField('Number of Bearing trees between 16 to 24',default= 0,blank=True)
    Bearing_trees_16_24_years= models.IntegerField('Estimated production Bearing trees between 16 to 24',default= 0,blank=True)
    Bearing_trees_6_15_years_quantity= models.IntegerField('Number of Bearing trees between 6 to 14',default= 0,blank=True)
    Bearing_trees_6_15_years_estimated_production= models.IntegerField('Estimated production Bearing trees between 6 to 14',default= 0,blank=True)
    Non_Bearing_trees_5_years_quantity= models.IntegerField('Number of Non-Bearing trees younger than 5 years',default= 0,blank=True)
    Non_Bearing_trees_5_years_estimated_production= models.IntegerField('Estimated production for Non-bearing trees younger than 5 years',default= 0,blank=True)
    Estimated_peak_period = models.IntegerField('What is the estimated peak period?',default= 0,blank=True)




    End_Use_Atlantic_Tall= models.CharField('What is the intended end use if the Atlantic Tall Tree',max_length=50, null=True,blank=True)
    End_Use_Dwarf= models.CharField('What is the intended end use of the Dwarf Tree',max_length=50, null=True,blank=True)
    No_of_Bearing_Trees_Atlantic_Tall= models.IntegerField('What is the number of Bearing trees for Atlantic Tall Trees',default= 0,blank=True)
    No_of_Bearing_Trees_Dwarf= models.IntegerField('What is the number of Bearing trees for Dwarf Trees',default= 0,blank=True)
    Estimated_Productiom_Atlantic_Tall= models.IntegerField('What is the estimated production of Atlantic Tall Trees',default= 0,blank=True)
    Estimated_Productiom_Dwarf= models.IntegerField('What is the estimated production of Dwarf Trees',default= 0,blank=True)
    No_of_Non_Bearing_Trees_Atlantic_Tall= models.IntegerField('What is the number of Non-Bearing trees for Atlantic Tall Trees',default= 0,blank=True)
    No_of_Non_Bearing_Trees_Dwarf= models.IntegerField('What is the number of Non-Bearing Dwarf Trees',default= 0,blank=True)
    Presence_of_Disease_Atlantic_Tall= models.CharField('What is the state disease for Atlantic Tall Trees',max_length=50, null=True,blank=True)
    Presence_of_Disease_Dwarf= models.CharField('What is the state disease for Dwarf Trees',max_length=50, null=True,blank=True)
    Cultivation_Atlantic_Tall= models.CharField('What is the state of the Atlantic Tall Tree cultivation',max_length=50, null=True,blank=True)
    Cultivation_Dwarf= models.CharField('What is the state of the Dwarf Tree cultivation',max_length=50, null=True,blank=True)

    # def __str__(self):
    #     return self.farmer_ID


class Land_Tenur(models.Model):
        TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


        ]



        FARM_TYPE = [
        ('', '--Select an option--'),
        ('Nutmeg', 'Nutmeg'),
        ('Coconut', 'Coconut'),
        ]




        Land_ID_N0 = models.CharField(default = land_id, max_length=20)

        farm_type = models.CharField(max_length=100, choices=FARM_TYPE, default='P')

        Worker_ID_No = models.CharField(max_length=50, null=True)
        Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
        parish = models.CharField(max_length=50, null=True) 
        training = models.CharField(max_length=50, null=True) 
        tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
        # visit = models.CharField(max_length=50, null=True) 

        village = models.CharField(max_length=50, null=True)
        # farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
        # tenure_status = models.CharField(max_length=50,choices=TENURE_TYPE, null=True)
        Owner_Legal_Title = models.CharField(max_length=50, null=True)
        Freehold = models.CharField(max_length=50, null=True)
        Family = models.CharField(max_length=100, null=True)
        Leashold = models.CharField(max_length=50, null=True)
        Leashold_comment = models.CharField(max_length=50, null=True)
        Caretaker = models.CharField(max_length=50, null=True)
        Agent = models.CharField(max_length=50, null=True)
        No_Legal_Title = models.CharField(max_length=50, null=True)
        Status = models.CharField(max_length=50, null=True)

        # def __str__(self):
        #     return self.farmer_ID
        # objects = models.Manager()

class Nutmeg_Trees(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, unique=True, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    # farmer_ID = models.ForeignKey(User_info,max_length=50, null=True, on_delete=models.CASCADE,to_field='farmer_ID')
    Mature_trees_25_years_quantity = models.IntegerField('Number of Mature trees older than 25 years',default= 0)
    Mature_trees_25_years_estimated_production = models.IntegerField('Estimated production for Mature older than 25 years',default= 0)
    Bearing_trees_16_24_years_quantity= models.IntegerField('Number of Bearing trees between 16 to 24',default= 0)
    Bearing_trees_16_24_years= models.IntegerField('Estimated production Bearing trees between 16 to 24',default= 0)
    Bearing_trees_6_15_years_quantity= models.IntegerField('Number of Bearing trees between 6 to 14',default= 0)
    Bearing_trees_6_15_years_estimated_production= models.IntegerField('Estimated production Bearing trees between 6 to 14',default= 0)
    Non_Bearing_trees_5_years_quantity= models.IntegerField('Number of Non-Bearing trees younger than 5 years',default= 0)
    Non_Bearing_trees_5_years_estimated_production= models.IntegerField('Estimated production for Non-bearing trees younger than 5 years',default= 0)
    Estimated_peak_period = models.IntegerField('What is the estimated peak period?',default= 0)


    # NonBearing_trees = models.IntegerField(default= 0)



class Nutmeg_Variety(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Banda=models.CharField('Is the Banda nutmeg present?',max_length=50, null=True)
    Papua=models.CharField('Is the Papua nutmeg present?',max_length=50, null=True)
    Malayan_Indonesia=models.CharField('Is the Malayan Indonesia nutmeg present?',max_length=50, null=True)
    dominant_Variety=models.CharField('What nutmeg type is the most common?',max_length=50, null=True)


class Other_Crops(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    other_crops = models.ManyToManyField(crop)

class Coconut_Trees(models.Model):
    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),
            ('Other', 'Other'),

    ]
    
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    End_Use_Atlantic_Tall= models.CharField('What is the intended end use if the Atlantic Tall Tree',max_length=50, null=True)
    End_Use_Dwarf= models.CharField('What is the intended end use of the Dwarf Tree',max_length=50, null=True)
    No_of_Bearing_Trees_Atlantic_Tall= models.IntegerField('What is the number of Bearing trees for Atlantic Tall Trees',default= 0)
    No_of_Bearing_Trees_Dwarf= models.IntegerField('What is the number of Bearing trees for Dwarf Trees',default= 0)
    Estimated_Productiom_Atlantic_Tall= models.IntegerField('What is the estimated production of Atlantic Tall Trees',default= 0)
    Estimated_Productiom_Dwarf= models.IntegerField('What is the estimated production of Dwarf Trees',default= 0)
    No_of_Non_Bearing_Trees_Atlantic_Tall= models.IntegerField('What is the number of Non-Bearing trees for Atlantic Tall Trees',default= 0)
    No_of_Non_Bearing_Trees_Dwarf= models.IntegerField('What is the number of Non-Bearing Dwarf Trees',default= 0)
    Presence_of_Disease_Atlantic_Tall= models.CharField('What is the state disease for Atlantic Tall Trees',max_length=50, null=True)
    Presence_of_Disease_Dwarf= models.CharField('What is the state disease for Dwarf Trees',max_length=50, null=True)
    Cultivation_Atlantic_Tall= models.CharField('What is the state of the Atlantic Tall Tree cultivation',max_length=50, null=True)
    Cultivation_Dwarf= models.CharField('What is the state of the Dwarf Tree cultivation',max_length=50, null=True)

class Citrus_Mango_Trees(models.Model):
    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    No_of_Bearing_Trees_Lime= models.IntegerField('What is the number of Bearing trees for Lime',default= 0)
    No_of_Bearing_Trees_Lemon= models.IntegerField('What is the number of Bearing trees for Lemon',default= 0)
    No_of_Bearing_Trees_Mangoes= models.IntegerField('What is the number of Bearing trees for Mangoes',default= 0)
    Estimated_Productiom_Lime= models.IntegerField('What is the estimated production of Lime',default= 0)
    Estimated_Productiom_Lemon= models.IntegerField('What is the estimated production of Lemon',default= 0)
    Estimated_Productiom_Mangoes= models.IntegerField('What is the estimated production of Mangoes',default= 0)
    No_of_Non_Bearing_Trees_Lime= models.IntegerField('What is the number of Non-Bearing trees for Lime',default= 0)
    No_of_Non_Bearing_Trees_Lemon= models.IntegerField('What is the number of Non-Bearing trees for Lemon',default= 0)
    No_of_Non_Bearing_Trees_Mangoes= models.IntegerField('What is the number of Non-Bearing trees for Mangoes',default= 0)
    Presence_of_Disease_Lime= models.CharField('What is the state disease for Lime',max_length=50, null=True)
    Presence_of_Disease_Lemon= models.CharField('What is the state disease for Lemon',max_length=50, null=True)
    Presence_of_Disease_Mangoes= models.CharField('What is the state disease for Mangoes',max_length=50, null=True)
    Cultivation_Lime= models.CharField('What is the state of the Lime cultivation',max_length=50, null=True)
    Cultivation_Lemon= models.CharField('What is the state of the Lemon cultivation',max_length=50, null=True)
    Cultivation_Mangoes= models.CharField('What is the state of the Mangoes cultivation',max_length=50, null=True)


class Other_Spices_Trees(models.Model):
    
    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]


    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    No_of_Bearing_Trees_Clove= models.IntegerField('What is the number of Bearing trees for clove',default= 0)
    No_of_Bearing_Trees_Cinnamon= models.IntegerField('What is the number of Bearing trees for Cinnamon',default= 0)
    No_of_Bearing_Trees_Bayleaf= models.IntegerField('What is the number of Bearing trees for Bayleaf',default= 0)
    No_of_Bearing_Trees_Tumeric= models.IntegerField('What is the number of Bearing trees for Tumeric',default= 0)
    No_of_Bearing_Trees_Ginger= models.IntegerField('What is the number of Bearing trees for Ginger',default= 0)
    Estimated_Productiom_Clove= models.IntegerField('What is the estimated production of clove',default= 0)
    Estimated_Productiom_Cinnamon= models.IntegerField('What is the estimated production of Cinnamon',default= 0)
    Estimated_Productiom_Bayleaf= models.IntegerField('What is the estimated production of Bayleaf',default= 0)
    Estimated_Productiom_Tumeric= models.IntegerField('What is the estimated production of Tumeric',default= 0)
    Estimated_Productiom_Ginger= models.IntegerField('What is the estimated production of Ginger',default= 0)
    No_of_Non_Bearing_Trees_Clove= models.IntegerField('What is the number of Non-Bearing trees for clove',default= 0)
    No_of_Non_Bearing_Trees_Cinnamon= models.IntegerField('What is the number of Non-Bearing trees for Cinnamon',default= 0)
    No_of_Non_Bearing_Trees_Bayleaf= models.IntegerField('What is the number of Non-Bearing trees for Bayleaf',default= 0)
    No_of_Non_Bearing_Trees_Tumeric= models.IntegerField('What is the number of Non-Bearing trees for Tumeric',default= 0)
    No_of_Non_Bearing_Trees_Ginger= models.IntegerField('What is the number of Non-Bearing trees for Ginger',default= 0)
    Presence_of_Disease_Clove= models.CharField('What is the state disease for Clove',max_length=50, null=True)
    Presence_of_Disease_Cinnamon= models.CharField('What is the state disease for Cinnamon',max_length=50, null=True)
    Presence_of_Disease_Bayleaf= models.CharField('What is the state disease for Bayleaf',max_length=50, null=True)
    Presence_of_Disease_Tumeric= models.CharField('What is the state disease for Tumeric',max_length=50, null=True)
    Presence_of_Disease_Ginger= models.CharField('What is the state disease for Ginger',max_length=50, null=True)
    Cultivation_Clove= models.CharField('What is the state of the Clove cultivation',max_length=50, null=True)
    Cultivation_Cinnamon= models.CharField('What is the state of the Cinnamon cultivation',max_length=50, null=True)
    Cultivation_Bayleaf= models.CharField('What is the state of the Bayleaf cultivation',max_length=50, null=True)
    Cultivation_Tumeric= models.CharField('What is the state of the Tumeric cultivation',max_length=50, null=True)
    Cultivation_Ginger= models.CharField('What is the state of the Ginger cultivation',max_length=50, null=True)


class Other_Seasoning_Trees(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    
    
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    No_of_Stools_chive= models.IntegerField('What is the number of stools  for chive',default= 0)
    No_of_Stools_Thyme= models.IntegerField('What is the number of stools  for Thyme',default= 0)
    No_of_Stools_Celery= models.IntegerField('What is the number of stools  for Celery',default= 0)
    No_of_Stools_Parsley= models.IntegerField('What is the number of stools for Parsley',default= 0)
    No_of_Stools_Petit_Bum= models.IntegerField('What is the number of stools  for Petit Bum',default= 0)
    No_of_Stools_Seasoning_Pepper= models.IntegerField('What is the number of stools  for Seasoning pepper',default= 0)
    No_of_Stools_Hot_Pepper= models.IntegerField('What is the number of stools for Hot pepper',default= 0)
    Presence_of_Disease_chive= models.CharField('What is the state disease for chive',max_length=50, null=True)
    Presence_of_Disease_Thyme= models.CharField('What is the state disease for Thyme',max_length=50, null=True)
    Presence_of_Disease_Celery= models.CharField('What is the state disease for Celery',max_length=50, null=True)
    Presence_of_Disease_Parsley= models.CharField('What is the state disease for Parsley',max_length=50, null=True)
    Presence_of_Disease_Petit_Bum= models.CharField('What is the state disease for Petit Bum ',max_length=50, null=True)
    Presence_of_Disease_Seasoning_Pepper= models.CharField('What is the state disease for Seasoning pepper',max_length=50, null=True)
    Presence_of_Disease_Hot_Pepper= models.CharField('What is the state disease for Hot pepper',max_length=50, null=True)
    Cultivation_chive= models.CharField('What is the state of the chive cultivation',max_length=50, null=True)
    Cultivation_Thyme= models.CharField('What is the state of the THYME cultivation',max_length=50, null=True)
    Cultivation_Celery= models.CharField('What is the state of the celery cultivation',max_length=50, null=True)
    Cultivation_Parsley= models.CharField('What is the state of the parsley cultivation',max_length=50, null=True)
    Cultivation_Petit_Bum= models.CharField('What is the state of the pwtit bum cultivation',max_length=50, null=True)
    Cultivation_Seasoning_Pepper= models.CharField('What is the state of the seasoning pepper cultivation',max_length=50, null=True)
    Cultivation_Hot_Pepper= models.CharField('What is the state of the hot pepper cultivation',max_length=50, null=True)
    



class Other_Crops_Cultivated(models.Model):

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
    Name_of_Crops= models.CharField(max_length=50, null=True)
    Number_of_Trees_or_stools= models.IntegerField(default= 0)



class Condition(models.Model):
    DECISIOn = [
        ('', '--Select an option--'),
        ('Y', 'Good'),
        ('N', 'Fair'),
        ('N', 'Poor'),
    ]
    

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]

    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Weeds = models.CharField('What is the state of the weeds?',max_length=1, choices=DECISIOn, default='P')
    Drains = models.CharField('What is the state of the drains Drains',max_length=1, choices=DECISIOn, default='P')
    Fertilizing = models.CharField('What is the state of the Fertilizing',max_length=1, choices=DECISIOn, default='P')
    Pruning = models.CharField('What is the state of the Pruning',max_length=1, choices=DECISIOn, default='P')
    Harvesting = models.CharField('What is the state of the Harvesting',max_length=1, choices=DECISIOn, default='P')
    Land_Clearing = models.CharField('What is the state of the Land_Clearing',max_length=1, choices=DECISIOn, default='P')
    Planting = models.CharField('What is the state of the Planting',max_length=1, choices=DECISIOn, default='P')
    Presence_of_pest_and_diseases_on_nutmegs = models.CharField('What is the state of pests and diseases?',max_length=1, choices=DECISIOn, default='P')
    Presence_of_pest_and_diseases_on_nutmegs_cont = models.CharField('Elaborate the pest and dieseases present,if any.',max_length=50, null=True)



class Nutmeg_Land(models.Model):
    # norm_land= models.CharField(max_length=50, null=True)
    # Seasonal= models.CharField(max_length=50, null=True)
    # Abandoned= models.CharField(max_length=50, null=True)
    DECISIOn = [
        ('', '--Select an option--'),
        ('Normal', 'Normal'),
        ('Seasonal', 'Seasonal'),
        ('Abandoned', 'Abandoned'),
    ]


    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    farm_type=models.CharField('Select the land type that best corresponds with the farm.',max_length=100, choices=DECISIOn, default='P')

class Nutmeg_Frequency(models.Model):
    # Regular = models.CharField(max_length=50, null=True)
    # Occasional= models.CharField(max_length=50, null=True)
    # Never= models.CharField(max_length=50, null=True)

    DECISIOn = [
        ('', '--Select an option--'),
        ('Regular', 'Regular'),
        ('Occasional', 'Occasional'),
        ('Never', 'Never'),
    ]
    

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]


    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Frequency=models.CharField('Select the frequency that best corresponds with the farm.',max_length=100, choices=DECISIOn, default='P')



class Potential_Risks(models.Model):

    DECISIOn = [
        ('', '--Select an option--'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50,  null=True)
    Nutmeg_ID_No = models.CharField(max_length=50,  null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Slides=models.CharField('Did land slides occur recently?',max_length=1, choices=DECISIOn, default='P')
    Flooding=models.CharField('Did flooding occur recently?',max_length=1, choices=DECISIOn, default='P')
    Heavy_Metal=models.CharField('Are Heavy Metals present?',max_length=1, choices=DECISIOn, default='P')
    Chemical_Spills=models.CharField('Are chemical Spills present?',max_length=1, choices=DECISIOn, default='P')
    Dumping_of_trash=models.CharField('Did the dumping of trash occur recently?',max_length=1, choices=DECISIOn, default='P')
    Feedlot=models.CharField('Is a feedlot Present?',max_length=1, choices=DECISIOn, default='P')



class Policy(models.Model):


    DECISIOn = [
        ('', '--Select an option--'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Pesticides=models.CharField('Was pesticides used?',max_length=1, choices=DECISIOn, default='P')
    Septic_Tanks=models.CharField('Are septic tanks used? ',max_length=1, choices=DECISIOn, default='P')
    Other=models.CharField(max_length=1, choices=DECISIOn, default='P')

class Road_Access(models.Model):

    DECISIOn = [
        ('', '--Select an option--'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    


    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]

    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Road_Access=models.CharField('Is road access available?',max_length=1, choices=DECISIOn, default='P')


class Food_Safety_and_Quality(models.Model):

    DECISIOn = [
        ('', '--Select an option--'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]


    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Fertilizer=models.CharField('Is fertilizer used?',max_length=1, choices=DECISIOn, default='P')
    Fertilizer_cont= models.CharField('If fertilizer is used, What are they?',max_length=50, null=True)
    Last_application= models.CharField('When was the last application of fertilizer',max_length=50, null=True)
    Picture = models.ImageField(upload_to='images/',null=True,blank=True)
    Raw_Manure=models.CharField('Is raw manure used?',max_length=1, choices=DECISIOn, default='P')
    Raw_Manure_cont= models.CharField('If raw manure is used, What type?',max_length=50, null=True)
    Composed_manure=models.CharField('Is composed manure used?',max_length=1, choices=DECISIOn, default='P')
    Other= models.CharField(max_length=50, null=True)


class Farm_Water_Source(models.Model):

    TREATED_WATER = [
        ('', '--Select an option--'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    WATER_SOURCE = [
        ('', 'Was this water source is used?'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]


    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]
    
    
    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Municipal_Nawasa= models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    River= models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    Spring= models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    Well= models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    Harvested_Rain_Water= models.CharField(max_length=1, choices=WATER_SOURCE, default='P')
    is_water_treated= models.CharField('Is the water source treated',max_length=1, choices=WATER_SOURCE, default='P')
    is_water_treated_cont= models.CharField('If the water was treated. How?',max_length=50, null=True, blank=True)

class Farm_House(models.Model):

    DECISIOn = [
        ('', 'Select'),
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    

    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]

    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    Farm_House=models.CharField('Is a Farm house present',max_length=1, choices=DECISIOn, default='P')

class inspector_symmary(models.Model):
     



    TENURE_TYPE = [
            ('', '--Select an option--'),
            ('Owned', 'Owned'),
            ('Freehold', 'Freehold'),
            ('Leased', 'Leased'),
            ('Family Land', 'Family Land'),
            ('ShareCrop', 'ShareCrop'),
            ('Rent', 'Rent'),
            ('Rented free', 'Rented free'),
            ('Premission to work land', 'Premission to work land'),
            ('Squatted', 'Squatted'),
            ('Government Land', 'Government Land'),
            ('Other', 'Other'),
            ('Caretaker', 'Caretaker'),
            ('Administrator', 'Administrator'),


    ]

    Land_ID_N0 = models.CharField(default = land_id, max_length=20)

    Worker_ID_No = models.CharField(max_length=50, null=True)  
    Nutmeg_ID_No = models.CharField(max_length=50, null=True)
    parish = models.CharField(max_length=50, null=True) 
    village = models.CharField(max_length=50, null=True)
    tenurship = models.CharField(max_length=100,null=True, choices=TENURE_TYPE, )
    estimated_annual_production = models.CharField('Enter estimated annual production',max_length=50, null=True)
    estimated_peak_productions = models.CharField('Enter estimated peak production',max_length=50, null=True)
    inspected_by = models.DateField('Inspection Date',null=True)
    date = models.DateField('Current Date',null=True)
    




class In_House_Drying(models.Model):
    STATION_CHOICES = [
        ('', '--Select Location--'),
        ('G', 'Grenville'),
        ('H', 'Hermitage'),
        ('M', 'Marli'),
        ('U', 'Union'),
        ('GP', 'Gouyave'),

   


    ]


    SHELF0 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY0 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION0 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]

    SHELF1 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY1 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION1 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]

    SHELF2 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY2 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION2 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]


    SHELF3 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY3 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION3 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]


    SHELF4 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]

    TRAY4 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]

    SECTION4 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]

    SELECTION = [
        ('', 'Send Alert?'),
        ('Y', 'Yes'),
        ('N', 'No'),

    ]

    Nutmeg_ID_No = models.CharField(max_length=50, null=True,blank=True)
    STATION= models.CharField('Station',max_length=50,  choices=STATION_CHOICES, null=True)
    DATE_OF_PURCHASE= models.DateField('Date of Purchase',null=True)
    TOTAL_NUM_OF_FARMERS= models.IntegerField('Total Numbers of Farmers',default= 0)
    TOTAL_LBS_NUTMEG_BOUGHT= models.IntegerField('Total lbs of nutmeg bought',default= 0)
    NUM_OF_BAGS= models.IntegerField('Number of Bags',default= 0)
    START_DRYING_DATE= models.DateField('Start drying date',null=True)
    APPROX_END_DRYING_DATE= models.DateField('Approximate end drying date',null=True)
    END_DRYING_DATE= models.DateField('End drying date',null=True)

# PLACEMENT ON SHELF



    ShelfG= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    Shelf= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    Tray= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    Section= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    Shelf= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    Tray= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    WeightG_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightG_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightG_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightG_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    WeightH_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightH_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightH_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightH_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    WeightM_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightM_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightM_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightM_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    WeightU_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightU_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightU_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightU_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    WeightGP_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightGP_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightGP_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    WeightGP_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    MoistureG_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureG_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureG_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureG_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    MoistureH_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureH_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureH_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureH_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    MoistureM_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureM_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureM_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureM_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    MoistureU_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureU_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureU_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureU_FL= models.CharField('Section',max_length=50, null=True,blank=True)

    MoistureGP_GF= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureGP_1F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureGP_2F= models.CharField('Section',max_length=50, null=True,blank=True)
    MoistureGP_FL= models.CharField('Section',max_length=50, null=True,blank=True)

     # LOCATION1  
 
    ShelfG_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfM_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfM_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfM_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfM_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

# MOISTURE TESTING (Weeks 3, 6, 8)



   # LOCATION2    

    ShelfG_0_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_0_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_0_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_0_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_0_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_0_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_0_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_0_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_0_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfG_0_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_0_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_0_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_0_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_0_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_0_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_0_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_0_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_0_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_0_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_0_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_0_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfH_0_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_0_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_0_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfM_0_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_0_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_0_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfM_0_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_0_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_0_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfM_0_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_0_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_0_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfM_0_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True)
    TrayM_0_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_0_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfU_0_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_0_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_0_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfU_0_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_0_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_0_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_0_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_0_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_0_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfU_0_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_0_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_0_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


    ShelfGP_0_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_0_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_0_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_0_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_0_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_0_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_0_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_0_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_0_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)

    ShelfGP_0_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_0_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_0_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)


# MONITORING AND INSPECTION

    Location_Status = [
        ('', '--Select Location--'),
        ('Ground Floor', 'Ground Floor'),
        ('1st Floor', '1st Floor'),
        ('2nd Floor', '2nd Floor'),
        ('Loft', 'Loft'),
    ]

    Status = [
        ('', '--Select Location--'),
        ('Cracked', 'Cracked'),
        ('Grow Heads', 'Grow Heads'),
        ('Lights', 'Lights'),
        ('Mould', 'Mould'),
    ]





    SHELF0 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY0 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION0 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]


    SHELF1 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY1 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION1 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]










    SHELF2 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY2 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION2 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]









    SHELF3 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY3 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION3 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]







    SHELF4 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY4 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION4 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]








    SELECTION = [
        ('', 'Send Alert?'),
        ('Yes', 'Yes'),
        ('No', 'No'),

    ]


    LOCATION3 = models.CharField('Location',max_length=50, choices=Location_Status, )    


    DEFECT = models.CharField('Defect',max_length=50, choices=Status, default='A')   

    PREDOMINANT_DEFECT = models.CharField('Predominant Defect',max_length=50, choices=Status, )   


    ALERT = models.CharField('Alert',max_length=50,null=True,blank=True, choices=SELECTION,)   


    ALERT_cont = models.CharField('Alert',max_length=50,null=True,blank=True)   

    STATION2= models.CharField('Station',max_length=50,null=True)

    Sampling_from_gouyvae= models.CharField('Sampling from Gouyvae',max_length=50, null=True)

    # Guideline_for_pickupmoisture_<6.5%_inhouse

    Control_number= models.CharField('Control Number',max_length=50, null=True)





class Dispatch_Of_Dried_Nutmeg(models.Model):








    STATION_CHOICES = [
        ('', '--Select Location--'),
        ('G', 'Grenville'),
        ('H', 'Hermitage'),
        ('M', 'Marli'),
        ('U', 'Union'),
        ('GP', 'Gouyave'),

   


    ]



    SHELF0 = [
        ('', '--Select shelf--'),
        ('1', '1'),
        ('2', '2'),


   


    ]



    TRAY0 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

   


    ]


    SECTION0 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
   


    ]




    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)



    STATION= models.CharField('Station',max_length=50,  choices=STATION_CHOICES, null=True)
    DATE_OF_PICK_UP= models.DateField('Date of pick up',null=True)
    FINAL_MOISTURE_CONTENT= models.IntegerField('Final moisture content',default= 0)
   
   # LOCATION1



    # # Ground_1= models.IntegerField('Ground',default= 0) 
    # Shelf_Ground_1= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Ground_1= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Ground_1= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




    # # Floor_1st_1= models.IntegerField('1st Floor',default= 0)
    # Shelf_Floor_1st_1= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_1st_1= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_1st_1= models.CharField('Section',max_length=50, choices=SECTION0, null=True)



    # # Floor_2nd_1= models.IntegerField('2nd Floor',default= 0)
    # Shelf_Floor_2nd_1= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_2nd_1= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_2nd_1= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




    # # Floor_Loft_1= models.IntegerField('Loft',default= 0)
    # Shelf_Floor_Loft_1= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_Loft_1= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_Loft_1= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




    # # LOCATION2

   
    # # Ground_1= models.IntegerField('Ground',default= 0) 
    # Shelf_Ground_2= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Ground_2= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Ground_2= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




    # # Floor_1st_2= models.IntegerField('1st Floor',default= 0)
    # Shelf_Floor_1st_2= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_1st_2= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_1st_2= models.CharField('Section',max_length=50, choices=SECTION0, null=True)



    # # Floor_2nd_2= models.IntegerField('2nd Floor',default= 0)
    # Shelf_Floor_2nd_2= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_2nd_2= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_2nd_2= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




    # # Floor_Loft_2= models.IntegerField('Loft',default= 0)
    # Shelf_Floor_Loft_2= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
    # Tray_Floor_Loft_2= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
    # Section_Floor_Loft_2= models.CharField('Section',max_length=50, choices=SECTION0, null=True)








    ShelfG= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)




    Shelf= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    Tray= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    Section= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)





    Shelf= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    Tray= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)






     # LOCATION1  
 
    ShelfG_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_GF= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfG_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_1F= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfG_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_2F= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfG_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_FL= models.CharField('Station',max_length=50, null=True,blank=True)








    ShelfH_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_GF= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfH_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_1F= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfH_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_2F= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfH_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_FL= models.CharField('Station',max_length=50, null=True,blank=True)









    ShelfM_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_GF= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfM_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_1F= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfM_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_2F= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfM_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_FL= models.CharField('Station',max_length=50, null=True,blank=True)











    ShelfU_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_GF= models.CharField('Station',max_length=50, null=True,blank=True)



    ShelfU_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_1F= models.CharField('Station',max_length=50, null=True,blank=True)



    ShelfU_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_2F= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfU_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_FL= models.CharField('Station',max_length=50, null=True,blank=True)










    ShelfGP_GF= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_GF= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_GF= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_GF= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfGP_1F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_1F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_1F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_1F= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfGP_2F= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_2F= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_2F= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_2F= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfGP_FL= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_FL= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_FL= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_FL= models.CharField('Station',max_length=50, null=True,blank=True)








    BATCH_NUMBER= models.CharField('Batch Number',max_length=50, null=True)

    CORRESPONDING_DELIVERY_ADVICE= models.CharField('Corresponding Delivery Advice',max_length=50, null=True)

    Control_number= models.IntegerField('Control Number',default= 0)


  

class Dispatch_Of_Green_Nutmeg(models.Model):
    STATION_CHOICES = [
        ('', '--Select Location--'),
        ('G', 'Grenville'),
        ('H', 'Hermitage'),
        ('M', 'Marli'),
        ('U', 'Union'),
        ('GP', 'Gouyave'),
        ('V', 'Victoria'),

   


    ]


    

    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)
 



    STATION= models.CharField('Station',max_length=50,  choices=STATION_CHOICES, null=True)
    DATE_OF_PURCHASE= models.DateField('Date of purchase',null=True)
    TOTAL_NUM_OF_FARMERS= models.IntegerField('Total Numbers of Farmers',default= 0)
    TOTAL_LBS_NUTMEG_BOUGHT= models.IntegerField('Total lbs of nutmeg bought',default= 0)
    NUM_OF_BAGS= models.IntegerField('Number of Bags',default= 0)
    DELIVERY_ADVICE_NUMBER= models.CharField('Delivery  advice Number',max_length=50, null=True)
    WAREHOUSE_RECEIPT_NUMBER= models.CharField('Warehouse Reciept Number',max_length=50, null=True)
    CONTROL_NUMBER= models.CharField('Control Number',max_length=50, null=True)




class Cracking_Summary(models.Model):
    STATION_CHOICES = [
        ('', '--Select Location--'),

        ('H', 'Beaulieu'),
        ('M', 'Gouyave'),
        ('G', 'Grenville'),
 
 


    ]



 



    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)
 



    STATION= models.CharField('Station',max_length=50,  choices=STATION_CHOICES, null=True)
    DATE_OF_CRACKING= models.DateField('Date of cracking',null=True)
    WAREHOUSE_RECEIPT_NUMBERS= models.CharField('Warehouse Reciept Number',max_length=50, null=True)
    NUM_OF_BAGS= models.IntegerField('Number of Bags',default= 0)
    LBS_OF_NUTMEGS_CRACKED= models.IntegerField('Lbs of Nutmegs cracked',default= 0)
    Delivery_Advice_Num= models.IntegerField('Number of Bags',default= 0)
    Control_Num= models.IntegerField('Number of Bags',default= 0)


class Floation_Summary(models.Model):
    STATION_CHOICES = [
        ('', '--Select Location--'),
        ('G', 'Beaulieu'),
        ('GP', 'Gouyave'),



    ]



    SHELF0 = [
        ('', '--Select shelf--'),
        ('1', '1'),
        ('2', '2'),


   


    ]



    TRAY0 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

   


    ]


    SECTION0 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
   


    ]















    SHELF0 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY0 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION0 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]










    SHELF1 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY1 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION1 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]










    SHELF2 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY2 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION2 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]









    SHELF3 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY3 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION3 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]







    SHELF4 = [
        ('', '--Select shelf--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
    ]



    TRAY4 = [
        ('', '--Select Tray--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]


    SECTION4 = [
        ('', '--Select Section--'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    ]


















    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)
 



    STATION= models.CharField('Station',max_length=50,  choices=STATION_CHOICES, null=True)    
    START_DRYING_DATE= models.DateField('Start drying date',null=True)
    APPROX_END_DRYING_DATE= models.DateField('Approximate end drying date',null=True)
    END_DRYING_DATE= models.DateField('End drying date',null=True)



# LOCATION - PLACEMENT ON SHELF 





#     # HEAVIES

#     # Ground_Floorh= models.CharField('Ground Floor', choices=STATION_CHOICES,max_length=50, null=True)
#     Shelfh= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
#     Trayh= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
#     Sectionh= models.CharField('Section',max_length=50, choices=SECTION0, null=True)




#     # LIGHTS

#     # Ground_Floorl= models.CharField('Ground Floor', choices=STATION_CHOICES,max_length=50, null=True)
#     Shelfl= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True) 
#     Trayl= models.CharField('Tray',max_length=50, choices=TRAY0, null=True)
#     Sectionl= models.CharField('Section',max_length=50, choices=SECTION0, null=True)


# # MOISTURE TESTING 

#     FINAL_MOISTURE_H =models.CharField('Heavy Final Moisture',max_length=50, null=True, blank=True) 
#     FINAL_MOISTURE_L =models.CharField('Light Final Moisture',max_length=50, null=True, blank=True) 









    ShelfG_light= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_light= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_light= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_light= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfG_heavy= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayG_heavy= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionG_heavy= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureG_heavy= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfH_light= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_light= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_light= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_light= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfH_heavy= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayH_heavy= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionH_heavy= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureH_heavy= models.CharField('Station',max_length=50, null=True,blank=True)


    ShelfM_light= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_light= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_light= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_light= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfM_heavy= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayM_heavy= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionM_heavy= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureM_heavy= models.CharField('Station',max_length=50, null=True,blank=True)



    ShelfU_light= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_light= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_light= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_light= models.CharField('Station',max_length=50, null=True,blank=True)



    ShelfU_heavy= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayU_heavy= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionU_heavy= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureU_heavy= models.CharField('Station',max_length=50, null=True,blank=True)



    ShelfGP_light= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_light= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_light= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_light= models.CharField('Station',max_length=50, null=True,blank=True)

    ShelfGP_heavy= models.CharField('Shelf',max_length=50, choices=SHELF0, null=True,blank=True) 
    TrayGP_heavy= models.CharField('Tray',max_length=50, choices=TRAY0, null=True,blank=True)
    SectionGP_heavy= models.CharField('Section',max_length=50, choices=SECTION0, null=True,blank=True)
    MoistureGP_heavy= models.CharField('Station',max_length=50, null=True,blank=True)












      #Heavies/Lights (drop down box)
    BATCH_NUMBER=models.CharField('Batch Number',max_length=50, null=True)
    Control_NUMBER=models.CharField('Batch Number',max_length=50, null=True)



class Package_Ciontrol(models.Model):


    PRODUCT_DESC = [
        ('', '--Select Description--'),
        ('SUNS', 'SUNS'),
        ('GROUND NUTMEG', 'GROUND NUTMEG'),
        ('CRACKED NUTMEG', 'CRACKED NUTMEG'),
        ('110’S', ' 110’S'),
        ('80’S', ' 80’S'),
        ('GUNS', 'GUNS'),
        ('MACE', 'MACE'),
        ('Others', 'Others'),

   


    ]



    PACKAGE_MAT = [
        ('', '--Select Location--'),
        ('Jute', 'Jute'),
        ('Polypropylene', 'Polypropylene'),
        ('Other', 'Other'),


   


    ]


    Nutmeg_ID_No = models.CharField(max_length=50, unique=True, null=True)

    PRODUCT_DESCRIPTION= models.CharField('Product Description',max_length=50, choices=PRODUCT_DESC, default='A')    
     # PRODUCT_DESCRIPTION_cont= models.CharField('Product Description',max_length=50,  default='A')    

    PRODUCT_DESCRIPTION_cont= models.CharField(max_length=50,null=True)  
# PACKAGING DATE

    START= models.DateField('Start  date',null=True)
    END= models.DateField('End date',null=True)
    QUANTITY_OF_BAGS= models.IntegerField('Quantity of Bags',default= 0)
    TOTAL_WEIGHT_LBS=models.CharField('Total weight in lbs',max_length=50, null=True)
    PACKAGING_MATERIAL= models.CharField('Pakaging Material',max_length=50, choices=PACKAGE_MAT, default='A')  
    PACKAGING_MATERIAL_cont= models.CharField(max_length=50,null=True)  
    BATCH_NUMBER=models.CharField('Batch Number',max_length=50, null=True)
    CONTRACT_NUMBER = models.CharField('Contract Shipment Number',max_length=50, null=True)
    OFFICIAL_LAB_RESULTS = models.CharField('Official Lab Results',max_length=50, null=True)
    Nutmeg_Assorted_cont = models.CharField(max_length=50, null=True)



    Physical_Analysis= models.CharField('Pakaging Material',max_length=50, choices=PACKAGE_MAT, default='A')     
    Chemical_Analysis= models.CharField('Pakaging Material',max_length=50, choices=PACKAGE_MAT, default='A')     
    Microbiological_Analysis= models.CharField('Pakaging Material',max_length=50, choices=PACKAGE_MAT, default='A')     




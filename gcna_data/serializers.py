# myapp/serializers.py
from rest_framework import serializers


from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 
from .models import Worker_Info 
from .models import Farmer_Info 
from .models import land_info 
from .models import Land_Tenur 
from .models import Nutmeg_Trees 
from .models import Nutmeg_Variety 



from .models import Other_Crops 
from .models import Coconut_Trees 
from .models import Citrus_Mango_Trees 
from .models import Other_Spices_Trees 
from .models import Other_Seasoning_Trees 
from .models import Other_Crops_Cultivated 
from .models import Condition 
from .models import Nutmeg_Land 
from .models import Nutmeg_Frequency 
from .models import Potential_Risks 
from .models import Policy 
from .models import Road_Access 
from .models import Food_Safety_and_Quality 
from .models import Farm_Water_Source 
from .models import Farm_House 
from .models import inspector_symmary 


from .models import visit 
from .models import In_House_Drying 
from .models import Dispatch_Of_Dried_Nutmeg 
from .models import Dispatch_Of_Green_Nutmeg 
from .models import Cracking_Summary 
from .models import Floation_Summary 
from .models import Package_Ciontrol 
from .models import Editors 
from .models import Labour_support 
from .models import Training_support 
from .models import Policy 

class Policy_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
        
        
class Dried_Moisture_Analysis_A_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dried_Moisture_Analysis_A
        fields = '__all__'

class Dried_Moisture_Analysis_B_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dried_Moisture_Analysis_B
        fields = '__all__'

class Floated_Moisture_Analysis_A_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Floated_Moisture_Analysis_A
        fields = '__all__'

class Floated_Moisture_Analysis_B_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Floated_Moisture_Analysis_B
        fields = '__all__'

class Quality_Control_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Quality_Control
        fields = '__all__'

class Farmer_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_Info
        fields = '__all__'

class Worker_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Worker_Info
        fields = '__all__'

class Nutmeg_Variety_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nutmeg_Variety
        fields = '__all__'

class land_info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = land_info
        fields = '__all__'

class Land_Tenur_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Land_Tenur
        fields = '__all__'

class Nutmeg_Trees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nutmeg_Trees
        fields = '__all__'

class Nutmeg_Variety_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nutmeg_Variety
        fields = '__all__'

class Other_Crops_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Crops
        fields = '__all__'

class Coconut_Trees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Coconut_Trees
        fields = '__all__'

class Citrus_Mango_Trees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Citrus_Mango_Trees
        fields = '__all__'

class Other_Spices_Trees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Spices_Trees
        fields = '__all__'

class Other_Seasoning_Trees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Seasoning_Trees
        fields = '__all__'

class Other_Crops_Cultivated_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Other_Crops_Cultivated
        fields = '__all__'

class Condition_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class Nutmeg_Land_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nutmeg_Land
        fields = '__all__'

class Nutmeg_Frequency_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nutmeg_Frequency
        fields = '__all__'

class Potential_Risks_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Potential_Risks
        fields = '__all__'

class Policy_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class Road_Access_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Road_Access
        fields = '__all__'

class Food_Safety_and_Quality_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Safety_and_Quality
        fields = '__all__'

class Farm_Water_Source_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farm_Water_Source
        fields = '__all__'

class Farm_House_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Farm_House
        fields = '__all__'

class inspector_symmary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = inspector_symmary
        fields = '__all__'

class visit_Serializer(serializers.ModelSerializer):
    class Meta:
        model = visit
        fields = '__all__'

class In_House_Drying_Serializer(serializers.ModelSerializer):
    class Meta:
        model = In_House_Drying
        fields = '__all__'

class Dispatch_Of_Dried_Nutmeg_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch_Of_Dried_Nutmeg
        fields = '__all__'

class Dispatch_Of_Green_Nutmeg_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch_Of_Green_Nutmeg
        fields = '__all__'

class Cracking_Summary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cracking_Summary
        fields = '__all__'

class Floation_Summary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Floation_Summary
        fields = '__all__'

class Package_Ciontrol_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Package_Ciontrol
        fields = '__all__'

class Editors_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Editors
        fields = '__all__'

class Labour_support_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Labour_support
        fields = '__all__'

class Training_support_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training_support
        fields = '__all__'



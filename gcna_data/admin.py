from django.contrib import admin
# from .models import User_info
# from .models import Land_tenurship 
# from .models import tree 
# from .models import farm 
# from .models import state 
# from .models import symmary 
# from .models import fullform 
from .models import crop 
from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 


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
from .models import Worker_Info 

from .models import Editors


from import_export.admin import ImportExportModelAdmin


from .models import In_House_Drying 
from .models import Dispatch_Of_Dried_Nutmeg 
from .models import Dispatch_Of_Green_Nutmeg 
from .models import Cracking_Summary 
from .models import Floation_Summary 
from .models import Package_Ciontrol 
from .models import Labour_support 
from .models import Training_support 
from .models import visit 








# admin.site.register(User_info)
# admin.site.register(Land_tenurship)
# admin.site.register(tree)
# admin.site.register(farm)
# admin.site.register(state)
# admin.site.register(symmary)
# admin.site.register(fullform)

admin.site.register(visit)

admin.site.register(crop)
admin.site.register(Dried_Moisture_Analysis_A)
admin.site.register(Dried_Moisture_Analysis_B)
admin.site.register(Floated_Moisture_Analysis_A)
admin.site.register(Floated_Moisture_Analysis_B)
admin.site.register(Quality_Control)


admin.site.register(Editors)



admin.site.register(Farmer_Info)
admin.site.register(Worker_Info)
admin.site.register(land_info)
admin.site.register(Land_Tenur)
admin.site.register(Nutmeg_Trees)
admin.site.register(Nutmeg_Variety)
admin.site.register(Other_Crops)
admin.site.register(Coconut_Trees)
admin.site.register(Citrus_Mango_Trees)
admin.site.register(Other_Spices_Trees)
admin.site.register(Other_Seasoning_Trees)
admin.site.register(Other_Crops_Cultivated)
admin.site.register(Condition)
admin.site.register(Nutmeg_Land)
admin.site.register(Nutmeg_Frequency)
admin.site.register(Potential_Risks)
admin.site.register(Policy)
admin.site.register(Road_Access)
admin.site.register(Food_Safety_and_Quality)
admin.site.register(Farm_Water_Source)
admin.site.register(Farm_House)
admin.site.register(inspector_symmary)



admin.site.register(Labour_support)
admin.site.register(Training_support)



admin.site.register(In_House_Drying)
admin.site.register(Dispatch_Of_Dried_Nutmeg)
admin.site.register(Dispatch_Of_Green_Nutmeg)
admin.site.register(Cracking_Summary)
admin.site.register(Floation_Summary)
admin.site.register(Package_Ciontrol)

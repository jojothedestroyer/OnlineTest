from django.shortcuts import render
import calendar
from tablib import Dataset
from calendar import HTMLCalendar 
from datetime import datetime


from django.http import HttpResponseRedirect
from .resources import fullformResources
from .resources import Dried_Form_A_Resources
from .resources import Dried_Form_B_Resources
from .resources import Floated_Form_A_Resources
from .resources import Floated_Form_B_Resources
from .resources import Quality_Control_Resources
from django.forms import modelformset_factory
from django.shortcuts import render, redirect


import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponse
# from .forms import Full_Form

from .forms import Dried_Form_A 
from .forms import Dried_Form_B 
from .forms import Floated_Form_A 
from .forms import Floated_Form_B 
from .forms import Quality_Form 
from .models import land_info
from .forms import land_info_Form

from .models import Dried_Moisture_Analysis_A 
from .models import Dried_Moisture_Analysis_B 
from .models import Floated_Moisture_Analysis_A 
from .models import Floated_Moisture_Analysis_B 
from .models import Quality_Control 




# from .forms import User_info_Form 
# from .forms import Land_tenurship_Form 
# from .forms import tree_Form 
# from .forms import farm_Form 
# from .forms import state_Form 
# from .forms import symmary_Form 







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







from .forms import Farmer_Info_Form
from .forms import land_info_Form
from .forms import Land_Tenur_Form
from .forms import Nutmeg_Trees_Form
from .forms import Nutmeg_Variety_Form
from .forms import Other_Crops_Form
from .forms import Coconut_Trees_Form
from .forms import Citrus_Mango_Trees_Form
from .forms import Other_Spices_Trees_Form
from .forms import Other_Seasoning_Trees_Form
from .forms import Other_Crops_Cultivated_Form

from .forms import Condition_Form
from .forms import Nutmeg_Land_Form
from .forms import Nutmeg_Frequency_Form
from .forms import Potential_Risks_Form
from .forms import Policy_Form
from .forms import Road_Access_Form
from .forms import Food_Safety_and_Quality_Form
from .forms import Farm_Water_Source_Form
from .forms import Farm_House_Form
from .forms import inspector_symmary_Form





from .forms import Labour_support_Form
from .forms import Training_support_Form

from .models import visit 


from .forms import visit_Form 



from .models import In_House_Drying 
from .models import Dispatch_Of_Dried_Nutmeg 
from .models import Dispatch_Of_Green_Nutmeg 
from .models import Cracking_Summary 
from .models import Floation_Summary 
from .models import Package_Ciontrol 




from .forms import In_House_Drying_Form 
from .forms import Dispatch_Of_Dried_Nutmeg_Form 
from .forms import Dispatch_Of_Green_Nutmeg_Form 
from .forms import Cracking_Summary_Form 
from .forms import Floation_Summary_Form 
from .forms import Package_Ciontrol_Form 


from .forms import LoginForm


from .models import Editors 

from .models import Labour_support 
from .models import Training_support 




# from .serializers import Dried_Moisture_Analysis_A_Serializer 
# from .serializers import Dried_Moisture_Analysis_B_Serializer 
# from .serializers import Floated_Moisture_Analysis_A_Serializer 
# from .serializers import Floated_Moisture_Analysis_B_Serializer 
# from .serializers import Quality_Control_Serializer 
# from .serializers import Worker_Info_Serializer 
# from .serializers import Farmer_Info_Serializer 

from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Dried_Moisture_Analysis_A_Serializer
from .serializers import Dried_Moisture_Analysis_B_Serializer 
from .serializers import Floated_Moisture_Analysis_A_Serializer 
from .serializers import Floated_Moisture_Analysis_B_Serializer 
from .serializers import Quality_Control_Serializer 
from .serializers import Worker_Info_Serializer 
from .serializers import Farmer_Info_Serializer 
from .serializers import land_info_Serializer 
from .serializers import Land_Tenur_Serializer 
from .serializers import Nutmeg_Trees_Serializer 
from .serializers import Nutmeg_Variety_Serializer 
from .serializers import Other_Crops_Serializer 
from .serializers import Coconut_Trees_Serializer 
from .serializers import Citrus_Mango_Trees_Serializer 
from .serializers import Other_Spices_Trees_Serializer 
from .serializers import Other_Seasoning_Trees_Serializer 
from .serializers import Other_Crops_Cultivated_Serializer 
from .serializers import Condition_Serializer 
from .serializers import Nutmeg_Land_Serializer 
from .serializers import Nutmeg_Frequency_Serializer 
from .serializers import Potential_Risks_Serializer 
from .serializers import Policy_Serializer 
from .serializers import Road_Access_Serializer 
from .serializers import Food_Safety_and_Quality_Serializer 
from .serializers import Farm_Water_Source_Serializer 
from .serializers import Farm_House_Serializer
from .serializers import inspector_symmary_Serializer 












from .serializers import visit_Serializer 
from .serializers import In_House_Drying_Serializer 
from .serializers import Dispatch_Of_Dried_Nutmeg_Serializer 
from .serializers import Dispatch_Of_Green_Nutmeg_Serializer 
from .serializers import Cracking_Summary_Serializer 
from .serializers import Floation_Summary_Serializer 
from .serializers import Package_Ciontrol_Serializer 
from .serializers import Editors_Serializer 
from .serializers import Labour_support_Serializer 
from .serializers import Training_support_Serializer 

from .serializers import Policy_Serializer 
from django.forms.models import model_to_dict





class Policy_CreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer



class Dried_Moisture_Analysis_A_CreateView(generics.ListCreateAPIView):
    queryset = Dried_Moisture_Analysis_A.objects.all()
    serializer_class = Dried_Moisture_Analysis_A_Serializer

class Dried_Moisture_Analysis_B_CreateView(generics.ListCreateAPIView):
    queryset = Dried_Moisture_Analysis_B.objects.all()
    serializer_class = Dried_Moisture_Analysis_B_Serializer

class Floated_Moisture_Analysis_A_CreateView(generics.ListCreateAPIView):
    queryset = Floated_Moisture_Analysis_A.objects.all()
    serializer_class = Floated_Moisture_Analysis_A_Serializer

class Floated_Moisture_Analysis_B_CreateView(generics.ListCreateAPIView):
    queryset = Floated_Moisture_Analysis_B.objects.all()
    serializer_class = Floated_Moisture_Analysis_B_Serializer


class Quality_Control_CreateView(generics.ListCreateAPIView):
    queryset = Quality_Control.objects.all()
    serializer_class = Quality_Control_Serializer


class Worker_Info_CreateView(generics.ListCreateAPIView):
    queryset = Worker_Info.objects.all()
    serializer_class = Worker_Info_Serializer



class Farmer_Info_CreateView(generics.ListCreateAPIView):
    queryset = Farmer_Info.objects.all()
    serializer_class = Farmer_Info_Serializer







class VisitView(generics.RetrieveUpdateDestroyAPIView):
    queryset = visit.objects.all()
    serializer_class = visit_Serializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.id in indexeddb_ids:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class visit_CreateView(generics.ListCreateAPIView):
    queryset = visit.objects.all()
    serializer_class = visit_Serializer
		
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = model_to_dict(instance)
        for key, value in request.data.items():
            if key in data:
                data[key] = value
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class In_House_Drying_CreateView(generics.ListCreateAPIView):
    queryset = In_House_Drying.objects.all()
    serializer_class = In_House_Drying_Serializer

class Dispatch_Of_Dried_Nutmeg_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Dried_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Dried_Nutmeg_Serializer

class Dispatch_Of_Green_Nutmeg_CreateView(generics.ListCreateAPIView):
    queryset = Dispatch_Of_Green_Nutmeg.objects.all()
    serializer_class = Dispatch_Of_Green_Nutmeg_Serializer

class Cracking_Summary_CreateView(generics.ListCreateAPIView):
    queryset = Cracking_Summary.objects.all()
    serializer_class = Cracking_Summary_Serializer

class Floation_Summary_CreateView(generics.ListCreateAPIView):
    queryset = Floation_Summary.objects.all()
    serializer_class = Floation_Summary_Serializer

class Package_Ciontrol_CreateView(generics.ListCreateAPIView):
    queryset = Package_Ciontrol.objects.all()
    serializer_class = Package_Ciontrol_Serializer

class Editors_CreateView(generics.ListCreateAPIView):
    queryset = Editors.objects.all()
    serializer_class = Editors_Serializer

class Labour_support_CreateView(generics.ListCreateAPIView):
    queryset = Labour_support.objects.all()
    serializer_class = Labour_support_Serializer

class Training_support_CreateView(generics.ListCreateAPIView):
    queryset = Training_support.objects.all()
    serializer_class = Training_support_Serializer






class land_info_CreateView(generics.ListCreateAPIView):
    queryset = land_info.objects.all()
    serializer_class = land_info_Serializer


class Land_Tenur_CreateView(generics.ListCreateAPIView):
    queryset = Land_Tenur.objects.all()
    serializer_class = Land_Tenur_Serializer


class Nutmeg_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Trees.objects.all()
    serializer_class = Nutmeg_Trees_Serializer

class Nutmeg_Variety_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Variety.objects.all()
    serializer_class = Nutmeg_Variety_Serializer

class Other_Crops_CreateView(generics.ListCreateAPIView):
    queryset = Other_Crops.objects.all()
    serializer_class = Other_Crops_Serializer


class Coconut_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Coconut_Trees.objects.all()
    serializer_class = Coconut_Trees_Serializer


class Citrus_Mango_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Citrus_Mango_Trees.objects.all()
    serializer_class = Citrus_Mango_Trees_Serializer



class Other_Spices_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Other_Spices_Trees.objects.all()
    serializer_class = Other_Spices_Trees_Serializer
    
    
    
class Other_Seasoning_Trees_CreateView(generics.ListCreateAPIView):
    queryset = Other_Seasoning_Trees.objects.all()
    serializer_class = Other_Seasoning_Trees_Serializer


class Other_Crops_Cultivated_CreateView(generics.ListCreateAPIView):
    queryset = Other_Crops_Cultivated.objects.all()
    serializer_class = Other_Crops_Cultivated_Serializer


class Condition_CreateView(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = Condition_Serializer



class Nutmeg_Land_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Land.objects.all()
    serializer_class = Nutmeg_Land_Serializer
    
    
    
class Nutmeg_Frequency_CreateView(generics.ListCreateAPIView):
    queryset = Nutmeg_Frequency.objects.all()
    serializer_class = Nutmeg_Frequency_Serializer


class Potential_Risks_CreateView(generics.ListCreateAPIView):
    queryset = Potential_Risks.objects.all()
    serializer_class = Potential_Risks_Serializer


class Policy_CreateView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = Policy_Serializer



class Road_Access_CreateView(generics.ListCreateAPIView):
    queryset = Road_Access.objects.all()
    serializer_class = Road_Access_Serializer
    
    
class Food_Safety_and_Quality_CreateView(generics.ListCreateAPIView):
    queryset = Food_Safety_and_Quality.objects.all()
    serializer_class = Food_Safety_and_Quality_Serializer


class Farm_Water_Source_CreateView(generics.ListCreateAPIView):
    queryset = Farm_Water_Source.objects.all()
    serializer_class = Farm_Water_Source_Serializer


class Farm_House_CreateView(generics.ListCreateAPIView):
    queryset = Farm_House.objects.all()
    serializer_class = Farm_House_Serializer



class inspector_symmary_CreateView(generics.ListCreateAPIView):
    queryset = inspector_symmary.objects.all()
    serializer_class = inspector_symmary_Serializer













import json
from django.http import JsonResponse
from .models import Farmer_Info

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Farmer_Info
import json

@csrf_exempt
def sync_data_to_server(request):
    if request.method == 'POST':
        try:
            # Get the data from the request and deserialize JSON
            data = json.loads(request.body)

            # Update the Django database with the received data
            # For example, you can create or update records in the Farmer_Info model
            farmer, created = Farmer_Info.objects.get_or_create(pk=data['id'])
            farmer.field1 = data['field1']
            farmer.field2 = data['field2']
            # Add more fields as needed
            farmer.save()

            return JsonResponse({'message': 'Data synced with the server'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'message': 'Only POST requests are supported'}, status=405)



def edit_Visit(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = visit.objects.get(Nutmeg_ID_No=farmer_info_id)
    except visit.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = visit_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = visit_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})











def view_Visit(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = visit.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except visit.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm_24.html',context)














def view_Training(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Training_support.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except Training_support.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm_22.html',context)









def view_labour(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Labour_support.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Labour_support.DoesNotExist:
		return redirect('error_table23')  



	return render(request, 'gcna/view_farm_23.html',context)







def edit_Training(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Training_support.DoesNotExist:
        return redirect('error_table22')  

    if request.method == 'POST':
        form = Training_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Training_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def edit_labour(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Labour_support.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = Labour_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Labour_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})

















def view_Training0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
	

	try:
		farmer_info_id = Training_support.objects.all()
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except Training_support.DoesNotExist:
		return redirect('error_table22')  


	return render(request, 'gcna/view_farm0_22.html',context)









def view_labour0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
		

	try:
		farmer_info_id = Labour_support.objects.all()
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Labour_support.DoesNotExist:
		return redirect('error_table23')  



	return render(request, 'gcna/view_farm0_23.html',context)







def edit_Training0(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Training_support.DoesNotExist:
        return redirect('error_table22')  

    if request.method == 'POST':
        form = Training_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Training_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def edit_labour0(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Labour_support.DoesNotExist:
        return redirect('error_table23')  

    if request.method == 'POST':
        form = Labour_support_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('table') 
    else:
        form = Labour_support_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})








def offline_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query your IndexedDB to check if the user's credentials match
        # the data stored in IndexedDB
        matching_data = YourIndexedDBQuery(username, password)

        if matching_data:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})









class EditorChartView(TemplateView):
    template_name = 'gcna/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        return context

     



def bar_chart(request):
    editors = Editors.objects.all()

    editor_names = []
    num_users = []

    for editor in editors:
        editor_names.append(editor.editor_name)
        num_users.append(editor.num_users)

    context = {
        'editor_names': editor_names,
        'num_users': num_users,
    }

    return render(request, 'gcna/bar_chart.html', context)




def bar_chart1(request):
    data = Dried_Moisture_Analysis_A.objects.all()

    nutmeg_ids = []
    sample_weights = []

    for entry in data:
        nutmeg_ids.append(entry.Nutmeg_ID_No)
        sample_weights.append(int(entry.Final_Sample_Weight))

    context = {
        'nutmeg_ids': nutmeg_ids,
        'sample_weights': sample_weights,
    }

    return render(request, 'gcna/bar_chart1.html', context)






def error_table0(request):

	return render(request, 'gcna/error_table0.html')


def error_table1(request):

	return render(request, 'gcna/error_table1.html')


def error_table2(request):

	return render(request, 'gcna/error_table2.html')


def error_table3(request):

	return render(request, 'gcna/error_table3.html')


def error_table4(request):

	return render(request, 'gcna/error_table4.html')


def error_table5(request):

	return render(request, 'gcna/error_table5.html')


def error_table6(request):

	return render(request, 'gcna/error_table6.html')


def error_table7(request):

	return render(request, 'gcna/error_table7.html')


def error_table8(request):

	return render(request, 'gcna/error_table8.html')


def error_table9(request):

	return render(request, 'gcna/error_table9.html')


def error_table10(request):

	return render(request, 'gcna/error_table10.html')


def error_table11(request):

	return render(request, 'gcna/error_table11.html')


def error_table12(request):

	return render(request, 'gcna/error_table12.html')


def error_table13(request):

	return render(request, 'gcna/error_table13.html')


def error_table14(request):

	return render(request, 'gcna/error_table14.html')


def error_table15(request):

	return render(request, 'gcna/error_table15.html')


def error_table16(request):

	return render(request, 'gcna/error_table16.html')


def error_table17(request):

	return render(request, 'gcna/error_table17.html')


def error_table18(request):

	return render(request, 'gcna/error_table18.html')


def error_table19(request):

	return render(request, 'gcna/error_table19.html')


def error_table20(request):

	return render(request, 'gcna/error_table20.html')


def error_table21(request):

	return render(request, 'gcna/error_table21.html')



def error_table22(request):

	return render(request, 'gcna/error_table22.html')


def error_table23(request):

	return render(request, 'gcna/error_table23.html')


def error_table24(request):

	return render(request, 'gcna/error_table24.html')




def error_table_driedA(request):

	return render(request, 'gcna/error_table_driedA.html')



def error_table_driedB(request):

	return render(request, 'gcna/error_table_driedB.html')



def error_table_floatA(request):

	return render(request, 'gcna/error_table_floatA.html')



def error_table_floatB(request):

	return render(request, 'gcna/error_table_floatB.html')



def error_table_quality(request):

	return render(request, 'gcna/error_table_quality.html')






def error_In_House(request):

	return render(request, 'gcna/error_In_House_Form.html')



def error_Dispatch_Dried_Nutmeg(request):

	return render(request, 'gcna/error_Dispatch_Dried_Nutmeg_Form.html')



def error_Dispatch_Green_Nutmeg(request):

	return render(request, 'gcna/error_Dispatch_Green_Nutmeg_Form.html')



def error_Cracking_Nutmeg(request):

	return render(request, 'gcna/error_Cracking_Nutmeg_Form.html')



def error_Floation(request):

	return render(request, 'gcna/error_Floation_Form.html')



def error_Package(request):

	return render(request, 'gcna/error_Package_Form.html')













def error_In_House_0(request):

	return render(request, 'gcna/error_In_House_Form_0.html')


                                      
def error_Dispatch_Dried_Nutmeg_0(request):

	return render(request, 'gcna/error_Dispatch_Dried_Nutmeg_Form_0.html')



def error_Dispatch_Green_Nutmeg_0(request):

	return render(request, 'gcna/error_Dispatch_Green_Nutmeg_Form_0.html')



def error_Cracking_Nutmeg_0(request):

	return render(request, 'gcna/error_Cracking_Nutmeg_Form_0.html')



def error_Floation_0(request):

	return render(request, 'gcna/error_Floation_Form_0.html')



def error_Package_0(request):

	return render(request, 'gcna/error_Package_Form_0.html')









def edit_table21(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except inspector_symmary.DoesNotExist:
		return redirect('error_table21')  

	if request.method == 'POST':
		form = inspector_symmary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table21') 
	else:
		form = inspector_symmary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table21.html', {'form': form})





def display_table_data21(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except inspector_symmary.DoesNotExist:
		return redirect('error_table21')

	return render(request, 'gcna/view_table21.html', context)















def edit_table20(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farm_House.DoesNotExist:
		return redirect('error_table20')  

	if request.method == 'POST':
		form = Farm_House_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table20') 
	else:
		form = Farm_House_Form(instance=farmer_info_id)





	return render(request, 'gcna/edit_table20.html', {'form': form})



def display_table_data20(request):

	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Farm_House.DoesNotExist:
		return redirect('error_table20')


	return render(request, 'gcna/view_table20.html', context)
















def edit_table19(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farm_Water_Source.DoesNotExist:
		return redirect('error_table19')  

	if request.method == 'POST':
		form = Farm_Water_Source_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table19') 
	else:
		form = Farm_Water_Source_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table19.html', {'form': form})



def display_table_data19(request):

	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Farm_Water_Source.DoesNotExist:
		return redirect('error_table19')


	return render(request, 'gcna/view_table19.html', context)

















def edit_table18(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Food_Safety_and_Quality.DoesNotExist:
		return redirect('error_table18')  

	if request.method == 'POST':
		form = Food_Safety_and_Quality_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table18') 
	else:
		form = Food_Safety_and_Quality_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table18.html', {'form': form})



def display_table_data18(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Food_Safety_and_Quality.DoesNotExist:
		return redirect('error_table18')


	return render(request, 'gcna/view_table18.html', context)














def edit_table17(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Road_Access.DoesNotExist:
		return redirect('error_table17')  

	if request.method == 'POST':
		form = Road_Access_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table17') 
	else:
		form = Road_Access_Form(instance=farmer_info_id)





	return render(request, 'gcna/edit_table17.html', {'form': form})



def display_table_data17(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Road_Access.DoesNotExist:
		return redirect('error_table17')


	return render(request, 'gcna/view_table17.html', context)














def edit_table16(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Policy.DoesNotExist:
		return redirect('error_table16')  

	if request.method == 'POST':
		form = Policy_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table16') 
	else:
		form = Policy_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table16.html', {'form': form})



def display_table_data16(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Policy.DoesNotExist:
		return redirect('error_table16')

	return render(request, 'gcna/view_table16.html', context)















def edit_table15(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Potential_Risks.DoesNotExist:
		return redirect('error_table15')  

	if request.method == 'POST':
		form = Potential_Risks_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table15') 
	else:
		form = Potential_Risks_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table15.html', {'form': form})



def display_table_data15(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Potential_Risks.DoesNotExist:
		return redirect('error_table15')


	return render(request, 'gcna/view_table15.html', context)

















def edit_table14(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Frequency.DoesNotExist:
		return redirect('error_table14')  

	if request.method == 'POST':
		form = NNutmeg_Frequency_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table14') 
	else:
		form = Nutmeg_Frequency_Cultivated_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table14.html', {'form': form})



def display_table_data14(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Nutmeg_Frequency.DoesNotExist:
		return redirect('error_table14')



	return render(request, 'gcna/view_table14.html', context)






















def edit_table13(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Land.DoesNotExist:
		return redirect('error_table13')  

	if request.method == 'POST':
		form = Nutmeg_Land_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table13') 
	else:
		form = Nutmeg_Land_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table13.html', {'form': form})



def display_table_data13(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Nutmeg_Land.DoesNotExist:
		return redirect('error_table13')


	return render(request, 'gcna/view_table13.html', context)




















def edit_table12(request):
	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Condition.DoesNotExist:
		return redirect('error_table12')  

	if request.method == 'POST':
		form = Condition_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table12') 
	else:
		form = Other_Crops_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table12.html', {'form': form})



def display_table_data12(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Condition.DoesNotExist:
		return redirect('error_table12')


	return render(request, 'gcna/view_table12.html', context)

























def edit_table11(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Crops_Cultivated.DoesNotExist:
		return redirect('error_table11')  

	if request.method == 'POST':
		form = Other_Crops_Cultivated_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table11') 
	else:
		form = Other_Crops_Cultivated_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table11.html', {'form': form})



def display_table_data11(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Other_Crops_Cultivated.DoesNotExist:
		return redirect('error_table11')




	return render(request, 'gcna/view_table11.html', context)
















def edit_table10(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Seasoning_Trees.DoesNotExist:
		return redirect('error_table10')  

	if request.method == 'POST':
		form = Other_Seasoning_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table10') 
	else:
		form = Other_Seasoning_Trees_Form(instance=farmer_info_id)




	return render(request, 'gcna/edit_table10.html', {'form': form})



def display_table_data10(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Other_Seasoning_Trees.DoesNotExist:
		return redirect('error_table10')


	return render(request, 'gcna/view_table10.html', context)




















def edit_table9(request):



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Other_Spices_Trees.DoesNotExist:
		return redirect('error_table9')  

	if request.method == 'POST':
		form = Other_Spices_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table9') 
	else:
		form = Other_Spices_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table9.html', {'form': form})



def display_table_data9(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Other_Spices_Trees.DoesNotExist:
		return redirect('error_table9')


	return render(request, 'gcna/view_table9.html', context)










def edit_table8(request):




	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Citrus_Mango_Trees.DoesNotExist:
		return redirect('error_table8')  

	if request.method == 'POST':
		form = Citrus_Mango_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table8') 
	else:
		form = Citrus_Mango_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table8.html', {'form': form})


def display_table_data8(request):


	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Citrus_Mango_Trees.DoesNotExist:
		return redirect('error_table8')



	return render(request, 'gcna/view_table8.html', context)















def edit_table7(request):



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Coconut_Trees.DoesNotExist:
		return redirect('error_table7')  

	if request.method == 'POST':
		form = Coconut_Trees_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table7') 
	else:
		form = Coconut_Trees_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table7.html', {'form': form})



def display_table_data7(request):


	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Coconut_Trees.DoesNotExist:
		return redirect('error_table7')


	return render(request, 'gcna/view_table7.html', context)
















def edit_table6(request):


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)

	except Other_Crops.DoesNotExist:
		return redirect('error_table6')  

	if request.method == 'POST':
		form = Other_Crops_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table6') 
	else:
		form = Other_Crops_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table6.html', {'form': form})



def display_table_data6(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Other_Crops.DoesNotExist:
		return redirect('error_table6')


	return render(request, 'gcna/view_table6.html', context)





# def display_table_data_null_field(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
	    farmer_info_list = Other_Crops.objects.filter(Nutmeg_ID_No=farmer_info_id)
	    context = {
	        'farmer_info_list': farmer_info_list
	    }

	except Other_Crops.DoesNotExist:
	    return redirect('error_table6')


	return render(request, 'gcna/view_table6.html', context)





def edit_table5(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Nutmeg_Variety.DoesNotExist:
		return redirect('error_table5')  

	if request.method == 'POST':
		form = Nutmeg_Variety_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table5') 
	else:
		form = Nutmeg_Variety_Form(instance=farmer_info_id)



	return render(request, 'gcna/edit_table5.html', {'form': form})



def display_table_data5(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Nutmeg_Variety.DoesNotExist:
		return redirect('error_table5')


	return render(request, 'gcna/view_table5.html', context)








def edit_table4(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Nutmeg_Trees.DoesNotExist:
        return redirect('error_table4')  

    if request.method == 'POST':
        form = Nutmeg_Trees_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('edit_table4') 
    else:
        form = Nutmeg_Trees_Form(instance=farmer_info_id)




    return render(request, 'gcna/edit_table4.html', {'form': form})











def display_table_data4(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Nutmeg_Trees.DoesNotExist:
		return redirect('error_table4')


	return render(request, 'gcna/view_table4.html', context)






def edit_table3(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')
    try:
        farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
    except Land_Tenur.DoesNotExist:
        return redirect('error_table3')  

    if request.method == 'POST':
        form = Land_Tenur_Form(request.POST, instance=farmer_info_id)
        if form.is_valid():
            form.save()
            return redirect('edit_table3') 
    else:
        form = Land_Tenur_Form(instance=farmer_info_id)
    return render(request, 'gcna/edit_table3.html', {'form': form})






def display_table_data3(request):

	farmer_info_id = request.session['Nutmeg_ID_No']
	try:
		farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Land_Tenur.DoesNotExist:
		return redirect('error_table3')


	return render(request, 'gcna/view_table3.html', context)












def edit_table2(request):
    farmer_info_id = request.session.get('Nutmeg_ID_No')

    try:
        farmer_info_entries = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
    except land_info.DoesNotExist:
        return redirect('error_table2')

    LandInfoFormSet = modelformset_factory(land_info, form=land_info_Form, extra=0)

    if request.method == 'POST':
        formset = LandInfoFormSet(request.POST, queryset=farmer_info_entries)
        if formset.is_valid():
            formset.save()
            return redirect('edit_table2')
    else:
        formset = LandInfoFormSet(queryset=farmer_info_entries)

    return render(request, 'gcna/edit_table2.html', {'formset': formset})







def display_table_data2(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except land_info.DoesNotExist:
		return redirect('error_table2')


	return render(request, 'gcna/view_table2.html', context)












def edit_table1(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Farmer_Info.DoesNotExist:
		return redirect('error_table1')  

	if request.method == 'POST':
		form = Farmer_Info_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('edit_table1') 
	else:
		form = Farmer_Info_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_table1.html', {'form': form})

def display_table_data1(request):
	farmer_info_id = request.session['Nutmeg_ID_No']
        
	try:
		farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}


	except Farmer_Info.DoesNotExist:
		return redirect('error_table1')


	return render(request, 'gcna/view_table1.html', context)


def table(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = land_info.objects.filter(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except land_info.DoesNotExist:
		pass


	return render(request, 'gcna/table_of_contents.html',context)


def Initial(request):


        
	return render(request, 'gcna/Initial_Form.html')

def rev_data00(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)           

        if form.is_valid():
            request.session['Worker_ID_No'] =  form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']


            Worker_ID_No=request.session['Worker_ID_No']
            Nutmeg_ID_No=request.session['Nutmeg_ID_No']


            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:

                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id


                return render(request, 'gcna/adhome.html',{'Worker_ID_No_id':Worker_ID_No_id})  
            
            else:

                return redirect('error_table0')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/adhome.html', context)




def add_to_session(request):
    if request.method == 'POST':
        farm_type = request.POST.get('farm_type')
        tenurship = request.POST.get('tenurship')
        training = request.POST.get('training')
        parish = request.POST.get('parish')
        village = request.POST.get('village')
        visit = request.POST.get('visit')
        # Get other field values if needed

        # Add the data to the session
        request.session['farm_type'] = farm_type
        request.session['tenurship'] = tenurship
        request.session['training'] = training
        request.session['parish'] = parish
        request.session['village'] = village
        request.session['visit'] = visit

 

        # Add other field values to the session
        
        return redirect('table')  
    else:
        return redirect('table001')  


 

from django.shortcuts import render, redirect
from .models import Worker_Info
from .forms import LoginForm




# def rev_data0(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)           

#         if form.is_valid():
#             request.session['Worker_ID_No'] =  form.cleaned_data['Worker_ID_No']
#             request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']


#             Worker_ID_No=request.session['Worker_ID_No']
#             Nutmeg_ID_No=request.session['Nutmeg_ID_No']



#             check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

#             if check2:

#                 Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
#                 Worker_ID_No_id = Worker_ID_No.id

#                 return redirect('table001')  
 
            
#             else:

#                 return redirect('error_table0_0')
#     else:
#         form = LoginForm()

#     context = {
#         'form': form,
#     }

#     return render(request, 'gcna/login.html', context)

    # form = LoginForm()
    # context = {'form': form}
    # return render(request, 'gcna/login.html', context)





def rev_data0(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session['Worker_ID_No'] = form.cleaned_data['Worker_ID_No']
            request.session['Nutmeg_ID_No'] = form.cleaned_data['Nutmeg_ID_No']

            Worker_ID_No = request.session['Worker_ID_No']
            Nutmeg_ID_No = request.session['Nutmeg_ID_No']

            check2 = Worker_Info.objects.filter(Worker_ID_No=Worker_ID_No).first()

            if check2:
                Worker_ID_No = Worker_Info.objects.get(Worker_ID_No=Worker_ID_No)
                Worker_ID_No_id = Worker_ID_No.id

                return redirect('table001')
            else:
                return redirect('error_table0_0')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/login.html', context)

def rev_data3230(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            request.session['Nutmeg_ID_No'] =  form.cleaned_data['Nutmeg_ID_No']
            request.session['name'] =  form.cleaned_data['name']

            return redirect('table')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'gcna/login.html', context)


# def second_page(request):
#     if request.method == 'POST':
#         form = Form2(request.POST)
# 		if form.is_valid():

#     else:
#         form = Form2()


#         if 'farmer_name' in request.session:
#             form.fields['name'].initial = request.session['farmer_name']
#         if 'farmer_address' in request.session:
#             form.fields['address'].initial = request.session['farmer_address']

#     context = {
#         'form': form,
#     }

#     return render(request, 'second_page.html', context)



def signin(request):
	submitted = False
	if request.method == "POST":
		form = Farmer_Info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/table')
	else:
		form = Farmer_Info_Form()



		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']
		if 'name' in request.session:
			form.fields['name'].initial = request.session['name']

	return render(request,'gcna/signin.html',{
		'form':form,
		'submitted':submitted})





def deny_entry(request):

	return render(request, 'gcna/deny_entry.html')




def rev_data1(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farmer_Info.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farmer_Info.DoesNotExist:


		if request.method == "POST":
			form = Farmer_Info_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_1')
		else:
			form = Farmer_Info_Form()



			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'name' in request.session:
				form.fields['name'].initial = request.session['name']

	return render(request,'gcna/revform1.html',{
		'form':form,
		'submitted':submitted})




def rev_data2(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')


	if request.method == "POST":
		form = land_info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_2')
	else:
		form = land_info_Form()

	if 'Nutmeg_ID_No' in request.session:
		form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

	if 'Worker_ID_No' in request.session:
		form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

	 
	if 'submitted' in request.GET:
		submitted = True

	return render(request,'gcna/revform2.html',{
		'form':form,
		'submitted':submitted})


def rev_data3(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Land_Tenur.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Land_Tenur.DoesNotExist:


		if request.method == "POST":
			form = Land_Tenur_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_3')
		else:
			form = Land_Tenur_Form()


			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

			if 'farm_type' in request.session:
				form.fields['farm_type'].initial = request.session['farm_type']




			if 'parish' in request.session:
				form.fields['parish'].initial = request.session['parish']

			if 'tenurship' in request.session:
				form.fields['tenurship'].initial = request.session['tenurship']

			if 'training' in request.session:
				form.fields['training'].initial = request.session['training']

			if 'village' in request.session:
				form.fields['village'].initial = request.session['village']	


			if 'submitted' in request.GET:
				submitted = True
 
	return render(request,'gcna/revform3.html',{
		'form':form,
		'submitted':submitted})


def rev_data4(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Trees.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_4')
		else:
			form = Nutmeg_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform4.html',{
		'form':form,
		'submitted':submitted})





def rev_data5(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Variety.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Variety.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Variety_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_5')
		else:
			form = Nutmeg_Variety_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform5.html',{
		'form':form,
		'submitted':submitted})












def rev_data6(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Crops.DoesNotExist:




		if request.method == "POST":
			form = Other_Crops_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_6')
		else:
			form = Other_Crops_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform6.html',{
		'form':form,
		'submitted':submitted})






def rev_data7(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Coconut_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Coconut_Trees.DoesNotExist:



		if request.method == "POST":
			form = Coconut_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_7')
		else:
			form = Coconut_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform7.html',{
		'form':form,
		'submitted':submitted})




def rev_data8(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Citrus_Mango_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Citrus_Mango_Trees.DoesNotExist:


		if request.method == "POST":
			form = Citrus_Mango_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_8')
		else:
			form = Citrus_Mango_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform8.html',{
		'form':form,
		'submitted':submitted})





def rev_data9(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Spices_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Spices_Trees.DoesNotExist:




		if request.method == "POST":
			form = Other_Spices_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_9')
		else:
			form = Other_Spices_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform9.html',{
		'form':form,
		'submitted':submitted})







def rev_data10(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Seasoning_Trees.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Seasoning_Trees.DoesNotExist:



		if request.method == "POST":
			form = Other_Seasoning_Trees_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_10')
		else:
			form = Other_Seasoning_Trees_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform10.html',{
		'form':form,
		'submitted':submitted})
















def rev_data11(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Other_Crops_Cultivated.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Other_Crops_Cultivated.DoesNotExist:



		if request.method == "POST":
			form = Other_Crops_Cultivated_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_11')
		else:
			form = Other_Crops_Cultivated_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform11.html',{
		'form':form,
		'submitted':submitted})












def rev_data12(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Condition.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Condition.DoesNotExist:




		if request.method == "POST":
			form = Condition_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_12')
		else:
			form = Condition_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform12.html',{
		'form':form,
		'submitted':submitted})









def rev_data13(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Land.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Land.DoesNotExist:



		if request.method == "POST":
			form = Nutmeg_Land_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_13')
		else:
			form = Nutmeg_Land_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform13.html',{
		'form':form,
		'submitted':submitted})


def rev_data14(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Nutmeg_Frequency.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Nutmeg_Frequency.DoesNotExist:


		if request.method == "POST":
			form = Nutmeg_Frequency_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_14')
		else:
			form = Nutmeg_Frequency_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform14.html',{
		'form':form,
		'submitted':submitted})





def rev_data15(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Potential_Risks.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Potential_Risks.DoesNotExist:



		if request.method == "POST":
			form = Potential_Risks_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_15')
		else:
			form = Potential_Risks_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform15.html',{
		'form':form,
		'submitted':submitted})












def rev_data16(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Policy.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Policy.DoesNotExist:



		if request.method == "POST":
			form = Policy_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_16')
		else:
			form = Policy_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform16.html',{
		'form':form,
		'submitted':submitted})






def rev_data17(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Road_Access.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Road_Access.DoesNotExist:


		if request.method == "POST":
			form = Road_Access_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_17')
		else:
			form = Road_Access_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform17.html',{
		'form':form,
		'submitted':submitted})




def rev_data18(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Food_Safety_and_Quality.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Food_Safety_and_Quality.DoesNotExist:


		if request.method == "POST":
			form = Food_Safety_and_Quality_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_18')
		else:
			form = Food_Safety_and_Quality_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform18.html',{
		'form':form,
		'submitted':submitted})





def rev_data19(request):
	submitted = False

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_Water_Source.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farm_Water_Source.DoesNotExist:


		if request.method == "POST":
			form = Farm_Water_Source_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_19')
		else:
			form = Farm_Water_Source_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform19.html',{
		'form':form,
		'submitted':submitted})







def rev_data20(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Farm_House.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Farm_House.DoesNotExist:



		if request.method == "POST":
			form = Farm_House_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_20')
		else:
			form = Farm_House_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform20.html',{
		'form':form,
		'submitted':submitted})



def rev_data21(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except inspector_symmary.DoesNotExist:

	
		if request.method == "POST":
			form = inspector_symmary_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = inspector_symmary_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform21.html',{
		'form':form,
		'submitted':submitted})









def rev_data22(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Training_support.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Training_support.DoesNotExist:

	
		if request.method == "POST":
			form = Training_support_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = Training_support_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform22.html',{
		'form':form,
		'submitted':submitted})










def rev_data23(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Labour_support.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except Labour_support.DoesNotExist:

	
		if request.method == "POST":
			form = Labour_support_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_21')
		else:
			form = Labour_support_Form()

			if 'Nutmeg_ID_No' in request.session:
				form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

			if 'Worker_ID_No' in request.session:
				form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform23.html',{
		'form':form,
		'submitted':submitted})








def rev_data24(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = visit.objects.get(Nutmeg_ID_No=farmer_info_id)
		verify = farmer_info_id
		if verify == farmer_info_id:
			return redirect('deny_entry')
	except visit.DoesNotExist:

	
		if request.method == "POST":
			form = visit_Form(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/gcna00_24')
		else:
			form = visit_Form()



			if 'submitted' in request.GET:
				submitted = True

	return render(request,'gcna/revform24.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_22(request):
	submitted = False



	farmer_info_id = request.session.get('Nutmeg_ID_No')


	if request.method == "POST":
		form = Training_support_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_21')
	else:
		form = Training_support_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_22.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_23(request):
	submitted = False


	farmer_info_id = request.session.get('Nutmeg_ID_No')



	if request.method == "POST":
		form = Labour_support_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna00_21')
	else:
		form = Labour_support_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_23.html',{
		'form':form,
		'submitted':submitted})










def rev_data0_1(request):
	submitted = False
	if request.method == "POST":
		form = Farmer_Info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_1')
	else:
		form = Farmer_Info_Form()



		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



	return render(request,'gcna/revform0_1.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_2(request):
	submitted = False
	if request.method == "POST":
		form = land_info_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_2')
	else:
		form = land_info_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']

 
		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_2.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_3(request):
	submitted = False
	if request.method == "POST":
		form = Land_Tenur_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_3')
	else:
		form = Land_Tenur_Form()


		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_3.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_4(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_4')
	else:
		form = Nutmeg_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_4.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_5(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Variety_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_5')
	else:
		form = Nutmeg_Variety_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_5.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_6(request):
	submitted = False
	if request.method == "POST":
		form = Other_Crops_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_6')
	else:
		form = Other_Crops_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']


		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_6.html',{
		'form':form,
		'submitted':submitted})






def rev_data0_7(request):
	submitted = False
	if request.method == "POST":
		form = Coconut_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_7')
	else:
		form = Coconut_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_7.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_8(request):
	submitted = False
	if request.method == "POST":
		form = Citrus_Mango_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_8')
	else:
		form = Citrus_Mango_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_8.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_9(request):
	submitted = False
	if request.method == "POST":
		form = Other_Spices_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_9')
	else:
		form = Other_Spices_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_9.html',{
		'form':form,
		'submitted':submitted})







def rev_data0_10(request):
	submitted = False
	if request.method == "POST":
		form = Other_Seasoning_Trees_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_10')
	else:
		form = Other_Seasoning_Trees_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_10.html',{
		'form':form,
		'submitted':submitted})
















def rev_data0_11(request):
	submitted = False
	if request.method == "POST":
		form = Other_Crops_Cultivated_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_11')
	else:
		form = Other_Crops_Cultivated_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_11.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_12(request):
	submitted = False
	if request.method == "POST":
		form = Condition_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_12')
	else:
		form = Condition_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_12.html',{
		'form':form,
		'submitted':submitted})









def rev_data0_13(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Land_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_13')
	else:
		form = Nutmeg_Land_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_13.html',{
		'form':form,
		'submitted':submitted})


def rev_data0_14(request):
	submitted = False
	if request.method == "POST":
		form = Nutmeg_Frequency_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_14')
	else:
		form = Nutmeg_Frequency_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_14.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_15(request):
	submitted = False
	if request.method == "POST":
		form = Potential_Risks_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_15')
	else:
		form = Potential_Risks_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_15.html',{
		'form':form,
		'submitted':submitted})












def rev_data0_16(request):
	submitted = False
	if request.method == "POST":
		form = Policy_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_16')
	else:
		form = Policy_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_16.html',{
		'form':form,
		'submitted':submitted})






def rev_data0_17(request):
	submitted = False
	if request.method == "POST":
		form = Road_Access_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_17')
	else:
		form = Road_Access_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_17.html',{
		'form':form,
		'submitted':submitted})




def rev_data0_18(request):
	submitted = False
	if request.method == "POST":
		form = Food_Safety_and_Quality_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_18')
	else:
		form = Food_Safety_and_Quality_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_18.html',{
		'form':form,
		'submitted':submitted})





def rev_data0_19(request):
	submitted = False
	if request.method == "POST":
		form = Farm_Water_Source_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_19')
	else:
		form = Farm_Water_Source_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_19.html',{
		'form':form,
		'submitted':submitted})







def rev_data0_20(request):
	submitted = False
	if request.method == "POST":
		form = Farm_House_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_20')
	else:
		form = Farm_House_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_20.html',{
		'form':form,
		'submitted':submitted})



def rev_data0_21(request):
	submitted = False
	if request.method == "POST":
		form = inspector_symmary_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/0gcna00_21')
	else:
		form = inspector_symmary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/revform0_21.html',{
		'form':form,
		'submitted':submitted})














# def step1(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step1')
#         if form.is_valid():
#             request.session['step1_data'] = form.cleaned_data
#             return redirect('step2')
#     else:
#         form = Full_Form(prefix='step1')
#     return render(request, 'gcna/step1.html', {'form': form})

# def step2(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step2')
#         if form.is_valid():
#             step1_data = request.session.get('step1_data')
#             if step1_data:
#                 step1_data.update(form.cleaned_data)
#                 request.session['step1_data'] = step1_data
#             else:
#                 request.session['step1_data'] = form.cleaned_data
#             return redirect('step3')
#     else:
#         step1_data = request.session.get('step1_data')
#         form = Full_Form(step1_data, prefix='step2')
#     return render(request, 'gcna/step2.html', {'form': form})

# def step3(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST, prefix='step3')
#         if form.is_valid():
#             step1_data = request.session.get('step1_data')
#             if step1_data:
#                 step1_data.update(form.cleaned_data)
#                 form = Full_Form(step1_data, prefix='step3')
#                 if form.is_valid():
#                     form.save()
#                     del request.session['step1_data']
#                     return redirect('submit')
#     else:
#         step1_data = request.session.get('step1_data')
#         form = Full_Form(step1_data, prefix='step3')
#     return render(request, 'gcna/step3.html', {'form': form})

# def submit(request):
#     if request.method == 'POST':
#         # Process the submitted form data
#         form_data = request.session.get('step1_data')
#         if form_data:
#             form = Full_Form(form_data)
#             if form.is_valid():
#                 form.save()
#                 del request.session['step1_data']
#                 return render(request, 'gcna/submit.html', {'form_data': form_data})
#     return redirect('`````````````````')


# def export(request):
#     person_resource = Land_tenurshipResource()
#     dataset = person_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response

def import_exel(request):
    if request.method == 'POST':
        person_resource = fullformResources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = fullform(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5]



        		)
            value.save()       
        
 
    return render(request, 'gcna/import_form.html')



def import_dried_A_exel(request):
    if request.method == 'POST':
        person_resource = Dried_Form_A_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Dried_Moisture_Analysis_A(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_driedA.html')


def import_dried_B_exel(request):
    if request.method == 'POST':
        person_resource = Dried_Form_B_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Dried_Moisture_Analysis_B(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		)
            value.save()       
        


    return render(request, 'gcna/import_driedB.html')






def import_floated_A_exel(request):
    if request.method == 'POST':
        person_resource = Floated_Form_A_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Floated_Moisture_Analysis_A(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		data[24],
        		data[25],
        		data[26],
        		data[27],
        		data[28],
        		data[29],
        		data[30],
        		data[31],
        		data[32],
        		data[33],
        		data[34],
        		data[35],
        		data[36],
        		data[37],
        		data[38],
        		data[39],
        		data[40],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_floatedA.html')


def import_floated_B_exel(request):
    if request.method == 'POST':
        person_resource = Floated_Form_B_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Floated_Moisture_Analysis_B(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		data[21],
        		data[22],
        		data[23],
        		data[24],
        		data[25],
        		data[26],
        		data[27],
        		data[28],
        		data[29],
        		data[30],
        		data[31],
        		data[32],
        		data[33],
        		data[34],
        		data[35],
        		data[36],
        		data[37],
        		data[38],
        		data[39],
        		data[40],
        		data[41],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_floatedB.html')




def import_Quality_Control_exel(request):
    if request.method == 'POST':
        person_resource = Quality_Control_Resources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
            print(data[1])
            value = Quality_Control(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
        		data[4],
        		data[5],
        		data[6],
        		data[7],
        		data[8],
        		data[9],
        		data[10],
        		data[11],
        		data[12],
        		data[13],
        		data[14],
        		data[15],
        		data[16],
        		data[17],
        		data[18],
        		data[19],
        		data[20],
        		)
            value.save()       
        
 
    return render(request, 'gcna/import_quality.html')

 


# def form_start_view(request):
#     return redirect('page1_view')


def your_view(request):
    if request.method == 'POST':
        form1 = Form1(request.POST)
        form2 = Form2(request.POST)
        if form1.is_valid() and form2.is_valid():
            field1_value = form1.cleaned_data['field1']
            form2.cleaned_data['field2'] = field1_value  # Set field2 value based on field1
            # Further processing or saving of form data

    else:
        form1 = Form1()
        form2 = Form2()

    context = {
        'form1': form1,
        'form2': form2
    }

    return render(request, 'your_template.html', context)







def comp_data(request):
	submitted = False
	if request.method == "POST":
		form1 = User_info_Form(request.POST)
		form2 = Land_tenurship_Form(request.POST)
		form3 = tree_Form(request.POST)
		form4 = farm_Form(request.POST)
		form5 = state_Form(request.POST)
		form6 = symmary_Form(request.POST)

		if all([form1.is_valid(),form2.is_valid(),form3.is_valid(),form4.is_valid(),form5.is_valid()]):
			# field1_value = form1.cleaned_data['farmer_ID']   
			# form2.cleaned_data['farmer_ID'] = field1_value
			# form3.cleaned_data['farmer_ID'] = field1_value
			# form4.cleaned_data['farmer_ID'] = field1_value
			# form5.cleaned_data['farmer_ID'] = field1_value
			# form6.cleaned_data['farmer_ID'] = field1_value


			form1.save()
			form2.save()
			form3.save()
			form4.save()
			form5.save()
			form6.save()

			return HttpResponseRedirect('/gcna0')
 


	else:
		form1 = User_info_Form
		form2 = Land_tenurship_Form
		form3 = tree_Form
		form4 = farm_Form
		form5 = state_Form
		form6 = symmary_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform.html',{
		'form1':form1,
		'form2':form2,
		'form3':form3,
		'form4':form4,
		'form5':form5,
		'form6':form6,
		'submitted':submitted})




def comp_data1(request):
	submitted = False
	if request.method == "POST":
		form1 = User_info_Form(request.POST,request.FILES)
		if form1.is_valid():
			form1.save()
			return HttpResponseRedirect('/gcna0_1')
	else:
		form1 = User_info_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform1.html',{
		'form1':form1,
		'submitted':submitted})



def comp_data2(request):
	submitted = False
	if request.method == "POST":
		form2 = Land_tenurship_Form(request.POST)
		if form2.is_valid():
			form2.save()
			return HttpResponseRedirect('/gcna0_2')
	else:
		form2 = Land_tenurship_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform2.html',{
		'form2':form2,
		'submitted':submitted})


def comp_data3(request):
	submitted = False
	if request.method == "POST":
		form3 = tree_Form(request.POST)
		if form3.is_valid():
			form3.save()
			return HttpResponseRedirect('/gcna0_3')
	else:
		form3 = tree_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform3.html',{
		'form3':form3,
		'submitted':submitted})









def comp_data4(request):
	submitted = False
	if request.method == "POST":
		form4 = farm_Form(request.POST)
		if form4.is_valid():
			form4.save()
			return HttpResponseRedirect('/gcna0_4')
	else:
		form4 = farm_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform4.html',{
		'form4':form4,
		'submitted':submitted})





def comp_data5(request):
	submitted = False
	if request.method == "POST":
		form5 = state_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return HttpResponseRedirect('/gcna0_5')
	else:
		form5 = state_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform5.html',{
		'form5':form5,
		'submitted':submitted})





def comp_data6(request):
	submitted = False
	if request.method == "POST":
		form6 = symmary_Form(request.POST)
		if form6.is_valid():
			form6.save()
			return HttpResponseRedirect('/gcna0_6')
	else:
		form6 = symmary_Form

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/compform6.html',{
		'form6':form6,
		'submitted':submitted})






def add_data(request):
	submitted = False
	if request.method == "POST":
		form = Full_Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/gcna7')

	else:
		form = Full_Form
		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/fillform.html',{'form':form, 'submitted':submitted})


def Dried_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form1 = Dried_Form_A(request.POST)
		if form1.is_valid():
			form1.save()
			return HttpResponseRedirect('/gcna8')

	else:
		form1 = Dried_Form_A()

		if 'Nutmeg_ID_No' in request.session:
			form1.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form1.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/DriedA.html',{'form1':form1, 'submitted':submitted})











def Dried_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form2 = Dried_Form_B(request.POST)
		if form2.is_valid():
			form2.save()
			return HttpResponseRedirect('/gcna9')

	else:
		form2 = Dried_Form_B()

		if 'Nutmeg_ID_No' in request.session:
			form2.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form2.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/DriedB.html',{'form2':form2, 'submitted':submitted})








def Floated_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form3 = Floated_Form_A(request.POST)
		if form3.is_valid():
			form3.save()
			return HttpResponseRedirect('/gcna10')

	else:
		form3 = Floated_Form_A()

		if 'Nutmeg_ID_No' in request.session:
			form3.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form3.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/FloatA.html',{'form3':form3, 'submitted':submitted})







def Floated_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form4 = Floated_Form_B(request.POST)
		if form4.is_valid():
			form4.save()
			return HttpResponseRedirect('/gcna11')

	else:
		form4 = Floated_Form_B()

		if 'Nutmeg_ID_No' in request.session:
			form4.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form4.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/FloatB.html',{'form4':form4, 'submitted':submitted})








def Quality_add_data(request):
	submitted = False
	if request.method == "POST":
		form5 = Quality_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return HttpResponseRedirect('/gcna12')

	else:
		form5 = Quality_Form()

		if 'Nutmeg_ID_No' in request.session:
			form5.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form5.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Quality.html',{'form5':form5, 'submitted':submitted})































def Dried0_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form1 = Dried_Form_A(request.POST)
		if form1.is_valid():
			form1.save()
			return redirect('Dried0_A_add_data')

	else:
		form1 = Dried_Form_A()

		if 'Nutmeg_ID_No' in request.session:
			form1.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form1.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Dried0A.html',{'form1':form1, 'submitted':submitted})











def Dried0_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form2 = Dried_Form_B(request.POST)
		if form2.is_valid():
			form2.save()
			return redirect('Dried0_B_add_data')

	else:
		form2 = Dried_Form_B()

		if 'Nutmeg_ID_No' in request.session:
			form2.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form2.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Dried0B.html',{'form2':form2, 'submitted':submitted})








def Floated0_A_add_data(request):
	submitted = False
	if request.method == "POST":
		form3 = Floated_Form_A(request.POST)
		if form3.is_valid():
			form3.save()
			return redirect('Floated0_A_add_data')

	else:
		form3 = Floated_Form_A()

		if 'Nutmeg_ID_No' in request.session:
			form3.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form3.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Float0A.html',{'form3':form3, 'submitted':submitted})







def Floated0_B_add_data(request):
	submitted = False
	if request.method == "POST":
		form4 = Floated_Form_B(request.POST)
		if form4.is_valid():
			form4.save()
			return redirect('Floated0_B_add_data')

	else:
		form4 = Floated_Form_B()

		if 'Nutmeg_ID_No' in request.session:
			form4.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form4.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Float0B.html',{'form4':form4, 'submitted':submitted})








def Quality0_add_data(request):
	submitted = False
	if request.method == "POST":
		form5 = Quality_Form(request.POST)
		if form5.is_valid():
			form5.save()
			return redirect('Quality0_add_data')

	else:
		form5 = Quality_Form()

		if 'Nutmeg_ID_No' in request.session:
			form5.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'Worker_ID_No' in request.session:
			form5.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']



		if 'submitted' in request.GET:
			submitted = True



	return render(request,'gcna/Quality0.html',{'form5':form5, 'submitted':submitted})













# def page1_view(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST)
#         if form.is_valid():
#             # Store form data in the session
#             request.session['page1_data'] = form.cleaned_data
#             return redirect('page2_view')
#     else:
#         form = Full_Form()
#     return render(request, 'gcna/step1.html', {'form': form})

# def page2_view(request):
#     if request.method == 'POST':
#         form = Full_Form(request.POST)
#         if form.is_valid():
#             # Retrieve form data from the session
#             page1_data = request.session.get('page1_data')

#             # Combine form data from all pages
#             combined_data = {**page1_data, **form.cleaned_data}

#             # Create and save the model instance
#             MyModel.objects.create(**combined_data)

#             # Clear the session data
#             del request.session['page1_data']

#             return render(request, 'gcna/step2.html')
#     else:
#         form = Full_Form()
#     return render(request, 'gcna/step2.html', {'form': form})



def Full_farmB(request):
	user_list = User_info.objects.all()
	Land_tenurship_list = Land_tenurship.objects.all()
	tree_list = tree.objects.all()
	farm_list = farm.objects.all()
	state_list = state.objects.all()
	symmary_list = symmary.objects.all()
	return render(request,'gcna/farm_view 5.html',{
		'user_list': user_list,
		'Land_tenurship_list':Land_tenurship_list,
		'tree_list':tree_list,
		'farm_list':farm_list,
		'state_list':state_list,
		'symmary_list':symmary_list})



def all_farm(request):
	user_list = User_info.objects.all()
	return render(request,'gcna/farm_view.html',{'user_list': user_list})

def all_farm1(request):
	Land_tenurship_list = Land_Tenur.objects.all()
	return render(request,'gcna/farm_view 1.html',{'Land_tenurship_list': Land_tenurship_list})

def all_farm2(request):
	tree_list = tree.objects.all()
	return render(request,'gcna/farm_view 2.html',{'tree_list': tree_list})

def all_farm3(request):
	farm_list = farm.objects.all()
	return render(request,'gcna/farm_view 3.html',{'farm_list': farm_list})



def all_farm4(request):
	state_list = state.objects.all()
	return render(request,'gcna/farm_view 4.html',{'state_list': state_list})


def all_farm5(request):
	symmary_list = symmary.objects.all()
	return render(request,'gcna/farm_view 5.html',{'symmary_list': symmary_list})


def all_farm6(request):
	fullform_list = fullform.objects.all()
	return render(request,'gcna/farm_view 6.html',{'fullform_list': fullform_list})

def dried_A_Form(request):
	dried_A_list = Dried_Moisture_Analysis_A.objects.all()
	return render(request,'gcna/view_driedA.html',{'dried_A_list': dried_A_list})

def dried_B_Form(request):
	dried_B_list = Dried_Moisture_Analysis_B.objects.all()
	return render(request,'gcna/view_driedB.html',{'dried_B_list': dried_B_list})


def floated_A_Form(request):
	float_A_list = Floated_Moisture_Analysis_A.objects.all()
	return render(request,'gcna/view_floatedA.html',{'float_A_list': float_A_list})


def floated_B_Form(request):
	float_B_list = Floated_Moisture_Analysis_B.objects.all()
	return render(request,'gcna/view_floatedB.html',{'float_B_list': float_B_list})


def quality_Form(request):
	# test = Quality_Control.objects.get(pk=id)

	quality_list = Quality_Control.objects.all()
	return render(request,'gcna/view_quality.html',{'quality_list': quality_list})



def delete_quality(request, pk):
    quality = get_object_or_404(Quality_Control, pk=pk)
    if request.method == 'POST':
        quality.delete()
        return redirect('view_quality') 
    return redirect('error_page') 


def edit_quality(request, pk):
    quality = get_object_or_404(Quality_Control, pk=pk)
    if request.method == 'POST':
        form = Quality_Form(request.POST, instance=quality)
        if form.is_valid():
            form.save()
            return redirect('view_quality') 
    else:
        form = Quality_Form(instance=quality)
    return render(request, 'gcna/edit_quality.html', {'form': form})


def delete_dried_A(request, pk):
    dried = Dried_Moisture_Analysis_A.objects.get(pk=pk)
    dried.delete()
    return redirect('view_driedA')  


def delete_dried_B(request, pk):
    dried = Dried_Moisture_Analysis_B.objects.get(pk=pk)
    dried.delete()
    return redirect('view_driedB')  # Redirect to the desired URL after deletion

def delete_floated_A(request, pk):
    dried = Floated_Moisture_Analysis_A.objects.get(pk=pk)
    dried.delete()
    return redirect('view_floatedA')  # Redirect to the desired URL after deletion

def delete_floated_B(request, pk):
    dried = Floated_Moisture_Analysis_B.objects.get(pk=pk)
    dried.delete()
    return redirect('view_floatedB')  # Redirect to the desired URL after deletion

def edit_floated_A(request, pk):
    float_A = Floated_Moisture_Analysis_A.objects.get(pk=pk)
    if request.method == 'POST':
        form = Floated_Form_A(request.POST, instance=float_A)
        if form.is_valid():
            form.save()
            return redirect('view_floatedA') 
    else:
        form = Floated_Form_A(instance=float_A)
    return render(request, 'gcna/edit_floated_A.html', {'form': form})

def edit_floated_B(request, pk):
    dried = Floated_Moisture_Analysis_B.objects.get(pk=pk)
    if request.method == 'POST':
        form = Floated_Form_B(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_floatedB') 
    else:
        form = Floated_Form_B(instance=dried)
    return render(request, 'gcna/edit_floated_B.html', {'form': form})

def edit_dried_B(request, pk):
    dried = Dried_Moisture_Analysis_B.objects.get(pk=pk)
    if request.method == 'POST':
        form = Dried_Form_B(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_driedB') 
    else:
        form = Dried_Form_B(instance=dried)
    return render(request, 'gcna/edit_dried_B.html', {'form': form})


def edit_dried_A(request, pk):
    dried = Dried_Moisture_Analysis_A.objects.get(pk=pk)
    if request.method == 'POST':
        form = Dried_Form_A(request.POST, instance=dried)
        if form.is_valid():
            form.save()
            return redirect('view_driedA') 
    else:
        form = Dried_Form_A(instance=dried)
    return render(request, 'gcna/edit_dried_A.html', {'form': form})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
# def home(request):
	request.session['Nutmeg_ID_No'] = ' '
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	month = month.capitalize()
	cal = HTMLCalendar().formatmonth(year, month_number)
	now = datetime.now()
	current_year= now.year
	time = now.strftime('%I:%M:%S %p')


	return render(request,'gcna/home.html', {
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"current_year":current_year,
		"time":time,
		})








def view_Farm_table1(request):
	farmer_info_id = Farmer_Info.objects.all()
	return render(request,'gcna/view_farm1.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table2(request):
	farmer_info_id = land_info.objects.all()
	return render(request,'gcna/view_farm2.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table3(request):
	farmer_info_id = Land_Tenur.objects.all()
	return render(request,'gcna/view_farm3.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table4(request):
	farmer_info_id = Nutmeg_Trees.objects.all()
	return render(request,'gcna/view_farm4.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table5(request):
	farmer_info_id = Nutmeg_Variety.objects.all()
	return render(request,'gcna/view_farm5.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table6(request):
	farmer_info_id = Other_Crops.objects.all()
	return render(request,'gcna/view_farm6.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table7(request):
	farmer_info_id = Coconut_Trees.objects.all()
	return render(request,'gcna/view_farm7.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table8(request):
	farmer_info_id = Citrus_Mango_Trees.objects.all()
	return render(request,'gcna/view_farm8.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table9(request):
	farmer_info_id = Other_Spices_Trees.objects.all()
	return render(request,'gcna/view_farm9.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table10(request):
	farmer_info_id = Other_Seasoning_Trees.objects.all()
	return render(request,'gcna/view_farm10.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table11(request):
	farmer_info_id = Other_Crops_Cultivated.objects.all()
	return render(request,'gcna/view_farm11.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table12(request):
	farmer_info_id = Condition.objects.all()
	return render(request,'gcna/view_farm12.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table13(request):
	farmer_info_id = Nutmeg_Land.objects.all()
	return render(request,'gcna/view_farm13.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table14(request):
	farmer_info_id = Nutmeg_Frequency.objects.all()
	return render(request,'gcna/view_farm14.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table15(request):
	farmer_info_id = Potential_Risks.objects.all()
	return render(request,'gcna/view_farm15',{'farmer_info_id': farmer_info_id})

def view_Farm_table16(request):
	farmer_info_id = Policy.objects.all()
	return render(request,'gcna/view_farm16.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table17(request):
	farmer_info_id = Road_Access.objects.all()
	return render(request,'gcna/view_farm17.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table18(request):
	farmer_info_id = Food_Safety_and_Quality.objects.all()
	return render(request,'gcna/view_farm18.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table19(request):
	farmer_info_id = Farm_Water_Source.objects.all()
	return render(request,'gcna/view_farm19.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table20(request):
	farmer_info_id = Farm_House.objects.all()
	return render(request,'gcna/view_farm20.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table21(request):
	farmer_info_id = inspector_symmary.objects.all()
	return render(request,'gcna/view_farm21.html',{'farmer_info_id': farmer_info_id})












def view_Farm_table0_1(request):
	farmer_info_id = Farmer_Info.objects.all()
	return render(request,'gcna/view_farm0_1.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_2(request):
	farmer_info_id = land_info.objects.all()
	return render(request,'gcna/view_farm0_2.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_3(request):
	farmer_info_id = Land_Tenur.objects.all()
	return render(request,'gcna/view_farm0_3.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_4(request):
	farmer_info_id = Nutmeg_Trees.objects.all()
	return render(request,'gcna/view_farm0_4.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_5(request):
	farmer_info_id = Nutmeg_Variety.objects.all()
	return render(request,'gcna/view_farm0_5.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_6(request):
	farmer_info_id = Other_Crops.objects.all()
	return render(request,'gcna/view_farm0_6.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_7(request):
	farmer_info_id = Coconut_Trees.objects.all()
	return render(request,'gcna/view_farm0_7.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_8(request):
	farmer_info_id = Citrus_Mango_Trees.objects.all()
	return render(request,'gcna/view_farm0_8.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_9(request):
	farmer_info_id = Other_Spices_Trees.objects.all()
	return render(request,'gcna/view_farm0_9.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_10(request):
	farmer_info_id = Other_Seasoning_Trees.objects.all()
	return render(request,'gcna/view_farm0_10.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_11(request):
	farmer_info_id = Other_Crops_Cultivated.objects.all()
	return render(request,'gcna/view_farm0_11.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_12(request):
	farmer_info_id = Condition.objects.all()
	return render(request,'gcna/view_farm0_12.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_13(request):
	farmer_info_id = Nutmeg_Land.objects.all()
	return render(request,'gcna/view_farm0_13.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_14(request):
	farmer_info_id = Nutmeg_Frequency.objects.all()
	return render(request,'gcna/view_farm0_14.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_15(request):
	farmer_info_id = Potential_Risks.objects.all()
	return render(request,'gcna/view_farm0_15.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_16(request):
	farmer_info_id = Policy.objects.all()
	return render(request,'gcna/view_farm0_16.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_17(request):
	farmer_info_id = Road_Access.objects.all()
	return render(request,'gcna/view_farm0_17.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_18(request):
	farmer_info_id = Food_Safety_and_Quality.objects.all()
	return render(request,'gcna/view_farm0_18.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_19(request):
	farmer_info_id = Farm_Water_Source.objects.all()
	return render(request,'gcna/view_farm0_19.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_20(request):
	farmer_info_id = Farm_House.objects.all()
	return render(request,'gcna/view_farm0_20.html',{'farmer_info_id': farmer_info_id})

def view_Farm_table0_21(request):
	farmer_info_id = inspector_symmary.objects.all()
	return render(request,'gcna/view_farm0_21.html',{'farmer_info_id': farmer_info_id})










def edit_table0_1(request, pk):
	pk = Farmer_Info.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farmer_Info_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Farmer_Info_Form(instance=pk)

	return render(request, 'gcna/edit_table0_1.html', {'form': form})





def edit_table0_2(request, pk):
	pk = land_info.objects.get(pk=pk)
	if request.method == 'POST':
		form = land_info_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('table001') 
	else:
		form = land_info_Form(instance=pk)

	return render(request, 'gcna/edit_table0_2.html', {'form': form})





def edit_table0_3(request, pk):
	pk = Land_Tenur.objects.get(pk=pk)
	if request.method == 'POST':
		form = Land_Tenur_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_3') 
	else:
		form = Land_Tenur_Form(instance=pk)

	return render(request, 'gcna/edit_table0_3.html', {'form': form})








def edit_table0_4(request, pk):
	pk = Nutmeg_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_4') 
	else:
		form = Nutmeg_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_4.html', {'form': form})





def edit_table0_5(request, pk):
	pk = Nutmeg_Variety.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Variety_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_5') 
	else:
		form = Nutmeg_Variety_Form(instance=pk)

	return render(request, 'gcna/edit_table0_5.html', {'form': form})






def edit_table0_6(request, pk):
	pk = Other_Crops.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Crops_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_6') 
	else:
		form = Other_Crops_Form(instance=pk)

	return render(request, 'gcna/edit_table0_6.html', {'form': form})





def edit_table0_7(request, pk):
	pk = Coconut_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Coconut_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_7') 
	else:
		form = Coconut_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_7.html', {'form': form})







def edit_table0_8(request, pk):
	pk = Citrus_Mango_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Citrus_Mango_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_8') 
	else:
		form = Citrus_Mango_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_8.html', {'form': form})



def edit_table0_9(request, pk):
	pk = Other_Spices_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Spices_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_9') 
	else:
		form = Other_Spices_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table0_9.html', {'form': form})








def edit_table0_10(request, pk):
	pk = Other_Seasoning_Trees.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Seasoning_Trees_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_10') 
	else:
		form = Other_Seasoning_Trees_Form(instance=pk)

	return render(request, 'gcna/edit_table_10.html', {'form': form})






def edit_table0_11(request, pk):
	pk = Other_Crops_Cultivated.objects.get(pk=pk)
	if request.method == 'POST':
		form = Other_Crops_Cultivated_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_11') 
	else:
		form = Other_Crops_Cultivated_Form(instance=pk)

	return render(request, 'gcna/edit_table_11.html', {'form': form})




def edit_table0_12(request, pk):
	pk = Condition.objects.get(pk=pk)
	if request.method == 'POST':
		form = Condition_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_12') 
	else:
		form = Condition_Form(instance=pk)

	return render(request, 'gcna/edit_table_12.html', {'form': form})




def edit_table0_13(request, pk):
	pk = Nutmeg_Land.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Land_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_13') 
	else:
		form = Nutmeg_Land_Form(instance=pk)

	return render(request, 'gcna/edit_table_13.html', {'form': form})






def edit_table0_14(request, pk):
	pk = Nutmeg_Frequency.objects.get(pk=pk)
	if request.method == 'POST':
		form = Nutmeg_Frequency_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_14') 
	else:
		form = Nutmeg_Frequency_Form(instance=pk)

	return render(request, 'gcna/edit_table_14.html', {'form': form})



def edit_table0_15(request, pk):
	pk = Potential_Risks.objects.get(pk=pk)
	if request.method == 'POST':
		form = Potential_Risks_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_15') 
	else:
		form = Potential_Risks_Form(instance=pk)

	return render(request, 'gcna/edit_table_15.html', {'form': form})




def edit_table0_16(request, pk):
	pk = Policy.objects.get(pk=pk)
	if request.method == 'POST':
		form = Policy_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_16') 
	else:
		form = Policy_Form(instance=pk)

	return render(request, 'gcna/edit_table_16.html', {'form': form})




def edit_table0_17(request, pk):
	pk = Road_Access.objects.get(pk=pk)
	if request.method == 'POST':
		form = Road_Access_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_17') 
	else:
		form = Road_Access_Form(instance=pk)

	return render(request, 'gcna/edit_table0_17.html', {'form': form})




def edit_table0_18(request, pk):
	pk = Food_Safety_and_Quality.objects.get(pk=pk)
	if request.method == 'POST':
		form = Food_Safety_and_Quality_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_18') 
	else:
		form = Food_Safety_and_Quality_Form(instance=pk)

	return render(request, 'gcna/edit_table0_18.html', {'form': form})




def edit_table0_19(request, pk):
	pk = Farm_Water_Source.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farm_Water_Source_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_19') 
	else:
		form = Farm_Water_Source_Form(instance=pk)

	return render(request, 'gcna/edit_table0_19.html', {'form': form})




def edit_table0_20(request, pk):
	pk = Farm_House.objects.get(pk=pk)
	if request.method == 'POST':
		form = Farm_House_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_20') 
	else:
		form = Farm_House_Form(instance=pk)

	return render(request, 'gcna/edit_table0_20.html', {'form': form})







def edit_table0_21(request, pk):
	pk = inspector_symmary.objects.get(pk=pk)
	if request.method == 'POST':
		form = inspector_symmary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_21') 
	else:
		form = inspector_symmary_Form(instance=pk)

	return render(request, 'gcna/edit_table0_21.html', {'form': form})







def edit_table0_22(request, pk):
	pk = Training_support.objects.get(pk=pk)
	if request.method == 'POST':
		form = Training_support_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_22') 
	else:
		form = Training_support_Form(instance=pk)

	return render(request, 'gcna/edit_table0_22.html', {'form': form})



  



def edit_table0_23(request, pk):
	pk = Labour_support.objects.get(pk=pk)
	if request.method == 'POST':
		form = Labour_support_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_23') 
	else:
		form = Labour_support_Form(instance=pk)

	return render(request, 'gcna/edit_table0_23.html', {'form': form})







def edit_dried0_A(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Dried_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_driedA')  


	if request.method == 'POST':
		form = Dried_Form_A(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dried_Form_A(instance=farmer_info_id)
	return render(request, 'gcna/edit_dried0_A.html', {'form': form})








def display_dried0_A(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Dried_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_driedA')

	return render(request, 'gcna/view_dried0_A.html', context)









def edit_dried0_B(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dried_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Dried_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_driedB')  


	if request.method == 'POST':
		form = Dried_Form_B(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dried_Form_B(instance=farmer_info_id)
	return render(request, 'gcna/edit_dried0_B.html', {'form': form})

  




def display_dried0_B(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Dried_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Dried_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_driedB')

	return render(request, 'gcna/view_dried0_B.html', context)















def edit_floated0_A(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floated_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floated_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_floatA')  


	if request.method == 'POST':
		form = Floated_Form_A(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floated_Form_A(instance=farmer_info_id)
	return render(request, 'gcna/edit_floated0_A.html', {'form': form})






def display_floated0_A(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Floated_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Floated_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_floatA')

	return render(request, 'gcna/view_floated0_A.html', context)












def edit_floated0_B(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floated_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floated_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_floatB')  


	if request.method == 'POST':
		form = Floated_Form_B(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floated_Form_B(instance=farmer_info_id)
	return render(request, 'gcna/edit_floated0_B.html', {'form': form})




def display_floated0_B(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Floated_Moisture_Analysis_B.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Floated_Moisture_Analysis_B.DoesNotExist:
		return redirect('error_table_floatB')

	return render(request, 'gcna/view_floated0_B.html', context)










def edit_quality0(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Quality_Control.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Quality_Control.DoesNotExist:
		return redirect('error_table_quality')  


	if request.method == 'POST':
		form = Quality_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Quality_Form(instance=farmer_info_id)
	return render(request, 'gcna/edit_quality0_.html', {'form': form})





def display_quality0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Quality_Control.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Quality_Control.DoesNotExist:
		return redirect('error_table_quality')

	return render(request, 'gcna/view_quality0_.html', context)







def display_table_data21(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = inspector_symmary.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except inspector_symmary.DoesNotExist:
		return redirect('error_table21')

	return render(request, 'gcna/view_table21.html', context)









def delete_table0_1(request, id):
    if request.method == 'POST':
        try:
            # Implement your deletion logic here, e.g., using Django ORM
            farmer = Farmer_Info.objects.get(pk=id)
            farmer.delete()
            
            # If successful, return a JSON response indicating success
            return JsonResponse({'message': 'Deletion successful'})
        except Farmer_Info.DoesNotExist:
            # If the record doesn't exist, return an error response
            return JsonResponse({'message': 'Record not found'}, status=404)
 


def delete_table0_2(request, pk):
    pk = land_info.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_2')  


def delete_table0_3(request, pk):
    pk = Land_Tenur.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_3')  



def delete_table0_4(request, pk):
    pk = Nutmeg_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_4')  



def delete_table0_5(request, pk):
    pk = Nutmeg_Variety.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_5')  



def delete_table0_6(request, pk):
    pk = Other_Crops.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_6')  



def delete_table0_7(request, pk):
    pk = Coconut_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_7')  



def delete_table0_8(request, pk):
    pk = Citrus_Mango_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_8')  



def delete_table0_9(request, pk):
    pk = Other_Spices_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_9')  



def delete_table0_10(request, pk):
    pk = Other_Seasoning_Trees.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_10')  



def delete_table0_11(request, pk):
    pk = Other_Crops_Cultivated.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_11')  



def delete_table0_12(request, pk):
    pk = Condition.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_12')  



def delete_table0_13(request, pk):
    pk = Nutmeg_Land.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_13')  



def delete_table0_14(request, pk):
    pk = Nutmeg_Frequency.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_14')  



def delete_table0_15(request, pk):
    pk = Potential_Risks.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_15')  



def delete_table0_16(request, pk):
    pk = Policy.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_16')  



def delete_table0_17(request, pk):
    pk = Road_Access.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_17')  



def delete_table0_18(request, pk):
    pk = Food_Safety_and_Quality.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_18')  



def delete_table0_19(request, pk):
    pk = Farm_Water_Source.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_19')  



def delete_table0_20(request, pk):
    pk = Farm_House.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_20')  



def delete_table0_21(request, pk):
    pk = inspector_symmary.objects.get(pk=pk)
    pk.delete()
    return redirect('view_Farm_table0_21')  


def delete_table0_22(request, pk):
    pk = Farm_House.objects.get(pk=pk)
    pk.delete()
    return redirect('Training_support')  



def delete_table0_23(request, pk):
    pk = inspector_symmary.objects.get(pk=pk)
    pk.delete()
    return redirect('Labour_support')  

 



def In_House_add_data(request):
	submitted = False
	if request.method == "POST":
		

		form = In_House_Drying_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('view_IH')

	else:
		form = In_House_Drying_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		# if 'Worker_ID_No' in request.session:
		# 	form.fields['Worker_ID_No'].initial = request.session['Worker_ID_No']


		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/In_House.html',{'form':form, 'submitted':submitted})
















def Dispatch_Dried_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Dispatch_Dried')

	else:
		form = Dispatch_Of_Dried_Nutmeg_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Dispatched_Dried.html',{'form':form, 'submitted':submitted})

def Dispatch_Green_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Dispatch_Green')

	else:
		form = Dispatch_Of_Green_Nutmeg_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Dispatched_Green.html',{'form':form, 'submitted':submitted})

def Cracking_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Cracking_Summary_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Cracking')

	else:
		form = Cracking_Summary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Cracking.html',{'form':form, 'submitted':submitted})

def Floation_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Floation_Summary_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Floation')

	else:
		form = Floation_Summary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Floation.html',{'form':form, 'submitted':submitted})


def Package_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Package_Ciontrol_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Package')

	else:
		form = Package_Ciontrol_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Package.html',{'form':form, 'submitted':submitted})










def In_House_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = In_House_Drying_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_In_House_0')

	else:
		form = In_House_Drying_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/In_House_0.html',{'form':form, 'submitted':submitted})




def Dispatch_Dried_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Dispatch_Dried_0')

	else:
		form = Dispatch_Of_Dried_Nutmeg_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Dispatched_Dried_0.html',{'form':form, 'submitted':submitted})






def Dispatch_Green_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Dispatch_Green_0')

	else:
		form = Dispatch_Of_Green_Nutmeg_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Dispatched_Green_0.html',{'form':form, 'submitted':submitted})





def Cracking_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Cracking_Summary_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Cracking_0')

	else:
		form = Cracking_Summary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Cracking_0.html',{'form':form, 'submitted':submitted})





def Floation_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Floation_Summary_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Floation_0')

	else:
		form = Floation_Summary_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Floation_0.html',{'form':form, 'submitted':submitted})





def Package_0_add_data(request):
	submitted = False
	if request.method == "POST":
		form = Package_Ciontrol_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_Package_0')

	else:
		form = Package_Ciontrol_Form()

		if 'Nutmeg_ID_No' in request.session:
			form.fields['Nutmeg_ID_No'].initial = request.session['Nutmeg_ID_No']

		if 'submitted' in request.GET:
			submitted = True

	return render(request,'gcna/Package_0.html',{'form':form, 'submitted':submitted})



















def view_In_House_Drying_table(request):
	form = In_House_Drying.objects.all()
	return render(request,'gcna/view_IHD.html',{'form': form})

def view_Dispatch_Of_Dried_Nutmeg_table(request):
	form = Dispatch_Of_Dried_Nutmeg.objects.all()
	return render(request,'gcna/view_DDN.html',{'form': form})


def view_Dispatch_Of_Green_Nutmeg_table(request):
	form = Dispatch_Of_Green_Nutmeg.objects.all()
	return render(request,'gcna/view_DGN.html',{'form': form})


def view_Cracking_Summary_table(request):
	form = Cracking_Summary.objects.all()
	return render(request,'gcna/view_CS.html',{'form': form})


def view_Floation_Summary_table(request):
	form = Floation_Summary.objects.all()
	return render(request,'gcna/view_FS.html',{'form': form})



def view_Package_Ciontrol_table(request):
	form = Package_Ciontrol.objects.all()
	return render(request,'gcna/view_PK.html',{'form': form})













def view_In_House_Drying_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = In_House_Drying.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
			'farmer_info_id': farmer_info_id
		}

	except In_House_Drying.DoesNotExist:
		return redirect('error_table_driedA')

	return render(request,'gcna/view_IHD_0.html',context)




def view_Dispatch_Of_Dried_Nutmeg_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = Dispatch_Of_Dried_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Dispatch_Of_Dried_Nutmeg.DoesNotExist:
		return redirect('error_table_driedA')




	return render(request,'gcna/view_DDN_0.html',context)


def view_Dispatch_Of_Green_Nutmeg_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = Dispatch_Of_Green_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Dispatch_Of_Green_Nutmeg.DoesNotExist:
		return redirect('error_table_driedA')




	return render(request,'gcna/view_DGN_0.html',context)


def view_Cracking_Summary_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = Cracking_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Cracking_Summary.DoesNotExist:
		return redirect('error_table_driedA')





	return render(request,'gcna/view_CS_0.html',context)


def view_Floation_Summary_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = Floation_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Floation_Summary.DoesNotExist:
		return redirect('error_table_driedA')



	return render(request,'gcna/view_FS_0.html',context)




def view_Package_Ciontrol_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']


	try:
		farmer_info_id = Package_Ciontrol.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Package_Ciontrol.DoesNotExist:
		return redirect('error_table_driedA')



	return render(request,'gcna/view_FS_0.html',context)










def edit_In_House_Drying_table_0(request, pk):
	pk = In_House_Drying.objects.get(pk=pk)
	if request.method == 'POST':
		form = In_House_Drying_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = In_House_Drying_Form(instance=pk)

	return render(request, 'gcna/edit_IHD_0.html', {'form': form})









def edit_Dispatch_Of_Dried_Nutmeg_table_0(request, pk):
	pk = Dispatch_Of_Dried_Nutmeg.objects.get(pk=pk)
	if request.method == 'POST':
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Dispatch_Of_Dried_Nutmeg_Form(instance=pk)

	return render(request, 'gcna/edit_DDN_0.html', {'form': form})







def edit_Dispatch_Of_Green_Nutmeg_table_0(request, pk):
	pk = Dispatch_Of_Green_Nutmeg.objects.get(pk=pk)
	if request.method == 'POST':
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Dispatch_Of_Green_Nutmeg_Form(instance=pk)

	return render(request, 'gcna/edit_DGN_0.html', {'form': form})







def edit_Cracking_Summary_table_0(request, pk):
	pk = Cracking_Summary.objects.get(pk=pk)
	if request.method == 'POST':
		form = Cracking_Summary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Cracking_Summary_Form(instance=pk)

	return render(request, 'gcna/edit_CS_0.html', {'form': form})







def edit_Floation_Summary_table_0(request, pk):
	pk = Floation_Summary.objects.get(pk=pk)
	if request.method == 'POST':
		form = Floation_Summary_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Floation_Summary_Form(instance=pk)

	return render(request, 'gcna/edit_FS_0.html', {'form': form})







def edit_Package_Ciontrol_table_0(request, pk):
	pk = Package_Ciontrol.objects.get(pk=pk)
	if request.method == 'POST':
		form = Package_Ciontrol_Form(request.POST, instance=pk)
		if form.is_valid():
			form.save()
			return redirect('view_Farm_table0_1') 
	else:
		form = Package_Ciontrol_Form(instance=pk)

	return render(request, 'gcna/edit_PC_0.html', {'form': form})






def edit_In_House_Drying_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = In_House_Drying.objects.get(Nutmeg_ID_No=farmer_info_id)
	except In_House_Drying.DoesNotExist:
		return redirect('error_In_House')  

	if request.method == 'POST':
		form = In_House_Drying_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = In_House_Drying_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_IHD.html', {'form': form})








def edit_Dispatch_Of_Dried_Nutmeg_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dispatch_Of_Dried_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Dispatch_Of_Dried_Nutmeg.DoesNotExist:
		return redirect('error_Dispatch_Dried_Nutmeg')  

	if request.method == 'POST':
		form = Dispatch_Of_Dried_Nutmeg_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dispatch_Of_Dried_Nutmeg_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_DDN.html', {'form': form})










def edit_Dispatch_Of_Green_Nutmeg_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Dispatch_Of_Green_Nutmeg.objects.get(Nutmeg_ID_No=farmer_info_id)

	except Dispatch_Of_Green_Nutmeg.DoesNotExist:
		return redirect('error_Dispatch_Green_Nutmeg')  

	if request.method == 'POST':
		form = Dispatch_Of_Green_Nutmeg_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Dispatch_Of_Green_Nutmeg_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_DGN.html', {'form': form})













def edit_Cracking_Summary_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Cracking_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Cracking_Summary.DoesNotExist:
		return redirect('error_Cracking_Nutmeg')  

	if request.method == 'POST':
		form = Cracking_Summary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Cracking_Summary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_CS.html', {'form': form})








def edit_Floation_Summary_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Floation_Summary.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Floation_Summary.DoesNotExist:
		return redirect('error_Floation')  

	if request.method == 'POST':
		form = Floation_Summary_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Floation_Summary_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_FS.html', {'form': form})










def edit_Package_Ciontrol_table(request):

	farmer_info_id = request.session.get('Nutmeg_ID_No')
	try:
		farmer_info_id = Package_Ciontrol.objects.get(Nutmeg_ID_No=farmer_info_id)
	except Package_Ciontrol.DoesNotExist:
		return redirect('error_Package')  

	if request.method == 'POST':
		form = Package_Ciontrol_Form(request.POST, instance=farmer_info_id)
		if form.is_valid():
			form.save()
			return redirect('table') 
	else:
		form = Package_Ciontrol_Form(instance=farmer_info_id)


	return render(request, 'gcna/edit_PC.html', {'form': form})























def view_Package_Ciontrol_table_0(request):
	farmer_info_id = request.session['Nutmeg_ID_No']



	try:
		farmer_info_id = Package_Ciontrol.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Package_Ciontrol.DoesNotExist:
		return redirect('error_table_driedA')





	return render(request,'gcna/view_PK_0.html',context)












def display_dried0_A(request):
	farmer_info_id = request.session['Nutmeg_ID_No']

	try:
		farmer_info_id = Dried_Moisture_Analysis_A.objects.get(Nutmeg_ID_No=farmer_info_id)
		context = {
	        'farmer_info_id': farmer_info_id
		}

	except Dried_Moisture_Analysis_A.DoesNotExist:
		return redirect('error_table_driedA')

	return render(request, 'gcna/view_dried0_A.html', context)







def adhome(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
# def home(request):
	request.session['Nutmeg_ID_No'] = ' '
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	month = month.capitalize()
	cal = HTMLCalendar().formatmonth(year, month_number)
	now = datetime.now()
	current_year= now.year
	time = now.strftime('%I:%M:%S %p')


	return render(request,'gcna/adhome.html', {
		"year":year,
		"month":month,
		"month_number":month_number,
		"cal":cal,
		"current_year":current_year,
		"time":time,
		})






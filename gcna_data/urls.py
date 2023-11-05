from django.urls import path
from . import views
from .views import  VisitView, Dried_Moisture_Analysis_A_CreateView, Dried_Moisture_Analysis_B_CreateView, Floated_Moisture_Analysis_A_CreateView, Floated_Moisture_Analysis_B_CreateView, Quality_Control_CreateView, Worker_Info_CreateView, Farmer_Info_CreateView
from gcna_data.views import EditorChartView

urlpatterns = [
    path('',views.home, name="home"),

    path('api/DriedA/',views.Dried_Moisture_Analysis_A_CreateView.as_view(), name="Dried_Moisture-Analysis-A-Create"),
    path('api/DriedB/',views.Dried_Moisture_Analysis_B_CreateView.as_view(), name="Dried_Moisture-Analysis-B-Create"),
    path('api/FloatA/',views.Floated_Moisture_Analysis_A_CreateView.as_view(), name="Floated_Moisture-Analysis-A-Create"),
    path('api/FloatB/',views.Floated_Moisture_Analysis_B_CreateView.as_view(), name="Floated_Moisture-Analysis-B-Create"),
    path('api/Quaility/',views.Quality_Control_CreateView.as_view(), name="Quality-Control-Create"),
    path('api/Worker/',views.Worker_Info_CreateView.as_view(), name="Worker-Info-Create"),
    path('api/Farmer/',views.Farmer_Info_CreateView.as_view(), name="Farmer-Info-Create"),



    path('api/visit/',views.visit_CreateView.as_view(), name="visit-Create"),
    path('api/In-House-Drying/',views.In_House_Drying_CreateView.as_view(), name="In-House-Drying-Create"),
    path('api/Dispatch-Of-Dried-Nutmeg/',views.Dispatch_Of_Dried_Nutmeg_CreateView.as_view(), name="Dispatch-Of-Dried-Nutmeg-Create"),
    path('api/Dispatch-Of-Green/',views.Dispatch_Of_Green_Nutmeg_CreateView.as_view(), name="Dispatch-Of-Green-Nutmeg-Create"),
    path('api/Cracking-Summary/',views.Cracking_Summary_CreateView.as_view(), name="Cracking-Summary-Create"),
    path('api/Floation-Summary/',views.Floation_Summary_CreateView.as_view(), name="Floation-Summary-Create"),
    path('api/Package-Ciontrol/',views.Package_Ciontrol_CreateView.as_view(), name="Package-Ciontrol-Create"),
    path('api/Editors/',views.Editors_CreateView.as_view(), name="Editors-Create"),
    path('api/Labour-support/',views.Labour_support_CreateView.as_view(), name="Labour-support-Create"),
    path('api/Training-support/',views.Training_support_CreateView.as_view(), name="Training-support-Create"),
    path('api/land-info/',views.land_info_CreateView.as_view(), name="land-info-Create"),
    path('api/Land-Tenur/',views.Land_Tenur_CreateView.as_view(), name="Land-Tenur-Create"),
    path('api/Nutmeg-Trees/',views.Nutmeg_Trees_CreateView.as_view(), name="Nutmeg-Trees-Create"),
    path('api/Nutmeg-Variety/',views.Nutmeg_Variety_CreateView.as_view(), name="Nutmeg-Variety-Create"),
    path('api/Other-Crops/',views.Other_Crops_CreateView.as_view(), name="Other-Crops-Create"),
    path('api/Coconut-Trees/',views.Coconut_Trees_CreateView.as_view(), name="Coconut-Trees-Create"),
    path('api/Citrus-Mango-Trees/',views.Citrus_Mango_Trees_CreateView.as_view(), name="Citrus-Mango-Trees-Create"),
    path('api/Other-Spices-Trees/',views.Other_Spices_Trees_CreateView.as_view(), name="Other-Spices-Trees-Create"),
    path('api/Other-Seasoning-Trees/',views.Other_Seasoning_Trees_CreateView.as_view(), name="Other-Seasoning-Trees-Create"),
    path('api/Other-Crops-Cultivated/',views.Other_Crops_Cultivated_CreateView.as_view(), name="Other-Crops-Cultivated-Create"),
    path('api/Condition/',views.Condition_CreateView.as_view(), name="Condition-Create"),
    path('api/Nutmeg-Land/',views.Nutmeg_Land_CreateView.as_view(), name="Nutmeg-Land-Create"),
    path('api/Nutmeg-Frequency/',views.Nutmeg_Frequency_CreateView.as_view(), name="Nutmeg-Frequency-Create"),
    path('api/Potential-Risks/',views.Potential_Risks_CreateView.as_view(), name="Potential-Risks-Create"),
    path('api/Road-Access/',views.Road_Access_CreateView.as_view(), name="Road-Access-Create"),
    path('api/Food-Safety-and-Quality/',views.Food_Safety_and_Quality_CreateView.as_view(), name="Food-Safety-and-Quality-Create"),
    path('api/Farm-Water-Source/',views.Farm_Water_Source_CreateView.as_view(), name="Farm-Water-Source-Create"),
    path('api/Farm-House/',views.Farm_House_CreateView.as_view(), name="Farm-House-Create"),
    path('api/inspector-symmary/',views.inspector_symmary_CreateView.as_view(), name="inspector-symmary-Create"),
    path('api/Policy/',views.Policy_CreateView.as_view(), name="Policy-Create"),
    # path('api/Policy/<int:id>/',views.Policy_CreateView.as_view(), name="Policy-Create"),
    path('api/visit2/<int:pk>/', VisitView.as_view(), name='visit-detail'),





























    path('adhome',views.adhome, name="adhome"),
    path('<int:year>/<str:month>/',views.home, name="home"),
    path("gcna", views.all_farm, name="database"),
    path("gcna1", views.all_farm1, name="database1"),
    path("gcna2", views.all_farm2, name="database2"),
    path("gcna3", views.all_farm3, name="database3"),
    path("gcna4", views.all_farm4, name="database4"),
    path("gcna5", views.all_farm5, name="database5"),
    path("gcna6", views.all_farm6, name="database6"),
    path('gcna7', views.add_data, name="database7"),
    path('import/', views.import_exel, name="import_data"),
    # path('multi/', views.Multi, name='multi'),
    # path('multi/gcna/success/', views.form_success, name='form_success'),


    path('gcna8', views.Dried_A_add_data, name="database8"),
    path('gcna9', views.Dried_B_add_data, name="database9"),
    path('gcna10', views.Floated_A_add_data, name="database10"),
    path('gcna11', views.Floated_B_add_data, name="database11"),
    path('gcna12', views.Quality_add_data, name="database12"),



    path('DriedA', views.Dried0_A_add_data, name="Dried0_A_add_data"),
    path('DriedB', views.Dried0_B_add_data, name="Dried0_B_add_data"),
    path('FloatA', views.Floated0_A_add_data, name="Floated0_A_add_data"),
    path('FloatB', views.Floated0_B_add_data, name="Floated0_B_add_data"),
    path('Quality', views.Quality0_add_data, name="Quality0_add_data"),






    path('gcna0', views.comp_data, name="database0"),




    path('gcna0_1', views.comp_data1, name="database0_1"),
    path('gcna0_2', views.comp_data2, name="database0_2"),
    path('gcna0_3', views.comp_data3, name="database0_3"),
    path('gcna0_4', views.comp_data4, name="database0_4"),
    path('gcna0_5', views.comp_data5, name="database0_5"),
    path('gcna0_6', views.comp_data6, name="database0_6"),




    path('importDA/', views.import_dried_A_exel, name="import_data1"),
    path('importDB/', views.import_dried_B_exel, name="import_data2"),
    path('importFA/', views.import_floated_A_exel, name="import_data3"),
    path('importFB/', views.import_floated_B_exel, name="import_data4"),
    path('importQC/', views.import_Quality_Control_exel, name="import_data5"),

    path("viewDA/", views.dried_A_Form, name="view_driedA"),


    # path('-/<str:pk>/', views.delete_invoice, name="delete_invoice"),



    path("viewDB/", views.dried_B_Form, name="view_driedB"),



    path("viewFA/", views.floated_A_Form, name="view_floatedA"),

    path("viewFB/", views.floated_B_Form, name="view_floatedB"),



    path("viewQC/", views.quality_Form, name="view_quality"),
    
    path('quality/delete/<int:pk>/', views.delete_quality, name='delete_quality'),
    path('quality/edit/<int:pk>/', views.edit_quality, name='edit_quality'),




    path('dried_A/delete/<int:pk>/', views.delete_dried_A, name='delete_dried_A'),
    path('dried_A/edit/<int:pk>/', views.edit_dried_A, name='edit_dried_A'),




    path('dried_B/delete/<int:pk>/', views.delete_dried_B, name='delete_dried_B'),
    path('dried_B/edit/<int:pk>/', views.edit_dried_B, name='edit_dried_B'),





    path('floated_A/delete/<int:pk>/', views.delete_floated_A, name='delete_floated_A'),
    path('floated_A/edit/<int:pk>/', views.edit_floated_A, name='edit_floated_A'),




    path('floated_B/delete/<int:pk>/', views.delete_floated_B, name='delete_floated_B'),
    path('floated_B/edit/<int:pk>/', views.edit_floated_B, name='edit_floated_B'),




    path('add_to_session/', views.add_to_session, name='add_to_session'),

    path('gcna00_1/', views.rev_data1, name='gcna00_1'),
    path('gcna00_2/', views.rev_data2, name='gcna00_2'),
    path('gcna00_3/', views.rev_data3, name='gcna00_3'),
    path('gcna00_4/', views.rev_data4, name='gcna00_4'),
    path('gcna00_5/', views.rev_data5, name='gcna00_5'),
    path('gcna00_6/', views.rev_data6, name='gcna00_6'),
    path('gcna00_7/', views.rev_data7, name='gcna00_7'),
    path('gcna00_8/', views.rev_data8, name='gcna00_8'),
    path('gcna00_9/', views.rev_data9, name='gcna00_9'),
    path('gcna00_10/', views.rev_data10, name='gcna00_10'),
    path('gcna00_11/', views.rev_data11, name='gcna00_11'),
    path('gcna00_12/', views.rev_data12, name='gcna00_12'),
    path('gcna00_13/', views.rev_data13, name='gcna00_13'),
    path('gcna00_14/', views.rev_data14, name='gcna00_14'),
    path('gcna00_15/', views.rev_data15, name='gcna00_15'),
    path('gcna00_16/', views.rev_data16, name='gcna00_16'),
    path('gcna00_17/', views.rev_data17, name='gcna00_17'),
    path('gcna00_18/', views.rev_data18, name='gcna00_18'),
    path('gcna00_19/', views.rev_data19, name='gcna00_19'),
    path('gcna00_20/', views.rev_data20, name='gcna00_20'),
    path('gcna00_21/', views.rev_data21, name='gcna00_21'),

    path('gcna00_22/', views.rev_data22, name='gcna00_22'),
    path('gcna00_23/', views.rev_data23, name='gcna00_23'),
    path('gcna00_24/', views.rev_data24, name='gcna00_24'),





    path('0gcna00_1/', views.rev_data0_1, name='0gcna00_1'),
    path('0gcna00_2/', views.rev_data0_2, name='0gcna00_2'),
    path('0gcna00_3/', views.rev_data0_3, name='0gcna00_3'),
    path('0gcna00_4/', views.rev_data0_4, name='0gcna00_4'),
    path('0gcna00_5/', views.rev_data0_5, name='0gcna00_5'),
    path('0gcna00_6/', views.rev_data0_6, name='0gcna00_6'),
    path('0gcna00_7/', views.rev_data0_7, name='0gcna00_7'),
    path('0gcna00_8/', views.rev_data0_8, name='0gcna00_8'),
    path('0gcna00_9/', views.rev_data0_9, name='0gcna00_9'),
    path('0gcna00_10/', views.rev_data0_10, name='0gcna00_10'),
    path('0gcna00_11/', views.rev_data0_11, name='0gcna00_11'),
    path('0gcna00_12/', views.rev_data0_12, name='0gcna00_12'),
    path('0gcna00_13/', views.rev_data0_13, name='0gcna00_13'),
    path('0gcna00_14/', views.rev_data0_14, name='0gcna00_14'),
    path('0gcna00_15/', views.rev_data0_15, name='0gcna00_15'),
    path('0gcna00_16/', views.rev_data0_16, name='0gcna00_16'),
    path('0gcna00_17/', views.rev_data0_17, name='0gcna00_17'),
    path('0gcna00_18/', views.rev_data0_18, name='0gcna00_18'),
    path('0gcna00_19/', views.rev_data0_19, name='0gcna00_19'),
    path('0gcna00_20/', views.rev_data0_20, name='0gcna00_20'),
    path('0gcna00_21/', views.rev_data0_21, name='0gcna00_21'),





    path('view_tablet/', views.view_Training, name='view_Training'),
    path('view_tablet2/', views.view_labour, name='view_labour'),


    path('view_Visit/', views.view_Visit, name='view_Visit'),
    path('edit_Visit/', views.edit_Visit, name='edit_Visit'),


    path('gcna000_22/', views.rev_data0_22, name='gcna000_22'),
    path('gcna000_23/', views.rev_data0_23, name='gcna000_23'),


   path('view_tablet000000/', views.view_Training0, name='view_Training0'),
    path('view_tablet0000002/', views.view_labour0, name='view_labour0'),


    path('edit_tablet0/', views.edit_Training0, name='edit_Training0'),
    path('edit_tablel0/', views.edit_labour0, name='edit_labour0'),



    path('edit_tablet/', views.edit_Training, name='edit_Training'),
    path('edit_tablel/', views.edit_labour, name='edit_labour'),






    path('table/', views.table, name='table'),
    path('table001/', views.Initial, name='table001'),

    path('table1/', views.display_table_data1, name='table1'),
    path('edit_table1/', views.edit_table1, name='edit_table1'),



    path('login/', views.rev_data0, name='login'),

    path('login1/', views.rev_data00, name='login1'),

    path('table2/', views.display_table_data2, name='table2'),
    path('edit_table2/', views.edit_table2, name='edit_table2'),



    path('table3/', views.display_table_data3, name='table3'),
    path('edit_table3/', views.edit_table3, name='edit_table3'),




    path('table4/', views.display_table_data4, name='table4'),
    path('edit_table4/', views.edit_table4, name='edit_table4'),



    path('table5/', views.display_table_data5, name='table5'),
    path('edit_table5/', views.edit_table5, name='edit_table5'),

    path('table6/', views.display_table_data6, name='table6'),
    path('edit_table6/', views.edit_table6, name='edit_table6'),

    path('table7/', views.display_table_data7, name='table7'),
    path('edit_table7/', views.edit_table7, name='edit_table7'),


    path('table8/', views.display_table_data8, name='table8'),
    path('edit_table8/', views.edit_table8, name='edit_table8'),

    path('table9/', views.display_table_data9, name='table9'),
    path('edit_table9/', views.edit_table9, name='edit_table9'),


    path('table10/', views.display_table_data10, name='table10'),
    path('edit_table10/', views.edit_table10, name='edit_table10'),

    path('table11/', views.display_table_data11, name='table11'),
    path('edit_table11/', views.edit_table11, name='edit_table11'),



    path('table12/', views.display_table_data12, name='table12'),
    path('edit_table12/', views.edit_table12, name='edit_table12'),

    path('table13/', views.display_table_data13, name='table13'),
    path('edit_table13/', views.edit_table13, name='edit_table13'),


    path('table14/', views.display_table_data14, name='table14'),
    path('edit_table14/', views.edit_table14, name='edit_table14'),


    path('table15/', views.display_table_data15, name='table15'),
    path('edit_table15/', views.edit_table15, name='edit_table15'),


    path('table16/', views.display_table_data16, name='table16'),
    path('edit_table16/', views.edit_table16, name='edit_table16'),



    path('table17/', views.display_table_data17, name='table17'),
    path('edit_table17/', views.edit_table17, name='edit_table17'),



    path('table18/', views.display_table_data18, name='table18'),
    path('edit_table18/', views.edit_table18, name='edit_table18'),



    path('table19/', views.display_table_data19, name='table19'),
    path('edit_table19/', views.edit_table19, name='edit_table19'),



    path('table20/', views.display_table_data20, name='table20'),
    path('edit_table20/', views.edit_table20, name='edit_table20'),



    path('table21/', views.display_table_data21, name='table21'),
    path('edit_table21/', views.edit_table21, name='edit_table21'),

    path('error_table0/', views.error_table0, name='error_table0'),
    path('error_table1/', views.error_table1, name='error_table1'),
    path('error_table2/', views.error_table2, name='error_table2'),
    path('error_table3/', views.error_table3, name='error_table3'),
    path('error_table4/', views.error_table4, name='error_table4'),
    path('error_table5/', views.error_table5, name='error_table5'),
    path('error_table6/', views.error_table6, name='error_table6'),
    path('error_table7/', views.error_table7, name='error_table7'),
    path('error_table8/', views.error_table8, name='error_table8'),
    path('error_table9/', views.error_table9, name='error_table9'),
    path('error_table10/', views.error_table10, name='error_table10'),
    path('error_table11/', views.error_table11, name='error_table11'),
    path('error_table12/', views.error_table12, name='error_table12'),
    path('error_table13/', views.error_table13, name='error_table13'),
    path('error_table14/', views.error_table14, name='error_table14'),
    path('error_table15/', views.error_table15, name='error_table15'),
    path('error_table16/', views.error_table16, name='error_table16'),
    path('error_table17/', views.error_table17, name='error_table17'),
    path('error_table18/', views.error_table18, name='error_table18'),
    path('error_table19/', views.error_table19, name='error_table19'),
    path('error_table20/', views.error_table20, name='error_table20'),
    path('error_table21/', views.error_table21, name='error_table21'),
    path('signin/', views.signin, name='signin'),



    path('error_table22/', views.error_table22, name='error_table22'),
    path('error_table23/', views.error_table23, name='error_table23'),


    path('view_Farm_table1/', views.view_Farm_table1, name='view_Farm_table1'),
    path('view_Farm_table2/', views.view_Farm_table2, name='view_Farm_table2'),
    path('view_Farm_table3/', views.view_Farm_table3, name='view_Farm_table3'),
    path('view_Farm_table4/', views.view_Farm_table4, name='view_Farm_table4'),
    path('view_Farm_table5/', views.view_Farm_table5, name='view_Farm_table5'),
    path('view_Farm_table6/', views.view_Farm_table6, name='view_Farm_table6'),
    path('view_Farm_table7/', views.view_Farm_table7, name='view_Farm_table7'),
    path('view_Farm_table8/', views.view_Farm_table8, name='view_Farm_table8'),
    path('view_Farm_table9/', views.view_Farm_table9, name='view_Farm_table9'),
    path('view_Farm_table10/', views.view_Farm_table10, name='view_Farm_table10'),
    path('view_Farm_table11/',views. view_Farm_table11, name='view_Farm_table11'),
    path('view_Farm_table12/', views.view_Farm_table12, name='view_Farm_table12'),
    path('view_Farm_table13/', views.view_Farm_table13, name='view_Farm_table13'),
    path('view_Farm_table14/', views.view_Farm_table14, name='view_Farm_table14'),
    path('view_Farm_table15/', views.view_Farm_table15, name='view_Farm_table15'),
    path('view_Farm_table16/', views.view_Farm_table16, name='view_Farm_table16'),
    path('view_Farm_table17/', views.view_Farm_table17, name='view_Farm_table17'),
    path('view_Farm_table18/', views.view_Farm_table18, name='view_Farm_table18'),
    path('view_Farm_table19/', views.view_Farm_table19, name='view_Farm_table19'),
    path('view_Farm_table20/', views.view_Farm_table20, name='view_Farm_table20'),
    path('view_Farm_table21/', views.view_Farm_table21, name='view_Farm_table21'),






    path('view_Farm_table0_1/', views.view_Farm_table0_1, name='view_Farm_table0_1'),
    path('view_Farm_table0_2/', views.view_Farm_table0_2, name='view_Farm_table0_2'),
    path('view_Farm_table0_3/', views.view_Farm_table0_3, name='view_Farm_table0_3'),
    path('view_Farm_table0_4/', views.view_Farm_table0_4, name='view_Farm_table0_4'),
    path('view_Farm_table0_5/', views.view_Farm_table0_5, name='view_Farm_table0_5'),
    path('view_Farm_table0_6/', views.view_Farm_table0_6, name='view_Farm_table0_6'),
    path('view_Farm_table0_7/', views.view_Farm_table0_7, name='view_Farm_table0_7'),
    path('view_Farm_table0_8/', views.view_Farm_table0_8, name='view_Farm_table0_8'),
    path('view_Farm_table0_9/', views.view_Farm_table0_9, name='view_Farm_table0_9'),
    path('view_Farm_table0_10/', views.view_Farm_table0_10, name='view_Farm_table0_10'),
    path('view_Farm_table0_11/', views.view_Farm_table0_11, name='view_Farm_table0_11'),
    path('view_Farm_table0_12/', views.view_Farm_table0_12, name='view_Farm_table0_12'),
    path('view_Farm_table0_13/', views.view_Farm_table0_13, name='view_Farm_table0_13'),
    path('view_Farm_table0_14/', views.view_Farm_table0_14, name='view_Farm_table0_14'),
    path('view_Farm_table0_15/', views.view_Farm_table0_15, name='view_Farm_table0_15'),
    path('view_Farm_table0_16/', views.view_Farm_table0_16, name='view_Farm_table0_16'),
    path('view_Farm_table0_17/', views.view_Farm_table0_17, name='view_Farm_table0_17'),
    path('view_Farm_table0_18/', views.view_Farm_table0_18, name='view_Farm_table0_18'),
    path('view_Farm_table0_19/', views.view_Farm_table0_19, name='view_Farm_table0_19'),
    path('view_Farm_table0_20/', views.view_Farm_table0_20, name='view_Farm_table0_20'),
    path('view_Farm_table0_21/', views.view_Farm_table0_21, name='view_Farm_table0_21'),







    path('edit/edit_table0_1/<int:pk>/', views.edit_table0_1, name='edit_table0_1'),
    path('edit/edit_table0_2/<int:pk>/', views.edit_table0_2, name='edit_table0_2'),
    path('edit/edit_table0_3/<int:pk>/', views.edit_table0_3, name='edit_table0_3'),
    path('edit/edit_table0_4/<int:pk>/', views.edit_table0_4, name='edit_table0_4'),
    path('edit/edit_table0_5/<int:pk>/', views.edit_table0_5, name='edit_table0_5'),
    path('edit/edit_table0_6/<int:pk>/', views.edit_table0_6, name='edit_table0_6'),
    path('edit/edit_table0_7/<int:pk>/', views.edit_table0_7, name='edit_table0_7'),
    path('edit/edit_table0_8/<int:pk>/', views.edit_table0_8, name='edit_table0_8'),
    path('edit/edit_table0_9/<int:pk>/', views.edit_table0_9, name='edit_table0_9'),
    path('edit/edit_table0_10/<int:pk>/', views.edit_table0_10, name='edit_table0_10'),
    path('edit/edit_table0_11/<int:pk>/', views.edit_table0_11, name='edit_table0_11'),
    path('edit/edit_table0_12/<int:pk>/', views.edit_table0_12, name='edit_table0_12'),
    path('edit/edit_table0_13/<int:pk>/', views.edit_table0_13, name='edit_table0_13'),
    path('edit/edit_table0_14/<int:pk>/', views.edit_table0_14, name='edit_table0_14'),
    path('edit/edit_table0_15/<int:pk>/', views.edit_table0_15, name='edit_table0_15'),
    path('edit/edit_table0_16/<int:pk>/', views.edit_table0_16, name='edit_table0_16'),
    path('edit/edit_table0_17/<int:pk>/', views.edit_table0_17, name='edit_table0_17'),
    path('edit/edit_table0_18/<int:pk>/', views.edit_table0_18, name='edit_table0_18'),
    path('edit/edit_table0_19/<int:pk>/', views.edit_table0_19, name='edit_table0_19'),
    path('edit/edit_table0_20/<int:pk>/', views.edit_table0_20, name='edit_table0_20'),
    path('edit/edit_table0_21/<int:pk>/', views.edit_table0_21, name='edit_table0_21'),

    path('edit/edit_table0_22/<int:pk>/', views.edit_table0_22, name='edit_table0_22'),
    path('edit/edit_table0_23/<int:pk>/', views.edit_table0_23, name='edit_table0_23'),




    path('delete/delete_table0_1/<int:id>/', views.delete_table0_1, name='delete_table0_1'),
    path('delete/delete_table0_2/<int:pk>/', views.delete_table0_2, name='delete_table0_2'),
    path('delete/delete_table0_3/<int:pk>/', views.delete_table0_3, name='delete_table0_3'),
    path('delete/delete_table0_4/<int:pk>/', views.delete_table0_4, name='delete_table0_4'),
    path('delete/delete_table0_5/<int:pk>/', views.delete_table0_5, name='delete_table0_5'),
    path('delete/delete_table0_6/<int:pk>/', views.delete_table0_6, name='delete_table0_6'),
    path('delete/delete_table0_7/<int:pk>/', views.delete_table0_7, name='delete_table0_7'),
    path('delete/delete_table0_8/<int:pk>/', views.delete_table0_8, name='delete_table0_8'),
    path('delete/delete_table0_9/<int:pk>/', views.delete_table0_9, name='delete_table0_9'),
    path('delete/delete_table0_10/<int:pk>/', views.delete_table0_10, name='delete_table0_10'),
    path('delete/delete_table0_11/<int:pk>/', views.delete_table0_11, name='delete_table0_11'),
    path('delete/delete_table0_12/<int:pk>/', views.delete_table0_12, name='delete_table0_12'),
    path('delete/delete_table0_13/<int:pk>/', views.delete_table0_13, name='delete_table0_13'),
    path('delete/delete_table0_14/<int:pk>/', views.delete_table0_14, name='delete_table0_14'),
    path('delete/delete_table0_15/<int:pk>/', views.delete_table0_15, name='delete_table0_15'),
    path('delete/delete_table0_16/<int:pk>/', views.delete_table0_16, name='delete_table0_16'),
    path('delete/delete_table0_17/<int:pk>/', views.delete_table0_17, name='delete_table0_17'),
    path('delete/delete_table0_18/<int:pk>/', views.delete_table0_18, name='delete_table0_18'),
    path('delete/delete_table0_19/<int:pk>/', views.delete_table0_19, name='delete_table0_19'),
    path('delete/delete_table0_20/<int:pk>/', views.delete_table0_20, name='delete_table0_20'),
    path('delete/delete_table0_21/<int:pk>/', views.delete_table0_21, name='delete_table0_21'),


    path('delete/delete_table0_22/<int:pk>/', views.delete_table0_22, name='delete_table0_22'),
    path('delete/delete_table0_23/<int:pk>/', views.delete_table0_23, name='delete_table0_23'),

     path('quality/edit0/', views.edit_quality0, name='edit_quality0'),




     path('dried_A/edit0/', views.edit_dried0_A, name='edit_dried0_A'),




     path('dried_B/edit0/', views.edit_dried0_B, name='edit_dried0_B'),





     path('floated_A/edit0/', views.edit_floated0_A, name='edit_floated0_A'),




     path('floated_B/edit0/', views.edit_floated0_B, name='edit_floated0_B'),






    path("view0DA/", views.display_dried0_A, name="view_dried0A"),





    path("view0DB/", views.display_dried0_B, name="view_dried0B"),



    path("view0FA/", views.display_floated0_A, name="view_floated0A"),

    path("view0FB/", views.display_floated0_B, name="view_floated0B"),


    path("view0QC/", views.display_quality0, name="view_quality0_"),



    # path('-/<str:pk>/', views.delete_invoice, name="delete_invoice"),





    path('error_table_driedA/', views.error_table_driedA, name='error_table_driedA'),
    path('error_table_driedB/', views.error_table_driedB, name='error_table_driedB'),
    path('error_table_floatA/', views.error_table_floatA, name='error_table_floatA'),
    path('error_table_floatB/', views.error_table_floatB, name='error_table_floatB'),
    path('error_table_quality/', views.error_table_quality, name='error_table_quality'),


    path('bar-chart/', views.bar_chart, name='bar_chart'),
    path('bar-chart1/', views.bar_chart1, name='bar_chart1'),

    path('chart1/', EditorChartView.as_view(), name='index'),
                                                                                                             






    path("addIH/", views.In_House_add_data, name="add_In_House"),
    path("addDISD/", views.Dispatch_Dried_add_data, name="add_Dispatch_Dried"),
    path("addDISG/", views.Dispatch_Green_add_data, name="add_Dispatch_Green"),
    path("addCRK/", views.Cracking_add_data, name="add_Cracking"),
    path("addFLT/", views.Floation_add_data, name="add_Floation"),
    path("addPKG/", views.Package_add_data, name="add_Package"),




    path("viewIH/", views.view_In_House_Drying_table, name="view_IH"),
    path("viewDISD/", views.view_Dispatch_Of_Dried_Nutmeg_table, name="view_DISD"),
    path("viewDISG/", views.view_Dispatch_Of_Green_Nutmeg_table, name="view_DISG"),
    path("viewCRK/", views.view_Cracking_Summary_table, name="view_CRK"),
    path("viewFLT/", views.view_Floation_Summary_table, name="view_FLT"),
    path("viewPKG/", views.view_Package_Ciontrol_table, name="view_PKG"),



    path("viewIH0/", views.view_In_House_Drying_table_0, name="view_IH_0"),
    path("viewDISD0/", views.view_Dispatch_Of_Dried_Nutmeg_table_0, name="view_DISD_0"),
    path("viewDISG0/", views.view_Dispatch_Of_Green_Nutmeg_table_0, name="view_DISG_0"),
    path("viewCRK0/", views.view_Cracking_Summary_table_0, name="view_CRK_0"),
    path("viewFLT0/", views.view_Floation_Summary_table_0, name="view_FLT_0"),
    path("viewPKG0/", views.view_Package_Ciontrol_table_0, name="view_PKG_0"),

    path("addIH0/", views.In_House_0_add_data, name="add_In_House_0"),
    path("addDISD0/", views.Dispatch_Dried_0_add_data, name="add_Dispatch_Dried_0"),
    path("addDISG0/", views.Dispatch_Green_0_add_data, name="add_Dispatch_Green_0"),
    path("addCRK0/", views.Cracking_0_add_data, name="add_Cracking_0"),
    path("addFLT0/", views.Floation_0_add_data, name="add_Floation_0"),
    path("addPKG0/", views.Package_0_add_data, name="add_Package_0"),

    path('edit/edit_IH0/<int:pk>/', views.edit_In_House_Drying_table_0, name='edit_In_House_0'),
    path('edit/edit_DISD0/<int:pk>/', views.edit_Dispatch_Of_Dried_Nutmeg_table_0, name='edit_Dispatch_Dried_0'),
    path('edit/edit_DISG0/<int:pk>/', views.edit_Dispatch_Of_Green_Nutmeg_table_0, name='edit_Dispatch_Green_0'),
    path('edit/edit_CRK0/<int:pk>/', views.edit_Cracking_Summary_table_0, name='edit_Cracking_0'),
    path('edit/edit_FLT0/<int:pk>/', views.edit_Floation_Summary_table_0, name='edit_Floation_0'),
    path('edit/edit_PKG0/<int:pk>/', views.edit_Package_Ciontrol_table_0, name='edit_Package_0'),



    path('edit/edit_IH/', views.edit_In_House_Drying_table, name='edit_In_House'),
    path('edit/edit_DISD/', views.edit_Dispatch_Of_Dried_Nutmeg_table, name='edit_Dispatch_Dried'),
    path('edit/edit_DISG/', views.edit_Dispatch_Of_Green_Nutmeg_table, name='edit_Dispatch_Green'),
    path('edit/edit_CRK/', views.edit_Cracking_Summary_table, name='edit_Cracking'),
    path('edit/edit_FLT/', views.edit_Floation_Summary_table, name='edit_Floation'),
    path('edit/edit_PKG/', views.edit_Package_Ciontrol_table, name='edit_Package'),








    path('error_In_House/', views.error_In_House, name='error_In_House'),
    path('error_Dispatch_Dried_Nutmeg/', views.error_Dispatch_Dried_Nutmeg, name='error_Dispatch_Dried_Nutmeg'),
    path('error_Dispatch_Green_Nutmeg/', views.error_Dispatch_Green_Nutmeg, name='error_Dispatch_Green_Nutmeg'),
    path('error_Cracking_Nutmeg/', views.error_Cracking_Nutmeg, name='error_Cracking_Nutmeg'),
    path('error_Floation/', views.error_Floation, name='error_Floation'),
    path('error_Package/', views.error_Package, name='error_Package'),




    path('error_In_House_0/', views.error_In_House_0, name='error_In_House_0'),
    path('error_Dispatch_Dried_Nutmeg_0/', views.error_Dispatch_Dried_Nutmeg_0, name='error_Dispatch_Dried_Nutmeg_0'),
    path('error_Dispatch_Green_Nutmeg_0/', views.error_Dispatch_Green_Nutmeg_0, name='error_Dispatch_Green_Nutmeg_0'),
    path('error_Cracking_Nutmeg_0/', views.error_Cracking_Nutmeg_0, name='error_Cracking_Nutmeg_0'),
    path('error_Floation_0/', views.error_Floation_0, name='error_Floation_0'),
    path('error_Package_0/', views.error_Package_0, name='error_Package_0'),



    path('Error/', views.deny_entry, name='deny_entry'),

                                                                                                             
]


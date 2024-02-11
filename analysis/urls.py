from django.contrib import admin
from django.urls import path
from analysis import views


urlpatterns = [
    path('report/',views.report,name='report'),
    path('currentbalance/',views.currentbalance,name='currentbalance'),
    path('liftingreport/', views.liftingreport, name='liftingreport'),
    path('salesreport/', views.salesreport, name='salesreport'),
    path('salesreportresult/<int:supplier_id>/<str:from_date>/<str:to_date>/', views.salesreportresult, name='salesreportresult'),
    path('damagereport/', views.damagereport, name='damagereport'),
    path('damagereportresult/<int:supplier_id>/<str:from_date>/<str:to_date>/', views.damage_report_result, name='damage_report_result'),
    path('costreport/', views.costreport, name='costreport'),  

    path('supplierledgerreport/', views.supplier_ledger_report, name='supplierledgerreport'),
    path('supplierledgerresult/', views.supplier_ledger_result, name='supplierledgerresult'),

    path('redamagetaka/', views.redamagetaka, name='redamagetaka'),

    path('displaytaka/', views.displaytaka, name='displaytaka'),
    path('displaytakaresult/', views.displaytakaresult, name='displaytakaresult'),

    path('claimtaka/', views.claimtaka, name='claimtaka'),
    path('claimtakaresult/', views.claimtakaresult, name='claimtakaresult'),
    path('statementreportresultall/', views.statementreportresultall, name='statementreportresultall'),
    path('statement/', views.statement, name='statement'),  
    path('statementreportresult/', views.statementreportresult, name='statementreportresult'),
    path('statementreportresultall/', views.statementreportresultall, name='statementreportresultall'),

]
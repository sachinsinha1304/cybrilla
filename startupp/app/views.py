from django.shortcuts import render
from .models import*
from django.db.models import Count
from django.db.models import Q
import datetime
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Create your views here.
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n".format(pct, absolute)

def showGraph(dict, que):
    x = list(dict.keys())
    y = [dict[i] for i in x]

    fig = plt.figure(figsize =(10, 7))
    plt.pie(y, labels = x ,autopct=lambda pct: func(pct, y))
    plt.savefig(f"static/{que}.png")

def index(request):
    # df = pd.read_csv(r'app/dataset.csv')
    # shap = df.shape
    # for i in range(shap[0]):
    #     obj = Employee(Lead = df.iloc[i][0],ID = df.iloc[i][1],Services = df.iloc[i][2],Domain = df.iloc[i][3],Channels = df.iloc[i][4],Stage = df.iloc[i][5],Status = df.iloc[i][6],Amount = df.iloc[i][7],Sale_Representative = df.iloc[i][8] ,Created_at = df.iloc[i][9],Signed_at = df.iloc[i][10],Closed_at = df.iloc[i][11])
    #     obj.save()
    date = datetime.date(2022, 10, 1)
    res = Employee.objects.filter(Signed_at__lt = date)
    res1 = Employee.objects.filter(Signed_at__lt = date).aggregate(total = Count('ID'))
    queryset = (Employee.objects.values('Status')).annotate(count = Count('Status'))
    queryset1 = (Employee.objects.values('Stage')).annotate(count = Count('Stage'))
    query = Employee.objects.filter(Q(Stage ='Contracting')| Q(Stage = 'Proposal')).exclude(Q(Status ='Standby') | Q(Status = 'Churned')).values()

    tot = 0
    for i in query:
        tot += int(i['Amount'])

    print(tot)

    dic1 = {}
    for i in queryset:
        dic1[i['Status']] = round(i['count']/30*100,2)

    dic2 = {}
    for i in queryset1:
        dic2[i['Stage']] = round(i['count']/30*100,2)


    showGraph(dic1,1)
    showGraph(dic2,2)

    query2 = Employee.objects.exclude(Closed_at = None).values()
    query2_dict = {}
    for i in query2:
        query2_dict[i['Lead']] = int(i['Amount'])*12

    tot2=0
    for i in query2_dict.values():
        tot2 += i
    return render(request, 'index.html', {'total' : res1, "res" :res, 'dict1':dic1.items(), 'dict2' :dic2.items() , 'query' :query, 'output1':tot, 'query2': query2_dict, 'output2':tot2})

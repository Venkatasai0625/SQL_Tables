from django.shortcuts import render


from app.models import * 

# Create your views here.

def display_emp(request):
    de=Emp.objects.all()
    de=Emp.objects.filter(ENAME='SAI')
    de=Emp.objects.filter(SAL__gt=1000)
    de=Emp.objects.filter(JOB='ANALYST')
    de=Emp.objects.filter(JOB='dev')
    de=Emp.objects.filter(JOB='MANAGER')
    de=Emp.objects.filter(JOB="MANAGER")
    de=Emp.objects.filter(COMM__isnull=False)
    de=Emp.objects.filter(COMM__isnull=True)
    de=Emp.objects.filter(DEPTNO=50)
    
    
    
    de=Emp.objects.all()
    
    
    d={'de':de}
     
    return render(request,'display_emp.html',d)

def insert_EMP(request):
    EMPNO= int(input("Enter empno"))
    ENAME= input("Enter Ename")
    JOB=input("ENTER JOB")
    MGR=input("ENTER MGR")
    HIREDATE=input("ENTER HIREDATE")
    SAL=int(input("ENTER SAL"))
    COMM=int(input("ENTER COMM"))
    DEPTNO=int(input("ENTER DEPTNO"))
    
    LDO=Dept.objects.get(DEPTNO=DEPTNO)
    if LDO:
        EO=Emp.objects.get_or_create(EMPNO=EMPNO,ENAME=ENAME,JOB=JOB,MGR=MGR,HIREDATE=HIREDATE,SAL=SAL,COMM=COMM,DEPTNO=DEPTNO)[0]
        EO.save()
        
        QLEO=Emp.objects.all()
        d={"QLEO":QLEO}
        return render(request,"display_emp.html",d)
    
def Equijoin_emp_dept(request):
    E=Emp.objects.select_related('DEPTNO').all()
    #E=Emp.objects.select_related('DEPTNO').filter(JOB='CLERK')
    #E=Emp.objects.select_related('DEPTNO').filter(JOB='SALESMAN')
    #E=Emp.objects.select_related('DEPTNO').filter(ENAME='SMITH')
    
    
    
    
    d={"E":E}
    
    return render(request,'Equijoin_emp_dept.html',d)

def empdeptmgr(request):
    EDMDO=Emp.objects.select_related('MGR','DEPTNO').all()
    d={'EDMDO':EDMDO}
    return render(request,'empdeptmgr.html',d)

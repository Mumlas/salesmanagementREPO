from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import *


# Create your views here.

class BranchView(View):
    def get(self, request):
        return render(request,'setup/branch.html')
    
    def post(self, request):
        # NewBranch = Branch()
        context = {
            'name':request.POST,
            'address':request.POST
        }
        if request.method=="POST":
            branch = request.POST['branchName']
            if not branch:
                messages.error(request, 'Provide the branch name')
                return render(request, 'setup/branch.html')
    
            address = request.POST['branchAddress']
            if not address:
                messages.error(request, 'Provide the branch address')
                return render(request, 'setup/branch.html')
        
            Branch.objects.create(branchName = branch,
                      branchAddress = address)
            #Branch.save()
            messages.success(request, 'Branch added successfully')
            return redirect('branch')
    

class ProductView(View):
    def get(self, request):
        facilities = Storage.objects.all()
        context = {
            'facilities':facilities,
            'values':request.POST
        }
        return render(request,'setup/product.html', context)
    
    def post(self, request):
        facilities = Storage.objects.all()
        context = {
            'facilities':facilities,
            'values':request.POST
        }
        if request.method=="POST":
            product = request.POST.get('product')
            if not product:
                messages.error(request, 'Select Product type')
                return render(request, 'setup/product.html', {'facilities':facilities})  
            
            facility = request.POST.get('facility')
            if not facility:
                messages.error(request, 'Select the storage/Tank')
                return render(request, 'setup/product.html', {'facilities':facilities})  
            try:
                facility_id = int(facility)
                facility = Storage.objects.get(id=facility_id)
            except Storage.DoesNotExist:
                return render(request, "setup/product.html", {
                    'facilities':facilities,
                    'error':'Selected Storage facility does not exist.'
                })
            
            quantitySupplied = request.POST.get('quantitySupplied')
            if not product:
                messages.error(request, 'Enter the Quantity supplied')
                return render(request, 'setup/product.html', {'facilities':facilities}) 
            
            dateSupplied = request.POST.get('dateSupplied')
            if not dateSupplied:
                messages.error(request, 'Select Date the Product was supplied')
                return render(request, 'setup/product.html', {'facilities':facilities}) 
            
            Product.objects.create(product=product,
                                storage = facility,
                                quantitySupplied = quantitySupplied,
                                dateSupplied =dateSupplied
                                )
            messages.success(request, 'Inventory Update successfully')
            return render(request,'setup/product.html', {'facilities':facilities})          
    
class PumpView(View):
    def get(self, request):
        facilities = Storage.objects.all()
        context = {
            'facilities':facilities,
            'values':request.POST
        }
        return render(request,'setup/pump.html', context)
    
    def post(self, request):
        facilities = Storage.objects.all()

        context = {
            'facilities':facilities,
            'values':request.POST
        }

        if request.method == "POST":
            pumpDescription = request.POST.get('pumpDescription')
            if not pumpDescription:
                messages.error(request, 'Provide the Name/Description')
                return render(request, 'setup/pump.html', {'facilities':facilities})  

            facility = request.POST.get('facility')
            if not facility:
                messages.error(request, 'Select the storage/Tank')
                return render(request, 'setup/pump.html', {'facilities':facilities})  
            try:
                facility_id = int(facility)
                facility = Storage.objects.get(id=facility_id)
            except Storage.DoesNotExist:
                return render(request, "setup/pump.html", {
                    'facilities':facilities,
                    'error':'Selected Storage facility does not exist.'
                })
            
            Pump.objects.create(pupmDesc=pumpDescription,
                                storage = facility)
            messages.success(request, 'Pump added successfully')
            return render(request,'setup/pump.html', {'facilities':facilities})  
                    

class ShiftView(View):
    def get(self, request):
        return render(request,'setup/shift.html')
    
class StorageView(View):
    def get(self,request):
        branches = Branch.objects.all()

        context = {
            'branches' : branches,
            'values' : request.POST
        }  

        return render(request,'setup/storage.html', context)

    #@login_required(login_url='validation/login')       
    def post(self,request):
        branches = Branch.objects.all()

        context = {
            'branches' : branches,
            'values' : request.POST
        }  

        if request.method == 'POST':
            storage = request.POST.get('storage')
            if not storage:
                messages.error(request, 'Provide the Name/Description')
                return render(request, 'setup/storage.html', {'branches':branches})

            branchID = int(request.POST.get('branch'))
            if not branchID:
                messages.error(request, 'Select the branch where the facility is located')
                return render(request, 'setup/storage.html', {'branches':branches})
                       
            quantity = request.POST.get('quantity')
            if not quantity:
                messages.error(request, 'Enter the capacity of the storage facility')
                return render(request, 'setup/storage.html', {'branches':branches})
            
            try:
                branch_id = int(branchID)
                branch = Branch.objects.get(id=branch_id)
            except Branch.DoesNotExist:
                return render(request, "setup/storage.html", {
                    'branches':branches,
                    'error':'Selected branch does not exist.'
                })
                        
            Storage.objects.create(storageDesc = storage,
                                   quantity = quantity,
                                   branch = branch)

            messages.success(request, 'Storage Facility added successfully')
            return render(request,'setup/storage.html', {'branches':branches})    

class StaffView(View):
    def get(self, request):
        return render(request,'setup/staff.html')
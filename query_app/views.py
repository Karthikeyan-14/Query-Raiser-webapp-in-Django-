from django.shortcuts import render,redirect
from.models import register_data,new_query,response_queries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime
from random import randint as ran
from redmail import gmail

# Create your views here.

#function for intial page render
@csrf_exempt
def start(request):
    return render(request,'index.html')

# function for redirect to register page
@csrf_exempt
def reg(request):
    return render(request,'reg.html')

#function for redirect to login page
@csrf_exempt
def login(request):
    return render(request,'log.html')

#function to redirect to dashboard page
def dash_go(request):
    return render(request,'dashboard.html')


"""def otp_check(request):
    if request.method=="POST":
    
        email_reg=request.POST.get('email')
        print(email_reg)
        ran_otp = str(ran(1000, 99999)) 
        gmail.username = "shukk.56@gmail.com"
        gmail.password = "gsar enfw yvvp mvty"

        # Send an email
        gmail.send(
            subject="OTP VERIFICATION",
            receivers=[email_reg],
            text="copy the otp to the clipboard.",
            html="<h1>Your otp is:</h1>"
        )
        otp_var="otp is sended"
        return render(request,'reg.html',{'otp':ran_otp})
      
    return render(request,"reg.html")"""

    



"""def next_page(request):
    return render(request, 'next_page.html')"""

##function for save the registerd details
def log(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        email_reg=request.POST.get('email')
        type_reg=request.POST.get('type')
        password_reg=request.POST.get('password')
        retype_reg=request.POST.get('retype_password')
        print(user_name)
        print(email_reg)
        print(type_reg)
        print(password_reg)
        # check if the user is alredy register if registerd return error message
        if not register_data.objects.filter(reg_mail=email_reg).exists():
            if len(user_name)>=5:
                if len(password_reg)>=8:
                    if(password_reg==retype_reg):
                        user=register_data(reg_user=user_name,reg_mail=email_reg,reg_type=type_reg,reg_pass=password_reg)
                        user.save()
                        #after user registratrion redirect to the login page
                        return render(request,"log.html")
                    else:
                        messages.error(request, 'The password is mismatched!')
                else:
                    messages.error(request, 'The minimum length of password is 8')
            else:
                messages.error(request, 'The minimum length of username is 5')


                
        else:
            print("hello")
            messages.error(request, 'An account with this email already exists.')
        
    return render(request,"reg.html")

##function for login and redirect to email
@csrf_exempt  
def go_dash(request):
    # set the global variable
    global user_id,types
    user_id = None
    if request.method=="POST":
        log_email=request.POST.get('login_email')
        log_password=request.POST.get('login_password')
        # check if the user is already registerd or not
        if register_data.objects.filter(reg_mail=log_email,reg_pass=log_password).exists():
            print(log_email)
            print(log_password)
            t_hr="hr"
            t_director="director"
            t_principal="principal"
    # redirect the necessary data to the dashboard page
            temp_id=register_data.objects.filter(reg_mail=log_email,reg_pass=log_password)
    
            
            
            for i in temp_id:
                name=i.reg_user
            for i in temp_id:
                user_id=i.id
                types=i.reg_type
            print(user_id)
            query_datas = list(response_queries.objects.filter(res_id_id=user_id).values())

            print(query_datas)

            query_dats = list(response_queries.objects.filter(res_id_id=user_id).values())
            
            query1=new_query.objects.filter(id_user_id=user_id)
            print(query1)
           

            length=len(query1)
        # change the options for the each user
            if types=="hr":
                option = [
                {"value": "director","label": "Director", "show": True},
                {"value": "principal","label": "Principal", "show": True},
                {"value": "employee","label": "Employee", "show": True},
                 ]
                context = {
                 'options':option,
                 'length_data':length,
                 'query_dat':query1,
                 'username':name,
                 'current_id':user_id,
                 'type':types,
                 'query_datss': query_dats,
                 'query_datass': query_datas
                }
                return render(request,'admin_dash.html',context)
            elif types=="principal":
                option = [
                {"value": "hr","label": "HR","show": True},
                {"value": "director","label": "Director", "show": True},
        
                {"value": "employee","label": "Employee", "show": True},
                 ]
                context = {
                 'options':option,
                 'query_dat':query1,
                 'username':name,
                 'length_data':length,
                 'current_id':user_id,
                 'type':types,
                 'query_datss': query_dats,
                 'query_datass': query_datas
                }
                return render(request,'admin_dash.html',context)
            elif types=="director":
        

                option = [
                {"value": "hr","label": "HR","show": True},
            
                {"value": "principal","label": "Principal", "show": True},
                {"value": "employee","label": "Employee", "show": True},
                 ]
        
                context = {
                 'options':option,
                 'query_dat':query1,
                 'length_data':length,
                 'username':name,
                 'current_id':user_id,
                 'type':types,
                 'query_datss': query_dats,
                 'query_datass': query_datas
                }
                return render(request,'admin_dash.html',context)
            elif types=="employee":

                option = [
                {"value": "hr","label": "HR","show": True},
                {"value": "director","label": "Director", "show": True},
                {"value": "principal","label": "Principal", "show": True},
                
                 ]
        
                context = {
                 'options':option,
                 'query_dat':query1,
                 'username':name,
                 'length_data':length,
                 'current_id':user_id,
                 'type':types,
                 'query_datss': query_dats,
                 'query_datass': query_datas
                }
                return render(request,'admin_dash.html',context)

        
             

            """ options = [
                {"value": "hr","label": "HR","show": True},
                {"value": "director","label": "Director", "show": True},
                {"value": "principal","label": "Principal", "show": True},
                {"value": "employee","label": "Employee", "show": show_student_options},
            ]"""

            context = {  
                 'query_dat':query1,
                 'username':name,
                 'current_id':user_id,
                 'type':types,
                 'length_data':length,
                 'query_datss': query_dats,
                 'query_datass': query_datas
            }
            return render(request,'dashboard.html',context)

        else:
            print("hello")
            messages.error(request, 'Invalid login details !.')

    return render(request,'log.html')

##function used to save the query details
@csrf_exempt
def save_data(request):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    print(formatted_date)
    if request.method=="POST":
        q_type=request.POST.get('type')
        q_priority=request.POST.get('priority')
        q_title=request.POST.get('title')
        q_query=request.POST.get('qdata')
        if len(q_query)>=20:
        

            print(q_type)
            print(q_priority)
            print(q_title)
            print(q_query)

            current_status="new"
            # saving the query
            use=new_query(query_type=q_type,query_priority=q_priority,query_title=q_title,query_data=q_query,query_date=formatted_date,query_sender=types,query_status=current_status,id_user_id=user_id)
            use.save()

            #return the updated data to dashboard
            query_datas = list(new_query.objects.filter(id_user_id=user_id).values())

            

            return JsonResponse({"status":"Saved","query_datass":query_datas})
        else:
            return JsonResponse({"status":"nothing"})
    else:
        return JsonResponse({"status":"error"})




# model to view the entered query
@csrf_exempt
def modal(request):
    if request.method == "POST":
        query_id = request.POST.get('query_id')
        # Fetch query data based on the query_id
        try:
            query_instance = new_query.objects.get(id=query_id)
            query_data = query_instance.query_data
            print(query_data)
            return JsonResponse({"status": "Success", "query_datass": query_data})
        except new_query.DoesNotExist:
            return JsonResponse({"status": "Error", "message": "Query not found"})
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})

##function for fetch the response
@csrf_exempt
def fetch_res(request):
    if request.method=="POST":
        print("koko")
        type_check=request.POST.get('admin_type')
        data_list=list(new_query.objects.filter(query_type=type_check).values())
        return JsonResponse({"status":"Saved","response_query":data_list})
    else:
        return JsonResponse({"status":"error"})
    
#function used to update the current status
@csrf_exempt
def update(request):
    if request.method=="POST":
        q_id=request.POST.get('q_id')
        q_status=request.POST.get('get_status')
        retrive_data=request.POST.get('quer_org')
        print(q_id)
        print(retrive_data)
        data_change = new_query.objects.get(id=q_id)
        temp_retrive=data_change.query_type
        print(temp_retrive)
        data_change.query_status = q_status
        data_change.save()

        try:
            query_datas = list(new_query.objects.filter(query_type=temp_retrive).values())

            print(query_datas)
            return JsonResponse({"status": "Success", "query_datass": query_datas})
        except new_query.DoesNotExist:
            return JsonResponse({"status": "Error", "message": "Query not found"})
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})
    


#function used to return the responsed data from the table
@csrf_exempt
def responses(request): 
    if request.method == "POST":
        query_userid = request.POST.get('query_userdata')
        print(query_userid)
        #try:
        data_change = register_data.objects.filter(id=query_userid)
        for i in data_change:
            temp_retrive=i.reg_type
        
        print(temp_retrive)
        #retrive the data for students 
        if temp_retrive=="student":
            print("poduu")
            query_datas = list(response_queries.objects.filter(res_id_id=user_id).values())
            print(query_datas)
        #retrive the data for admin
        else:
            query_datas = list(response_queries.objects.filter(res_typ=temp_retrive).values())
            print("ithan",query_datas)            
        return JsonResponse({"status": "Success", "responsed_datas": query_datas})     
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})

 #function used to return the responsed data from the table
@csrf_exempt
def adm_res(request): 
    if request.method == "POST":
        query_userid = request.POST.get('query_userdata')
        print(query_userid)
        #try:
        data_change = register_data.objects.filter(id=query_userid)
        for i in data_change:
            temp_retrive=i.reg_type
        print(temp_retrive)
     
        #retrive the data for admin
        
        query_datas = list(response_queries.objects.filter(query_sender=temp_retrive).values())
        print("ithan",query_datas)            
        return JsonResponse({"status": "Success", "responsed_datas": query_datas})     
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})
  
# function used to save the responses  
@csrf_exempt
def save_res(request):
    if request.method=="POST":
        qid=request.POST.get("res_id")
        r_data=request.POST.get("res_data")
        if len(r_data)>=20:
            print("error")

            res_date = datetime.now()
            responded_date = res_date.strftime("%Y-%m-%d")
            quer_data=new_query.objects.get(id=qid)
            response_type=quer_data.query_type
            print(response_type)
            test_id=quer_data.id_user_id
            print(test_id)
            print("hello")
            temp_id=register_data.objects.filter(id=qid)
            print(temp_id)

            response_priority=quer_data.query_priority
            response_title=quer_data.query_title
        
            query_send_date=quer_data.query_date
            response_sender=quer_data.query_sender
            response_status="closed"

            use=response_queries(res_typ=response_type, res_priority=response_priority, res_title=response_title, query_date=query_send_date, response_data=r_data, resonded_date=responded_date, query_sender=response_sender, status=response_status,res_id_id=test_id)
            use.save()

            temp=new_query.objects.get(id=qid)
            temp.delete()

            return JsonResponse({"status":"Saved"})
    
        else:
            return JsonResponse({"status":"nothing"})

    else:
        return JsonResponse({"status":"error"})

#function used to display the modal  
@csrf_exempt
def modal2(request):
    if request.method == "POST":
        print("hhh")
        query_id_ = request.POST.get('query_ids')
        # Fetch query data based on the query_id
        try:
            query_instance = response_queries.objects.get(id=query_id_)
            query_data = query_instance.response_data

            print(query_data)
            return JsonResponse({"status": "Success", "query_datass": query_data})
        except response_queries.DoesNotExist:
            return JsonResponse({"status": "Error", "message": "Query not found"})
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})
    
#function used to display the report data
@csrf_exempt
def report_data(request):
    if request.method == "POST":
        print("helllll")
        # Fetch query data based on the query_id
        try:
            temp_id=register_data.objects.filter(id=user_id)
            print(temp_id)
            for i in temp_id:
                temp_2=i.reg_type
            print(temp_2)
            if temp_2=="student":
                res_query = list(response_queries.objects.filter(res_id_id=user_id).values())
                send_query = list(new_query.objects.filter(id_user_id=user_id).values())
            else:
                res_query = list(response_queries.objects.filter(res_typ=temp_2).values())
                send_query = list(new_query.objects.filter(query_type=temp_2).values())
            print(res_query)
            print(send_query)
         
            print(send_query)

        
            return JsonResponse({"status": "Success", "responsed_queries":res_query,"sended_queries":send_query})
        except response_queries.DoesNotExist:
            return JsonResponse({"status": "Error", "message": "Query not found"})
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})

#function used to display the query question in modal
@csrf_exempt
def get_question(request):
    if request.method == "POST":
        query_id = request.POST.get('res_id_')
        print(query_id)
        # Fetch query data based on the query_id
    
        query_instance = new_query.objects.get(id=query_id)
        query_data=query_instance.query_data

        print(query_data)

        return JsonResponse({"status": "Success", "question_ques": query_data})
        
    else:
        return JsonResponse({"status": "Error", "message": "Invalid request method"})


     











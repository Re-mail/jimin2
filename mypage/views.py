from django.shortcuts import render, redirect
from user.models import User
from .models import Remail

def mypage(request):
    return render(request,'mypage/mypage.html')

# def check_unique_remails(input_remail):
#     if Remail.objects.filter(remail1=input_remail).exists() or \
#        Remail.objects.filter(remail2=input_remail).exists() or \
#        Remail.objects.filter(remail3=input_remail).exists() or \
#        Remail.objects.filter(remail4=input_remail).exists() or \
#        Remail.objects.filter(remail5=input_remail).exists():
#         return False
#     return True

    # if input_remail:
    #     all_remails = Remail.objects.exclude(
    #         remail1='', remail2='', remail3='', remail4='', remail5=''
    #     )
        
    #     for remail in all_remails:
    #         if (remail.remail1 == input_remail or
    #             remail.remail2 == input_remail or
    #             remail.remail3 == input_remail or
    #             remail.remail4 == input_remail or
    #             remail.remail5 == input_remail):
    #             return False  # 중복되는 이메일이 발견되면 False 반환
    #     return True  # 중복되는 이메일이 없으면 True 반환
    # return False  # input_remail이 빈 값인 경우에도 중복으로 처리

    

def new_address(request):
    if request.method == 'GET':
        return render(request, 'mypage/new_address.html')
    
    elif request.method == 'POST':
        user = request.user
        remail_instance, created = Remail.objects.get_or_create(user=user)
        input_remail = request.POST.get('input_remail')
        
        if input_remail:
            
            remail_instance.remail1 = input_remail
            remail_instance.save()
        # number = request.POST.get('number')
        # if number == '1':
        #         remail_instance.remail1 = input_remail
        # elif number == '2':
        #     remail_instance.remail2 = input_remail
        # elif number == '3':
        #     remail_instance.remail3 = input_remail
        # elif number == '4':
        #     remail_instance.remail4 = input_remail
        # elif number == '5':
        #     remail_instance.remail5 = input_remail
        
                
        return render(request, 'mypage/mypage.html')
   
    # user = request.user
    # remail_instance = request.user.remail
    
    # input_remail = request.POST.get('input_remail')
    # number = int(request.POST.get("number", 0))
    
    # if check_unique_remails(input_remail):
    #     remail_instance, created = Remail.objects.get_or_create(user=user)
    #     if number == 1:
    #         setattr(remail_instance, f'remail{number}', input_remail)
    #     elif number == 2:
    #         setattr(remail_instance, f'remail{number}', input_remail)
    #     elif number == 3:
    #         setattr(remail_instance, f'remail{number}', input_remail)
    #     elif number == 4:
    #         setattr(remail_instance, f'remail{number}', input_remail)
    #     elif number == 5:
    #         setattr(remail_instance, f'remail{number}', input_remail)
    #     remail_instance.save()
    #     return render(request, 'mypage/mypage.html')
    
    # else:
    #     error_message = '잘못된 번호입니다.'
    #     return render(request, 'mypage/new_address.html', {'error_message': error_message})
        
  

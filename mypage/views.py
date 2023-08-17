from django.shortcuts import render, redirect, get_object_or_404
from user.models import User
from .models import Remail, Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls import reverse

def mypage(request):
    if request.method == 'GET':
        return render(request, 'mypage/mypage.html')
    
    elif request.method == 'POST':
        try:
            user = request.user
            remail_instance, created = Remail.objects.get_or_create(user=user)
            number = request.POST.get('number')
            
            if number == "1":
                if remail_instance.remail1:
                    address = remail_instance.remail1
                    cate = remail_instance.category1
                    
                    return render(request,'mypage/mypage.html', {'add1':address,'ctgr1':cate })
                else:
                    address = 'none'
                    return render(request,'mypage/mypage.html', {'add1':address})
                
            if number == "2":
                if remail_instance.remail2:
                    address = remail_instance.remail2
                    cate = remail_instance.category2
                    
                    return render(request,'mypage/mypage.html', {'add2':address,'ctgr2':cate})
                else:
                    address = 'none'
                    return render(request,'mypage/mypage.html', {'add2':address})
                
            if number == "3":
                if remail_instance.remail3:
                    address = remail_instance.remail3
                    cate = remail_instance.category3
                    
                    return render(request,'mypage/mypage.html', {'add3':address,'ctgr3':cate})
                else:
                    address = 'none'
                    return render(request,'mypage/mypage.html', {'add3':address})
                
            if number == "4":
                if remail_instance.remail4:
                    address = remail_instance.remail4
                    cate = remail_instance.category4
                    
                    return render(request,'mypage/mypage.html', {'add4':address,'ctgr4':cate})
                else:
                    address = 'none'
                    return render(request,'mypage/mypage.html', {'add4':address})
            if number == "5":
                if remail_instance.remail5:
                    address = remail_instance.remail5
                    cate = remail_instance.category5
                    
                    return render(request,'mypage/mypage.html', {'add5':address,'ctgr5':cate})
                else:
                    address = 'none'
                    return render(request,'mypage/mypage.html', {'add5':address})
        except:
            return render(request,'mypage/mypage.html')


def check_unique_remails(input_remail):
    if Remail.objects.filter(remail1=input_remail).exists() or \
       Remail.objects.filter(remail2=input_remail).exists() or \
       Remail.objects.filter(remail3=input_remail).exists() or \
       Remail.objects.filter(remail4=input_remail).exists() or \
       Remail.objects.filter(remail5=input_remail).exists():
        return False # 중복되는 이메일이 발견되면 False 반환
    return True

def check_null(input):
    if input == "" :
        return True
    else : 
        return False
    

def new_address(request):
    if request.method == 'GET':
        return render(request, 'mypage/new_address.html')
    
    elif request.method == 'POST':
        try:
            user = request.user
            remail_instance, created = Remail.objects.get_or_create(user=user)
            
            input_remail = request.POST.get('input_remail')
            input_category = request.POST.get('input_category')
            
            number = request.POST.get('number')
    
            if input_remail and '@re-mail.link' in input_remail:
                if check_unique_remails(input_remail):
                    if number == "1":
                        if not remail_instance.remail1:
                            remail_instance.remail1 = input_remail
                            remail_instance.category1 = input_category
                            remail_instance.save()
                        else : 
                            return  render(request, "mypage/new_address.html", {"message": "already_exists"})
                    elif number == "2":
                        if not remail_instance.remail2:
                            remail_instance.remail2 = input_remail
                            remail_instance.category2 = input_category
                            remail_instance.save()
                        else : 
                            return  render(request, "mypage/new_address.html", {"message": "already_exists"})
                    elif number == "3":
                        if not remail_instance.remail3:
                            remail_instance.remail3 = input_remail
                            remail_instance.category3 = input_category
                            remail_instance.save()
                        else : 
                            return  render(request, "mypage/new_address.html", {"message": "already_exists"})
                    elif number == "4":
                        if not remail_instance.remail4:
                            remail_instance.remail4 = input_remail
                            remail_instance.category4 = input_category
                            remail_instance.save()
                        else : 
                            return  render(request, "mypage/new_address.html", {"message": "already_exists"})
                    elif number == "5":
                        if not remail_instance.remail5:
                            remail_instance.remail5 = input_remail
                            remail_instance.category5 = input_category
                            remail_instance.save()
                        else : 
                            return  render(request, "mypage/new_address.html", {"message": "already_exists"})
                else:
                    return render(request, 'mypage/new_address.html', {'message': "overlap_address"})
        except:
              return render(request, 'mypage/new_address.html', {'message': "overlap_address"})

        else:
            return render(request, 'mypage/new_address.html', {'message': "invalid"})
    return render(request, 'mypage/mypage.html')
  
def polls(request):
    question = Question.objects.all()
    return render(request, 'mypage/polls.html',{'question':question})

def detail(request,qid):
    choice = get_object_or_404(Question,id=qid)
    return render(request, 'mypage/detail.html',{'q':choice})

def vote(request):
    if request.method == 'GET':
        return render(request, 'mypage/new_address.html')
    
    elif request.method == "POST":
        vote_id = request.POST.get('question') #사용자가 선택한 질문 번호
        c = get_object_or_404(Choice,id=vote_id)
        
        # c = Choice.objects.get_or_create(id=vote_id)
        c.votes +=1
        c.save()
        return render(request, 'mypage/polls.html', {'message': "complete"})
    
    else:
        return render(request, 'mypage/mypage.html')
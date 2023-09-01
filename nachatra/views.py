from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, SellerRegistrationForm
from astro .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    # astro_users = Profile.objects.filter(Role='Astro')
    astro_users = Pooja.objects.all().order_by()[:4]
    print(astro_users)
    context = {'astro': astro_users ,"profile":"2"}
    return render(request, 'home.html',context)


# views.py
@csrf_exempt
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # if profile_id is not None:
            #     recommended_by_profile = Profile.objects.get(id=profile_id)
            #     print('profile',recommended_by_profile)
            #     instance = form.save()
            #     register_user = User.objects.get(id=instance.id)
            #     register_profile = Profile.objects.get(user =register_user)
            #     register_profile.recommended_by = recommended_by_profile.user
            #     register_profile.save()
            # else:
            form.save()
            user = form.save(commit=False)
            user.is_active = False
            print("1 active = flse")
            user.save()
            
         
            return render(request , 'login.html')

    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})
    # if request.method == 'POST':
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         # Process form data and create user account
    #         return redirect('login')  # Redirect to login page
    # else:
    #     form = UserRegistrationForm()
    # return render(request, 'user_registration.html', {'form': form})
@csrf_exempt
def seller_registration(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.is_active = False
            print("1 active = flse")
            user.save()
            
            return redirect('login')  # Redirect to login page
    else:
        form = SellerRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

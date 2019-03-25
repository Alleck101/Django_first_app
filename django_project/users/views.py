from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

"""
Profile update section.
We have 3 fields (username, email and pic). First of all we check if the current data in those fields 
is valid (default values are current profile data). 
VALID ROUTE: If edited values are valid, than we proceed with
POST request, our new data is saved and success message is shown. After this page will be reloaded
(redirected to itself) to submit new data.
INVALID ROUTE: if data is invalid it wont submit and small message will be shown under fields that
dont meet the requirement conditions.
"""
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save() 
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)

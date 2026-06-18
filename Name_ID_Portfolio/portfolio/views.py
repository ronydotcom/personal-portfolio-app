from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from portfolio.models import *
from portfolio.forms import *


# Registration

def register_page(request):
    if request.method=='POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Registration Complete')
            return redirect('login_page')
    else:
        form_data=RegistrationForm()

    context={
        'form_data':form_data,
        'form_title':'Registration Form',
        'form_btn':'Register'
    }

    return render(request,'master/base-form.html',context)


# Login

def login_page(request):
    form_data=AuthenticationForm(request,data=request.POST)

    if request.method=='POST':
        if form_data.is_valid():
            user=form_data.get_user()
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('dashboard_page')

    context={
        'form_data':form_data,
        'form_title':'Login Form',
        'form_btn':'Login'
    }

    return render(request,'master/base-form.html',context)


# Logout

@login_required
def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('login_page')


# Profile Create / Update / Delete

@login_required
def profile_page(request):

    profile=Profile.objects.filter(user=request.user).first()

    if request.method=='POST' and 'delete_profile' in request.POST:
        if profile:
            profile.delete()
            messages.success(request,'Profile Deleted Successfully')
        return redirect('profile_page')

    if request.method=='POST':
        form_data=ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.user=request.user
            save_data.save()

            if profile:
                messages.success(request,'Profile Updated Successfully')
            else:
                messages.success(request,'Profile Created Successfully')

            return redirect('profile_page')

    else:
        form_data=ProfileForm(instance=profile)

    if not profile or request.GET.get('edit'):
        context={
            'form_data':form_data,
            'form_title':'Profile Form',
            'form_btn':'Save Profile'
        }

        return render(request,'master/base-form.html',context)

    return render(request,'profile.html',{'profile':profile})


# Dashboard

@login_required
def dashboard_page(request):

    profile=Profile.objects.filter(user=request.user).first()

    skill_count=Skill.objects.filter(user=request.user).count()
    education_count=Education.objects.filter(user=request.user).count()
    experience_count=Experience.objects.filter(user=request.user).count()
    project_count=Project.objects.filter(user=request.user).count()

    context={
        'profile':profile,
        'skill_count':skill_count,
        'education_count':education_count,
        'experience_count':experience_count,
        'project_count':project_count,
    }

    return render(request,'dashboard.html',context)


# Resume
@login_required
def resume_page(request):

    profile=Profile.objects.filter(user=request.user).first()

    skills=Skill.objects.filter(user=request.user)
    educations=Education.objects.filter(user=request.user)
    experiences=Experience.objects.filter(user=request.user)

    context={
        'profile':profile,
        'skills':skills,
        'educations':educations,
        'experiences':experiences,
    }

    return render(request,'resume.html',context)


# Project List
@login_required
def project_page(request):

    projects=Project.objects.filter(user=request.user).order_by('-id')

    return render(request,'project.html',{'projects':projects})


# Add Project

@login_required
def add_project_page(request):

    if request.method=='POST':
        form_data=ProjectForm(
            request.POST,
            request.FILES
        )

        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.user=request.user
            save_data.save()

            messages.success(request,'Project Added Successfully')
            return redirect('project_page')

    else:
        form_data=ProjectForm()

    context={
        'form_data':form_data,
        'form_title':'Add Project',
        'form_btn':'Save Project'
    }

    return render(request,'master/base-form.html',context)


# Update Project

@login_required
def update_project_page(request,id):

    project=get_object_or_404(
        Project,
        id=id,
        user=request.user
    )

    if request.method=='POST':
        form_data=ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Project Updated Successfully')
            return redirect('project_page')

    else:
        form_data=ProjectForm(instance=project)

    context={
        'form_data':form_data,
        'form_title':'Update Project',
        'form_btn':'Update Project'
    }

    return render(request,'master/base-form.html',context)


# Delete Project

@login_required
def delete_project_page(request,id):

    project=get_object_or_404(
        Project,
        id=id,
        user=request.user
    )

    project.delete()

    messages.success(
        request,
        'Project Deleted Successfully'
    )

    return redirect('project_page')


# Skill List

@login_required
def skill_page(request):

    skill_data=Skill.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'skill.html',
        {'skill_data':skill_data}
    )


# Add Skill

@login_required
def add_skill_page(request):

    if request.method=='POST':
        form_data=SkillForm(request.POST)

        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.user=request.user
            save_data.save()

            messages.success(request,'Skill Added Successfully')
            return redirect('skill_page')

    else:
        form_data=SkillForm()

    context={
        'form_data':form_data,
        'form_title':'Add Skill',
        'form_btn':'Save Skill'
    }

    return render(request,'master/base-form.html',context)


# Update Skill

@login_required
def update_skill_page(request,id):

    skill=get_object_or_404(
        Skill,
        id=id,
        user=request.user
    )

    if request.method=='POST':
        form_data=SkillForm(
            request.POST,
            instance=skill
        )

        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Skill Updated Successfully')
            return redirect('skill_page')

    else:
        form_data=SkillForm(instance=skill)

    context={
        'form_data':form_data,
        'form_title':'Update Skill',
        'form_btn':'Update Skill'
    }

    return render(request,'master/base-form.html',context)


# Delete Skill

@login_required
def delete_skill_page(request,id):

    skill=get_object_or_404(
        Skill,
        id=id,
        user=request.user
    )

    skill.delete()

    messages.success(request,'Skill Deleted Successfully')

    return redirect('skill_page')


# Education List

@login_required
def education_page(request):

    education_data=Education.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'education.html',
        {'education_data':education_data}
    )


# Add Education

@login_required
def add_education_page(request):

    if request.method=='POST':
        form_data=EducationForm(request.POST)

        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.user=request.user
            save_data.save()

            messages.success(request,'Education Added Successfully')
            return redirect('education_page')

    else:
        form_data=EducationForm()

    context={
        'form_data':form_data,
        'form_title':'Add Education',
        'form_btn':'Save Education'
    }

    return render(request,'master/base-form.html',context)




# Update Education

@login_required
def update_education_page(request,id):

    education=get_object_or_404(
        Education,
        id=id,
        user=request.user
    )

    if request.method=='POST':
        form_data=EducationForm(
            request.POST,
            instance=education
        )

        if form_data.is_valid():
            form_data.save()
            messages.success(
                request,
                'Education Updated Successfully'
            )
            return redirect('education_page')

    else:
        form_data=EducationForm(instance=education)

    context={
        'form_data':form_data,
        'form_title':'Update Education',
        'form_btn':'Update Education'
    }

    return render(
        request,
        'master/base-form.html',
        context
    )


# Delete Education

@login_required
def delete_education_page(request,id):

    education=get_object_or_404(
        Education,
        id=id,
        user=request.user
    )

    education.delete()

    messages.success(
        request,
        'Education Deleted Successfully'
    )

    return redirect('education_page')




# Experience List

@login_required
def experience_page(request):

    experience_data=Experience.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'experience.html',
        {'experience_data':experience_data}
    )


# Add Experience

@login_required
def add_experience_page(request):

    if request.method=='POST':
        form_data=ExperienceForm(request.POST)

        if form_data.is_valid():
            save_data=form_data.save(commit=False)
            save_data.user=request.user
            save_data.save()

            messages.success(request,'Experience Added Successfully')
            return redirect('experience_page')

    else:
        form_data=ExperienceForm()

    context={
        'form_data':form_data,
        'form_title':'Add Experience',
        'form_btn':'Save Experience'
    }

    return render(request,'master/base-form.html',context)



# Update Experience

@login_required
def update_experience_page(request,id):

    experience=get_object_or_404(
        Experience,
        id=id,
        user=request.user
    )

    if request.method=='POST':

        form_data=ExperienceForm(
            request.POST,
            instance=experience
        )

        if form_data.is_valid():

            form_data.save()

            messages.success(
                request,
                'Experience Updated Successfully'
            )

            return redirect('experience_page')

    else:

        form_data=ExperienceForm(
            instance=experience
        )

    context={
        'form_data':form_data,
        'form_title':'Update Experience',
        'form_btn':'Update Experience'
    }

    return render(
        request,
        'master/base-form.html',
        context
    )


# Delete Experience

@login_required
def delete_experience_page(request,id):

    experience=get_object_or_404(
        Experience,
        id=id,
        user=request.user
    )

    experience.delete()

    messages.success(
        request,
        'Experience Deleted Successfully'
    )

    return redirect('experience_page')




# Contact
@login_required
def contact_page(request):

    if request.method=='POST':
        form_data=ContactForm(request.POST)

        if form_data.is_valid():
            form_data.save()

            messages.success(
                request,
                'Message Sent Successfully'
            )

            return redirect('contact_page')

    else:
        form_data=ContactForm()

    context={
        'form_data':form_data,
        'form_title':'Contact Form',
        'form_btn':'Send Message'
    }

    return render(request,'master/base-form.html',context)
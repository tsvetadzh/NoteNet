from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.utils import timezone
import datetime
import re
from .models import UserProfile, Material, MaterialFile


SUBJECTS = {
    (8, 'system'): [
        {'name': 'Intro into Programming', 'slug': 'inro_program'},
        {'name': 'IT', 'slug': 'it'},
        {'name': 'Intro to Specialty', 'slug': 'intro_special'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Chemistry', 'slug': 'chem'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
    ],

    (8, 'networks'): [
        {'name': 'Intro into Programming', 'slug': 'inro_program'},
        {'name': 'IT', 'slug': 'it'},
        {'name': 'Intro to Specialty', 'slug': 'intro_special'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Chemistry', 'slug': 'chem'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
    ],

    (8, 'ai'): [
        {'name': 'Intro into Programming', 'slug': 'inro_program'},
        {'name': 'IT', 'slug': 'it'},
        {'name': 'Intro to Specialty', 'slug': 'intro_special'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Chemistry', 'slug': 'chem'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
    ],

    (9, 'system'): [
        {'name': 'Scripts', 'slug': 'scripts'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'Programming', 'slug': 'programming'},
        {'name': 'Networks', 'slug': 'networkssubj'},
        {'name': 'Electrotechnics', 'slug': 'electrotechnics'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Gradivni', 'slug': 'gradivni'},
        {'name': 'Chemistry', 'slug': 'chemistry'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'Enterprenuering', 'slug': 'enterprenuering'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'IT', 'slug': 'it'},
        {'name': 'Zbut', 'slug': 'zbut'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Russian', 'slug': 'russian'},
    ],

    (9, 'networks'): [
        {'name': 'Scripts', 'slug': 'scripts'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'Programming', 'slug': 'programming'},
        {'name': 'Networks', 'slug': 'networkssubj'},
        {'name': 'Electrotechnics', 'slug': 'electrotechnics'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Gradivni', 'slug': 'gradivni'},
        {'name': 'Chemistry', 'slug': 'chemistry'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'Enterprenuering', 'slug': 'enterprenuering'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'IT', 'slug': 'it'},
        {'name': 'Zbut', 'slug': 'zbut'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Russian', 'slug': 'russian'},
    ],

    (10, 'system'): [
        {'name': 'Intro to OOP', 'slug': 'oop'},
        {'name': 'Intro to ASD', 'slug': 'asd'},
        {'name': 'Intro to VMKS', 'slug': 'vmks'},
        {'name': 'Digital schemotech', 'slug': 'digital_sch'},
        {'name': 'Analogy schemotech', 'slug': 'analogy_sch'},
        {'name': 'Gradivni', 'slug': 'gradivni'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Chemistry', 'slug': 'chem'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'Iconomics', 'slug': 'iconomics'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Russian', 'slug': 'russian'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Maths', 'slug': 'maths'},
    ],

    (10, 'networks'): [
        {'name': 'Intro to OOP', 'slug': 'oop'},
        {'name': 'CAPD', 'slug': 'comp_arch_per_dev'},
        {'name': 'Intro to VMKS', 'slug': 'vmks'},
        {'name': 'Digital schemotech', 'slug': 'digital_sch'},
        {'name': 'Analogy schemotech', 'slug': 'analogy_sch'},
        {'name': 'CMr', 'slug': 'intro_cmr'},
        {'name': 'Physycs', 'slug': 'physycs'},
        {'name': 'Chemistry', 'slug': 'chem'},
        {'name': 'Phylosophy', 'slug': 'phylosophy'},
        {'name': 'History', 'slug': 'history'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'Iconomics', 'slug': 'iconomics'},
        {'name': 'Geography', 'slug': 'geography'},
        {'name': 'Biology', 'slug': 'biology'},
        {'name': 'Russian', 'slug': 'russian'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Maths', 'slug': 'maths'},
    ],

    (11, 'system'): [
        {'name': 'OS', 'slug': 'os'},
        {'name': 'Databases', 'slug': 'database'},
        {'name': 'Object-oriented programming', 'slug': 'object_progr'},
        {'name': 'Software', 'slug': 'software'},
        {'name': 'Math programming', 'slug': 'math_progr'},
        {'name': 'VMKS', 'slug': 'vmks'},
        {'name': 'VOT', 'slug': 'vot'},
        {'name': 'GO', 'slug': 'go'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'Russian', 'slug': 'russian'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'English', 'slug': 'english'},
    ],

    (11, 'networks'): [
        {'name': 'APE', 'slug': 'ape'},
        {'name': 'USSS', 'slug': 'usss'},
        {'name': 'BOMT', 'slug': 'bomt'},
        {'name': 'Networks', 'slug': 'networkssubj'},
        {'name': 'Math programming', 'slug': 'mpt'},
        {'name': 'VMKS', 'slug': 'vmks'},
        {'name': 'KTT', 'slug': 'ktt'},
        {'name': 'GO', 'slug': 'go'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'Russian', 'slug': 'russian'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'English', 'slug': 'english'},
    ],

    (12, 'system'): [
        {'name': 'IoT', 'slug': 'iot'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Software Engineering', 'slug': 'software_eng'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'GO', 'slug': 'go'},
        {'name': 'VMKS', 'slug': 'vmks'},
        {'name': 'Internet Programming', 'slug': 'internet_prog'},
        {'name': 'Graphical Interface', 'slug': 'gr_inter'},
        {'name': 'Graphical Design', 'slug': 'gr_design'},
        {'name': 'Russian', 'slug': 'russian'},
        {'name': 'IDKM', 'slug': 'idkm'},
        {'name': 'VOT', 'slug': 'vot'},
    ],

    (12, 'networks'): [
        {'name': 'Switched Networks', 'slug': 'snetworks'},
        {'name': 'Global Networks', 'slug': 'global_networks'},
        {'name': 'Network Security', 'slug': 'net_security'},
        {'name': 'System Administration', 'slug': 'sistem_adm'},
        {'name': 'IoT', 'slug': 'iot'},
        {'name': 'VMKS', 'slug': 'vmks'},
        {'name': 'Literature', 'slug': 'literature'},
        {'name': 'English', 'slug': 'english'},
        {'name': 'Maths', 'slug': 'maths'},
        {'name': 'Russian', 'slug': 'russian'},
    ],
}

_SUBJECT_NAMES = {s['slug']: s['name'] for subjects in SUBJECTS.values() for s in subjects}

def check_profile(request):
    if not request.user.is_authenticated:
        return None
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if profile.check_and_update_grade():
        messages.success(request, f"Congratulations! You have automatically advanced to Grade {profile.get_grade_display()}!")
    return profile

def parse_grade(grade_str):
    grade_str = grade_str.strip().lower()
    match = re.match(r'^(\d+)([a-d])$', grade_str)
    if match:
        num = int(match.group(1))
        letter = match.group(2)
        if 8 <= num <= 12:
            return num, letter
    return None

def homepage(request):
    profile = None
    if request.user.is_authenticated:
        profile = check_profile(request)
        if not profile.full_name or not profile.grade_number:
            return redirect('setup_profile')
    return render(request, 'homepage.html', {'profile': profile})


def setup_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        grade_str = request.POST.get('grade', '').strip()
        
        parsed = parse_grade(grade_str)
        if not full_name:
            messages.error(request, "Name is required.")
        elif not parsed:
            messages.error(request, "Invalid Grade. Must be like 9a, 8b, 10c, 11d, 12a (Grade 8-12, Section a-d).")
        else:
            num, letter = parsed
            profile.full_name = full_name
            profile.grade_number = num
            profile.grade_letter = letter
            profile.grade_updated_at = timezone.now()
            profile.save()
            messages.success(request, f"Profile updated! Welcome to NoteNet, Grade {profile.get_grade_display()}.")
            return redirect('profile')
            
    return render(request, 'setup_profile.html', {'profile': profile})

def simulate_grade_advancement(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
        
    # Shift grade_updated_at exactly 365 days into the past
    profile.grade_updated_at = profile.grade_updated_at - datetime.timedelta(days=365)
    profile.save()
    
    # Check if the rollover triggers
    if profile.check_and_update_grade():
        messages.success(request, f"[SIMULATION] 365 Days passed! Automatically advanced to Grade {profile.get_grade_display()}!")
    else:
        messages.warning(request, "[SIMULATION] Date shifted back 365 days, but rollover did not trigger (already capped at 12?).")
        
    return redirect('profile')

def upload_material(request, grade, subject):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=401)
    
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number or profile.grade_number != grade:
        return JsonResponse({'success': False, 'error': 'Access Denied'}, status=403)
        
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        description = request.POST.get('description', '').strip()
        section = request.POST.get('section', profile.grade_letter).strip().lower()
        
        if not files:
            return JsonResponse({'success': False, 'error': 'No files uploaded.'}, status=400)
            
        # Create Material
        material = Material.objects.create(
            grade=grade,
            section=section,
            subject=subject,
            description=description,
            uploaded_by=request.user
        )
        
        # Save each file associated with this material
        for f in files:
            MaterialFile.objects.create(material=material, file=f)
        
        return JsonResponse({
            'success': True,
            'message': 'Material uploaded successfully!'
        })
        
    return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=400)


def addnote(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
    return render(request, 'addnote.html')

def materials(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
    return render(request, 'materials.html', {'profile': profile})

def myclass(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
    
    group = 'networks' if profile.grade_letter == 'd' else 'system'
    info = _GRADE_INFO.get(profile.grade_number)
    prefix = info['prefix']
    url_name = f"{prefix}_{group}"
    return redirect(url_name)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
        
    # Calculate days remaining for the next grade rollover
    next_advancement = profile.grade_updated_at + datetime.timedelta(days=365)
    delta = next_advancement - timezone.now()
    days_left = max(0, delta.days)
    
    # Progress percentage
    days_passed = 365 - days_left
    progress_percentage = min(100, max(0, int((days_passed / 365.0) * 100)))
    
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': profile,
        'days_left': days_left,
        'progress_percentage': progress_percentage,
        'grade_updated_at': profile.grade_updated_at
    })

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if not username or not password1:
            messages.error(request, 'Username and password are required.')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('setup_profile')

    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile, _ = UserProfile.objects.get_or_create(user=user)
            if not profile.full_name or not profile.grade_number:
                return redirect('setup_profile')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')

_GRADE_INFO = {
    8:  {'ordinal': '8th',  'prefix': 'eight'},
    9:  {'ordinal': '9th',  'prefix': 'nine'},
    10: {'ordinal': '10th', 'prefix': 'ten'},
    11: {'ordinal': '11th', 'prefix': 'eleven'},
    12: {'ordinal': '12th', 'prefix': 'twelve'},
}

def class_grade(request, grade):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
        
    if profile.grade_number != grade:
        messages.warning(request, f"Access Denied: You are in grade {profile.get_grade_display()} and can only access Grade {profile.grade_number} resources.")
        return redirect('class_grade', grade=profile.grade_number)
        
    info = _GRADE_INFO.get(grade)
    if not info:
        raise Http404
    prefix = info['prefix']
    return render(request, 'classes/class.html', {
        'grade': grade,
        'grade_name': info['ordinal'],
        'system_url': f'{prefix}_system',
        'networks_url': f'{prefix}_networks',
    })

def subject_list(request, grade, group):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
        
    if profile.grade_number != grade:
        messages.warning(request, f"Access Denied: You are in grade {profile.get_grade_display()} and can only access Grade {profile.grade_number} resources.")
        return redirect('class_grade', grade=profile.grade_number)
        
    subjects = SUBJECTS.get((grade, group), [])
    return render(request, 'subjects/subject_list.html', {
        'subjects': subjects,
        'grade': grade,
        'group': group,
    })

def discipline(request, grade, subject):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = check_profile(request)
    if not profile.full_name or not profile.grade_number:
        return redirect('setup_profile')
        
    if profile.grade_number != grade:
        messages.warning(request, f"Access Denied: You are in grade {profile.get_grade_display()} and can only access Grade {profile.grade_number} resources.")
        return redirect('class_grade', grade=profile.grade_number)
        
    name = _SUBJECT_NAMES.get(subject, subject.replace('_', ' ').title())
    
    selected_section = request.GET.get('section', profile.grade_letter).strip().lower()
    if selected_section not in ['a', 'b', 'c', 'd']:
        selected_section = profile.grade_letter
        
    materials_list = Material.objects.filter(
        grade=grade,
        subject=subject,
        section=selected_section
    ).order_by('-uploaded_at')
    
    return render(request, 'disciplines/discipline.html', {
        'grade': grade,
        'subject': subject,
        'subject_name': name,
        'materials': materials_list,
        'selected_section': selected_section,
        'sections': ['a', 'b', 'c', 'd'],
        'profile': profile
    })



from django.shortcuts import render 

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

def homepage(request):
    return render(request, 'homepage.html')

def addnote(request):
    return render(request, 'addnote.html')

def materials(request):
    return render(request, 'materials.html')

def myclass(request):
    return render(request, 'myclass.html')

def profile(request):
    return render(request, 'profile.html')



_GRADE_INFO = {
    8:  {'ordinal': '8th',  'prefix': 'eight'},
    9:  {'ordinal': '9th',  'prefix': 'nine'},
    10: {'ordinal': '10th', 'prefix': 'ten'},
    11: {'ordinal': '11th', 'prefix': 'eleven'},
    12: {'ordinal': '12th', 'prefix': 'twelve'},
}

def class_grade(request, grade):
    from django.http import Http404
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
    subjects = SUBJECTS.get((grade, group), [])
    return render(request, 'subjects/subject_list.html', {
        'subjects': subjects,
        'grade': grade,
        'group': group,
    })

def discipline(request, grade, subject):
    name = _SUBJECT_NAMES.get(subject, subject.replace('_', ' ').title())
    return render(request, 'disciplines/discipline.html', {
        'grade': grade,
        'subject': subject,
        'subject_name': name,
    })


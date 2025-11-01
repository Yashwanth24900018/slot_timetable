from django.shortcuts import render

def timetable(request):
    return render(request, 'timetable_display/timetable.html')

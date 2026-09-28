from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student


def add_student(request):

    if request.method == "POST":

        name = request.POST.get("student_name")
        email = request.POST.get("student_email")
        course = request.POST.get("student_course")
        fees = request.POST.get("student_fees")

        Student.objects.create(
            student_name=name,
            student_email=email,
            student_course=course,
            student_fees=fees
        )

        return redirect("student_list")

    return render(request, "add_student.html")

def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        "student_list.html",
        {"students": students}
    )


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.student_name = request.POST.get("student_name")
        student.student_email = request.POST.get("student_email")
        student.student_course = request.POST.get("student_course")
        student.student_fees = request.POST.get("student_fees")

        student.save()

        return redirect("student_list")

    return render(
        request,
        "edit_student.html",
        {"student": student}
    )


def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect("student_list")
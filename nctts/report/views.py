from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from nctts.sendEmail import SendEmail
from . import models

# Create your views here.


def report(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        vulnerable_website = request.POST["vweb"]
        date_time = request.POST["dtg"]
        description = request.POST["vdesc"]
        replicate = request.POST["vrep"]
        exploit_code = request.POST["expcode"]
        potential_fix = request.POST["pfix"]
        video = request.POST["vlink"]

        # Checking for duplicates - we do not save duplicate users, but save the vulnerability only
        try:
            duplicate_check = models.PublicUser.objects.get(email=email)
        except ObjectDoesNotExist:
            ins_user = models.PublicUser(
                first_name=first_name, last_name=last_name, email=email
            )
            ins_user.save()
        except MultipleObjectsReturned:
            pass  # we do not have to anything

        user_id = models.PublicUser.objects.filter(
            email=email
        ).first()  # Getting user_id (foreign key)
        ins_vulnerability = models.Vulnerabilities(
            reported_by=user_id,
            vulnerable_website=vulnerable_website,
            date_time=date_time,
            description=description,
            replicate=replicate,
            exploit_code=exploit_code,
            potential_fix=potential_fix,
            video=video,
        )
        ins_vulnerability.save()

        if email != "":
            SendEmail(
                "NCTTS vulnerability submission",
                """
Hello {first_name} {last_name},
Thank you for submitting your vulnerability.
We will review and try to fix the vulnerability within 60 days. Once we fixed the vulnerability, detailed information will be published on our website.""".format(
                    first_name=first_name, last_name=last_name
                ),
                email,
            ).start()

        return redirect("/report/success")

    else:
        return render(request, "report.html")


def success(request):
    return render(request, "success.html")


def delete_info(request):
    if request.method == "POST":
        email = request.POST["email"]
        remarks = request.POST["comments"]
        try:
            record = models.PublicUser.objects.get(email=email)
            record.first_name = "Anonymous"  # When user leaves these fields empty, we have "Anonymous", "User" and "No email".
            record.last_name = "User"  # Hence, when we delete user's contact information, we revert back to the default.
            record.email = "No email"
            record.remarks = remarks
            record.save()
        except ObjectDoesNotExist:
            return redirect("/report/delete_error")
        return redirect("/report/delete_success")
    else:
        return render(request, "delete_info.html")


def delete_success(request):
    return render(request, "delete_success.html")


def view_vulnerabilities(request):
    vulnerabilities = models.Vulnerabilities.objects.filter(status="Fixed")
    return render(
        request, "view_vulnerabilities.html", {"vulnerabilities": vulnerabilities}
    )


def delete_error(request):
    return render(request, "delete_error.html")

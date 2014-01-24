from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from volunteer.models import Volunteer, Timesheet, TimesheetApproval, VolunteerTask, Purchase

admin.site.unregister(User)

class VolunteerInline(admin.StackedInline):
	model = Volunteer

class VolunteerAdmin(UserAdmin):
	inlines = [
		VolunteerInline,
	]

class TimesheetApprovalInline(admin.StackedInline):
	model = TimesheetApproval

class TimesheetAdmin(admin.ModelAdmin):
	model = Timesheet

	inlines = [
		TimesheetApprovalInline,
	]

	list_display = ('volunteer', 'day', 'hours', 'approved',)
	list_filter = ('volunteer',)

class VolunteerTaskAdmin(admin.ModelAdmin):
	model = VolunteerTask
	list_display = ('title', 'description',)

admin.site.register(User, VolunteerAdmin)
admin.site.register(Timesheet, TimesheetAdmin)
admin.site.register(VolunteerTask, VolunteerTaskAdmin)
admin.site.register(Purchase)

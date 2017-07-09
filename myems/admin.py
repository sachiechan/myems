from django.contrib import admin
from .forms import EmployeeForm
from .models import (Employee, Department, DeptEmp, DeptManager,
    Salaries, Titles)


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    search_fields = ('emp_no', 'first_name', 'last_name')
    list_display = ('emp_no', 'first_name', 'last_name')
    save_on_top = True
    actions_on_bottom = False

    def get_form(self, request, obj=None, **kwargs):
        return super(EmployeeAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
admin.site.register(DeptEmp)
admin.site.register(DeptManager)
admin.site.register(Salaries)
admin.site.register(Titles)
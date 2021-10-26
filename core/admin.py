from django.contrib import admin

from core.models import Position, Salary, Employee


def deleter(modeladmin, request, queryset):
    delete_sum_paid = list(queryset.values_list('id', flat=True))
    Salary.objects.filter(employee__in=delete_sum_paid).delete()


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'position', 'employment_date', 'chief',
                    'wages', 'get_all_salary')
    list_filter = ('position', 'position__level')
    actions = [deleter]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('position', 'level')


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('employee', 'date_paid', 'sum_paid')



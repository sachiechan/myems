
def mark_feedback_as_read(modeladmin, request, queryset):
    for emp_feedback in queryset:
        emp_feedback.is_read = True
        emp_feedback.save()

    modeladmin.message_user(request, '{} successfully marked as read'.format(len(queryset)))

mark_feedback_as_read.short_description = 'Mark feedback as read'
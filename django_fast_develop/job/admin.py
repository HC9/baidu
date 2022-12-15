import datetime

from django.contrib import admin, messages
# Register your models here.

# 导入定义的模型
# 再在 admin 的管理网站上进行注册
from job.models import Job, Resume
from interview.models import Candidate


class JobAdmin(admin.ModelAdmin):
	# list_play 是 ModelAdmin 提供的默认属性，可以控制模型的哪些字段可以显示在页面
	# 从而显示字段值，而不是 Object 对象
	list_display = ("job_types", "job_name", "job_city", "job_responsibility", "job_requirement")
	exclude = ("creator", "create_date", "modified_date")

	# exclude 控制表单排除哪些字段
	# 创建时间和更新时间有默认值
	# 可创建人的默认值没法在 model 定义的时间保存

	def save_model(self, request, obj, form, change):
		# save_model 是 django-admin 提供的默认方法，由后台自动调用
		obj.user = request.user
		super().save_model(request, obj, form, change)


class ResumeAdmin(admin.ModelAdmin):
	# list display 控制有哪些属性可以显示
	list_display = (
		'username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major', 'created_date',)
	# 只读属性，某些属性是不能由本人修改的
	readonly_fields = ('applicant', 'created_date', 'modified_date',)
	# 属性需要分段显示
	fieldsets = (
		(None, {'fields': (
			"applicant", ("username", "city", "phone", "email"), ("apply_position", 'born_address', 'gender'),
			("bachelor_school", "master_school", "doctor_school"), ("major", "degree"),
			("candidate_introduction", "work_experience", "project_experience"),
			("created_date", "modified_date"),
		)}),
	)

	def save_model(self, request, obj, form, change):
		obj.applicant = request.user
		super().save_model(request, obj, form, change)

	@admin.action(description="进入面试流程")
	def _enter_interview_process(self, request, queryset):
		candidate_names = ""
		for resume in queryset:
			candidate = Candidate()
			# 使用 __dict__ 属性进行拷贝
			candidate.__dict__.update(resume.__dict__)
			candidate.created_date = datetime.datetime.now()
			candidate.modified_date = datetime.datetime.now()
			candidate.creator = request.user.username
			candidate.save()
			candidate_names = candidate.username + ',' + candidate_names
		messages.add_message(request, messages.INFO, '候选人:{} 已进入面试流程'.format(candidate_names))

	actions = (_enter_interview_process,)


admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)

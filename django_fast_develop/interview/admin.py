from django.contrib import admin
from django.db.models import Q
from django.http.response import HttpResponse
from django.utils.safestring import mark_safe
from datetime import datetime
import csv
import logging


from interview import candidate_fields as CF
from interview.dingtalk import send
from interview.models import Candidate
from job.models import Resume

# Register your models here.
logger = logging.getLogger(__name__)


# 导出面试者的信息
def _export_candidate(modeladmin, request, queryset):
	export_fields = ["username", "city", "email", "apply_position", "bachelor_school",
					 "major", "degree", "first_score", "first_result", "second_score",
					 "second_result", "hr_score", "hr_result"]
	response = HttpResponse(content_type="text/csv")
	response["Content-Disposition"] = "attachment;filename={}.csv".format(datetime.now().strftime("%Y-%m-%d:%H_%M_%S"))
	writer = csv.writer(response)
	# 将字段名转成 verbose_name 中文名
	# 遍历 export_fields
	# 通过 model._meta.getfield()
	writer.writerow([queryset.model._meta.get_field(i).verbose_name.title() for i in export_fields])

	for candidate in queryset:
		csv_row_values = []
		for field in export_fields:
			# https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.Field.value_from_object
			# 先获取字段的对象，使用 django-admin 提供的 value_from_obj 方法，从对象获取特定的字段值
			field_object = queryset.model._meta.get_field(field)
			value = field_object.value_from_object(candidate)
			csv_row_values.append(value)
		writer.writerow(csv_row_values)
	logger.info("{} exported {} candidate records".format(request.user, len(queryset)))
	return response


_export_candidate.short_description = "导出所选的面试者信息进csv文件"
_export_candidate.allowed_permissions = ("export",)


# 钉钉通知面试官准备面试
def _notify_interviewer(modeladmin, request, queryset):
	message = ""
	for candidate_obj in queryset :
		message = "应聘者【" + candidate_obj.username + "】的面试官是【" + candidate_obj.first_interviewer_user.username + '】\n' + message
	send(message)


_notify_interviewer.short_description = "通知一面面试官准备面试"
_notify_interviewer.allowed_permissions = ('notify',)




# 应聘者的字段现在都是在网页中都是连续显示
# 默认首页显示的时候也是对象值，而非每一个字段显示在一排
# 配置 Candidate 的 admin model
class CandidateAdmin(admin.ModelAdmin):
	# list_display 是控制页面的显示哪个字段，用在同一界面显示
	# exclude 是排除哪个配置不能让配置的时候手动配置
	actions = [_export_candidate, _notify_interviewer]
	exclude = ("creator", "created_date", "modified_date")
	list_display = (
		"username", "city", "bachelor_school", "first_score", "first_result", 'get_resume',
		"first_interviewer_user", "second_score", "second_result", "second_interviewer_user", "hr_score", "hr_result",
		"hr_interviewer_user", "last_editor"
	)

	# list_display 可以添加函数实体
	# 添加查看简历的按钮并支持跳转到用户简历的原始详情页
	def get_resume(self, obj):
		if not obj.phone:
			return ""
		resumes = Resume.objects.filter(phone=obj.phone)
		if resumes and len(resumes) > 0:
			# 如果简历存在，则显示一个可以查看简历的跳转链接
			# make_safe() 作用是将字符串转换为安全的 html 元素
			return mark_safe("<a href='/resume/{}/' target='_blank'>{}</a>".format(resumes[0].id, "查看简历"))
		return ""

	get_resume.short_description = "查看简历"
	get_resume.allow_tag = True


	# export 导出 CSV 文件权限控制
	def has_export_permission(self, request):
		opts = self.opts
		logger.info(opts.app_label)
		logger.info(request.user.has_perm("%s.%s" % (opts.app_label, "export")))
		return request.user.has_perm("%s.%s" % (opts.app_label, "export"))

	# 只有管理员和 HR 才能通知面试官准备面试
	def has_notify_permission(self, request):
		# 获取当前的用户，判断当前的用户是有权限
		# 权限存在用户的 options 信息中，通过 app_label.permission 获取
		opts = self.opts
		return request.user.has_perm("{}.{}".format(opts.app_label, 'notify'))

	# fieldsets 是一个元组，内部最少是由两个元组组成，用于将字段的排列分组显示
	# 每个分组默认每一个字段是占用一行显示
	# 多行显示使用的是一个 () 括住另一些元组

	# 通过 get_fieldsets() 对于面试官可以访问的字段进行控制
	def get_fieldsets(self, request, obj=None):

		groups = request.user.groups.all()
		groups_name = [i.name for i in groups]

		if 'interviewer' in groups_name and obj.first_interviewer_user == request.user:
			return CF.first_fields
		if 'interviewer' in groups_name and obj.second_interviewer_user == request.user:
			return CF.second_fields
		if 'hr' in groups_name or '110' == request.user.username:
			return CF.default_fieldsets
		return CF.base_fieldsets

	# 设置数据集功能，限制非 HR 和管理员查询到的用户数
	def get_queryset(self, request):
		queryset_all = super(CandidateAdmin, self).get_queryset(request)

		groups_name = [i.name for i in request.user.groups.all()]
		if request.user.is_superuser or 'hr' in groups_name:
			return queryset_all
		logger.info(queryset_all)
		return queryset_all.filter(Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user))

	search_fields = ("username", "city", "apply_position")
	list_filter = ("paper_score", "first_interviewer_user", "second_interviewer_user", "hr_interviewer_user")
	ordering = ("first_score", "second_score", "hr_score")

	# readonly_fields 是只读字段，默认所有人都不能修改
	# readonly_fields = ["first_interviewer_user", "second_interviewer_user", "hr_interviewer_user"]
	def get_group_names(self, user):
		group_names = []
		for g in user.groups.all():
			group_names.append(g.name)
		return group_names

	# 只有 HR 和管理员才能指定面试官
	def get_readonly_fields(self, request, obj=None):
		group_name = self.get_group_names(request.user)

		if "hr" in group_name or request.user.is_superuser:
			return []
		return ["first_interviewer_user", "second_interviewer_user", "hr_interviewer_user"]

	# list_editable = ["first_interviewer_user", "second_interviewer_user", "hr_interviewer_user"]
	# get_list_editable() 已无法使用，需要使用 get_changlist_instance 替代
	def get_changelist_instance(self, request):
		groups = request.user.groups.all()
		user_groups = [i.name for i in groups]

		if "hr" not in user_groups:
			self.list_editable = []
		else:
			self.list_editable = ["first_interviewer_user", "second_interviewer_user", "hr_interviewer_user"]
		return super(CandidateAdmin, self).get_changelist_instance(request)


admin.site.register(Candidate, CandidateAdmin)

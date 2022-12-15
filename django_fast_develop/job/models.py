from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from interview.models import DEGREE_TYPE

# Create your models here.


JobTypes = [
	(0, "技术类"),
	(1, "产品类"),
	(2, "运营类"),
	(3, "设计类"),
]

JobCities = [
	(0, "广州"),
	(1, "深圳"),
	(2, "上海"),
	(3, "杭州"),
	(4, "北京"),
]


# 创建 Job 模型
# 模型的基类是 models.Model
class Job(models.Model):
	# job_types 是职位类别，定为一个整数类型字段，从定义好的类别是中挑选
	job_types = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
	job_name = models.CharField(max_length=250, blank=False, verbose_name="职位名称")
	job_city = models.SmallIntegerField(blank=False, choices=JobCities, verbose_name="工作地点")
	job_responsibility = models.TextField(max_length=1024, verbose_name="工作职责")
	job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="工作要求")
	creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
	# 创建一个职位通常是由已登录的用户创建，有权限操作数据库的用户通常是管理员
	create_date = models.DateTimeField(blank=False, default=datetime.now(), verbose_name="创建日期")
	modified_date = models.DateTimeField(blank=False, default=datetime.now(), verbose_name="修改时间")


# 简历模型
class Resume(models.Model):
	username = models.CharField(max_length=135, verbose_name="姓名")
	applicant = models.ForeignKey(User, verbose_name="申请人", null=True, on_delete=models.SET_NULL)
	city = models.CharField(max_length=135, verbose_name="城市")
	phone = models.CharField(max_length=135, verbose_name="手机号码")
	email = models.EmailField(max_length=135, verbose_name="邮箱")
	apply_position = models.CharField(max_length=135, verbose_name="应聘职位")
	born_address = models.CharField(max_length=135, blank=True, verbose_name="生源地")
	gender = models.CharField(max_length=135, blank=True, verbose_name="性别")

	# 学校与学历信息
	bachelor_school = models.CharField(max_length=135, blank=True, verbose_name="本科学校")
	master_school = models.CharField(max_length=135, blank=True, verbose_name="研究生学校")
	doctor_school = models.CharField(max_length=135, blank=True, verbose_name="博士生学校")
	major = models.CharField(max_length=135, blank=True, verbose_name="专业")
	degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name="学历")
	created_date = models.DateTimeField(verbose_name="创建时间", default=datetime.now)
	modified_date = models.DateTimeField(verbose_name="修改日期", default=datetime.now)

	# 候选人自我介绍，工作经历和项目经理
	candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name="自我介绍")
	work_experience = models.TextField(max_length=1024, blank=True, verbose_name="工作经历")
	project_experience = models.TextField(max_length=1024, blank=True, verbose_name="项目经历")

	class Meta:
		verbose_name = "简历"
		verbose_name_plural = "简历列表"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.Model 中的 choices 字段会用到
# 每个元组的左值是实际存储的数据，右值是用户看到的数据
# 元组可以包含在列表或元组中
# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = [
	(u"建议复试", u"建议复试"),
	(u"待定", u"待定"),
	(u"放弃", u"放弃")
]

# 复试面试建议
INTERVIEW_RESULT_TYPE = (
	(u"建议录用", u"建议录用"),
	(u"待定", u"待定"),
	(u"放弃", u"放弃"),
)

# 候选人学历
DEGREE_TYPE = (
	(u"专科", u"专科"),
	(u"本科", u"本科"),
	(u"硕士", u"硕士"),
	(u"博士", u"博士")
)

# HR 终面结论
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))


# Candidate 是候选者的意思
# models.Model 是 Django 数据库模型管理器
class Candidate(models.Model):
	# 基础信息
	user_id = models.IntegerField(
		unique=True, blank=True, null=True, verbose_name=u"应聘者ID")
	username = models.CharField(max_length=135, verbose_name=u"姓名")
	city = models.CharField(max_length=135, verbose_name=u"城市")
	phone = models.CharField(max_length=11, verbose_name=u"手机号码")
	email = models.CharField(max_length=134, verbose_name=u"邮箱地址")
	apply_position = models.CharField(max_length=135, verbose_name=u"应聘职位")
	born_address = models.CharField(
		max_length=135, blank=True, verbose_name=u"出生地址")
	gender = models.CharField(max_length=4, blank=True, verbose_name=u"性别")
	candidate_remark = models.CharField(
		max_length=135, blank=True, verbose_name=u"候选人备注")

	# 学校与学历信息
	bachelor_school = models.CharField(
		max_length=135, blank=True, verbose_name=u"本科学校")
	master_school = models.CharField(
		max_length=135, blank=True, verbose_name=u"研究生学校")
	doctor_school = models.CharField(
		max_length=135, blank=True, verbose_name=u"博士生学校")
	major = models.CharField(max_length=135, blank=True, verbose_name=u"专业")
	degree = models.CharField(
		max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u"学历")

	# 综合能力测评成绩，笔试测评成绩
	test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
														verbose_name=u"综合能力测评成绩")
	paper_score = models.DecimalField(
		decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u"笔试成绩")

	# 第一轮的面试记录
	first_score = models.DecimalField(
		decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u"初试分", help_text="分数范围1-9")
	first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
												 verbose_name=u"学习能力得力", help_text="分数范围1-9")
	first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
														verbose_name=u"专业能力得分", help_text="分数范围1-9")
	first_advantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"优势")
	first_disadvantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"顾虑和不足")
	first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
									verbose_name=u"初试结果")
	first_recommend_position = models.CharField(
		max_length=256, blank=True, verbose_name=u"推荐部门")
	first_interviewer = models.CharField(
		max_length=256, blank=True, verbose_name=u"面试官")
	first_interviewer_user = models.ForeignKey(User, related_name="first_interviewer_user", blank=True, null=True,
											   on_delete=models.CASCADE, verbose_name=u"一面面试官")
	first_remark = models.CharField(
		max_length=135, blank=True, verbose_name=u"初试备注")

	# 第二轮的面试记录
	second_score = models.DecimalField(
		decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u"初试分")
	second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
												  verbose_name=u"学习能力得力")
	second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
														 verbose_name=u"专业能力得分")
	second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
													  verbose_name=u"追求卓越得分")
	second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
													   verbose_name=u"沟通能力得分")
	second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
												verbose_name=u"抗压能力得分")
	second_interviewer_user = models.ForeignKey(User, related_name="second_interviewer_user", blank=True, null=True,
												on_delete=models.CASCADE, verbose_name=u"二面面试官")
	second_advantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"优势")
	second_disadvantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"顾虑和不足")
	second_recommend_position = models.CharField(
		max_length=256, blank=True, verbose_name=u"推荐部门")
	second_result = models.CharField(
		max_length=256, blank=True, verbose_name=u"复试结果")
	second_remark = models.CharField(
		max_length=135, blank=True, verbose_name=u"专业复试备注")

	# HR终面
	hr_score = models.CharField(
		max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u"HR-复试评级")
	hr_responsibility = models.CharField(
		max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u"HR-责任心")
	hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
												verbose_name=u"HR-坦诚沟通能力")
	hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
										verbose_name=u"HR-逻辑思维能力")
	hr_potential = models.CharField(
		max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u"HR-发展潜力")
	hr_stability = models.CharField(
		max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u"HR-稳定性")
	hr_advantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"HR-优势")
	hr_disadvantage = models.TextField(
		max_length=1024, blank=True, verbose_name=u"HR-顾虑和不足")
	hr_result = models.CharField(
		max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u"HR-复试结果")
	hr_interviewer_user = models.ForeignKey(User, related_name="hr_interviewer_user", blank=True, null=True,
											on_delete=models.CASCADE, verbose_name=u"人力资源官")
	hr_remark = models.CharField(
		max_length=256, blank=True, verbose_name=u"HR-复试备注")

	creator = models.CharField(max_length=256, blank=True, verbose_name=u"创建人")
	created_date = models.DateTimeField(
		auto_now_add=True, verbose_name=u"创建时间")
	modified_date = models.DateTimeField(auto_now=True, verbose_name=u"记录更新时间")
	last_editor = models.CharField(
		max_length=256, blank=True, verbose_name=u"最后编辑者")

	# TODO: 需要分析 META 中三个字段在 Django 中的功能
	class Meta:
		# Meta 类是给 Model 模型赋予元数据
		# 里面的字段是指“所有不是字段的东西”，这里面的数据不是在数据库中存储的，是在模型运行时需要用到的信息
		db_table = u"candidate"
		verbose_name = u"应聘者"
		verbose_name_plural = u"应聘者"

		permissions = [
			("export", "Can export candidate list"),
			("notify", "notify interviewer for candidate review"),
		]

	def __unicode__(self):
		return self.username

	def __str__(self):
		return self.username

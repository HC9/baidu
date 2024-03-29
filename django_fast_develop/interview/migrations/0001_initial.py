# Generated by Django 4.1 on 2022-08-29 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='应聘者ID')),
                ('username', models.CharField(max_length=135, verbose_name='姓名')),
                ('city', models.CharField(max_length=135, verbose_name='城市')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('email', models.CharField(max_length=134, verbose_name='邮箱地址')),
                ('apply_position', models.CharField(max_length=135, verbose_name='应聘职位')),
                ('born_address', models.CharField(blank=True, max_length=135, verbose_name='出生地址')),
                ('gender', models.CharField(blank=True, max_length=4, verbose_name='性别')),
                ('candidate_remark', models.CharField(blank=True, max_length=135, verbose_name='候选人备注')),
                ('bachelor_school', models.CharField(blank=True, max_length=135, verbose_name='本科学校')),
                ('master_school', models.CharField(blank=True, max_length=135, verbose_name='研究生学校')),
                ('doctor_school', models.CharField(blank=True, max_length=135, verbose_name='博士生学校')),
                ('major', models.CharField(blank=True, max_length=135, verbose_name='专业')),
                ('degree', models.CharField(blank=True, choices=[('专科', '专科'), ('本科', '本科'), ('硕士', '硕士'), ('博士', '博士')], max_length=135, verbose_name='学历')),
                ('test_score_of_general_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='综合能力测评成绩')),
                ('paper_score', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='笔试成绩')),
                ('first_score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='初试分')),
                ('first_learning_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='学习能力得力')),
                ('first_professional_competency', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='专业能力得分')),
                ('first_advantage', models.TextField(blank=True, max_length=1024, verbose_name='优势')),
                ('first_disadvantage', models.TextField(blank=True, max_length=1024, verbose_name='顾虑和不足')),
                ('first_result', models.CharField(blank=True, choices=[('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='初试结果')),
                ('first_recommend_position', models.CharField(blank=True, max_length=256, verbose_name='推荐部门')),
                ('first_interviewer', models.CharField(blank=True, max_length=256, verbose_name='面试官')),
                ('first_remark', models.CharField(blank=True, max_length=135, verbose_name='初试备注')),
                ('second_score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='初试分')),
                ('second_learning_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='学习能力得力')),
                ('second_professional_competency', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='专业能力得分')),
                ('second_pursue_of_excellence', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='追求卓越得分')),
                ('second_communication_ability', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='沟通能力得分')),
                ('second_pressure_score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='抗压能力得分')),
                ('second_advantage', models.CharField(blank=True, max_length=1024, verbose_name='优势')),
                ('second_disadvantage', models.CharField(blank=True, max_length=1024, verbose_name='顾虑和不足')),
                ('second_recommend_position', models.CharField(blank=True, max_length=256, verbose_name='推荐部门')),
                ('second_result', models.CharField(blank=True, max_length=256, verbose_name='复试结果')),
                ('second_interviewer', models.CharField(blank=True, max_length=256, verbose_name='面试官')),
                ('second_remark', models.CharField(blank=True, max_length=135, verbose_name='专业复试备注')),
                ('hr_score', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-复试评级')),
                ('hr_responsibility', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-责任心')),
                ('hr_communication_ability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-坦诚沟通能力')),
                ('hr_logic_ability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-逻辑思维能力')),
                ('hr_potential', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-发展潜力')),
                ('hr_stability', models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR-稳定性')),
                ('hr_advantage', models.CharField(blank=True, max_length=1024, verbose_name='HR-优势')),
                ('hr_disadvantage', models.CharField(blank=True, max_length=1024, verbose_name='HR-顾虑和不足')),
                ('hr_result', models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='HR-复试结果')),
                ('hr_interviewer', models.CharField(blank=True, max_length=256, verbose_name='面试官')),
                ('hr_remark', models.CharField(blank=True, max_length=256, verbose_name='HR-复试备注')),
                ('creator', models.CharField(blank=True, max_length=256, verbose_name='创建人')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='记录更新时间')),
                ('last_editor', models.CharField(blank=True, max_length=256, verbose_name='最后编辑者')),
            ],
            options={
                'verbose_name': '应聘者',
                'verbose_name_plural': '应聘者',
                'db_table': 'candidate',
            },
        ),
    ]

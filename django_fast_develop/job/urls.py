from django.urls import re_path,path
# 课程中使用 django.conf.urls 的 url
# 该特性在 3.0 中已减少使用，并在 4.0 版本中移除
from job import views


urlpatterns = [
	re_path(r"^joblist", views.joblist, name="joblist"),

	# 职位详情页
	re_path(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),

	# 提交简历
	path('resume/add/', views.ResumeCreateView.as_view(), name="resume-add"),

	# 简历的详情页，用于 HR 观看原始的简历页面
	# pk 是主键 primary key
	path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
	# re_path(r"^resume/(?P<pkid>\d+)/$", views.test, name="detail"),
]
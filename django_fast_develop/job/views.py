from django.shortcuts import render

# Create your views here.
# django 实现视图有两种方法，一种是函数定义，一种是视图的类
# 现在介绍的是视图的函数定义方法
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from job.models import Job, Resume
from job.models import JobCities, JobTypes


def joblist(request):
	# model.objects.order_by() 是 models 默认实现的方法
	# 该例中利用 job_types 进行排序
	job_list = Job.objects.order_by("job_types")
	template = loader.get_template('joblist.html')
	context = {"job_list": job_list}
	# job_list 是模板中使用到的一个变量名

	for job in job_list:
		job.job_city = JobCities[job.job_city][1]
		job.job_types = JobTypes[job.job_types][1]

	# 一开始默认这个页面没有显示登录的用户名，是因为 request 上下文没有传递到模板中
	return render(request, "joblist.html", context=context)


def detail(request, job_id):
	# pk 主键 primary key https://docs.djangoproject.com/zh-hans/4.1/topics/db/queries/#the-pk-lookup-shortcut
	# objects.get() https://docs.djangoproject.com/zh-hans/4.1/topics/db/queries/#retrieving-a-single-object-with-get
	try:
		job_detail = Job.objects.get(pk=job_id)
		job_detail.job_city = JobCities[job_detail.job_city][1]
		job_detail.job_types = JobTypes[job_detail.job_types][1]
	except Job.DoesNotExist:
		raise Http404("No Job Look!")
	return render(request, 'job.html', {"job": job_detail})


class ResumeCreateView(LoginRequiredMixin, CreateView):
	# createView 是通用继承模板
	# LoginRequireMixin 是登陆校验，Mixin 意即还可以继承多个父类
	template_name = 'resume_form.html'
	success_url = '/joblist/'
	model = Resume
	fields = ["username", "city", "phone",
			  "email", "apply_position", "gender",
			  "bachelor_school", "master_school", "major", "degree",
			  "candidate_introduction", "work_experience", "project_experience"]

	# 从 URL 请求参数进入默认值
	def get_initial(self):
		initial = {}
		# 获取 request 中用户的请求信息
		for x in self.request.GET:
			initial[x] = self.request.GET[x]
		return initial

	# 简历与当前的用户进行关联
	def form_valid(self, form):
		self.object = form.save(commit=False)
		# applicant 外建关系，绑定简历与用户的的绑定关系
		self.object.applicant = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())


class ResumeDetailView(DetailView):
	model = Resume
	template_name = 'resume_detail.html'


# def test(request, pkid):
# 	print(pkid)
# 	resume = Resume.objects.get(pk=pkid)
# 	response = HttpResponse()
# 	response.write(resume.project_experience)
# 	print(resume.project_experience)
# 	return response

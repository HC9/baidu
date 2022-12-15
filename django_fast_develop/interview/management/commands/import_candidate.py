from ast import parse
import csv
from django.core.management import BaseCommand
from interview.models import Candidate


# BaseCommand 是基类，用于
class Command(BaseCommand):
	# help 是命令行显示的帮助字体，了解该命令的作用
	help = "从 excel 表导入命令"

	def add_arguments(self, parser) -> None:
		# add_arguments 是默认方法
		# 用于从命令行获取参数
		# parser 用于解析参数
		# parser 后无需再处理，django 便能自识别并获取参数
		# parser 使用的是 parser.add_argument。不是带有复数形势的 arguments
		parser.add_argument('--path', type=str)

	def handle(self, *args, **options):
		# handle 是 Command 自动回调的函数
		# 参数获取完成后，handle 内的代码会自动运行
		path = options['path']
		with open(path, 'r', encoding='gbk') as file:
			reader = csv.reader(file)
			for i in reader:
				Candidate.objects.create(username=i[0], phone=i[1], city=i[2], email=i[3], apply_position=i[4])

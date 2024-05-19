import os
import django
from langfuse.decorators import observe, langfuse_context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiaoxi.settings_dev')  # 替换为你的settings文件路径
django.setup()

import xiaoxi_ai.MVC.service.knowledge.knowledge as knowledge

knowledge_service = knowledge.KnowledgeService()

if __name__ == '__main__':
    print(knowledge_service.completion("悉尼大学是哪个国家的大学？"))

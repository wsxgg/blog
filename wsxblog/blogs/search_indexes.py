from haystack import indexes
from blogs.models import Blogs
# 指定对于某个类的某些数据建立索引
# 索引类型格式名：模型类名+Index
class BlogsIndex(indexes.SearchIndex, indexes.Indexable):
    # use_template=True表示使用模板
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Blogs

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

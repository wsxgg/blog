from django.db import models

# Create your models here.
class Categorys(models.Model):
    name = models.CharField(max_length=128, verbose_name='分类')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name
    
class Tags(models.Model):
    name = models.CharField(max_length=128, verbose_name='标签')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

class Blogs(models.Model):
    title = models.CharField(max_length=128, verbose_name='文章标题')
    author = models.CharField(max_length=30, verbose_name='作者')
    img = models.ImageField(upload_to='blod_img', null=True, blank=True, verbose_name='博客配图')
    body = models.TextField(verbose_name='正文')
    abstract = models.TextField(max_length=256, null=True, blank=True, verbose_name='描述')
    visiting = models.PositiveIntegerField(verbose_name='访问量', default=0)
    category = models.ForeignKey('Categorys', verbose_name='博客分类', on_delete=models.CASCADE)
    tags = models.ForeignKey('Tags', verbose_name='标签', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifyed_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_top = models.BooleanField(default=False, verbose_name='加精')
    
    def __str__(self):
        return self.title
    
    def get_detail_url(self):
        # 获取当前微博详细页的url
        return reverse("blog:blog_detail", kwargs={"blog_id":self.id})  
    
    def increase_visiting(self):
        # 访问量+1
        self.visiting += 1
        self.save(update_fields=['visiting'])
    
    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客正文'
        verbose_name_plural = verbose_name

class Comments(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户名")
    email = models.CharField(max_length=128, null=True, verbose_name="邮件")
    body = models.CharField(max_length=256, verbose_name="评论")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    belongto = models.ForeignKey("Blogs", verbose_name="从属", null=True, on_delete=models.CASCADE)
    # recover = models.ForeignKey("self", verbose_name="回复", null=True, on_delete=models.CASCADE)
    belongtovlog = models.ForeignKey("Vlogs", verbose_name="从属vlog", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ['-created_time']
        verbose_name = '评论'
        verbose_name_plural = verbose_name

class Vlogs(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    author = models.CharField(max_length=30, verbose_name='作者')
    img = models.ImageField(upload_to='blod_img', null=True, blank=True, verbose_name='vlog配图')
    body = models.TextField(verbose_name='正文')
    abstract = models.TextField(max_length=256, null=True, blank=True, verbose_name='描述')
    visiting = models.PositiveIntegerField(verbose_name='访问量', default=0)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modifyed_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    
    def __str__(self):
        return self.title
    
    def get_detail_url(self):
        # 获取当前微博详细页的url
        return reverse("blog:vlog", kwargs={"vlog_id":self.id})  
    
    def increase_visiting(self):
        # 访问量+1
        self.visiting += 1
        self.save(update_fields=['visiting'])
    
    class Meta:
        ordering = ['-created_time']
        verbose_name = 'vlog'
        verbose_name_plural = verbose_name

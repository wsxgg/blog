from django.shortcuts import render, reverse, redirect
from django.views.generic import View

from blogs.models import Blogs, Tags, Comments, Vlogs
import markdown, pygments
import re
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
class IndexView(View):
    def get(self, request):
        blogs_tags = Tags.objects.all()
        # 获取分类以及所有博客
        # all_blogs是一个字典,格式为:
        # all_blogs = {
        #     'python': {first, second, ....... }           #值的部分为一个查询集
        #     'django': {......}
        # }
        all_blogs = {}
        for tag in blogs_tags:
            blogs = Blogs.objects.filter(tags=tag)[:4]
            all_blogs[tag] = blogs
        #  获取精选博客
        top_blogs= Blogs.objects.filter(is_top=True)

        # 组织上下文
        context = {
            'blogs_tags': blogs_tags,
            'all_blogs': all_blogs,
            'top_blogs': top_blogs,
        }

        return render(request, 'index.html', context)

# /blog/(?P<blog_id>\d+)
class ShowBlogView(View):
    def get(self, request, blog_id):
        #  获取参数blog_id
        try:
            blog = Blogs.objects.get(id=blog_id)
        except:
            return redirect(reverse('blog:index'))
        tag = blog.tags
        # 获取上一章和下一章的blog
        blog_previous = Blogs.objects.filter(tags=tag, id__lt=blog_id).first()
        blog_next = Blogs.objects.filter(tags=tag, id__gt=blog_id).last()
        # 如果没有上一章/下一章
        if blog_previous == None:
            blog_previous = '没有了'
        if blog_next == None:
            blog_next = '没有了'
        # 获取右侧所有文章排行
        hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]
        # 获取右边的热门推荐
        tag_top_blogs = Blogs.objects.filter(tags=tag).order_by('-visiting')[:8]
        # 获取右边栏目更新推荐
        tag_new_blogs = Blogs.objects.filter(tags=tag).order_by('-created_time')[:8]

        # 访问量+1
        blog.visiting += 1
        blog.save() 

        # 渲染blog的正文
        # markdown.markdown的两个参数，第一个指渲染的文本，第二个参数指语法的扩展
        # blog.body = markdown.markdown(blog.body, extensions=[
        #     # 包含 缩写、表格等常用扩展
        #     'markdown.extensions.extra',
        #     # 语法高亮扩展
        #     'markdown.extensions.codehilite',
        #     #允许我们自动生成目录
        #     'markdown.extensions.toc',
        # ])
        md = markdown.Markdown(extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            #允许我们自动生成目录
            'markdown.extensions.toc',
        ])
        # 渲染正文
        blog.body = md.convert(blog.body)
        # 给blog添加标题属性，在md实例创建的时候，会自动生成toc属性
        blog.toc = md.toc
        blog.increase_visiting()
        # m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', blog.toc, re.S)
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', blog.toc, re.S)
        blog.toc = m.group(1) if m is not None else ''

        # 获取评论
        try:
            comments = Comments.objects.filter(belongto_id=blog.id).order_by("created_time")
        except:
            comments = ''
        
        # 组织上下文参数
        context = {
            'blog': blog,
            'tag': tag,
            'blog_previous': blog_previous,
            'blog_next': blog_next,
            'tag_top_blogs': tag_top_blogs,
            'tag_new_blogs': tag_new_blogs,
            'hot_blogs': hot_blogs,
            "comments": comments,
        }
        # 返回页面
        return render(request, 'blog_detail.html', context)

# /list/(?P<tag>.+)/(?P<index>\d+)
class ListView(View):
    def get(slef, request, tag, page):
        # 获取对应对应分组的blog
        try:
            tag_id = Tags.objects.get(name=tag).id
        except:
            return redirect(reverse('blog:index'))
        blogs = Blogs.objects.filter(tags=tag_id)
        # 分页
        paginator = Paginator(blogs, 4)
        try:
            page = int(page)
        except:
            page = 1
        if page > paginator.num_pages:
            page = 1
        blogs = paginator.page(page)
 		# 3.3 编辑页码
        # ① 页码总数小于7，显示全部页码
        # ② 当前页小于4，显示1-7
        # ③ 当前页是最后4页，显示最后7页
        # ④ 其他情况，显示当前页和前后3页
        num_pages = paginator.num_pages
        if num_pages < 7:
            pages = range(1, num_pages+1)
        elif page < 4:
            pages = range(1, 8)
        elif num_pages - page <= 3:
            pages = range(num_pages-6, num_pages+1)
        else:
            pages = range(page-3, page+4)


        blogs = paginator.page(page)

        # 获取右侧所有文章排行
        hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]
        # 获取右侧热门推荐blog
        tag_top_blogs = Blogs.objects.filter(tags=tag_id).order_by('-visiting')[:8]
        # 获取右边栏目更新推荐
        tag_new_blogs = Blogs.objects.filter(tags=tag_id).order_by('-modifyed_time')[:8]

        # 组织上下文tag_new_blog,
        context = {
            'blogs': blogs,
            'tag_top_blogs': tag_top_blogs,
            'tag_new_blogs': tag_new_blogs,
            'hot_blogs': hot_blogs,
            'pages': pages,
            'num_pages': num_pages,
            'tag': tag,
        }
        # 返回应答
        return render(request, 'list.html', context)

#  /search
class SearchView(View):
    def get(self, request, page):
        # 获取搜索值，默认None
        keyword = request.GET.get('keyboard', None)
        # 如果没有关键词，转到首页
        if not keyword:
            err_msg = '请输入关键词'
            return redirect(reverse('blog:index'))


        blogs = Blogs.objects.filter(Q(title__icontains=keyword)
                                    | Q(body__icontains=keyword)
                                    | Q(abstract__icontains=keyword))

        # 分页
        paginator = Paginator(blogs, 4)
        # 3.3 编辑页码
        # ① 页码总数小于7，显示全部页码
        # ② 当前页小于4，显示1-7
        # ③ 当前页是最后4页，显示最后7页
        # ④ 其他情况，显示当前页和前后3页
        num_pages = paginator.num_pages
        if num_pages < 7:
            pages = range(1, num_pages+1)
        elif page < 4:
            pages = range(1, 8)
        elif num_pages - page <= 3:
            pages = range(num_pages-6, num_pages+1)
        else:
            pages = range(page-3, page+4)

        blogs = paginator.page(page)

        # 获取右侧所有文章排行
        hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]

        # 组织上下文
        context = {
            'blogs': blogs,
            'comment': False,
            'pages': pages,
            'num_pages': num_pages,
            'keyboard': keyword,
            'hot_blogs': hot_blogs,

        }
        return render(request, 'base_search.html', context)

# /comment/1
class CommentView(View):
    def get(self, request, page):
        # 获取评论
        try:
            comments = Comments.objects.filter(Q(belongto_id=None)&Q(belongtovlog_id=None))
            # 分页
            paginator = Paginator(comments, 10)
            try:
                page = int(page)
            except:
                page = 1
            if page > paginator.num_pages:
                page = 1
            comments = paginator.page(page)
            # 编辑页码
            # ① 页码总数小于7，显示全部页码
            # ② 当前页小于4，显示1-7
            # ③ 当前页是最后4页，显示最后7页
            # ④ 其他情况，显示当前页和前后3页
            num_pages = paginator.num_pages
            if num_pages < 7:
                pages = range(1, num_pages+1)
            elif page < 4:
                pages = range(1, 8)
            elif num_pages - page <= 3:
                pages = range(num_pages-6, num_pages+1)
            else:
                pages = range(page-3, page+4)

            comments = paginator.page(page)

            # 获取右侧所有文章排行
            hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]

            # 组织上下文
            context = {
                "comments": comments,
                "hot_blogs": hot_blogs,
                "pages": pages,
                "comment": False,    # 控制右侧有无最新和本栏
            }

            # 返回页面
            return render(request, 'comment.html', context)
        except:
            comments = ''
            # 获取右侧所有文章排行
            hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]
            # 组织上下文
            context = {
                "comments": comments,
                "hot_blogs": hot_blogs,
                "comment": False,    # 控制右侧有无最新和本栏
            }
           # 返回页面
            return render(request, 'comment.html', context)

# /newcomment
class NewCommentView(View):
    def get(self, request):    
        # 获取右侧所有文章排行
        hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]

        # 生成上下文
        context = {
            "hot_blogs": hot_blogs,
            "comment": False,       # 控制右侧有无最新和本栏
        }

        return render(request, "new_comment.html", context)
    
    def post(self, request):
        # 获取留言表单的内容
        name = request.POST.get("name")
        email = request.POST.get("email", '')
        body = request.POST.get("comment")
        path = request.POST.get("path")
        if path is None:
            path = request.path

 
        if name == '' or body == '':
            return redirect(path)

        # 保存数据库
        comment = Comments()
        comment.name = name
        comment.email = email
        comment.body = body

        blog_id = request.POST.get("blog_id")
        vlog_id = request.POST.get("vlog_id")


        if blog_id is not None:
            # 能获取blog_id，则为博客回复
            comment.belongto_id = blog_id
            comment.save()
            return redirect(reverse("blog:detail", kwargs={"blog_id": blog_id}))  
        elif vlog_id is not None:
            # 能获取vlog_id，则为vlog回复  
            comment.belongtovlog_id = vlog_id
            comment.save()
            return redirect(reverse("blog:vlog", kwargs={"vlog_id": vlog_id}))
        else:
            # 如果都没有，默认为留言
            comment.save()
            return redirect(reverse("blog:comment", kwargs={"page": 1}))


# /vlog/list/(?P<page>.*)
class VlogListView(View):
    def get(self, request, page):
        # 获取所有vlog
        vlogs = Vlogs.objects.all()
        # 分页
        paginator = Paginator(vlogs, 4)
        try:
            page = int(page)
        except:
            page = 1
        if page > paginator.num_pages:
            page = 1
        vlogs = paginator.page(page)
        # 3.3 编辑页码
        # ① 页码总数小于7，显示全部页码
        # ② 当前页小于4，显示1-7
        # ③ 当前页是最后4页，显示最后7页
        # ④ 其他情况，显示当前页和前后3页
        num_pages = paginator.num_pages
        if num_pages < 7:
            pages = range(1, num_pages+1)
        elif page < 4:
            pages = range(1, 8)
        elif num_pages - page <= 3:
            pages = range(num_pages-6, num_pages+1)
        else:
            pages = range(page-3, page+4)


        vlogs = paginator.page(page)

        # 获取右侧所有文章排行
        hot_vlogs = Vlogs.objects.all().order_by('-visiting')[:8]

        # 组织上下文tag_new_blog,
        context = {
            'vlogs': vlogs,
            'hot_vlogs': hot_vlogs,
            'pages': pages,
            'num_pages': num_pages,
            "comment": False,    # 控制右侧有无最新和本栏
        }
        # 返回应答
        return render(request, 'vlog_list.html', context)


# /vlog/(?P<vlog_id>\d+)
class VlogDetailView(View):
    def get(self, request, vlog_id):
        # 获取参数blog_id
        try:
            vlog = Vlogs.objects.get(id=vlog_id)
        except:
            return redirect(reverse('blog:index'))
        # 获取上一章和下一章的blog
        vlog_previous = Vlogs.objects.filter(id__lt=vlog_id).first()
        vlog_next = Vlogs.objects.filter(id__gt=vlog_id).last()
        # 如果没有上一章/下一章
        if vlog_previous == None:
            vlog_previous = '没有了'
        if vlog_next == None:
            vlog_next = '没有了'
        # 获取右侧所有文章排行
        hot_vlogs = Vlogs.objects.all().order_by('-visiting')[:8]


        # 访问量+1
        vlog.visiting += 1
        vlog.save() 

        # 获取评论
        try:
            comments = Comments.objects.filter(belongtovlog_id=vlog.id).order_by("created_time")
        except:
            comments = ''
        
        # 组织上下文参数
        context = {
            'vlog': vlog,
            'vlog_previous': vlog_previous,
            'vlog_next': vlog_next,
            'hot_vlogs': hot_vlogs,
            "comments": comments,
            "comment": False,
        }
        # 返回页面
        return render(request, 'vlog_detail.html', context)

# 404
def page_not_found(request, **kwargs):
    # 获取页面所需参数
    # 获取右侧所有文章排行
    hot_blogs = Blogs.objects.all().order_by('-visiting')[:8]

    # 组织上下文
    context = {
        'hot_blogs': hot_blogs,
        'comment': False,
    }

    return render(request, '404.html', context)
    


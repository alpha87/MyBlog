import markdown
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404
from .models import Post
from Comments.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

BLOG_NAME = "Note."


def index(request):

    post_list = Post.objects.all().order_by("-create_date")

    for post in post_list:
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        post.excerpt = strip_tags(md.convert(post.body))[:54]

    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    try:
        page_items = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        page_items = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        page_items = paginator.page(paginator.num_pages)

    return render(
        request,
        "Documents/index.html",
        context={"title": BLOG_NAME,
                 # "post_list": post_list,
                 "post_list": page_items}
    )


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    form = CommentForm()
    comment_list = post.comment_set.all()

    return render(
        request,
        "Documents/detail.html",
        context={"title": BLOG_NAME,
                 "post": post,
                 "form": form,
                 "comment_list": comment_list}
    )

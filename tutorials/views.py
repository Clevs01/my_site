from django.views import generic
from tutorials.models import Post
from tutorials.forms import CommentForm
from django.shortcuts import render, get_object_or_404 #, HttpResponseRedirect, reverse
# from PIL import Image


# def about_tuts(request):
#     return render(request, 'tutorials/about.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-posted_on')
    template_name = 'tutorials/tutorials.html'
    paginate_by = 3


def posts(request, slug):
    post = Post.objects.filter(status=1).order_by('-posted_on')
    template_name = 'tutorials/tutorials.html'
    paginate_by = 3
    return render(request, template_name, {'post': post})


# def post_detail(request, slug):
#     template_name = 'tutorials/tuts_details.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})


def post_detail(request, slug):
    template_name = 'tutorials/tuts_details.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

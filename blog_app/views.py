from urllib import request
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post
from .forms import PostForm


def post_create(request):
    context = {}

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def post_list(request):
    context = {}
    context["dataset"] = Post.objects.all()

    return render(request, "list_view.html", context)


def post_detail(request, id):
    context = {}
    context["data"] = Post.objects.get(id=id)

    return render(request, "detail_view.html", context)


def post_update(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, "update_view.html", context)


def post_delete(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

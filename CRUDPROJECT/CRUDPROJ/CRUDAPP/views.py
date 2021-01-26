from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from CRUDAPP.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'pages']

def blog_list(request, template_name='blogs/blog_list.html'):
    blog = Blog.objects.all()
    data = {}
    data['object_list'] = blog
    print(blog)
    return render(request, template_name, data)

def blog_view(request, pk, template_name='blogs/blog_detail.html'):
    blog= get_object_or_404(Blog, pk=pk)
    return render(request, template_name, {'object':blog})

def blog_create(request, template_name='blogs/blog_form.html'):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_update(request, pk, template_name='blogs/blog_form.html'):
    blog= get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_delete(request, pk, template_name='blogs/blog_confirm_delete.html'):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name, {'object':blog})

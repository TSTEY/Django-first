from django.shortcuts import render

def index(arg):
    return render (arg,"index.html")

def about(arg):
    return render (arg,"about.html")

def blog(arg):
    return render (arg,"blog.html")

def clas(arg):
    return render (arg,"class.html")


def copy_li_fun(argument):
    copy_li = [
        {"name":"Home","url":"index","active":True},
        {"name":"About","url":"about","active":True},
        {"name":"Class","url":"class","active":True},
        {"name":"Blog","url":"blog","active":True},
    ]
    return render(argument,"index.html",{"copy_li":copy_li})

def copy_blog_fun(argument):
    copy_blog = [
        {"img":"static/images/b1.jpg","age":17,"name":"Fed","profi":"Boxer Joniya Daro","active":True},
        {"img":"static/images/b2.jpg","age":27,"name":"Jun","profi":"Boxer Joniya Daro","active":True},
    ]
    return render(argument, "index.html",{"copy_blog":copy_blog})

from django.shortcuts import render, redirect
from .models import Profile, AMGPost
from .forms import PostForm

# Create your views here.


def dashboard(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("AMGTeer:dashboard")

    followed_profiles = AMGPost.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(
        request,
        "AMGTeer/dashboard.html",
        {"form": form, "followed_profiles": followed_profiles},
    )


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "AMGTeer/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, "profile"):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile = current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile = current_user_profile.follows.remove(profile)
    return render(request, "AMGTeer/profile.html", {"profile": profile})

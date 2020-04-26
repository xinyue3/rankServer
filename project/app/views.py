from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Rank
# Create your views here.


def upload_score(request):
    uname = request.POST.get('uname', '')
    score = request.POST.get('score', '')
    if Users.objects.filter(uname=uname).exists():
        u = Users.objects.get(uname=uname)
        u.score = score
        u.save()
        if Rank.objects.filter(user=u).exists():
            rank = Rank.objects.get(user=u)
            update_rank(rank, score, u)
        else:
            rank = Rank()
            update_rank(rank, score, u)
    else:
        u = Users()
        u.uname = uname
        u.score = score
        u.save()
        if Rank.objects.filter(user=u).exists():
            rank = Rank.objects.get(user=u)
            update_rank(rank, score, u)
        else:
            rank = Rank()
            update_rank(rank, score, u)
    return HttpResponse('上传分数成功')

def upload_score_form(request):
    return render(request, 'app/upload_score.html')




def rank_info(request):
    uname = request.POST.get('uname', '')
    rank_range = request.POST.get('range', '').split('-')
    top_limit, floor = int(rank_range[0]), int(rank_range[1])
    dic = {}
    if Users.objects.filter(uname=uname).exists():
        u = Users.objects.get(uname=uname)
        current_user_rank = Rank.objects.get(user=u)

        ranks = Rank.objects.all()[top_limit-1: floor-1]

        dic['rank'] = [{'ranknum':rank.rankNum, "uname": rank.user.uname, "score":rank.user.score} for rank in ranks]
        dic['rank'].extend([{'ranknum':current_user_rank.rankNum, "uname": current_user_rank.user.uname, "score":current_user_rank.user.score} ])

        print(dic)

        return render(request, 'app/rank_show.html', dic)
    return HttpResponse('查询数据用户不存在', 403)


def search_rank_info(request):
    return render(request, 'app/search_rank_info.html')




def update_rank(rank, score, u):
    users = Users.objects.all()
    u_score_num_list = [user.score for user in users]
    rank.rankNum = u_score_num_list.index(score) + 1
    rank.user = u
    rank.save()

    return ''
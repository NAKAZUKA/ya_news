import pytest
from django.urls import reverse
# from news.models import Comment


COUNT_OBJECT_ON_DIFFERENT_PAGE = 10


@pytest.mark.django_db
def test_main_home_news_count(client, create_news_objects):
    """Тест проверяет количество новостей на главной странице"""
    create_news_objects(COUNT_OBJECT_ON_DIFFERENT_PAGE)
    url = reverse('news:home')
    response = client.get(url)
    assert len(
        response.context['object_list']
    ) == COUNT_OBJECT_ON_DIFFERENT_PAGE


@pytest.mark.django_db
def test_order_news_on_home_page(client, create_news_objects):
    """Тест проверяет правильность сортировки новостей на главной странице"""
    create_news_objects(COUNT_OBJECT_ON_DIFFERENT_PAGE)
    url = reverse('news:home')
    response = client.get(url)
    object_list = response.context['object_list']
    all_dates = [news.date for news in object_list]
    sorted_dates = sorted(all_dates, reverse=True)
    assert all_dates == sorted_dates


@pytest.mark.django_db
def test_comment_form_availability(client, news, get_url_news_detail):
    """
    Тест проверяет доступность формы для отправки
    комментария на странице новости анонимному пользователю
    """
    url = reverse('news:detail', args=get_url_news_detail(news))
    response = client.get(url)
    assert 'comment_form' not in response.context



# @pytest.mark.django_db
# def test_order_cooments_on_page_new(news, author, not_author_client, get_url_news_detail):
#     """
#     Тест проверяет правильность сортировки комментариев
#     на странице новости
#     """
#     for i in range(COUNT_OBJECT_ON_DIFFERENT_PAGE):
#         Comment.objects.create(
#             text=f'text {i}',
#             news=news,
#             author=author,
#         )
#     url = reverse('news:detail', args=get_url_news_detail(news))
#     response = not_author_client.get(url)
#     object_list = response.context['comment']
#     all_dates = [comment.date for comment in object_list]
#     sorted_dates = sorted(all_dates, reverse=True)
#     assert all_dates == sorted_dates


menu=[{'title':"Поиск", 'url_name':'home'},
      {'title':'ОБРАТНАЯ СВЯЗЬ', 'url_name':'feedback'},
      {'title':'ДОБАВИТЬ АНКЕТУ', 'url_name':'add'},
      {'title':'ВОЙТИ', 'url_name':'login'},
      {'title':'РЕГИСТРАЦИЯ', 'url_name':'register'}]

class MyMixin:
    def get_user_context(self, **kwargs):
        context=kwargs
        context['menu']=menu
        return context
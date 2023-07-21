
menu=[{'title':"Поиск анкет", 'url_name':'home'},
      {'title':'Обратная связь', 'url_name':'feedback'},
      {'title':'Добавить анкету', 'url_name':'add'},
      {'title':'Войти', 'url_name':'login'},
      {'title':'Регистрация', 'url_name':'register'}]

class MyMixin:
    def get_user_context(self, **kwargs):
        context=kwargs
        context['menu']=menu
        return context
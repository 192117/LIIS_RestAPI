## Описание работы веб-сервиса

# Endpoints:

- https://whispering-escarpment-44420.herokuapp.com/api/v1/auth/registr/
    
Для регистрации пользователей. Принимает POST запрос с содержимым:

```
{
    "email": "",
    "password": "",
    "role": null
}
```

Можно зарегистрировать две роли: 'subscriber' и 'author'. По умолчанию стоит 'subscriber'.

- https://whispering-escarpment-44420.herokuapp.com/api/v1/article/all/

Для просмотра неавторизованными пользователями публичных статей.

- https://whispering-escarpment-44420.herokuapp.com/api/v1/article/privat/

Для просмотра 'subscriber' закрытых постов. Для просмотра требует BasicAuthentication.

- https://whispering-escarpment-44420.herokuapp.com/api/v1/article/create/

Для создания требует BasicAuthentication. Для пользователя с ролью 'subscriber' при отправке POST запроса получит ответ,
что не может создать пост.

```
You are not author!
```

- https://whispering-escarpment-44420.herokuapp.com/api/v1/article/detail/<int:pk>/

Для создания требует BasicAuthentication. Только для автора можно будет редактировать, для остальных только просмотр.
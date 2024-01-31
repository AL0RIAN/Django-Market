## Start Commands

### Requirements

```
$ pip install -r requirements.txt
```

### Super User

```
$ python manage.py createsuperuser
```

## Celery and Flower

The app utilizes Celery for asynchronous task processing. To ensure optimal performance, it is recommended
to use a message broker, such as RabbitMQ

```
$ celery -A myshop worker -l info
```
```
$ celery -A myshop flower
```

## Redis

The app incorporates Redis for its recommendation system.

```
$ docker run -d -p 6379:6379 --name redis redis
```

## Stripe

The app uses the [Stripe](https://stripe.com/) payment gateway.

### Secrets

Enter your secrets into the settings.py file.

```
STRIPE_PUBLISHABLE_KEY = 'YOUR_SECRET'
STRIPE_SECRET_KEY = 'YOUR_SECRET'
STRIPE_API_VERSION = '2023-10-16'
STRIPE_WEBHOOK_SECRET = 'YOUR_SECRET'
```

## Main paths

- /
- cart/ 
- orders/
- payment/
- coupons/
- rosetta/
- admin/


from PIL import Image, ImageDraw


TOKEN = 'vk1.a.T8pZdO2-oTklBKLrJyITlkO4WjRHHYvXosxBuMAViWM5gK-u_B06t5K_b10HdOBkBCVmYFZPvlwcu0A6Q0u6cjnQ5iwyfPjSST1YDFJOkXjPrv23DWrF-wD2N6FQUve4EcTsKFdSD6JNeln_vkTCUmSGi5llOydeIzRKEhGDZXcE0e3j0Cw2NpvMM_jxaUeRdB9XjtQD0jVo_MSsGhy-Ng'
CANCEL_WORDS = ('отмена', 'назад', 'стоп', 'хватит', 'завершить', 'в меню', 'в меню.', 'главная', 'меню', 'stop', 'back', 'interrupt', 'Вернуться назад') # слова выхода в предыддущее меню
CURRENCY = '💳' # валюта
MIN_BET = 100 # минимальная ставка
ALLOWED_USERS =  '__all__' #[545885694, 494414313] 
DEBUG = True
DAY = 3600 * 24
GIM = 194071489
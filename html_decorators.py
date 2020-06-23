def div(func):
    def wrapper(*args, **kwargs):
        text_function = func(args[0])
        # func = func(*args, **kwargs)
        print(f'<div> {text_function} </div>')
        return text_function

    return wrapper

def article(func):
    def wrapper(*args, **kwargs):
        text_function = func(args[0])
        # func = func(*args, **kwargs)
        print(f'<article> {text_function} </article>')
        return text_function

    return wrapper


def p(func):
    def wrapper(*args, **kwargs):
        text_function = func(args[0])
        # # func = func(*args, **kwargs)
        # print(f'<p> {text_function} </p>')
        # return text_function
        return f'<p> {text_function} </p>'

    return wrapper
    
# Here you must apply the decorators, uncomment this later
@p
@article
@div
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>

def add_tag(tag):
    def fun_decorate(fun):
        def inner():
            return f"<{tag}>{fun()}</{tag}>"

        return inner

    return fun_decorate


@add_tag('h1')
def write_something():
    return 'something'


result = write_something()
print(result)
assert result == '<h1>something</h1>'

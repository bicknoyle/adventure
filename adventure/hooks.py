from typing import Dict
# adapted from from https://gist.github.com/marc-x-andre/1c55b3fafd1d00cfdaa205ec53a08cf3
class Hooks:

    def __init__(self):
        self._callbacks: Dict[str, callable] = {}

    def on(self, hook_name, function):
        self._callbacks[hook_name] = function
        return function

    def run(self, hook_name, *args, **kwargs):
        if hook_name in self._callbacks:
            return self._callbacks[hook_name](*args, **kwargs)

class HookError(Exception):
    pass

def hookable(fn):
    def decorated_fn(*args, **kwargs):
        result = None
        result = args[0].hooks.run('pre_' + fn.__name__, *args, **kwargs)
        if result is not None:
            return result

        return fn(*args, **kwargs)

    return decorated_fn
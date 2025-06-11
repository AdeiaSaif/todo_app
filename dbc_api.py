from functools import wraps
import tkinter.messagebox as msgbox

class DBC:
    def __init__(self):
        self.violations = []
    
    def requires(self, condition, message="Condition not met"):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if not condition(*args, **kwargs):
                    simplified_msg = self._simplify_error(message)
                    msgbox.showwarning("Easy Fix!", simplified_msg)
                    self._log_violation(simplified_msg)
                    raise ValueError(simplified_msg)
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def ui_friendly_error(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_msg = self._simplify_error(str(e))
                msgbox.showwarning("Easy Fix!", error_msg)
                self._log_violation(error_msg)
        return wrapper
    
    def _simplify_error(self, error):
        return (error.replace("_", " ")
                .replace("lambda", "")
                .capitalize() + " ⚠️")
    
    def _log_violation(self, message):
        self.violations.append(message)

dbc = DBC()
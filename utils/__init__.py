from flask import session,redirect
from functools import wraps

def login_required(func):
  """
  Decorator to check for user session and redirect to "/login" if not logged in.

  Args:
      func: The function to be decorated.

  Returns:
      A decorated function that checks user session before execution.
  """
  @wraps(func)
  def decorated_function(*args, **kwargs):
    if not "logged" in session:
      return redirect("/login")
    return func(*args, **kwargs)
  return decorated_function
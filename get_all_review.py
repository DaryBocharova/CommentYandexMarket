from reviewapp import create_app
from reviewapp.review import get_python_review,get_mobile_all

app = create_app()
with app.app_context():
    get_python_review()


c=get_mobile_all()
print(c)    
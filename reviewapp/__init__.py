from flask import Flask,render_template

from reviewapp.model import db,Review

def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route("/")
    def hello():
        title="Отзывы на телефоны"
        
        review_list = Review.query.all()
        
        #return render_template('index.html',page_title=title,review_list=review_list)
            
    return app
   
            
    
  



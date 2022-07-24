from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


#@app.post("/createposts")   
#def create_posts(post:Post) :
 #   print(post)
  #  print(post.dict())
   # return {"data".post}

   @app.put("/posts/{id}")
def update_post(id:int, post:Post):
     print(post)
     return{'message': "updated post"}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)   
def delete_post(id: int):
    #deleting post
    #find the index in the array that has required ID
    #my_posts.pop(index)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"post with id:{id} does not exist")


    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

    from importlib.resources import contents
from operator import index
from turtle import title
from typing import Optional
from fastapi.params import Body
from markdown import postprocessors
from pydantic import BaseModel
from random import randrange
from fastapi import FastAPI, Response ,status,HTTPException

#class Post(BaseModel):
#      title:str
 #     contents:str
 #     published: bool = True
 #     rating: Optional[int]= None

 @app.post("/posts")
def create_posts(post: Post ):
    post_dict = post.dict()
    post_dict['id']= randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}

my_posts=[{"title":"title of post 1", "content":"content of post 1" , "id": 1 }, {"title":"favorite foods","content": "I like pizza", "id": 2 }]      

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

#request Get method url: "/"

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id :
            return i


@app.get("/") #is a decorator in python turns the below function into actual path operator so that someone who wants to use API can use this endpoint 
#/ within bracket is the path url{path operation}
#.get is the http path method
def root():
    # root() is the function or specific path operation function
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


#ID
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    print(type(id))
    post = find_post(id)
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #RETURN {'message' : f"post with id: {id} was not found}
    return {"post_detail": post}
   
   
#def find_post(id):
 #   for p in my_posts:
  #         return p

#request Get method url: "/"

#def find_index_post(id):
  #  for i,p in enumerate(my_posts):
  #      if p['id'] == id :
   #         return i

   from fastapi import FastAPI, Response,status,HTTPException,Depends

  


from fastapi.params import Body
from pydantic import BaseModel



from fastapi import FastAPI, Response,status,HTTPException,Depends
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from .  import models
from .database import engine,SessionLocal

models.Base.metadata.create_all(bind=engine)
#engine = create_engine('postgre://manpreet@localhost/fastapi',
                      # pool_size=20, max_overflow=0)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "success"}

 

      from pyexpat import model

      from enum import auto
#create posts
print(current_user.id)
    #print(current_user.email)
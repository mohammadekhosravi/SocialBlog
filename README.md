***A Social Blog Site With Flask***
---
<p align="center"><img src="https://github.com/mohamadkhosravi/SocialBlog/blob/master/blog/static/git1.png" alt="Image Not Found"></p>
<p align="center"><img src="https://github.com/mohamadkhosravi/SocialBlog/blob/master/blog/static/git2.png" alt="Image Not Found"></p>
---

#### How To Install:
1. `python3 -m venv VirtualEnvironmentName`<br>
2. `source VirtualEnvironmentName/bin/activate`<br>
3. `pip3 install --upgrade -r requirements.txt`<br><br>
**To continue you must be at the same directory as app.py**
<br><br>
4. `flask db init`<br>
5. `flask db migrate -m "MESSAGE"`<br>
6. `flask db upgrade`<br>
7. `python app.py`<br>
<p><em>If you follow the instruction there should be no error </em></p>
<p>And now site is running in debug mode. you can open your browser and go to <strong>http://127.0.0.1/5000</strong> </p>

# TODO:
* ##### Fix DB bug.
* ##### Add google and github OAuth.
* ##### Make site looks better.
* ##### Add ability to add picture for blog posts.
* ##### Add writting tools.

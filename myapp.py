from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
   # Load current count
   f = open("count.txt", "r")
   count = int(f.read())
   f.close()
   # Increment the count
   count += 1
   # Overwrite the count
   f = open("count.txt", "w")
   f.write(str(count))
   f.close()

   return render_template('hello.html', name=name, count=count)

if __name__ == '__main__':
   app.run(host ='0.0.0.0', debug = True)

## Ref:
## https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
## https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
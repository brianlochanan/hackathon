from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<class_group>')
def class_group(class_group):
   return render_template('/MyTimetable.htm', class_group = class_group)

if __name__ == '__main__':
   app.run(debug = True)
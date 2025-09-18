from flask import Flask, render_template, request, redirect, url_for
from config import get_db_connection

app = Flask(__name__)

# Home page - list tasks
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template("add_task.html")

# Edit/Update a task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        updated_task = request.form['task']
        cursor.execute("UPDATE tasks SET task=%s WHERE id=%s", (updated_task, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    # GET request: fetch existing task
    cursor.execute("SELECT id, task FROM tasks WHERE id=%s", (id,))
    task = cursor.fetchone()
    conn.close()
    return render_template("edit_task.html", task=task)

# Delete task
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

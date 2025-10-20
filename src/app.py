from flask import Flask, jsonify, request
from models import db, Task

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    if test_config:
        app.config.update(test_config)
    db.init_app(app)

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([t.to_dict() for t in tasks])

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()
        task = Task(title=data['title'], status='To Do')
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201

    @app.route('/tasks/<int:id>', methods=['PUT'])
    def update_task(id):
        task = Task.query.get(id)
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify(task.to_dict())

    @app.route('/tasks/<int:id>', methods=['DELETE'])
    def delete_task(id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all() 
    app.run(debug=True)

from flask import Flask, render_template, flash, redirect, render_template, request, send_from_directory, url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True


debug = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    @app.route("/")
    def home_page():
        pets = Pet.query.all()
        return render_template("home.html", pets=pets)

    @app.route('/images/pet-avatar.png')
    def get_image():
        return send_from_directory('static/images', 'pet-avatar.png')

    @app.route("/add", methods=["GET", "POST"])
    def add_pet_form():
        form = AddPetForm()
        if form.validate_on_submit():
            name = form.name.data
            species = form.species.data
            photo_url = form.photo_url.data
            age = form.age.data
            notes = form.notes.data
            new_pet = Pet(name=name, species=species, photo_url=photo_url,
                          age=age, notes=notes)
            db.session.add(new_pet)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("add_pet_form.html", form=form)

    @app.route("/detail/<int:pet_id>", methods=["GET"])
    def show_pet_details(pet_id):
        pet = Pet.query.get_or_404(pet_id)
        return render_template ("pet_details.html", pet = pet)

    @app.route("/<int:pet_id>", methods=["GET", "POST"])
    def edit_pet(pet_id):
        """Edit pet."""

        pet = Pet.query.get_or_404(pet_id)
        form = EditPetForm(obj=pet)

        if form.validate_on_submit():
            pet.notes = form.notes.data
            pet.available = form.available.data
            pet.photo_url = form.photo_url.data
            db.session.commit()
            flash(f"{pet.name} updated.")
            return redirect(url_for('home_page'))

        else:
            # failed; re-present form for editing
            return render_template("edit_pet_form.html", form=form, pet=pet)




    #     @app.route("/snacks/new", methods=["GET", "POST"])
    # def add_snack():
    #     form = AddSnackForm()

    #     # checks for of authenticity of csrf token/ validates submitted form and passes instance of form to template
    #     # checks for data in request.form and automatically converts it to appropriate data type from a string
    #     # the validate_on_submit also fill the empty form object ^^ with data from the request.form
    #     if form.validate_on_submit():
    #         # 1. is this is a post request? 2. is the token valid?
    #         name = form.name.data
    #         price = form.price.data
    #         flash(f"Created new snack: name is {name}, price is ${price}")
    #         return redirect("/")
    #     # Either form didn't validate token or sending a GET request for the first time
    #     else:
    #         return render_template("snack_add_form.html", form=form)

    # @app.route('/phones')
    # def list_phones():
    #     """Renders directory of employees and phone numbers  (from dept)"""
    #     emps = Employee.query.all()
    #     return render_template('phones.html', emps=emps)

    # @app.route('/employees/new', methods=["GET", "POST"])
    # def add_employee():
    #     form = EmployeeForm()
    #     depts = db.session.query(Department.dept_code, Department.dept_name)
    #     form.dept_code.choices = [
    #         (dept.dept_code, dept.dept_name) for dept in depts]
    #     if form.validate_on_submit():
    #         name = form.name.data
    #         state = form.state.data
    #         dept_code = form.dept_code.data

    #         emp = Employee(name=name, state=state, dept_code=dept_code)
    #         db.session.add(emp)
    #         db.session.commit()
    #         return redirect('/phones')
    #     else:
    #         return render_template('add_employee_form.html', form=form)

    # @app.route('/employees/<int:id>/edit', methods=["GET", "POST"])
    # def edit_employee(id):
    #     emp = Employee.query.get_or_404(id)
    #     # obj attribute needs to have matching attributes for form fields and Employee model
    #     form = EmployeeForm(obj=emp)
    #     depts = db.session.query(Department.dept_code, Department.dept_name)
    #     form.dept_code.choices = [
    #         (dept.dept_code, dept.dept_name) for dept in depts]

    #     if form.validate_on_submit():
    #         emp.name = form.name.data
    #         emp.state = form.state.data
    #         emp.dept_code = form.dept_code.data
    #         db.session.commit()
    #         return redirect('/phones')
    #     else:
    #         return render_template("edit_employee_form.html", form= form)

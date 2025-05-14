from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import LibroForm, ChangePasswordForm
from app.models import db, LibroPersonal, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.old_password.data):
            flash('Current password is incorrect.')
            return render_template('cambiar_password.html', form=form)
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('✅ Password updated successfully.')
        return redirect(url_for('main.dashboard'))
    return render_template('cambiar_password.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    libros = LibroPersonal.query.filter_by(usuario_id=current_user.id).all()
    return render_template('dashboard.html', libros=libros)

@main.route('/libros', methods=['GET', 'POST'])
@login_required
def libros():
    form = LibroForm()
    if form.validate_on_submit():
        libro = LibroPersonal(
            titulo=form.titulo.data,
            autor=form.autor.data,
            genero=form.genero.data,
            anio_publicacion=form.anio_publicacion.data,
            url=form.url.data,
            notas=form.notas.data,
            etiquetas=form.etiquetas.data,
            usuario_id=current_user.id
        )
        db.session.add(libro)
        db.session.commit()
        flash("Book added successfully.")
        return redirect(url_for('main.dashboard'))
    return render_template('libro_form.html', form=form)

@main.route('/libros/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_libro(id):
    libro = LibroPersonal.query.get_or_404(id)
    if libro.usuario_id != current_user.id and current_user.role.name != 'Admin':
        flash('You do not have permission to edit this book.')
        return redirect(url_for('main.dashboard'))
    form = LibroForm(obj=libro)
    if form.validate_on_submit():
        form.populate_obj(libro)
        db.session.commit()
        flash("Book updated successfully.")
        return redirect(url_for('main.dashboard'))
    return render_template('libro_form.html', form=form, editar=True)

@main.route('/libros/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_libro(id):
    libro = LibroPersonal.query.get_or_404(id)
    if libro.usuario_id != current_user.id and current_user.role.name != 'Admin':
        flash('You do not have permission to delete this book.')
        return redirect(url_for('main.dashboard'))
    db.session.delete(libro)
    db.session.commit()
    flash("Book deleted successfully.")
    return redirect(url_for('main.dashboard'))


@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash("You do not have permission to view this page.")
        return redirect(url_for('main.dashboard'))
    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

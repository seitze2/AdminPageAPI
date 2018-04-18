@bp.route('/admin/')
@login_required
def admin():
    from AdminPage.AdminPageAPI.adminPage import admin
    from AdminPage.AdminPageAPI.adminPage import is_admin

    isAdmin = is_admin(current_user)

    if isAdmin :
        return admin()
    else:
        return render_template('404.html'), 404
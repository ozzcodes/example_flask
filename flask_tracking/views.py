@app.route("/")
def index():
    site_form = SiteForm()
    visit_form = VisitForm()
    return render_template("index.html",
                           site_form=site_form,
                           visit_form=visit_form)


@app.route("/site", methods=("POST", ))
def add_site():
    form = SiteForm()
    if form.validate_on_submit():
        site = Site()
        form.populate_obj(site)
        db.session.add(site)
        db.session.commit()
        flash("Added site")
        return redirect(url_for("index"))
    return render_template("validation_error.html", form=form)


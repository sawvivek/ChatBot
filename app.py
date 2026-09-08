from flask import Flask, render_template, request, jsonify, redirect
from tfidf_model import find_best_answer, refresh_tfidf_model
from database import get_all_faqs, add_faq, update_faq, delete_faq

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    faqs = get_all_faqs()

    return render_template(
        "admin.html",
        faqs=faqs
    )
@app.route("/admin/add", methods=["POST"])
def admin_add():
    question = request.form.get("question", "").strip()
    answer = request.form.get("answer", "").strip()

    if question and answer:
        add_faq(question, answer)
        refresh_tfidf_model()

    return redirect("/admin")

@app.route("/admin/edit/<int:faq_id>")
def edit_faq(faq_id):
    from database import get_faq_by_id

    faq = get_faq_by_id(faq_id)

    if faq is None:
        return "FAQ not found", 404

    return render_template(
        "edit.html",
        faq=faq
    )

@app.route("/admin/edit/<int:faq_id>", methods=["POST"])
def admin_edit(faq_id):
    question = request.form.get("question", "").strip()
    answer = request.form.get("answer", "").strip()

    if question and answer:
        update_faq(faq_id, question, answer)

    return redirect("/admin")
@app.route("/admin/delete/<int:faq_id>", methods=["POST"])
def admin_delete(faq_id):
    delete_faq(faq_id)
    refresh_tfidf_model()

    return redirect("/admin")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    answer = find_best_answer(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(debug=True)
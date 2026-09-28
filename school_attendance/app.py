from flask import Flask, render_template, request, redirect, url_for, send_file
from datetime import date, datetime
import csv, io

app = Flask(__name__)

# ── Data ──────────────────────────────────────────────────────────────────────
classes = {
    "Class 1": list(range(1, 41)),
    "Class 2": list(range(1, 41)),
    "Class 3": list(range(1, 41)),
    "Class 4": list(range(1, 41)),
    "Class 5": list(range(1, 41)),
}

# attendance[class_name][date_str][roll_no] = "P" | "A"
attendance = {}


def today():
    return date.today().isoformat()


def get_day(cls, date_str):
    return attendance.get(cls, {}).get(date_str, {})


def stats(cls, date_str):
    day   = get_day(cls, date_str)
    total = len(classes[cls])
    pres  = sum(1 for v in day.values() if v == "P")
    abst  = sum(1 for v in day.values() if v == "A")
    unm   = total - pres - abst
    pct   = round(pres / total * 100) if total else 0
    return dict(total=total, present=pres, absent=abst, unmarked=unm, pct=pct)


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return redirect(url_for("attendance_page", cls=list(classes.keys())[0]))


@app.route("/attendance")
def attendance_page():
    cls      = request.args.get("cls", list(classes.keys())[0])
    date_str = request.args.get("date", today())
    if cls not in classes:
        cls = list(classes.keys())[0]

    day   = get_day(cls, date_str)
    rolls = classes[cls]
    st    = stats(cls, date_str)
    all_classes_stats = {c: stats(c, date_str) for c in classes}

    return render_template("index.html",
        cls=cls, date_str=date_str, today=today(),
        rolls=rolls, day=day, st=st,
        classes=list(classes.keys()),
        all_classes_stats=all_classes_stats)


@app.route("/mark", methods=["POST"])
def mark():
    cls      = request.form.get("cls")
    date_str = request.form.get("date", today())
    roll     = request.form.get("roll")
    status   = request.form.get("status")   # "P" or "A"

    if cls in classes:
        attendance.setdefault(cls, {}).setdefault(date_str, {})[roll] = status

    return redirect(url_for("attendance_page", cls=cls, date=date_str))


@app.route("/mark_all", methods=["POST"])
def mark_all():
    cls      = request.form.get("cls")
    date_str = request.form.get("date", today())
    status   = request.form.get("status")   # "P" or "A"

    if cls in classes:
        attendance.setdefault(cls, {}).setdefault(date_str, {})
        for roll in classes[cls]:
            attendance[cls][date_str][str(roll)] = status

    return redirect(url_for("attendance_page", cls=cls, date=date_str))


@app.route("/report")
def report():
    cls = request.args.get("cls", list(classes.keys())[0])
    if cls not in classes:
        cls = list(classes.keys())[0]

    roll_data = []
    all_dates = sorted(attendance.get(cls, {}).keys())

    for roll in classes[cls]:
        row = {"roll": roll, "days": {}, "present": 0, "total": 0}
        for d in all_dates:
            s = attendance[cls][d].get(str(roll), "")
            row["days"][d] = s
            if s in ("P", "A"):
                row["total"] += 1
            if s == "P":
                row["present"] += 1
        row["pct"] = round(row["present"] / row["total"] * 100) if row["total"] else 0
        roll_data.append(row)

    return render_template("report.html",
        cls=cls, classes=list(classes.keys()),
        roll_data=roll_data, all_dates=all_dates, today=today())


@app.route("/export")
def export():
    cls      = request.args.get("cls", list(classes.keys())[0])
    date_str = request.args.get("date", today())
    day      = get_day(cls, date_str)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Roll No", "Status", "Date", "Class"])
    for roll in classes.get(cls, []):
        s = day.get(str(roll), "Unmarked")
        writer.writerow([roll, s, date_str, cls])

    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()),
                     mimetype="text/csv", as_attachment=True,
                     download_name=f"{cls.replace(' ','_')}_{date_str}.csv")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

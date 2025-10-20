import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Challenge 1 analysis""")
    return


@app.cell(hide_code=True)
def _():
    import polars as pl
    from polars import col as c
    import seaborn as sns
    import matplotlib.pyplot as plt
    import marimo as mo
    from marimo import md
    return c, md, mo, pl, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Raw data""")
    return


@app.cell(hide_code=True)
def _(pl):
    # df = pl.read_csv("grades/challenge_1.csv")
    df = pl.read_csv("grades/quiz-PSYC137 Challenge 1 FA25-full-2.csv")
    df
    return (df,)


@app.cell
def _(c, df, pl):
    by_nblm = df.group_by(c("Stu27"))
    by_nblm.len()
    by_nblm.agg(c("PercentCorrect").mean(), pl.len() / df.height).sort(
        c("PercentCorrect")
    )
    return


@app.cell
def _(df, plt, sns):
    sns.set_style("whitegrid")
    ax = sns.barplot(
        data=df,
        x="Stu27",
        y="PercentCorrect",
        hue="Stu27",
        order=["A", "B", "C", "D"],
        legend=False,
    )
    ax.set(
        ylim=(60, 100),
        ylabel="Score",
        xticklabels=["No", "Once or Twice", "Challenge Prep", "Consistently"],
        xlabel="",
    )
    sns.despine()
    plt.show()
    return


@app.cell
def _(c, df):
    # Add column without bonus
    grades = df.select(
        c("ZipGrade ID").alias("student"),
        c("Num Correct").alias("score"),
        c("Percent Correct").alias("score_norm"),
    ).with_columns(
        score_nobonus=c("score") - 2, score_nobonus_norm=(c("score") - 2) / 52 * 100
    )
    return (grades,)


@app.cell(hide_code=True)
def _(md):
    md("without bonus")
    return


@app.cell(hide_code=True)
def _(c, grades):
    grades.select(
        c("score_nobonus_norm").mean().alias("mean"),
        c("score_nobonus_norm").min().alias("min"),
        c("score_nobonus_norm").max().alias("max"),
        c("score_nobonus_norm").median().alias("median"),
        c("score_nobonus_norm").std().alias("std"),
    )
    return


@app.cell(hide_code=True)
def _(md):
    md("with bonus")
    return


@app.cell(hide_code=True)
def _(c, grades, md):
    # With bonus
    md("Descriptives including bonus:")
    grades.select(
        c("score_norm").mean().alias("mean"),
        c("score_norm").min().alias("min"),
        c("score_norm").max().alias("max"),
        c("score_norm").median().alias("median"),
        c("score_norm").std().alias("std"),
    )
    return


@app.cell(hide_code=True)
def _(mo):
    cutoff = mo.ui.number(start=1, stop=100, step=1)
    cutoff
    return (cutoff,)


@app.cell
def _(alt, grades_filtered):
    _chart = (
        alt.Chart(grades_filtered)  # <-- replace with data
        .mark_bar()
        .encode(
            x=alt.X("PercentCorrect", type="quantitative", bin=True, title="Score"),
            y=alt.Y("count()", type="quantitative", title="# Students"),
            tooltip=[
                alt.Tooltip(
                    "PercentCorrect",
                    type="quantitative",
                    bin=True,
                    title="Score",
                    format=",.2f",
                ),
                alt.Tooltip(
                    "count()",
                    type="quantitative",
                    format=",.0f",
                    title="# Students",
                ),
            ],
        )
        .properties(width="container")
        .configure_view(stroke=None)
    )
    _chart
    return


@app.cell
def _(c, grades_filtered):
    grades_filtered.select(c("PercentCorrect")).describe()
    return


@app.cell
def _(c, grades_filtered):
    grades_filtered.filter(c("PercentCorrect") >= 85).height
    return


@app.cell
def _(grades_filtered):
    grades_filtered.height
    return


@app.cell
def _():
    import altair as alt
    return (alt,)


@app.cell(hide_code=True)
def _(cutoff, md):
    md(f"## After filtering grades <= {cutoff.value}%")
    return


@app.cell(hide_code=True)
def _(c, cutoff, df, mo):
    low_students = df.filter(c("PercentCorrect") <= cutoff.value)
    mo.md(
        f"""Number of students with scores < {cutoff.value}% (after bonus): {low_students.height}"""
    )
    return (low_students,)


@app.cell(hide_code=True)
def _(low_students):
    low_students
    return


@app.cell(hide_code=True)
def _(c, cutoff, df):
    # drop erroneous students
    grades_filtered = df.filter(c("PercentCorrect") > cutoff.value)
    grades_filtered
    return (grades_filtered,)


@app.cell
def _(grades_s):
    grades_s
    return


@app.cell(hide_code=True)
def _(md):
    md("With bonus")
    return


@app.cell(hide_code=True)
def _(c, grades_filtered):
    grades_filtered.select(
        c("score_norm").mean().alias("mean"),
        c("score_norm").min().alias("min"),
        c("score_norm").max().alias("max"),
        c("score_norm").median().alias("median"),
        c("score_norm").std().alias("std"),
    )
    return


@app.cell(hide_code=True)
def _(md):
    md("without bonus")
    return


@app.cell(hide_code=True)
def _(c, grades_filtered):
    grades_filtered.select(
        c("score_nobonus_norm").mean().alias("mean"),
        c("score_nobonus_norm").min().alias("min"),
        c("score_nobonus_norm").max().alias("max"),
        c("score_nobonus_norm").median().alias("median"),
        c("score_nobonus_norm").std().alias("std"),
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

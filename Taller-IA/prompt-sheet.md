# Prompt Sheet: Building Teaching Notebooks with AI

UEM STEAM Faculty Workshop, "Jupyter in Teaching: Building with AI", 26 November 2026. Eric Van Dusen, UC Berkeley CDSS.

## How to use this sheet

A good prompt reads like a lesson plan: who the students are, what they should learn, and what the notebook must contain. You already have that expertise; the AI supplies the code.

- Replace everything in [brackets] with your own course details.
- Write prompts in Spanish or English. Ask for the notebook text in the language your students use.
- The prompts work in Gemini chat, in Colab's Gemini side panel, and in most other AI assistants.
- Always run the notebook yourself before students see it. The AI writes a first draft; you decide whether it is correct.

## Notebooks and project-based learning

The notebook is the lab bench for the project: the place where students do the work, not just read about it.

- **Real question, real data.** Students work on open data (INE, Eurostat, their own measurements) instead of textbook numbers.
- **Visible process.** Code, results and reasoning sit in one document, so you can assess how students reached a conclusion, not only the answer.
- **Iteration.** Change a value, rerun, compare: the hypothesis, test and revise cycle that PBL is built on.
- **A shareable product.** The finished notebook is the deliverable, ready to present, publish on GitHub, or pass to the next cohort.

With AI, faculty who do not code can build a project scaffold in an hour. Your role shifts to designing the driving question and judging quality.

PBL prompts:

- `Turn [topic] into a PBL project: a driving question, a real public dataset, three milestones over [n] weeks, and a final deliverable.`
- `Create a starter notebook for this project: load the data, show one example analysis, then leave open questions for teams to explore.`
- `Suggest roles for a team of four working on this notebook project, with what each person contributes.`
- `Write a rubric for the final notebook that assesses the question, the method, the interpretation and the presentation.`
- `Suggest three ways teams could extend this project if they finish early.`

### Three project models

In each model, the grade depends on transparency and judgement, the skills AI does not replace.

1. **Reproduce a journal article.** Teams take a published figure or claim, find the data, and rebuild it. They learn that results are earned, and how often methods are under-reported.
   - `Here is a paper [PDF]. Identify its main claim and key figure, the data it uses, and where that data can be found. Create a notebook scaffold to reproduce the figure step by step.`
2. **Business case with reproducible claims.** Teams present a case, and every number on every slide must trace to a notebook cell. In Q&A, the question is "show me the cell".
   - `For this business case on [company or market], list every quantitative claim a presentation would make, and create a notebook section that computes each one from public data.`
3. **Swap and peer-grade.** Each team builds a multi-step analysis, then hands it to another team, who must run it, follow it and grade the documentation.
   - `Write a peer-review rubric for a data analysis notebook focused on documentation: can a stranger run it, follow each step, and understand why each decision was made?`

### A warning on "bring your own dataset" projects

A fully open project where each team finds its own dataset often goes wrong. Common reasons:

- **Students are not yet good judges of a dataset.** They may not ask who collected it, how, from whom, or whether it is large enough to say anything.
- **The data may be censored or incomplete.** Missing groups, suppressed small counts, top-coded values or only the survivors can silently distort every result.
- **The question and the data do not match.** The idea a team is excited about may need a variable, time period or level of detail the dataset does not have.
- **Time goes into searching and cleaning, not learning.** Teams can lose weeks before any analysis starts.
- **AI makes it easier to go wrong confidently.** It will analyse a bad dataset without complaint, and may even invent one.
- **Projects become hard to compare and grade fairly.**

What works better:

1. Offer a **curated menu** of 5 to 10 vetted datasets, with open choice of question within them.
2. Add a **data audit milestone** in the first weeks: source, collection method, what is missing, what it can and cannot show.
3. Require a **question and data fit check** that you approve before teams continue.

Prompts for the audit:

- `Before I analyse this dataset, help me audit it: who collected it, how, for what period, what is missing or suppressed, and what it can and cannot be used to conclude.`
- `Here is my research question and the dataset's columns: [paste]. Can this dataset answer my question? If not, what would I need instead?`
- `What biases or gaps could make results from this dataset misleading?`

## 1. Build a notebook from scratch (Gemini chat)

Start from the master prompt below. The more specific you are about students and learning goals, the better the first draft.

```
I teach [course name] to [year, e.g. first-year] [degree] students at a project-based university.
Create a Jupyter notebook (.ipynb) that teaches [one concept].
Students have [no / some / good] coding experience.
Learning goal: by the end, students can [specific skill or understanding].
Include:
- a short introduction in markdown explaining why this matters in [field]
- small code cells (under 10 lines each) with a comment on every line
- at least one plot with labelled axes and units
- two "predict, then change the value and check" questions
- one short open question connecting the result to a real case
- a final reflection question
Use only pandas, numpy and matplotlib.
Write all text in [Spanish / English].
Give me the complete .ipynb file to download.
```

Useful follow-ups in the same chat:

- `Make the explanations shorter. Students should read less and run more.`
- `Add a section that uses real data from [source, e.g. INE, Eurostat, NASA, a CSV I will upload].`
- `Split this into two notebooks: a guided version for class and an open project for homework.`
- `Rewrite the notebook for students with no maths beyond secondary school.`

To share: download the .ipynb, open it in Colab (File, Upload notebook), run all cells, then share the Colab link or put the file in your course repository.

## 2. Improve a notebook (Colab with Gemini in the side panel)

Open the notebook in Colab, click the Gemini icon, and work on it cell by cell.

| Goal | Prompt |
| --- | --- |
| Understand a cell | `Explain this cell to a first-year student in two sentences.` |
| Fix an error | `This cell gives an error. Fix it and explain what was wrong in plain language.` |
| Simplify | `Rewrite this cell so a student with no coding experience can follow it. Keep the same result.` |
| Make it interactive | `Add a slider so students can change [parameter] and see the plot update.` |
| Use real data | `Replace the made-up numbers with data from [URL or uploaded CSV]. Show the first rows before using it.` |
| Better visuals | `Improve this plot for a lecture slide: larger fonts, axis labels with units, a clear title.` |
| Add context | `Add a markdown cell before this one explaining why [concept] matters in [field], with one real example.` |
| Extend | `Add a final challenge where students apply the same method to [new case].` |

## 3. Discipline starters (STEAM)

Each line can replace "[one concept]" in the master prompt, or be used on its own as a quick first request.

| Area | Starter prompt |
| --- | --- |
| Physics | `A notebook that simulates a falling object with and without air resistance, where students change mass and drag and compare the curves.` |
| Biology / Health | `A notebook that models how an infection spreads (SIR model), where students change the contact rate and see the effect on the peak.` |
| Chemistry | `A notebook that plots reaction rate against temperature using the Arrhenius equation, with a question on why fridges slow food spoilage.` |
| Environmental science | `A notebook that loads monthly temperature data for Madrid and shows the trend over the last 50 years.` |
| Computing / Technology | `A notebook that compares the speed of two sorting methods on lists of growing size, with a plot of time against list size.` |
| Engineering | `A notebook that calculates the deflection of a simple beam under a load, where students change the material and length.` |
| Architecture | `A notebook that estimates daylight hours and sun angle through the year for a building in Madrid, to inform window placement.` |
| Arts / Design | `A notebook that extracts the main colour palette from an image and compares palettes from two artistic periods.` |
| Music / Audio | `A notebook that generates and plots sound waves, shows how adding frequencies creates chords, and lets students listen to the result.` |
| Humanities / Language | `A notebook that counts word frequencies in two public-domain texts and compares their vocabulary.` |
| Mathematics | `A notebook that shows how compound interest grows, comparing yearly, monthly and continuous compounding.` |
| Economics / Business | `A notebook that plots Spanish GDP and unemployment over time and asks students to identify the 2008 and 2020 crises.` |
| Sports science | `A notebook that analyses heart rate during an interval session and finds the time spent in each training zone.` |

## 4. Assess and give feedback

- `Make a student version of this notebook: keep the explanations, replace the solution code with "# your code here", and give me the answers separately.`
- `Add a check cell after each exercise that tells the student if their answer is correct, without showing the answer.`
- `Write three exercises of increasing difficulty: one that changes a value, one that modifies code, one that applies the method to new data.`
- `Write a rubric (4 levels) for the final open question, focused on reasoning, not code.`
- `Add a short multiple-choice quiz at the end with explanations for each wrong option.`
- `Turn this notebook into a group project brief: a question, a dataset, deliverables and a timeline of [n] weeks.`
- `Here is a student's submitted notebook. Point out errors in reasoning and suggest one question I could ask them, without rewriting their work.`

## 5. Review the output as a skeptical instructor

This is the most important step. Your subject knowledge is what makes the notebook trustworthy.

- `Review this notebook as a skeptical [field] professor. List anything that is wrong, oversimplified, or misleading.`
- `Check every formula and unit in this notebook. Show your working for each one.`
- `Where would a first-year student most likely get stuck or confused? Suggest a fix for each point.`
- `Is the data source real and correctly cited? Give me the link so I can verify it.`
- `Which cells could a student complete by just asking an AI? Suggest changes that require their own thinking.`
- `Estimate how long a student would need to complete this notebook, section by section.`

## 6. Teaching students to use Gemini well

You can build a course tutor as a Gemini Gem. Paste instructions like these into the Gem's instructions field:

```
You are a tutor for [course name] at Universidad Europea.
Students are [year] [degree] students working in Jupyter notebooks.
Never give the full solution to an exercise. Instead, ask a guiding question,
point to the relevant concept, or show a similar example with different numbers.
If a student shares code with an error, explain what the error message means
and where to look, but let them write the fix.
Stay within the course topics: [list topics]. If asked about something else,
say so and redirect to the course.
Answer in the language the student uses. Keep answers under 150 words.
```

Prompts to teach students, so AI supports their learning rather than replacing it:

- `Explain this error message to me, but do not fix my code.`
- `Ask me three questions to check whether I understand [concept].`
- `I think the answer is [x] because [reason]. Where is my reasoning weak?`
- `Give me a similar exercise with different numbers so I can practise.`

Test your Gem before sharing it: ask it directly for the answer to your hardest exercise, and see whether it holds the line.

## Tips and cautions

- **Start small.** One concept, one notebook, 20 to 30 minutes of student work. Iterate from there.
- **Run every cell yourself** before class. AI often produces code that looks right but fails, or plots that are subtly wrong.
- **Verify data and citations.** AI can invent datasets, URLs and references.
- **Ask for changes, not restarts.** Refining in the same chat keeps the context and gives better results.
- **Keep the code visible.** Avoid hidden helper files, so students can see and question every step.
- **Do not paste student personal data** into AI tools.
- **Share what works.** Add your notebooks to the UEM Jupyter pilot collection so colleagues can reuse and adapt them.

| [home page](https://cmustudent.github.io/tswd-portfolio-templates/) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# Final Project, Part I: Call Home

*How much time international students really have left with their parents, and why the phone call matters more than we think.*

---

## 1. Project summary

When an international student comes to the U.S. to study and then stays to work, home becomes something you visit, not somewhere you live. Most of us assume there will be plenty of time to see our parents later. This project uses data to test that assumption. Combining remaining life expectancy for parents in the two largest sending countries (India and China), how often H-1B workers actually enter and leave the U.S., and how long visa stamping appointments take, I estimate how many weeks, meals and festivals an international student can realistically expect to spend with their parents in person. The answer is far smaller than it feels.

But the story does not end there. Because in-person time is rare and depends on visa calendars we do not control, the phone call becomes the main place where our relationship with our parents lives. Even that has limits: time zones leave only a few overlapping waking hours a day. And survey data shows parents, especially fathers, want more contact than they get. The project ends with something every reader can control: a short daily call adds up to almost another visit's worth of time every year. The goal is simple: after reading, people pick up the phone and call home.

**Audience:** International students and early-career workers (F-1, OPT, H-1B) in the U.S., especially from India and China. Secondary audience: anyone living far from their parents.

## 2. Project structure

### One-sentence summary

For international students who stay to work in the U.S., visits home are rare and fragile, so the phone call is where most of our remaining time with our parents will happen, and most of us are not using it enough.

### User story and call to action

> As an international student, I want to understand how little in-person time I have left with my parents **so that I can** make the most of the time we do have.
> **I can do this by** setting a recurring call with my parents, starting this week.

### Story arc

![Story arc](images/story_arc.svg)

| Beat | Section header | What the reader learns | Evidence |
|---|---|---|---|
| 1. Hook | "About 38 weeks left with your mom" | For a 60-year-old mother in India, about 19 more years of life and one two-week visit a year add up to about 38 weeks together, compared with about 1,144 weeks before leaving home | Life expectancy at 60 (India SRS life tables) + visit-frequency assumptions |
| 2. Why so few | "Getting home isn't up to you" | Indian H-1B workers enter the U.S. about 1.4 times a year; Canadians, who need no visa stamp, about 3.9 | DHS OHSS FY2022 fact sheet |
| 3. The wait | "Your consulate sets the calendar" | Predicted waits for an H-1B-type appointment range from 1 to 6.5 months across Indian consulates, and appointments can be rescheduled | U.S. State Department Global Visa Wait Times |
| 4. Low point | "Even a phone call has a window" | With work and sleep, a U.S. worker shares only about 4.5 free waking hours a weekday with parents in India (about 7 for China) | Own time-zone calculation |
| 5. The turn | "They want to hear from you" | 44% of fathers and 30% of mothers say they talk with their young adult child less than they'd like | Pew Research Center, fall 2023 |
| 6. The rise | "Every call counts" | A 30-minute daily call adds up to about 182 hours a year, roughly 80% of a two-week visit's waking hours | Own calculation (assumptions below) |
| 7. Call to action | "Call home" | Set a recurring call. Start with your dad. | — |

### Design choices (Good Charts, Chapter 6)

Every chart is a manipulation; the question is whether it persuades or deceives. I use persuasion techniques on purpose: the hook shows the *whole* next 20 years as a grid of weeks and colors only the weeks spent with parents (isolation with the full denominator visible), and compares them to the weeks already spent together (an added reference point). To stay on the honest side of the line, I use remaining life expectancy at the parent's age (not life expectancy at birth), print every assumption next to the visuals, and let readers change the assumptions in the calculator.

### One-minute presentation plan

I will present live from the Shorthand page, not slides: hook question ("When did you last eat a meal your mom cooked?") → hero number from the calculator → the call-window timeline → the Pew "dads want more" chart → call to action.

## 3. Initial sketches

The sketch below combines the story arc with the planned visual for each beat: the top shows the emotional shape of the story, and each card underneath is one scrolling section of the Shorthand story, with its header, the planned chart, and its data source.

![Story arc with planned visuals (sketch)](images/story_arc_sketch.png)

**Hero screen (section 1):** an interactive calculator. Readers pick their country, their parent's age and how often they can visit (every 1 to 6 years), and choose a measure: weeks, meals, or festivals at home (Diwali for India, Lunar New Year for China). Orange marks show what they get; gray marks show what they lose compared with visiting every year.

## 4. The data

### Primary sources

1. **Remaining life expectancy at age 60, by sex.** Used to estimate how many years a parent has left. Current values: India, women 19.2 and men 17.4 years, from the national Sample Registration System life tables as reported in [Genus (2025)](https://link.springer.com/article/10.1186/s41118-025-00247-2); China, women 23.2 and men 20.2 years, from [BMC Geriatrics (2025)](https://link.springer.com/article/10.1186/s12877-025-06262-4). For the final project I will replace both with the World Health Organization's [Life expectancy at age 60](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-age-60-(years)) indicator so the two countries come from one consistent method.
2. **H-1B entries per worker, by country.** U.S. Department of Homeland Security, Office of Homeland Security Statistics, *Nonimmigrant Admissions and Estimated Nonimmigrant Individuals* fact sheets for [FY2022](https://www.dhs.gov/sites/default/files/2024-04/24_0416_ohss_nonimmigrant-admissions-and-estimated-nonimmigrant-individuals-2022.pdf) and [FY2016](https://ohss.dhs.gov/sites/default/files/2023-12/Nonimmigrant%2520Admissions%2520and%2520Estimated%2520Nonimmigrant%2520Individuals%2520Fact%2520Sheet%25202016_0.pdf). Used as a proxy for how often workers travel. ([fact sheet index](https://ohss.dhs.gov/topics/immigration/nonimmigrant/nonimmigrant-fact-sheet))
3. **Visa appointment wait times.** U.S. Department of State, [Global Visa Wait Times](https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/global-visa-wait-times.html), snapshot of October 21, 2026, petition-based (H, L, O, P, Q) category. The consulate chart focuses on India's five posts, since India sends the most students and has the widest spread of waits.
4. **Parent–child contact.** Pew Research Center, [Young adults' relationship with their parents](https://www.pewresearch.org/social-trends/2024/01/25/young-adults-relationship-with-their-parents/) (Jan. 2024) and [short read on fathers](https://www.pewresearch.org/short-reads/2024/03/21/among-parents-with-young-adult-children-some-dads-feel-less-connected-to-their-kids-than-moms-do/) (Mar. 2024).
5. **Context: international student counts.** Institute of International Education, [Open Doors](https://opendoorsdata.org/annual-release/international-students/). India and China are the two largest sending countries and together make up more than half of international students in the U.S., which is why the project focuses on them.

### How I will use the data

The life-expectancy, visit-frequency and visit-length values combine in one small country table to power the calculator (weeks, meals and festivals left). The DHS, State Department and Pew data each drive one chart on their own, so they do not need to be joined. Time-zone overlap is calculated from standard UTC offsets with a short script, so anyone can check it. I limit the first version to India and China because DHS reports entries per worker only for the largest H-1B countries; Canada appears in one chart as a gray reference point because it needs no visa stamp.

### Limitations

- **Entries are not trips home.** DHS counts every entry into the U.S., including business trips and first arrivals, so 1.4 a year is an upper bound on trips home. Workers who did not travel that year are not counted at all.
- **Both DHS years predate the 2025–26 visa changes.** I treat them as a "before" baseline and the 2026 wait-time snapshot as "now."
- **Wait times are predictions** and change monthly; they do not capture appointments that were cancelled or rescheduled.
- **Pew surveyed U.S. families**, not families of international students abroad. *Optional:* a short anonymous survey of international students ("When did you last go home? What stopped you?") would fill this gap; I will check with the instructor before collecting it.

### Data files (in this repository)

| File | Contents |
|---|---|
| [`data/country_facts.csv`](data/country_facts.csv) | One row per country: festival, life expectancy at 60 by sex (with source), entries per worker, time-zone offset, call window |
| [`data/dhs_h1b_entries_per_worker.csv`](data/dhs_h1b_entries_per_worker.csv) | DHS FY2016 and FY2022 H-1B entries per worker for India, China, Canada, Mexico |
| [`data/visa_wait_times_india_2026-10-21.csv`](data/visa_wait_times_india_2026-10-21.csv) | Predicted months to next petition-based appointment, five Indian consulates |
| [`data/pew_parent_contact.csv`](data/pew_parent_contact.csv) | Pew contact-frequency and "less than I'd like" percentages |
| [`data/call_window.csv`](data/call_window.csv) | Output of the time-zone script |
| [`data/assumptions.csv`](data/assumptions.csv) | Every assumption used in the calculations |
| [`scripts/call_window.py`](scripts/call_window.py) | Reproducible time-zone overlap calculation |

**Next steps for Part II:** standardize life expectancy on the WHO indicator, archive monthly snapshots of the State Department wait-time page to show change over time, and (with instructor approval) run the short survey of international students.

## 5. Method and medium

The final story will be built in **Shorthand** as a scrolling, section-by-section narrative following the story arc above. Charts and the hero calculator will be built in **Tableau Public** and embedded in Shorthand. The calculator uses Tableau parameters (country, parent's age, visit frequency, measure) and calculated fields on the country table; the weeks grid is a unit chart. All data, the time-zone script and the sketches are stored in this GitHub repository. Images will come only from Creative Commons, public-domain or licensed sources, following the CMU Library guide.

## References

- Berinato, S. (2023). *Good charts: The HBR guide to making smarter, more persuasive data visualizations* (updated and expanded ed.). Harvard Business Review Press.
- Institute of International Education. (2026). *Open Doors 2026 Report on International Educational Exchange.*
- Pew Research Center. (2024, January 25). *Young adults' relationship with their parents.*
- Pew Research Center. (2024, March 21). *Among parents with young adult children, some dads feel less connected to their kids than moms do.*
- U.S. Department of Homeland Security, Office of Homeland Security Statistics. (2024). *Nonimmigrant admissions and estimated nonimmigrant individuals: 2022.*
- U.S. Department of Homeland Security, Office of Immigration Statistics. (2018). *Nonimmigrant admissions and estimated nonimmigrant individuals: 2016.*
- U.S. Department of State. (2026, October 21). *Global visa wait times.*
- *Sex disparities in health of older adults in India: assessing the morbidity-mortality paradox through disability-free life expectancy.* (2025). *Genus.*
- *Population-based estimates of healthy working life expectancy in China.* (2025). *BMC Geriatrics.*
- World Health Organization. *Global Health Observatory: Life expectancy at age 60 (years).*

**AI acknowledgement:** I used Claude (Anthropic) to help develop this proposal: to brainstorm and refine the story angle and call to action, to locate public data sources, to draft sections of this page, to write the time-zone script, and to produce the digital storyboard and story-arc sketches. I chose the topic, made the final framing decisions, checked the figures against the original sources, and edited the text.

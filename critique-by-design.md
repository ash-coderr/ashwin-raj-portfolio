| [home page](https://cmustudent.github.io/tswd-portfolio-templates/) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# Critique by Design
The task was to select an existing data visualization and improve it by following a five-step design process: selecting a visualization, critiquing its strengths and weaknesses, sketching a possible redesign, gathering feedback, and building the final solution. The goal was to apply good data visualization principles to make the information clearer, more engaging, and easier for the audience to understand. This process also helped us understand how feedback and experimentation can improve a design.

## Step one: the visualization
Here is the original visualization I chose for the redesign. -- https://makeovermonday.vercel.app/dataset/what-are-the-world-s-deadliest-animals

<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/7a866968-092a-4f3f-9a86-01f39671c8eb" />


## Step two: the critique
The original visualization was effective at grabbing attention and challenging common assumptions about the deadliest animals. The use of animal icons and large blocks made it visually interesting. However, the combination of a treemap and bar chart felt inconsistent and somewhat confusing. Mosquitoes and humans dominated the visualization, while smaller animals were harder to compare. The animal icons also did not consistently represent the differences in death counts. Overall, the visualization communicated the main message well but could have been clearer, more balanced, and easier for the general public to understand.
## Step three: Sketch a solution
<img width="940" height="627" alt="image" src="https://github.com/user-attachments/assets/ba42f8f7-adcc-4da1-82a9-15182e5a9ca7" />

## Step four: Test the solution


Questions for the Interview: 

- Can you tell me what you think this is?

- Can you describe to me what this is telling you?

- Is there anything you find surprising or confusing?

- Who do you think is the intended audience for this?

- Is there anything you would change or do differently?

Results: 

## Interview Feedback

| Question | Interview 1 – Public Policy & Management (Data Analytics Track) | Interview 2 – MISM (BIDA) | Interview 3 – Public Policy & Management |
|----------|-------------|-------------|-------------|
| **What worked?** | The treemap clearly highlighted mosquitoes and humans as the largest contributors to human deaths. | The rectangle sizes made it easy to understand the differences in death counts. | The visualization was engaging and helped communicate important public health information. |
| **What didn't work?** | The animal images were inconsistent, as only mosquitoes and humans had pictures. | Smaller animals were difficult to see and compare because the larger categories dominated the space. | The title was confusing, some numbers needed correction, and the colors could have been lighter for better readability. |
| **What questions came up?** | Could images be added for all animals without making the visualization cluttered? | How could viewers explore smaller animals without changing the accuracy of the data? | Would viewers understand that the numbers represented human deaths, including deaths caused by diseases? |
| **What new inspiration arose?** | Simplify the layout and remove unnecessary visual elements. | Add interactive filters so users could exclude larger categories and explore smaller death counts separately. | Improve the title, use shades of red, and make the visualization easier to understand. |

## How Feedback Influenced My Final Redesign

The feedback helped me identify issues with my initial treemap sketch, including the confusing title, inconsistent animal images, color choices, and incorrect data values. One of the biggest challenges was making smaller animals visible because mosquitoes and humans dominated the visualization. Based on this feedback, I redesigned the visualization in Tableau using different shades of red and improved the title and labels. I also added interactive filters that allowed users to exclude the largest categories and deep dive into animals with smaller death counts separately. This made the final visualization cleaner, more interactive, and easier to explore.


Synthesis: 


I checked and corrected the numbers, revised the title to mention human deaths, and built an interactive treemap in Tableau. I used lighter-to-darker shades of red instead of many unrelated colors. Most importantly, I added **interactive filters through the Explore Animals dropdown**. Viewers could start with all 21 animals, filter out mosquitoes and humans, or deep-dive separately into categories with fewer than 10,000 estimated deaths per year. This made the smaller numbers easier to investigate without artificially enlarging their rectangles; the treemap recalculated areas and colors within each selected view.


## Step five: build the solution

The feedback on my initial treemap sketch helped me identify several areas for improvement, including a confusing title, inconsistent use of animal images, color choices, and incorrect data values. One of the biggest challenges was making smaller animals visible since mosquitoes and humans dominated the visualization. The feedback also encouraged me to explore better ways of separating the categories without losing the accuracy of the data. Based on these suggestions, I redesigned the visualization in Tableau using an interactive treemap with different shades of red to represent the number of human deaths. I corrected the data, improved the title and labels, and added a dropdown that allowed users to filter out larger categories and explore smaller animals more clearly. Overall, the feedback helped me move from a static sketch to a cleaner, more interactive visualization that made the data easier to understand and explore.
<div class='tableauPlaceholder' id='viz1794457141878' style='position: relative'><noscript><a href='#'><img alt='Which Species Cause the Most Human Deaths?From mosquitoes to sharks: Explore how estimated human deaths vary across 21 animal categories. ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5W&#47;5WQ483M6Y&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;5WQ483M6Y' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5W&#47;5WQ483M6Y&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
<script type='text/javascript'>                    
  var divElement = document.getElementById('viz1794457141878');                   
  var vizElement = divElement.getElementsByTagName('object')[0];                    
  if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1300px';vizElement.style.height='927px';} 
  else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1300px';vizElement.style.height='927px';} 
  else { vizElement.style.width='100%';vizElement.style.height='727px';}                    
  var scriptElement = document.createElement('script');                   
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                   
  vizElement.parentNode.insertBefore(scriptElement, vizElement);               
</script>

## References

1. Berinato, S. (2019). *Good Charts Workbook: Tips, Tools, and Exercises for Making Better Data Visualizations*. Harvard Business Review Press.
   - Chapter 3: Choosing Chart Types
   - Chapter 4: Practicing Persuasion
   - https://store.hbr.org/product/good-charts-workbook-tips-tools-and-exercises-for-making-better-data-visualizations/10209

2. Peck, E. (2019, May 20). *Data Is Personal: What We Learned from 42 Interviews in Rural America*. Multiple Views: Visualization Research Explained, Medium.
   - https://medium.com/multiple-views-visualization-research-explained/data-is-personal-what-we-learned-from-42-interviews-in-rural-america-93539f25836d

3. Ritchie, H., & Spooner, F. (2026, March 9). *What Are the World's Deadliest Animals, and Can We Protect Ourselves Against Them?* Our World in Data.
   - https://ourworldindata.org/deadliest-animals


## AI acknowledgements
I used ChatGPT to assist with brainstorming ideas for my visualization redesign, refining my written explanations, and troubleshooting certain steps in Tableau. AI was also used to help develop the initial treemap sketch and organize interview feedback. I reviewed and corrected the suggestions based on the dataset and feedback I received. The final design decisions, Tableau implementation, and evaluation of the visualization were completed by me.


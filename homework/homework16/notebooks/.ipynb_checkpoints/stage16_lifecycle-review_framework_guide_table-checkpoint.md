# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined a real-world financial problem, clarified project objectives and stakeholder needs. Created a stakeholder persona and project repo. | Balancing multiple objectives and ambiguity in scope required careful framing of success metrics. | Created stakeholder memos and clear README documentation to align expectations. Established GitHub repo structure early. | Adopt standardized project scoping templates to ensure clarity from the start. |
| **2. Tooling Setup** | Set up a reproducible environment with GitHub, folder scaffolding, .gitignore, and README. | Version control integration and dependency management were key issues. | Used GitHub to enforce versioning, documented environment setup, and modularized project structure. | Automate environment setup with setup scripts for easier onboarding. |
| **3. Python Fundamentals** | Practiced NumPy and pandas operations and wrote reusable Python functions. | Developing reusability was challenging initially. | Created simple utility functions, added markdown documentation, and began a tests. | Expand testing and refactoring to improve maintainability. |
| **4. Data Acquisition / Ingestion** | Pulled data from APIs. | Ensuring data integrity and avoiding hardcoding. | Used .env for secret management and ensured reproducible filenames. |Implement automated ingestion pipelines and logging for data source validation. |
| **5. Data Storage** | Organized data/raw and data/processed folders. | Handling file path was challenges. | Documented folder structure and storage approach in README | Use cloud storage integration. |
| **6. Data Preprocessing** | Wrote reusable data cleaning functions in src/cleaning.py and saved cleaned datasets. | Transformation choices were key hurdles. | Systematically documented assumptions and validated cleaning functions in notebooks. | Automate preprocessing with pipelines and add validation tests. |
| **7. Outlier Analysis** | Built outlier detection functions and performed sensitivity analysis. And visualized effects. | Distinguishing true anomalies from valid data points was challenging. | Documented outlier policies and visual comparisons | Adopt advanced statistical detection methods. |
| **8. Exploratory Data Analysis (EDA)** | Created notebooks with histograms, scatter plots, correlation matrices, and summaries to guide feature engineering. | Interpreting patterns was tricky. | Enhanced visuals with annotations and ensured reproducibility. | Expand EDA automation. |
| **9. Feature Engineering** | Designed domain-informed features. Added scripts to pipeline. | Validating feature importance. | Linked feature design to EDA findings and domain knowledge. | Use feature selection algorithms and cross-validation to refine features. |
| **10. Modeling (Regression / Time Series / Classification)** | Implemented linear regression, classification models, and time series analysis; evaluated with evaluation metrics. | Addressing independence, homoscedasticity, and time-aware validation were key challenges. | Adopted pipelines, feature transformations, and diagnostic plots to validate assumptions. | Explore ARIMA. |
| **11. Evaluation & Risk Communication** | Conducted scenario testing and subgroup diagnostics| Explaining statistical assumptions and uncertainty | Used visuals, sensitivity tables, and commentary to communicate model risk. | Automate scenario testing pipelines and expand subgroup analyses. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Prepared decision-focused reports, slides, and dashboards with sensitivity analyses and assumptions. | Balancing technical completeness with clear communication; ensuring reproducibility. | Used executive summaries, clear visuals, and separated artifacts for different audiences. | Adopt automated reporting workflows and build interactive dashboards. |
| **13. Productization** | Ensured reproducibility for handoff; prepared dashboards/APIs. | Managing reproducibility and avoiding notebook clutter. | Added README guidance, version control, and folder organization. | Integrate pipelines and containerization for scalability. |
| **14. Deployment & Monitoring** | Designed conceptual deployment strategy and documented handoff plans. | Addressing drift, delayed feedback, and defining simple but effective monitoring systems. | Outlined layered metrics. | Build automated alerting and retraining pipelines. |
| **15. Orchestration & System Design** | Mapped workflow to DAGs, added logging, checkpoints, and designed repeatable pipelines. | Balancing complexity and maintainability in design. | Introduced lightweight scheduling, config separation, and script-based job management. | Adopt large-scale orchestration |
| **16. Lifecycle Review & Reflection** | Synthesized full lifecycle, documented learnings, and prepared professional-grade repo for handoff. | Ensuring clarity, structure, and maintainability for future use. | Added final polish, mapped lifecycle stages to artifacts, and reflected on workflow design. | Continuous improvement with better governance tools. |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?
  The Modeling and Evaluation stages were the most difficult because they required balancing technical rigor with interpretability, especially under strict financial assumptions. Ensuring model validity while managing time-aware splits, sensitivity testing, and clear communication made this stage particularly challenging.
- Which stage was the most **rewarding**?
  Feature Engineering and EDA were the most rewarding because they revealed actionable insights and transformed raw data into meaningful predictors.
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?
  Early decisions in Problem Framing and Tooling Setup heavily influenced downstream work by providing a clear structure and reproducible foundation.
- If you repeated this project, what would you **do differently across the lifecycle**?
  I would invest more time upfront in automating data ingestion and preprocessing to reduce manual adjustments later.
- Which skills do you most want to **strengthen** before your next financial engineering project?
  I want to strengthen my expertise in time series modeling and machine learning methods.

---
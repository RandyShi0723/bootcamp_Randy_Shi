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
| **1. Problem Framing & Scoping** | Defined a real-world financial problem, clarified project objectives, constraints, and stakeholder needs. Created a stakeholder persona and project repo with initial documentation.【27†source】 | Balancing multiple objectives and ambiguity in scope required careful framing of success metrics.【27†source】 | Created stakeholder memos and clear README documentation to align expectations. Established GitHub repo structure early.【27†source】 | Adopt standardized project scoping templates and stakeholder interviews to ensure clarity from the start.【27†source】 |
| **2. Tooling Setup** | Set up a reproducible environment with GitHub, folder scaffolding, .gitignore, and README. Optional scripts like Makefile or requirements.txt supported reproducibility.【28†source】 | Version control integration, dependency management, and maintaining folder consistency were key issues.【28†source】 | Used GitHub to enforce versioning, documented environment setup, and modularized project structure.【28†source】 | Automate environment setup with setup scripts and pyproject.toml for easier onboarding.【28†source】 |
| **3. Python Fundamentals** | Practiced NumPy and pandas operations, wrote reusable Python functions in src/utils.py, and documented code for future use.【29†source】 | Developing reusability and modularity habits was challenging initially.【29†source】 | Created simple utility functions, added markdown documentation, and began a tests/ folder.【29†source】 | Expand testing and refactoring to improve maintainability.【29†source】 |
| **4. Data Acquisition / Ingestion** | Pulled data from APIs and/or web scraping, saved raw data to /data/raw/, and used .env for secure credentials.【30†source】 | Ensuring data integrity, avoiding hardcoding, and handling authentication keys were obstacles.【30†source】 | Used .env and example templates for secret management and ensured reproducible filenames.【30†source】 | Implement automated ingestion pipelines and logging for data source validation.【30†source】 |
| **5. Data Storage** | Organized data/raw and data/processed folders, implemented reproducible save/load code with environment variables.【31†source】 | File path consistency and handling multiple formats were challenges.【31†source】 | Documented folder structure and storage approach in README; implemented secure path handling.【31†source】 | Use cloud storage integration and add schema validation for scalability.【31†source】 |
| **6. Data Preprocessing** | Wrote reusable data cleaning functions in src/cleaning.py, documented assumptions, and saved cleaned datasets.【32†source】 | Data quality and transformation choices (imputation, normalization) were key hurdles.【32†source】 | Systematically documented assumptions and validated cleaning functions in notebooks.【32†source】 | Automate preprocessing with pipelines; add validation tests.【32†source】 |
| **7. Outlier Analysis** | Built reusable outlier detection/handling functions, performed sensitivity analysis, and visualized effects.【33†source】 | Distinguishing true anomalies from valid data points was challenging.【33†source】 | Documented outlier policies, visual comparisons, and sensitivity tables.【33†source】 | Adopt advanced statistical or ML-based anomaly detection methods.【33†source】 |
| **8. Exploratory Data Analysis (EDA)** | Created notebooks with histograms, scatter plots, correlation matrices, and summaries to guide feature engineering.【34†source】 | Interpreting patterns and ensuring data representation clarity was tricky.【34†source】 | Enhanced visuals with annotations and ensured reproducibility.【34†source】 | Expand EDA automation; integrate interactive dashboards.【34†source】 |
| **9. Feature Engineering** | Designed domain-informed features, documented rationale, and added scripts to pipeline.【35†source】 | Balancing model performance with explainability; validating feature importance.【35†source】 | Linked feature design to EDA findings and domain knowledge.【35†source】 | Use feature selection algorithms and cross-validation to refine features.【35†source】 |
| **10. Modeling (Regression / Time Series / Classification)** | Implemented linear regression, classification models, and time series analysis; evaluated with R², RMSE, precision, recall.【36†source】【48†source】 | Addressing independence, homoscedasticity, and time-aware validation were key challenges.【36†source】【48†source】 | Adopted pipelines, feature transformations, and diagnostic plots to validate assumptions.【36†source】【48†source】 | Explore ARIMA, GARCH, and ensemble classifiers; use advanced CV strategies.【48†source】 |
| **11. Evaluation & Risk Communication** | Conducted scenario testing, bootstrap confidence intervals, and subgroup diagnostics; created visual and narrative summaries.【49†source】 | Explaining statistical assumptions and uncertainty to non-technical stakeholders.【49†source】 | Used visuals, sensitivity tables, and plain-language commentary to communicate model risk.【49†source】 | Automate scenario testing pipelines and expand subgroup analyses.【49†source】 |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Prepared decision-focused reports, slides, and dashboards with sensitivity analyses and assumptions.【50†source】 | Balancing technical completeness with clear communication; ensuring reproducibility.【50†source】 | Used executive summaries, clear visuals, and separated artifacts for different audiences.【50†source】 | Adopt automated reporting workflows and build interactive dashboards.【50†source】 |
| **13. Productization** | Modularized code, documented workflows, and ensured reproducibility for handoff; prepared dashboards/APIs.【51†source】 | Managing reproducibility and avoiding notebook clutter.【51†source】 | Added README guidance, version control, and folder organization.【51†source】 | Integrate CI/CD pipelines and containerization for scalability.【51†source】 |
| **14. Deployment & Monitoring** | Designed conceptual deployment strategy (batch jobs/APIs) and monitoring metrics; documented handoff plans.【52†source】 | Addressing drift, delayed feedback, and defining simple but effective monitoring systems.【52†source】 | Outlined layered metrics, alert thresholds, and retraining triggers.【52†source】 | Build automated alerting, retraining pipelines, and containerized services.【52†source】 |
| **15. Orchestration & System Design** | Mapped workflow to DAGs, added logging, checkpoints, and designed repeatable pipelines.【53†source】 | Balancing complexity vs. maintainability in orchestration design.【53†source】 | Introduced lightweight scheduling, config separation, and script-based job management.【53†source】 | Adopt Airflow/Prefect for large-scale orchestration.【53†source】 |
| **16. Lifecycle Review & Reflection** | Synthesized full lifecycle, documented learnings, and prepared professional-grade repo for handoff.【54†source】 | Ensuring clarity, structure, and maintainability for future users.【54†source】 | Added final polish, mapped lifecycle stages to artifacts, and reflected on workflow design.【54†source】 | Continuous improvement cycle with peer reviews and better governance tools.【54†source】 |

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
- Which stage was the most **rewarding**?  
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
- If you repeated this project, what would you **do differently across the lifecycle**?  
- Which skills do you most want to **strengthen** before your next financial engineering project?  

---
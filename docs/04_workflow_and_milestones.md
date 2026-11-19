# 04 — Workflow and Milestones

## Milestone 0 — Repository and reproducibility
- Create repository and folder structure.
- Set Python environment and dependencies.
- Record version, seed and run commands.

## Milestone 1 — Physics definition
- Freeze geometry abstraction and heat-flow direction.
- Confirm units and parameter ranges.
- Implement thermal resistance and die temperature.
- Implement CTE mismatch strain and stress indicator.
- Review equations and dimensional consistency.

**Exit criteria:** equations documented; functions tested on hand-calculated cases.

## Milestone 2 — Dataset generation
- Sample input variables using a fixed seed.
- Calculate target outputs using physics functions.
- Check finite values and bounds.
- Save CSV and metadata.

**Exit criteria:** reproducible dataset with no missing or non-finite values.

## Milestone 3 — Physics verification
- Increase power while holding other inputs fixed: temperature rise should increase.
- Increase any series-layer conductivity: total thermal resistance should decrease.
- Increase a layer thickness: total thermal resistance should increase.
- Increase absolute CTE difference: mismatch strain magnitude should increase.
- Check zero power: thermal rise and mismatch strain should be zero in this model.

**Exit criteria:** automated tests pass and trend checks are recorded.

## Milestone 4 — ML training
- Define inputs and targets explicitly.
- Use a fixed train/test split.
- Fit preprocessing only on training data where applicable.
- Train Linear Regression, Random Forest and Gradient Boosting.
- Evaluate each target independently.

**Exit criteria:** metrics saved with model names, target names and split information.

## Milestone 5 — Interpretation
- Generate parity plots and residual plots.
- Inspect errors across input ranges.
- Compare feature importance.
- Check whether ML predictions preserve expected physical trends.

**Exit criteria:** plots and concise interpretation notes saved.

## Milestone 6 — Technical report and portfolio packaging
- Update README with actual run instructions and results.
- Document limitations and future FEA comparison.
- Add reproducibility details.
- Prepare a concise project summary and resume bullets only after implementation is complete.

## Initial 48-hour sprint
**Day 1:** model definition, thermal and thermo-mechanical functions, dataset generation, unit and trend tests.  
**Day 2:** ML training, metrics, plots, interpretation, README update and repository publication.

The 48-hour sprint is an initial demonstrator, not the completion of a validated package-reliability study.

# Git Branching Strategy

WildSight follows a feature-based Git workflow to keep development organized and maintain a stable main branch.

## Main Branches

### `main`

* Always contains stable, production-ready code.
* Protected from direct development.
* Updated through pull requests after features have been completed and reviewed.

### `develop` *(optional for future use)*

* Serves as the integration branch for completed features before merging into `main`.
* May be introduced as the project grows and development becomes more complex.

## Feature Branches

Each GitHub issue is developed in its own feature branch using the following naming convention:

```text
feature/<issue-number>-<short-description>
```

Examples:

```text
feature/1-project-planning
feature/2-development-environment
feature/8-observation-api
feature/15-user-authentication
```

Each feature branch should focus on a single task or issue.

## Workflow

1. Create a GitHub Issue.
2. Create a feature branch from `main`.
3. Implement the feature.
4. Commit regularly with meaningful commit messages.
5. Push the feature branch to GitHub.
6. Open a Pull Request.
7. Review and merge into `main`.
8. Delete the feature branch after merging.

## Commit Messages

Commits should reference the related issue.

Examples:

```text
#2: Create Docker development environment

#8: Add observation API endpoint

#15: Implement JWT authentication
```

Commit messages should be concise, descriptive, and explain the purpose of the change.

## Branch Protection

The `main` branch should remain stable at all times.

Development should never occur directly on `main`; all work should be completed through feature branches and merged via Pull Requests.

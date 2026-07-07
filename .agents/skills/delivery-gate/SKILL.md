---
name: delivery-gate
description: Verify a Hatch Restore 2 change before it is accepted or prepared for GitHub.
---

# Delivery gate

1. Match the diff to the approved task and reject unrelated changes.
2. Run the smallest relevant build and tests.
3. Have `code_reviewer` check correctness and removable complexity.
4. Have `documentation_agent` verify usage and intent against the code.
5. List hardware behavior that remains unverified.
6. Return pass/fail evidence. A passing gate permits `github` to commit, push, and open a pull request; PR merge and high-risk publication still require explicit human approval.

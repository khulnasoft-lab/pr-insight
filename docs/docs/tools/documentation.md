## Overview
The `add_docs` tool scans the PR code changes, and automatically suggests documentation for any code components that changed in the PR (functions, classes, etc.).

It can be invoked manually by commenting on any PR:
```
/add_docs
```

## Example usage

Invoke the tool manually by commenting `/add_docs` on any PR:

![Docs command](https://khulnasoft/images/pr_insight/docs_command.png){width=768}

The tool will generate documentation for all the components that changed in the PR:

![Docs component](https://khulnasoft/images/pr_insight/docs_components.png){width=768}

![Docs single component](https://khulnasoft/images/pr_insight/docs_single_component.png){width=768}

You can state a name of a specific component in the PR to get documentation only for that component:
```
/add_docs component_name
```

## Configuration options
 - `docs_style`: The exact style of the documentation (for python docstring). you can choose between: `google`, `numpy`, `sphinx`, `restructuredtext`, `plain`. Default is `sphinx`.
 - `extra_instructions`: Optional extra instructions to the tool. For example: "focus on the changes in the file X. Ignore change in ...".

!!! note "Notes"
    - The following languages are currently supported: Python, Java, C++, JavaScript, TypeScript, C#.
    - This tool can also be triggered interactively by using the [`analyze`](./analyze.md) tool.

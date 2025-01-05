# Generated by KhulnaSoft

from pr_insight.algo.git_patch_processing import omit_deletion_hunks

"""
Code Analysis

Objective:
The objective of the "omit_deletion_hunks" function is to remove deletion hunks from a patch file and return only the
added lines.

Inputs:
- "patch_lines": a list of strings representing the lines of a patch file.

Flow:
- Initialize empty lists "temp_hunk" and "added_patched", and boolean variables "add_hunk" and "inside_hunk".
- Compile a regular expression pattern to match hunk headers.
- Iterate through each line in "patch_lines".
- If the line starts with "@@", match the line with the hunk header pattern, finish the previous hunk if necessary,
and append the line to "temp_hunk".
- If the line does not start with "@@", append the line to "temp_hunk", check if it is an added line, and set
"add_hunk" to True if it is.
- If the function reaches the end of "patch_lines" and there is an unfinished hunk with added lines, append it to
"added_patched".
- Join the lines in "added_patched" with newline characters and return the resulting string.

Outputs:
- A string representing the added lines in the patch file.

Additional aspects:
- The function only considers hunks with added lines and ignores hunks with deleted lines.
- The function assumes that the input patch file is well-formed and follows the unified diff format.
"""


class TestOmitDeletionHunks:
    # Tests that the function correctly handles a simple patch containing only additions
    def test_simple_patch_additions(self):
        patch_lines = ['@@ -1,0 +1,1 @@\n', '+added line\n']
        expected_output = '@@ -1,0 +1,1 @@\n\n+added line\n'
        assert omit_deletion_hunks(patch_lines) == expected_output

    # Tests that the function correctly omits deletion hunks and concatenates multiple hunks in a patch.
    def test_patch_multiple_hunks(self):
        patch_lines = ['@@ -1,0 +1,1 @@\n', '-deleted line', '+added line\n', '@@ -2,0 +3,1 @@\n', '-deleted line\n',
                       '-another deleted line\n']
        expected_output = '@@ -1,0 +1,1 @@\n\n-deleted line\n+added line\n'
        assert omit_deletion_hunks(patch_lines) == expected_output

    # Tests that the function correctly omits deletion lines from the patch when there are no additions or context
    # lines.
    def test_patch_only_deletions(self):
        patch_lines = ['@@ -1,1 +1,0 @@\n', '-deleted line\n']
        expected_output = ''
        assert omit_deletion_hunks(patch_lines) == expected_output

        # Additional deletion lines
        patch_lines = ['@@ -1,1 +1,0 @@\n', '-deleted line\n', '-another deleted line\n']
        expected_output = ''
        assert omit_deletion_hunks(patch_lines) == expected_output

        # Additional context lines
        patch_lines = ['@@ -1,1 +1,0 @@\n', '-deleted line\n', '-another deleted line\n', 'context line 1\n',
                       'context line 2\n', 'context line 3\n']
        expected_output = ''
        assert omit_deletion_hunks(patch_lines) == expected_output

    # Tests that the function correctly handles an empty patch
    def test_empty_patch(self):
        patch_lines = []
        expected_output = ''
        assert omit_deletion_hunks(patch_lines) == expected_output

    # Tests that the function correctly handles a patch containing only one hunk
    def test_patch_one_hunk(self):
        patch_lines = ['@@ -1,0 +1,1 @@\n', '+added line\n']
        expected_output = '@@ -1,0 +1,1 @@\n\n+added line\n'
        assert omit_deletion_hunks(patch_lines) == expected_output

    # Tests that the function correctly handles a patch containing only deletions and no additions
    def test_patch_deletions_no_additions(self):
        patch_lines = ['@@ -1,1 +1,0 @@\n', '-deleted line\n']
        expected_output = ''
        assert omit_deletion_hunks(patch_lines) == expected_output

### Posting issues

The [issues page](https://github.com/shitwolfymakes/Endless-Sky-Mission-Builder/issues) on GitHub is for tracking bugs and feature requests. When posting a new issue, please:

* Check to make sure it's not a duplicate of an existing issue.
* Create a separate "issue" for each bug you are reporting and each feature you are requesting.
* Do not use the issues page for things other than bug reports, documentation requests, and feature requests.

If reporting a bug, please try to see if it occurs on both the windows and linux versions. They should have no differences, but the GUI code behaves differently depending on the operating system!

If you are posting a pull request, please:

* Do not combine multiple unrelated changes into a single pull.
* Check the diff and make sure the pull request does not contain unintended changes.
* If changing the Python code, follow the [style guide](https://github.com/shitwolfymakes/Endless-Sky-Mission-Builder/blob/master/style_guide.md).

If proposing a major pull request, start by posting an issue and discussing the best way to implement it. Often the first strategy that occurs to you will not be the cleanest or most effective way to implement a new feature. I will not merge pull requests that are too large for me to read through the diff and check that the change will not introduce bugs.

### Closing issues

If you believe your issue has been resolved, you can close the issue yourself. I won't close an issue unless it has been idle for a few weeks, to avoid having me mark something as fixed when the original poster does not think their request has been fully addressed.

If an issue is a bug and it has been fixed in the code, it may be helpful to leave it "open" until an official release that fixes the bug has been made, so that other people encountering the same bug will see that it has already been reported.

### Issue labels

The labels I assign to issues are:

* bug: Anything where the game is not behaving as intended.
* documentation: Something missing or incorrect in the user or code documentation.
* enhancement: A request for new functionality in ESMB.

# Contributing

We accept contributions of every kind: documentation, code, artwork. Any help is greatly
appreciated. This document contains everything needed to get started with your first contribution.


## Contributing Code

We keep the source code on [GitHub](https://www.github.com) and take contributions through
[GitHub pull requests](https://help.github.com/articles/using-pull-requests).

For smaller patches and bug fixes just go ahead and either report an issue or submit a pull
request.

It is usually a good idea to discuss major changes with the developers, this will help us
determine whether the contribution would be a good fit for the project and if it is likely to be
accepted. There's nothing worse than seeing your hard work being rejected because it falls outside
of the scope of the project.

Make sure your editor respects the [EditorConfig](http://editorconfig.org) configuration file we
put at the root of the repository.

We follow [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html) as our git workflow of
choice which boils down to:

* The `master` branch is always stable and deployable.
* To work on something new, branch off `master` and give the new branch a descriptive name (e.g.:
  `sort-packages-by-name`, `issue-32`, etc).
* Regularly __rebase__ that branch against `master` and push your work to a branch with the same
  name on the server.
* When you need feedback, help or think you are ready,
  [submit a pull request](https://help.github.com/articles/using-pull-requests).
* Once the branch has been merged (or rebased) into `master`, delete it from both your local and
  remote repository.

We invite you to follow
[these guidelines](http://who-t.blogspot.de/2009/12/on-commit-messages.html) to write useful
commit messages.

Additionally, you don't need to add entries to the [CHANGELOG.md](CHANGELOG.md) file, this is our
responsibility.


## Contributing Tests

Testing is done with input/output examples.
Since this project is in its early stages, we lack meaningful examples.
We encourage you to suggest improvements, fixes, and additions to these tests by opening pull requests.

To contribute to this effort, please check out the following folders:
* [tests/source](/tests/source): input RST files and `conf.py`
* [tests/my_module](/tests/my_module): input code to produce documentation with the `sphinx.ext.autodoc` extension
* [tests/expected](/tests/expected): the desired output if applied to the input sources and code

You are encouraged to suggest changes to these files to address any discrepancies.

Important
: For resolving discrepancies, don't worry about passing CI tests.
Upon accepting your PR, developers will make additional effort to resolve these discrepancies and make the tests pass.

The following command tests that the generated output matches existing results:
```bash
make test
```

If it fails, it will show the difference between generated and expected output.

To better view the difference after running `make test`, you can use the following command:
```bash
make diff DIFFTOOL=meld
```
Where you can replace 'DIFFTOOL=meld' with any diff tool you have on your local machine.
The default is `meld`.


## Reading List

* [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html)
* [Keep a Changelog](http://keepachangelog.com/)
* [On Commit Messages](http://who-t.blogspot.de/2009/12/on-commit-messages.html)
* [Semantic Versioning](http://semver.org/)

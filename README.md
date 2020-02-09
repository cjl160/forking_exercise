# GitHub Forking Practical 

In this practical, you will Fork a repo, extend the code committing to your forked repo and once satisfied create a pull request to the upstream (original repo). 

* If any of these steps are unclear please see the run thru video on
  [Canvas Discussion page for this practical](
  https://canvas.anglia.ac.uk/courses/14266/discussion_topics/131015)
* Please Fork this repo by hitting the Fork Button at the top right of this 
  page, it looks like:
  <img src="https://aru-bioinf-ibds.github.io/images/GitHub_fork_button.png">
  (but hit the one at the top right of the GitHub page!)
* Once you have forked the repo then turn on the GitHub workflow by
  selecting the Actions tab and enabling it. The GitHub workflow is a
  new CI/CD tool like Travis but run within GitHub. 
  Make an initial commit altering the comment line in [person.py](person.py)

  ```python
  # TODO add another person - anyone you like
  ```

  replacing `anyone you like` with your favourite cartoon character.
* The programming task is to add a person record for your favourite 
  cartoon character to people dictionary. 
  * You should follow test driven 
    development first creating a new test for the new person in 
    [test_people.py](test_people.py)
    This test should fail. Check it does with `pytest`. Once you are
    happy commit the change
  * Add then create your new person in
    [person.py](person.py)
    making sure that your test works and commit it.
* The code uses namedtuples for person please see 
  https://pymotw.com/3/collections/namedtuple.html
  to see how these work.
* Once you are happy with your great addition to the code create a
  pull request to asking to merge the change back to the upstream repo.
* Note that it might be necessary to [Sync your fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) ask for help with this!



ARU apprentices should now go to the 
[Canvas Discussion page for this practical](
https://canvas.anglia.ac.uk/courses/14266/discussion_topics/131015)

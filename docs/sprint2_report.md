# Sprint 2 Report
Video Link:
## What's New (User Facing)
 * User authentication and persisting user sessions
 * Add/Remove new clubs to the tracker
 * Edit existing clubs
 * Automated processing of data sent over email
 * View accesses of a specific location in a dynamic time range
 * View total events for all clubs in a dynamic time range

## Work Summary (Developer Facing)
Provide a one paragraph synopsis of what your team accomplished this sprint. Don't repeat the "What's New" list of features. Instead, help the instructor understand how you went about the work described there, any barriers you overcame, and any significant learnings for your team.

The focus of sprint 2 was on completing the last few remaining developers tools needed to speed up the project and then spending the remaining time implementing MVP features. During sprint 2 the team completed the creation of the sqlite database, created new python types to interface with the database, defined table schemas, created scripts to handle incoming email data, set up simple authentication and then began extending the current back end of the project. Each of these individual tasks required several supporting tasks including but not limited to front end work in HTML and CSS, backend work in python and flask, and then supporting "helper" code that simplified development such as scripts for wiping the database and re-initializing with test data. The breadth of the work this sprint required lots of handoffs between members of the team and as a result lots of communication! Compared to the misses during sprint 1, things were much easier this sprint, but were not without a few hiccups in the form of duplicating work. Much of the improvements were due to better sprint planning at the beginning of the month and creating more specific GitHub issues for each task. All in all the team has made great strides in working together as a team, but there is always more room to improve!

## Unfinished Work
If applicable, explain the work you did not finish in this sprint. For issues/user stories in the current sprint that have not been closed, (a) any progress toward completion of the issues has been clearly tracked (by checking the checkboxes of  acceptance criteria), (b) a comment has been added to the issue to explain why the issue could not be completed (e.g., "we ran out of time" or "we did not anticipate it would be so much work"), and (c) the issue is added to a subsequent sprint, so that it can be addressed later.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * [Admin page routes](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134332296&issue=lacroixmeariver%7CWSU_Cpts_322%7C41)
 * [DB Table Creation](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134332298&issue=lacroixmeariver%7CWSU_Cpts_322%7C44)
 * [DB Table Types](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134332301&issue=lacroixmeariver%7CWSU_Cpts_322%7C46)
 * [User authentication backend](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134158695&issue=lacroixmeariver%7CWSU_Cpts_322%7C42)
 * [Viewing aggregate data](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134158677&issue=lacroixmeariver%7CWSU_Cpts_322%7C7)
 * [Generating model data](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=135320613&issue=lacroixmeariver%7CWSU_Cpts_322%7C49)
 * [Add admin home web page](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134158693&issue=lacroixmeariver%7CWSU_Cpts_322%7C40)
 * [Allow admin to search for under-utilized spaces](https://github.com/users/lacroixmeariver/projects/4/views/1?pane=issue&itemId=134158683&issue=lacroixmeariver%7CWSU_Cpts_322%7C11)


 Desirables (Remove this section when you save the file):
  * Each issue should be assigned to a milestone
  * Each completed issue should be assigned to a pull request
  * Each completed pull request should include a link to a "Before and After" video
  * All team members who contributed to the issue should be assigned to it on GitHub
  * Each issue should be assigned story points using a label
  * Story points contribution of each team member should be indicated in a comment

 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:

 * URL of issue 1 <<One sentence explanation of why issue was not completed>>
 * URL of issue 2 <<One sentence explanation of why issue was not completed>>
 * URL of issue n <<One sentence explanation of why issue was not completed>>

 Examples of explanations (Remove this section when you save the file):
  * "We ran into a complication we did not anticipate (explain briefly)."
  * "We decided that the feature did not add sufficient value for us to work on it in this sprint (explain briefly)."
  * "We could not reproduce the bug" (explain briefly).
  * "We did not get to this issue because..." (explain briefly)

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [Database Table Types](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/attendance_tracker/types/tables.py0)
 * [Authentication Endpoints](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/attendance_tracker/controllers/auth.py)
 * [Database Schema Script](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/sqlite/init.sql)
 * [Admin Endpoints](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/attendance_tracker/controllers/admin.py)
 * [Flask CLI scripts](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/attendance_tracker/__init__.py)
 * [Data Analytics Endpoints](https://github.com/lacroixmeariver/WSU_Cpts_322/blob/master/attendance_tracker/__init__.py)

## Retrospective Summary
Here's what went well:
  * Sprint planning meeting saved so much time!
  * App structure led to different features "just working" when connecting different developers code
  * Picked a reasonable amount of issues for the sprint, we just barely cleared the spring backlog
  * Team prioritizing of features was well done this sprint, there were no major issues that blocked development of future features

Here's what we'd like to improve:
   * Get more customer feedback to validate some new ideas
   * Create validation tests for risky areas such as data pipeline process
   * The CSS styling :-)

Here are changes we plan to implement in the next sprint:
   * Schedule time with our customer to demo the project for feedback (we are already booked for next week)
   * Communicate more frequently with customers using email or video to tighten feedback loops
   * Try to create more tickets at the beginnging of the sprint and minimize making tickets throughout the sprint

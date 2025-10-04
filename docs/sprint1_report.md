# Sprint x Report
Video Link:  ==DO NOT FORGET TO UPDATE==
## What's New (User Facing)
* Web app navigation bar
* Web app data visualization page
* Web app login page
## Work Summary (Developer Facing)
This initial sprint was primarily focused on setting up the foundation of the application, including laying out the structure and design of the website and database. Additionally, many new developer tools were implemented that enforce code style, python project structure, and python type correctness all of which simplify the process of creating new features! As mentioned previously, all of this work culminated in several user facing features that map to project functional requirements. In tandem with the software development side of the project, the team has also made strides to interact with customers to request real life data and testing. These efforts include two meetings with WSU club administrators and WSU IT members. Through this process the team has also established an email chain that will be used to ask more questions and request more data when required. Overall, The `__init__` to win it team has made lots of progress on the project, while there are currently only a few customer facing features available the team is set up well for success in future sprints!
## Unfinished Work
If applicable, explain the work you did not finish in this sprint. For issues/user
stories in the current sprint that have not been closed, (a) any progress toward
completion of the issues has been clearly tracked (by checking the checkboxes of
acceptance criteria), (b) a comment has been added to the issue to explain why the
issue could not be completed (e.g., "we ran out of time" or "we did not anticipate
it would be so much work"), and (c) the issue is added to a subsequent sprint, so
that it can be addressed later.

While the team was successful in shipping several basic features there were a handful of features expected to be completed during sprint 1 that were not completed. These tasks linked below in the incomplete user stories sections were blocked by a common issue in that the data input for the project has not been finalized yet. Since the attendance tracker project is going to process and present real data the steps required to get access to this data has taken longer than anticipated. The team currently has access to a basic schema for activity event data and room assignments, however the exact format is still being reviewed by customers. To minimize rework the team has decided to delay these tasks until the customer is less likely to change the form of the data! These decisions have resulted in other tasks that were expected to be completed in sprint 2 be moved forward into sprint 1 so the surprise delay has not changed the throughput of the team this sprint, it has only changed the features that are available. One other detail to note is that since the activity data is derived from sensitive information (student id) the method for transferring data from school IT services to the attendance tracker project has to be carefully considered by the customer. These extra precautions while very important for data privacy have resulted in increased delays.
## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:
* [Project installation](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=132042509&issue=GrTravis2%7CWSU_Cpts_322%7C37)
* [Web app structure](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=130974069&issue=GrTravis2%7CWSU_Cpts_322%7C14)
* [Deploy flask app tool](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=130974238&issue=GrTravis2%7CWSU_Cpts_322%7C17)
* [Template file structure](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131011376&issue=GrTravis2%7CWSU_Cpts_322%7C22)
* [Login template](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131025687&issue=GrTravis2%7CWSU_Cpts_322%7C24)
* [Data view page](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131885307&issue=GrTravis2%7CWSU_Cpts_322%7C29)
* [Create and register sqlite db object](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131474203&issue=GrTravis2%7CWSU_Cpts_322%7C25)
* [Create basic UI](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131711108&issue=GrTravis2%7CWSU_Cpts_322%7C27)
* [Template database](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=130946805&issue=GrTravis2%7CWSU_Cpts_322%7C12)
* [Automate tailwindCSS usage](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131901656&issue=GrTravis2%7CWSU_Cpts_322%7C34)
* [Example CSV and database after parsing](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=131896377&issue=GrTravis2%7CWSU_Cpts_322%7C32) ==still need to approve!!!==
## User Story Scoreboard:
| Team Member | Cumulative Story Points |
| ----------- | ----------------------- |
| Dylan       | 3                       |
| Ingrid      | 5                       |
| Gavin       | 9                       |
**Footnote: Dylan put lots of time and effort in communicating with customers, story points do not capture the whole picture for tasks related to customer involvement**
 Desirables (Remove this section when you save the file):
* Each issue should be assigned to a milestone
* Each completed issue should be assigned to a pull request
* Each completed pull request should include a link to a "Before and After" video
* All team members who contributed to the issue should be assigned to it on GitHub
* Each issue should be assigned story points using a label
* Story points contribution of each team member should be indicated in a comment
## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:
* [Make sure a room has a club assigned before accepting user data](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=128355247&issue=GrTravis2%7CWSU_Cpts_322%7C3)
	* Pending data source finalization.
* [Allow club members to record their usage of the room](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=128385210&issue=GrTravis2%7CWSU_Cpts_322%7C10)
	* Pending data source finalization
* [Add clubs/rooms to the system](https://github.com/users/GrTravis2/projects/5/views/1?pane=issue&itemId=128356784&issue=GrTravis2%7CWSU_Cpts_322%7C8)
	* Pending data source finalization and user authentication feature

**See unfinished work section and issue posts for more details on why the features were not completed.**

Examples of explanations (Remove this section when you save the file):
* "We ran into a complication we did not anticipate (explain briefly)."
* "We decided that the feature did not add sufficient value for us to work on it in this sprint (explain briefly)."
* "We could not reproduce the bug" (explain briefly).
* "We did not get to this issue because..." (explain briefly)
## Code Files for Review
Please review the following code files, which were actively developed during this
sprint, for quality:
* [Web app entry point and resources](https://github.com/GrTravis2/WSU_Cpts_322/blob/master/attendance_tracker/app.py)
* [HTML templates and CSS file](https://github.com/GrTravis2/WSU_Cpts_322/tree/master/attendance_tracker/templates)
* [Web app controllers (functionalities) folder](https://github.com/GrTravis2/WSU_Cpts_322/tree/master/attendance_tracker/controllers)
* [Data analytics specific endpoints and types](https://github.com/GrTravis2/WSU_Cpts_322/blob/master/attendance_tracker/controllers/analytics.py)

**Note that other work was done in other controllers and bash scripts, but the bulk of work was split across these linked files/folders**

## Retrospective Summary
Here's what went well:
* Getting customers involved early and gaining lots of valuable feedback
* Creation of internal/developer features which will speed up future development
* Team members specializing in their areas of interest, becoming subject matter experts for the team!

Here's what we'd like to improve:
* Reduce feature bottlenecks
* Reduce redundant work in the form of developers working on the same code across different tasks
* Reduce uncertainty of data format and method of delivery
* Improve Sprint planning effectiveness

Here are changes we plan to implement in the next sprint:
* Finalize sprint plan early and do not deviate unless absolutely necessary
* Reduce task scope until there is no chance of two tasks overlapping
* Fully complete sprint planning before starting development, try not to add many tasks during the sprint
* For understanding customer needs and other external services/requirements, make sure the right stakeholders are in the meeting.
